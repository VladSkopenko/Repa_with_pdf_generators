from fpdf import FPDF
from generator_text import contract_template_english
from generator_text2 import contract_template_ukraine
from generator_text3 import contract_template_russia

class StreamPDF(FPDF):
    DEFAULT_MARGIN = 15
    DEFAULT_TOP_MARGIN = 20
    DEFAULT_BOTTOM_MARGIN = 20
    DEFAULT_FONT_SIZE = 10
    COLUMN_PADDING = 2

    def __init__(self, num_columns=1, align='L'):
        super().__init__()
        self.add_font('TimesNewRoman', '', 'fonts/TIMES.TTF')
        self.add_font('TimesNewRoman', 'B', 'fonts/TIMESBD.TTF')
        self.add_font('TimesNewRoman', 'I', 'fonts/TIMESI.TTF')
        self.add_font('TimesNewRoman', 'BI', 'fonts/TIMESBI.TTF')
        self.set_font("TimesNewRoman", '', self.DEFAULT_FONT_SIZE)
        self.align = align
        self.set_left_margin(self.DEFAULT_MARGIN)
        self.set_right_margin(self.DEFAULT_MARGIN)
        self.set_top_margin(self.DEFAULT_TOP_MARGIN)
        self.set_auto_page_break(auto=True, margin=self.DEFAULT_BOTTOM_MARGIN)
        self.num_columns = num_columns

    def add_stream_text(self, *columns_text):
        column_width = (self.w - 2 * self.DEFAULT_MARGIN) / self.num_columns
        y_start = self.DEFAULT_TOP_MARGIN
        x_starts = [self.DEFAULT_MARGIN + i * column_width for i in range(self.num_columns)]
        # Разбиваем текст на абзацы
        columns_paragraphs = [col.split('\n\n') for col in columns_text]
        indexes = [0] * self.num_columns
        finished = [False] * self.num_columns

        while not all(finished):
            self.add_page()
            y_positions = [y_start for _ in range(self.num_columns)]
            for col_idx in range(self.num_columns):
                self.set_xy(x_starts[col_idx], y_positions[col_idx])
                self.set_font("TimesNewRoman", '', self.DEFAULT_FONT_SIZE)
                while indexes[col_idx] < len(columns_paragraphs[col_idx]):
                    para = columns_paragraphs[col_idx][indexes[col_idx]].strip()
                    if not para:
                        indexes[col_idx] += 1
                        continue
                    # dry_run чтобы узнать высоту
                    lines = self.multi_cell(column_width - 2 * self.COLUMN_PADDING, 5, para, dry_run=True, output="LINES")
                    est_height = len(lines) * 5
                    if self.get_y() + est_height > self.h - self.DEFAULT_BOTTOM_MARGIN:
                        break
                    self.multi_cell(column_width - 2 * self.COLUMN_PADDING, 5, para, border=0, align=self.align)
                    y_positions[col_idx] = self.get_y()
                    indexes[col_idx] += 1
                if indexes[col_idx] >= len(columns_paragraphs[col_idx]):
                    finished[col_idx] = True

if __name__ == "__main__":
    # Получаем потоковый текст для каждой колонки (можно собрать из секций)
    def sections_to_stream(sections):
        # Просто склеиваем все тексты секций через два перевода строки
        return '\n\n'.join(s['text'] for s in sections)

    sections_uk = contract_template_ukraine.render_all_sections(
        goods_description="Пшениця українська навалом",
        incoterms_year="2024",
        quantity=1000,
        tolerance=5,
        metrics=["Білок: база 10,5%, не менше 9% (N x 5,7 на суху основу)\n\nПокупець застосовує штраф у розмірі 1% від поставленої кількості / договірної ціни за кожне заниження на 1% від основної пропорції білка. За білок більше 10,5% бонуси не надаються.\n",
                "Вологість: база 14,0%, макс.15%\n\n Покупець застосовує штраф у розмірі 1% від поставленої кількості / договірної ціни за кожне перевищення 1% базової пропорційної вологості. За вологість менше 14% бонуси не надаються."],
        price_per_ton=250,
        price_per_ton_text="двісті п'ятдесят",
        total_value=250000,
        total_value_text="двісті п'ятдесят тисяч"
    )
    sections_en = contract_template_english.render_all_sections(
        goods_description="Ukrainian wheat in bulk",
        incoterms_year="2024",
        quantity=1000,
        tolerance=5,
        metrics=["Protein: base 10.5%, min.9% (N x 5.7 on dry basis)\n\nThe buyer applies a penalty of 1% of the delivered quantity / contract price for understatement 1% of the base-proportional protein. No bonuses are awarded for a protein content of more than 10.5%.\n",
                "Moisture: base 14.0%, max.15%\n\n The buyer applies a penalty of 1% of the delivered quantity / contract price for each excess of 1% of the base-proportional humidity. For humidity less than 14% no bonuses are granted."],
        price_per_ton=350,
        price_per_ton_text="three hundred fifty",
        total_value=350000,
        total_value_text="three hundred fifty thousand"
    )
    sections_ru = contract_template_russia.render_all_sections(
        goods_description="Пшеница украинская навалом",
        incoterms_year="2024",
        quantity=1000,
        tolerance=5,
        metrics=["Білок: база 10,5%, не менше 9% (N x 5,7 на суху основу)\n\nПокупець застосовує штраф у розмірі 1% від поставленої кількості / договірної ціни за кожне заниження на 1% від основної пропорції білка. За білок більше 10,5% бонуси не надаються.\n",
                "Вологість: база 14,0%, макс.15%\n\n Покупець застосовує штраф у розмірі 1% від поставленої кількості / договірної ціни за кожне перевищення 1% базової пропорційної вологості. За вологість менше 14% бонуси не надаються."],
        price_per_ton=300,
        price_per_ton_text="триста",
        total_value=300000,
        total_value_text="триста тисяч"
    )
    # Преобразуем секции в потоковый текст
    stream_uk = sections_to_stream(sections_uk)
    stream_en = sections_to_stream(sections_en)
    stream_ru = sections_to_stream(sections_ru)

    pdf = StreamPDF(num_columns=3)
    pdf.add_stream_text(stream_uk, stream_en, stream_ru)
    pdf.output("contract_stream.pdf") 
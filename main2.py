from fpdf import FPDF
from generator_text import contract_template_english
from generator_text2 import contract_template_ukraine

class ContractPDF(FPDF):
    DEFAULT_MARGIN = 5
    DEFAULT_TOP_MARGIN = 30
    DEFAULT_BOTTOM_MARGIN = 10
    DEFAULT_FONT_SIZE = 10
    DEFAULT_HEADER_FONT_SIZE = 10
    DEFAULT_LINE_HEIGHT = 5
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

    def _get_column_x(self, col_idx, column_width):
        return self.DEFAULT_MARGIN + col_idx * column_width

    def get_string_height(self, w, txt):
        # Подсчёт высоты текста с учётом переносов
        lines = 0
        for paragraph in txt.split('\n'):
            str_width = self.get_string_width(paragraph)
            lines += max(1, int(str_width // w) + 1)
        return lines * self.DEFAULT_LINE_HEIGHT

    def add_text(self, *sections_columns):
        column_width = (self.w - 2 * self.DEFAULT_MARGIN) / self.num_columns
        y_start = self.DEFAULT_TOP_MARGIN

        # Заголовки для каждой колонки
        headers = [contract_template_english.render_header() for _ in range(self.num_columns)]
        # Делаем длины секций одинаковыми
        max_len = max(len(col) for col in sections_columns)
        for col in sections_columns:
            while len(col) < max_len:
                col.append({"text": "", "bold": False})

        self.add_page()
        # Печатаем заголовки только на первой странице
        for col_idx in range(self.num_columns):
            x = self._get_column_x(col_idx, column_width)
            self.set_xy(x + self.COLUMN_PADDING, y_start)
            self.set_font("TimesNewRoman", 'B', self.DEFAULT_HEADER_FONT_SIZE)
            self.multi_cell(column_width - 2 * self.COLUMN_PADDING, 8, headers[col_idx], border=0, align='C', ln=3)
        self.set_y(y_start + 18)

        for i in range(max_len):
            y_row_start = self.get_y()
            max_height = 0
            heights = []
            # Считаем высоту текста для каждой колонки
            for col_idx in range(self.num_columns):
                section = sections_columns[col_idx][i]
                text = section["text"]
                height = self.get_string_height(column_width - 2 * self.COLUMN_PADDING, text)
                heights.append(height)
                if height > max_height:
                    max_height = height
            # Проверяем, не вылезет ли строка за пределы страницы
            if y_row_start + max_height > self.h - self.DEFAULT_BOTTOM_MARGIN:
                self.add_page()
                y_row_start = self.get_y()
                # ... (печать заголовков, если нужно) ...
                self.set_y(y_start + 18)
                y_row_start = self.get_y()
            # Печатаем каждую колонку с одинакового Y
            for col_idx in range(self.num_columns):
                x = self._get_column_x(col_idx, column_width)
                self.set_xy(x + self.COLUMN_PADDING, y_row_start)
                section = sections_columns[col_idx][i]
                self.set_font("TimesNewRoman", 'B' if section["bold"] else '', self.DEFAULT_FONT_SIZE)
                self.multi_cell(column_width - 2 * self.COLUMN_PADDING, self.DEFAULT_LINE_HEIGHT, section["text"], border=0, align=self.align, ln=3)
            # После всех колонок — выставляем Y для следующей строки
            self.set_y(y_row_start + max_height)

# Пример использования:
sections_uk = contract_template_ukraine.render_all_sections(
    goods_description="Пшениця українська навалом",
    incoterms_year="2024",
    quantity=1000,
    tolerance=5,
    metrics=["Білок: база 10,5%, не менше 9% (N x 5,7 на суху основу)\n\n Покупець застосовує штраф у розмірі 1% від поставленої кількості / договірної ціни за кожне заниження на 1% від основної пропорції білка. За білок більше 10,5% бонуси не надаються.\n",
            "Вологість: база 14,0%, макс.15%\n\n Покупець застосовує штраф у розмірі 1% від поставленої кількості / договірної ціни за кожне перевищення 1% базової пропорційної вологості. За вологість менше 14% бонуси не надаються."],
    price_per_ton=250,
    price_per_ton_text="двісті п'ятдесят",
    total_value=250000,
    total_value_text="двісті п'ятдесят тисяч"
)

sections_ru = contract_template_english.render_all_sections(
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
sections_en = contract_template_english.render_all_sections(
    goods_description="Ukrainian wheat in bulk",
    incoterms_year="2024",
    quantity=1000,
    tolerance=5,    
    metrics=["Protein: base 10.5%, min.9% (N x 5.7 on dry basis)\n\n The buyer applies a penalty of 1% of the delivered quantity / contract price for understatement 1% of the base-proportional protein. No bonuses are awarded for a protein content of more than 10.5%.\n",
            "Moisture: base 14.0%, max.15%\n\n The buyer applies a penalty of 1% of the delivered quantity / contract price for each excess of 1% of the base-proportional humidity. For humidity less than 14% no bonuses are granted."],
    price_per_ton=350,
    price_per_ton_text="three hundred fifty",
    total_value=350000,
    total_value_text="three hundred fifty thousand"
)

if __name__ == "__main__":
    pdf = ContractPDF(num_columns=2)
    pdf.add_text(sections_uk, sections_ru, sections_en)
    pdf.output("contract_w2.pdf") 
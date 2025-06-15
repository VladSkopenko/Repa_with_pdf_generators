from fpdf import FPDF
from fpdf.enums import XPos, YPos
from generator_text import contract_template_english
from generator_text2 import contract_template_ukraine
from generator_text3 import contract_template_russia

class ContractPDF(FPDF):

    DEFAULT_MARGIN = 5
    DEFAULT_TOP_MARGIN = 30
    DEFAULT_BOTTOM_MARGIN = 20
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

    def _render_column_header(self, header, x_start, y_start, column_width):
        self.set_xy(x_start + self.COLUMN_PADDING, y_start + self.COLUMN_PADDING)
        self.set_font("TimesNewRoman", 'B', self.DEFAULT_HEADER_FONT_SIZE)
        self.multi_cell(column_width - 2 * self.COLUMN_PADDING, 8, header, border=0, align='C')
        self.set_font("TimesNewRoman", '', self.DEFAULT_FONT_SIZE)
        return self.get_y()

    def _calculate_text_height(self, text, column_width):
        available_width = column_width - 2 * self.COLUMN_PADDING
        lines = 0
        
        # Разбиваем текст на параграфы
        paragraphs = text.split('\n')
        
        for paragraph in paragraphs:
            if not paragraph.strip():  # Пустая строка
                lines += 1
                continue
                
            # Рассчитываем количество строк для параграфа
            str_width = self.get_string_width(paragraph)
            if str_width <= available_width:
                lines += 1
            else:
                # Если текст не помещается в одну строку, рассчитываем количество строк
                lines += max(1, int(str_width / available_width) + 1)
        
        return lines * self.DEFAULT_LINE_HEIGHT

    def _render_column_content(self, sections, start_index, x_start, y_start, column_width):
        y = y_start
        self.set_xy(x_start + self.COLUMN_PADDING, y)
        current_index = start_index
        
        while current_index < len(sections):
            section = sections[current_index]
            self.set_font("TimesNewRoman", 'B' if section["bold"] else '', self.DEFAULT_FONT_SIZE)
            
            # Рассчитываем примерную высоту текста
            est_height = self._calculate_text_height(section["text"], column_width)
            
            # Проверяем, поместится ли текст на текущей странице
            if y + est_height > self.h - self.DEFAULT_BOTTOM_MARGIN:
                # Если не помещается, прерываем и переходим на новую страницу
                break
            
            # Рендерим текст
            self.set_font("TimesNewRoman", 'B' if section["bold"] else '', self.DEFAULT_FONT_SIZE)
            self.multi_cell(column_width - 2 * self.COLUMN_PADDING, self.DEFAULT_LINE_HEIGHT, section["text"], border=0, align=self.align)
            
            # Обновляем позицию Y
            y = self.get_y()
            self.set_xy(x_start + self.COLUMN_PADDING, y)
            current_index += 1
            
        return current_index

    def _get_column_x(self, col_idx, column_width):
        return self.DEFAULT_MARGIN + col_idx * column_width

    def add_text(self, templates, *sections_columns):
        column_width = (self.w - 2 * self.DEFAULT_MARGIN) / self.num_columns
        column_height = self.h - self.DEFAULT_TOP_MARGIN - self.DEFAULT_BOTTOM_MARGIN
        y_start = self.DEFAULT_TOP_MARGIN

        # Генерируем заголовки используя переданные шаблоны
        headers = [templates[i].render_header() for i in range(self.num_columns)]
        indexes = [0] * self.num_columns
        lengths = [len(col) for col in sections_columns]
        first_page = [True] * self.num_columns

        while any(indexes[i] < lengths[i] for i in range(self.num_columns)):
            self.add_page()
            y_positions = [y_start + self.COLUMN_PADDING for _ in range(self.num_columns)]

            if self.num_columns > 1:
                for col_idx in range(self.num_columns):
                    x_start = self._get_column_x(col_idx, column_width)
                    self.set_xy(x_start, y_start)
                    self.draw_column_border(x_start, y_start, column_width, column_height)

            for col_idx in range(self.num_columns):
                x_start = self._get_column_x(col_idx, column_width)
                if first_page[col_idx]:
                    y_positions[col_idx] = self._render_column_header(headers[col_idx], x_start, y_start, column_width)
                    first_page[col_idx] = False
                else:
                    y_positions[col_idx] = y_start + self.COLUMN_PADDING
                    self.set_xy(x_start + self.COLUMN_PADDING, y_positions[col_idx])

            for col_idx in range(self.num_columns):
                x_start = self._get_column_x(col_idx, column_width)
                y = y_positions[col_idx]
                indexes[col_idx] = self._render_column_content(
                    sections_columns[col_idx], 
                    indexes[col_idx], 
                    x_start, 
                    y, 
                    column_width
                )

    def draw_column_border(self, x, y, w, h):
        self.set_xy(x, y)
        self.cell(w, h, '', border=1)



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

if __name__ == "__main__":
    # Генерація PDF
    pdf = ContractPDF(num_columns=3)
    pdf.add_text([contract_template_ukraine, contract_template_english, contract_template_russia], sections_uk, sections_en, sections_ru)
    pdf.output("contract_w.pdf")

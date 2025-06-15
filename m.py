from fpdf import FPDF
from fpdf.enums import XPos, YPos
from generator_text import contract_template_english

class ContractPDF(FPDF):
    
    def __init__(self, num_columns=2):
        super().__init__()
        self.add_font('TimesNewRoman', '', 'fonts/TIMES.TTF')
        self.add_font('TimesNewRoman', 'B', 'fonts/TIMESBD.TTF')
        self.add_font('TimesNewRoman', 'I', 'fonts/TIMESI.TTF')
        self.add_font('TimesNewRoman', 'BI', 'fonts/TIMESBI.TTF')
        self.set_font("TimesNewRoman", '', 10)
        self.setup_page(num_columns)

    def setup_page(self, num_columns=2, left=10, right=10, top=20, bottom=20):
        self.set_left_margin(left)
        self.set_right_margin(right)
        self.set_top_margin(top)
        self.set_auto_page_break(auto=True, margin=bottom)
        self.num_columns = num_columns  

    def add_text(self, *sections_columns):
        margin = 10
        top_margin = 30
        bottom_margin = 20
        num_columns = self.num_columns
        column_width = (self.w - 2 * margin) / num_columns
        column_height = self.h - top_margin - bottom_margin
        font_size = 10
        y = top_margin

        headers = [contract_template_english.render_header() for _ in range(num_columns)]
        texts = []
        for sections in sections_columns:
            texts.append('\n'.join([s['text'] for s in sections]))

        for i in range(num_columns):
            x = margin + i * column_width
            self.set_xy(x, y)
            self.cell(column_width, column_height, '', border=1)
            self.set_xy(x + 2, y + 2)
            self.set_font("TimesNewRoman", 'B', 12)
            self.multi_cell(column_width - 4, 8, headers[i], border=0, align='C')
            self.set_font("TimesNewRoman", '', font_size)
            y_after_header = self.get_y()
            self.set_xy(x + 2, y_after_header)
            self.multi_cell(column_width - 4, 5, texts[i], border=0, align='L')

# Тестовые данные
sections = contract_template_english.render_all_sections(
    delivery_basis="FOB Odessa",
    incoterms_year="2020",
    amount_usd="100000"
)

sections_ru = contract_template_english.render_all_sections(
    delivery_basis="FOB Odessa2",
    incoterms_year="20202",
    amount_usd="10000022"
)

sections_en = contract_template_english.render_all_sections(
    delivery_basis="FOB Odessa3",
    incoterms_year="20203",
    amount_usd="10000033"
)
sections_en.extend(sections_ru)
sections_en.extend(sections)
sections_en.extend(sections_ru)

# Генерация PDF
pdf = ContractPDF(num_columns=2)
pdf.add_page()

pdf.add_text(sections, sections_ru, sections_en)
pdf.output("contract.pdf")

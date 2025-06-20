from fpdf import FPDF
from dotenv import load_dotenv
load_dotenv()


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
        lines = self.multi_cell(
            available_width,
            self.DEFAULT_LINE_HEIGHT,
            text,
            border=0,
            align=self.align,
            dry_run=True,
            output="LINES"
        )
        return len(lines) * self.DEFAULT_LINE_HEIGHT

    def _render_column_content(self, sections, start_index, x_start, y_start, column_width):
        y = y_start
        self.set_xy(x_start + self.COLUMN_PADDING, y)
        current_index = start_index
        
        while current_index < len(sections):
            section = sections[current_index]
            self.set_font("TimesNewRoman", 'B' if section["bold"] else '', self.DEFAULT_FONT_SIZE)
            
            est_height = self._calculate_text_height(section["text"], column_width)
            
            if y + est_height > self.h - self.DEFAULT_BOTTOM_MARGIN:
                break
            

            self.set_font("TimesNewRoman", 'B' if section["bold"] else '', self.DEFAULT_FONT_SIZE)
            self.multi_cell(column_width - 2 * self.COLUMN_PADDING, self.DEFAULT_LINE_HEIGHT, section["text"], border=0, align=self.align)
            

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
        headers = [template.render_header() for template in templates]
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



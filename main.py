from fpdf import FPDF
from generator_text2 import DAPTemplateUkraine
from generator_text import DAPTemplateEnglish
from generator_text3 import DAPTemplateRus
import requests
import os
from dotenv import load_dotenv
load_dotenv()

from typing import Dict, Any

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

        # Генерируем заголовки используя переданные шаблоны
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

# Базовый словарь параметров (на английском языке)
base_contract_params = {
    'contract_number': '1234567890',
    'date': '2024-01-01',
    'seller_name': 'LLC "Best Grain"',
    'seller_representative': 'Ivan Ivanov',
    'buyer_name': 'LLC "AgroImport"',
    'buyer_representative': 'John Smith',
    'goods_description': 'Ukrainian wheat in bulk',
    'incoterms_year': '2024',
    'quantity': 1000,
    'tolerance': 5,
    'metrics': [
        "\nProtein: base 10.5%, not less than 9% (N x 5.7 on dry basis)\nThe Buyer applies a penalty of 1% of the delivered quantity / contract price for each reduction of 1% from the base protein ratio. No bonuses are provided for protein above 10.5%.",
        "\nMoisture: base 14.0%, max 15%\nThe Buyer applies a penalty of 1% of the delivered quantity / contract price for each excess of 1% of the base proportional moisture. No bonuses are provided for moisture below 14%."
    ],
    'price_per_ton': 250,
    'price_per_ton_text': 'two hundred and fifty',
    'total_value': 250000,
    'total_value_text': 'two hundred and fifty thousand',
    'delivery_start_date': '01.01.2025',
    'delivery_end_date': '31.12.2025',
    'exporter_name': '_______________________',
    'edrpou_code': '________',
    'delivery_address': 'Odessa region, Odessa district, Yuzhny port, berth No. 17, LLC "TIS-MINDOBRIVA" or Yuzhny port, berth No. 16, LLC "TIS-MINDOBRIVA"',
    'first_payment_percent': 90,
    'first_payment_days': 3,
    'second_payment_percent': 10,
    'second_payment_days': 10,
    'seller_email': 'seller@example.com',
    'buyer_email': 'buyer@example.com'
}

def translate_with_deepl(text: str, target_lang: str, api_key: str = None) -> str:
    """
    Переводит текст с помощью DeepL API
    """
    if not api_key:
        api_key = os.getenv('DEEPL_API_KEY')
    
    if not api_key:
        print("⚠️ DeepL API ключ не найден. Используйте переменную окружения DEEPL_API_KEY")
        return text
    
    url = "https://api-free.deepl.com/v2/translate"
    headers = {"Authorization": f"DeepL-Auth-Key {api_key}"}
    

    lang_mapping = {
        'uk': 'UK',
        'ru': 'RU',
        'en': 'EN' 
    }
    
    target_lang_code = lang_mapping.get(target_lang, target_lang.upper())
    
    data = {
        "text": [text],
        "target_lang": target_lang_code
    }
    
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        response.raise_for_status()
        result = response.json()
        return result['translations'][0]['text']
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при переводе через DeepL: {e}")
        return text
    except (KeyError, IndexError) as e:
        print(f"❌ Ошибка при обработке ответа DeepL: {e}")
        return text

def translate_contract_params_deepl(language: str, api_key: str = None) -> Dict[str, Any]:
    """
    Создает словарь параметров для указанного языка с автоматическим переводом через DeepL
    """
    if language == 'en':
        return base_contract_params.copy()
    
    # Создаем копию базового словаря
    translated_params = base_contract_params.copy()
    
    # Поля, которые нужно переводить
    translatable_fields = [
        'seller_name',
        'seller_representative', 
        'buyer_name',
        'buyer_representative',
        'goods_description',
        'delivery_address'
    ]
    
    # Переводим текстовые поля
    for field in translatable_fields:
        if field in translated_params and isinstance(translated_params[field], str):
            print(f"🔄 Перевод {field}: {translated_params[field][:50]}...")
            translated_params[field] = translate_with_deepl(
                translated_params[field], language, api_key
            )
    
    # Переводим метрики (список строк)
    if 'metrics' in translated_params and isinstance(translated_params['metrics'], list):
        print(f"🔄 Перевод metrics...")
        translated_metrics = []
        for metric in translated_params['metrics']:
            translated_metric = translate_with_deepl(metric, language, api_key)
            translated_metrics.append(translated_metric)
        translated_params['metrics'] = translated_metrics
    
    # Переводим числовые значения в текст
    if 'price_per_ton' in translated_params:
        price_text = translate_with_deepl(
            f"{translated_params['price_per_ton']} dollars per ton", 
            language, api_key
        )
        translated_params['price_per_ton_text'] = price_text
    
    if 'total_value' in translated_params:
        total_text = translate_with_deepl(
            f"{translated_params['total_value']} dollars", 
            language, api_key
        )
        translated_params['total_value_text'] = total_text
    
    return translated_params

# Генерация параметров для всех языков
contract_params_uk = translate_contract_params_deepl('uk')
contract_params_en = translate_contract_params_deepl('en')
contract_params_ru = translate_contract_params_deepl('ru')

contract_template_ukraine = DAPTemplateUkraine(contract_params_uk)
contract_template_english = DAPTemplateEnglish(contract_params_en)
contract_template_russia = DAPTemplateRus(contract_params_ru)

# Генерация секций для всех трех языков
ukraine_section = contract_template_ukraine.render_all_sections()
english_section = contract_template_english.render_all_sections()
ru_section = contract_template_russia.render_all_sections()

if __name__ == "__main__":
    pdf = ContractPDF(num_columns=3)
    pdf.add_text([contract_template_ukraine, contract_template_english, contract_template_russia], ukraine_section, english_section, ru_section)
    pdf.output("contract_w.pdf")

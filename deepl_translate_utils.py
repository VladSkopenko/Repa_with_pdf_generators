import os
import re
import requests
from typing import Dict, Any, List
from trasliterat import Transliterator
import copy

class ContractTranslator:
    DEEPL_URL = "https://api-free.deepl.com/v2/translate"
    LANG_MAP = {'uk': 'UK', 'ru': 'RU', 'en': 'EN'}

    def __init__(self, language: str):

        self.language = language
        self.api_key = os.getenv('DEEPL_API_KEY')
        self.transliterator = Transliterator()


    def _deepl_request(self, text: str) -> str:
        if not self.api_key:
            return text

        target_lang_code = self.LANG_MAP.get(self.language, self.language.upper())
        headers = {"Authorization": f"DeepL-Auth-Key {self.api_key}"}
        data = {"text": [text], "target_lang": target_lang_code}

        try:
            response = requests.post(self.DEEPL_URL, headers=headers, data=data, timeout=10)
            response.raise_for_status()
            return response.json()['translations'][0]['text']
        except (requests.RequestException, KeyError, IndexError) as e:
            return text

    def _translate_text(self, text: str) -> str:
        return self._deepl_request(text)

    def _translate_list(self, items: List[str]) -> List[str]:
        return [self._translate_text(item) for item in items]

    def _translate_field(self, params: dict, field: str):
        if field in params and isinstance(params[field], str):
            params[field] = self._translate_text(params[field])

    def _translate_company_name(self, name: str) -> str:
        match = re.match(r'^([A-Za-zА-Яа-яЁёІіЇїЄєҐґ]+)\s*[\'"]?(.+?)[\'"]?$', name)
        if match:
            abbr, company = match.groups()
        else:
            abbr, company = '', name

        abbr_for_lang = self.transliterator.transform_abbr(abbr, self.language)

        if self.language == 'en':
            translated = self._translate_text(company)
            return f'{abbr_for_lang} "{translated}"' if abbr_for_lang else f'"{translated}"'
        elif self.language == 'uk':
            translit = self.transliterator.transliterate(company, 'lat_to_cyr_uk')
            return f'{abbr_for_lang} "{translit}"' if abbr_for_lang else f'"{translit}"'
        elif self.language == 'ru':
            translit = self.transliterator.transliterate(company, 'lat_to_cyr_ru')
            return f'{abbr_for_lang} "{translit}"' if abbr_for_lang else f'"{translit}"'
        else:
            return name

    def translate_contract(self, contract_params: dict) -> Dict[str, Any]:
        if self.language == 'en':
            return copy.deepcopy(contract_params)

        translated = copy.deepcopy(contract_params)

        transliteratable = ['seller_name', 'buyer_name']
        translatable = ['seller_representative', 'buyer_representative', 'goods_description', 'delivery_address',]

        for field in transliteratable:
            if field in translated and isinstance(translated[field], str):
                translated[field] = self._translate_company_name(translated[field])

        for field in translatable:
            self._translate_field(translated, field)

        if isinstance(translated.get('metrics'), list):
            translated['metrics'] = self._translate_list(translated['metrics'])

        if 'price_per_ton' in translated:
            translated['price_per_ton_text'] = self._translate_text(
                f"{translated['price_per_ton']} dollars per ton")

        if 'total_value' in translated:
            translated['total_value_text'] = self._translate_text(
                f"{translated['total_value']} dollars")

        return translated
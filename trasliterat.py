class Transliterator:
    def __init__(self):
        self.language_maps = {
            'cyr_to_lat': {
                'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
                'Г': 'G', 'г': 'g', 'Ґ': 'G', 'ґ': 'g', 'Д': 'D', 'д': 'd',
                'Е': 'E', 'е': 'e', 'Є': 'Ye', 'є': 'ye', 'Ё': 'Yo', 'ё': 'yo',
                'Ж': 'Zh', 'ж': 'zh', 'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i',
                'І': 'I', 'і': 'i', 'Ї': 'Yi', 'ї': 'yi', 'Й': 'Y', 'й': 'y',
                'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l', 'М': 'M', 'м': 'm',
                'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p',
                'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's', 'Т': 'T', 'т': 't',
                'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh',
                'Ц': 'Ts', 'ц': 'ts', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh',
                'Щ': 'Shch', 'щ': 'shch', 'Ъ': '', 'ъ': '', 'Ы': 'Y', 'ы': 'y',
                'Ь': '', 'ь': '', 'Э': 'E', 'э': 'e', 'Ю': 'Yu', 'ю': 'yu',
                'Я': 'Ya', 'я': 'ya',
            },
            'lat_to_cyr_ru': {
                'Shch': 'Щ', 'shch': 'щ', 'Zh': 'Ж', 'zh': 'ж', 'Ch': 'Ч', 'ch': 'ч',
                'Sh': 'Ш', 'sh': 'ш', 'Kh': 'Х', 'kh': 'х', 'Ts': 'Ц', 'ts': 'ц',
                'Yo': 'Ё', 'yo': 'ё', 'Ye': 'Є', 'ye': 'є', 'Yi': 'Ї', 'yi': 'ї',
                'Yu': 'Ю', 'yu': 'ю', 'Ya': 'Я', 'ya': 'я', 'A': 'А', 'a': 'а',
                'B': 'Б', 'b': 'б', 'V': 'В', 'v': 'в', 'G': 'Г', 'g': 'г',
                'D': 'Д', 'd': 'д', 'E': 'Е', 'e': 'е', 'Z': 'З', 'z': 'з',
                'I': 'И', 'i': 'и', 'Y': 'Й', 'y': 'й', 'K': 'К', 'к': 'к',
                'L': 'Л', 'л': 'л', 'M': 'М', 'm': 'м', 'N': 'Н', 'n': 'н',
                'O': 'О', 'o': 'о', 'P': 'П', 'p': 'п', 'R': 'Р', 'r': 'р',
                'S': 'С', 's': 'с', 'T': 'Т', 't': 'т', 'U': 'У', 'u': 'у',
                'F': 'Ф', 'f': 'ф',
            },
            'lat_to_cyr_uk': {
                'Shch': 'Щ', 'shch': 'щ', 'Zh': 'Ж', 'zh': 'ж', 'Ch': 'Ч', 'ch': 'ч',
                'Sh': 'Ш', 'sh': 'ш', 'Kh': 'Х', 'kh': 'х', 'Ts': 'Ц', 'ts': 'ц',
                'Yo': 'Ё', 'yo': 'ё', 'Ye': 'Є', 'ye': 'є', 'Yi': 'Ї', 'yi': 'ї',
                'Yu': 'Ю', 'yu': 'ю', 'Ya': 'Я', 'я': 'я', 'A': 'А', 'a': 'а',
                'B': 'Б', 'b': 'б', 'V': 'В', 'v': 'в', 'G': 'Г', 'g': 'г',
                'D': 'Д', 'd': 'д', 'E': 'Е', 'e': 'е', 'Z': 'З', 'z': 'з',
                'I': 'І', 'i': 'і', 'Y': 'Й', 'y': 'й', 'K': 'К', 'к': 'к',
                'L': 'Л', 'л': 'л', 'M': 'М', 'm': 'м', 'N': 'Н', 'n': 'н',
                'O': 'О', 'o': 'о', 'P': 'П', 'p': 'п', 'R': 'Р', 'r': 'р',
                'S': 'С', 's': 'с', 'T': 'Т', 't': 'т', 'U': 'У', 'u': 'у',
                'F': 'Ф', 'f': 'ф',
            }
        }
        self.abbr_map = {
            'en': {'LLC': 'LLC', 'LTD': 'LTD', 'INC': 'INC', 'ТОВ': 'LLC', 'ООО': 'LLC', 'АТ': 'INC', 'ЗАТ': 'LTD'},
            'uk': {'LLC': 'ТОВ', 'LTD': 'ТОВ', 'INC': 'АТ', 'ТОВ': 'ТОВ', 'ООО': 'ТОВ', 'АТ': 'АТ', 'ЗАТ': 'ЗАТ'},
            'ru': {'LLC': 'ООО', 'LTD': 'ООО', 'INC': 'АО', 'ТОВ': 'ООО', 'ООО': 'ООО', 'АТ': 'АО', 'ЗАТ': 'ЗАО'},
        }

    def transform_abbr(self, abbr: str, target_lang: str) -> str:
        abbr = abbr.upper()
        return self.abbr_map.get(target_lang, {}).get(abbr, abbr)
    

    
    def transliterate(self, text: str, direction: str) -> str:
        """Main transliteration function"""
        if direction not in self.language_maps:
            raise ValueError(f"Unknown direction: {direction}. Available: {list(self.language_maps.keys())}")
        
        mapping = self.language_maps[direction]
        
        if any(len(key) > 1 for key in mapping.keys()):
            return self._transliterate_multi_char(text, mapping)
        else:
            return self._transliterate_single_char(text, mapping)
    
    def _transliterate_single_char(self, text: str, mapping: dict) -> str:
        """Character-by-character transliteration"""
        result = ''
        for char in text:
            result += mapping.get(char, char)
        return result
    
    def _transliterate_multi_char(self, text: str, mapping: dict) -> str:
        """Transliteration with multi-character mapping support"""
        result = ''
        i = 0
        while i < len(text):
            for length in (4, 3, 2, 1):
                part = text[i:i+length]
                if part in mapping:
                    result += mapping[part]
                    i += length
                    break
            else:
                result += text[i]
                i += 1
        return result
    

    
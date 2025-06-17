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
            'lat_to_cyr': {
                'Shch': 'Щ', 'shch': 'щ', 'Zh': 'Ж', 'zh': 'ж', 'Ch': 'Ч', 'ch': 'ч',
                'Sh': 'Ш', 'sh': 'ш', 'Kh': 'Х', 'kh': 'х', 'Ts': 'Ц', 'ts': 'ц',
                'Yo': 'Ё', 'yo': 'ё', 'Ye': 'Є', 'ye': 'є', 'Yi': 'Ї', 'yi': 'ї',
                'Yu': 'Ю', 'yu': 'ю', 'Ya': 'Я', 'ya': 'я', 'A': 'А', 'a': 'а',
                'B': 'Б', 'b': 'б', 'V': 'В', 'v': 'в', 'G': 'Г', 'g': 'г',
                'D': 'Д', 'd': 'д', 'E': 'Е', 'e': 'е', 'Z': 'З', 'z': 'з',
                'I': 'И', 'i': 'і', 'Y': 'Й', 'y': 'й', 'K': 'К', 'k': 'к',
                'L': 'Л', 'l': 'л', 'M': 'М', 'm': 'м', 'N': 'Н', 'n': 'н',
                'O': 'О', 'o': 'о', 'P': 'П', 'p': 'п', 'R': 'Р', 'r': 'р',
                'S': 'С', 's': 'с', 'T': 'Т', 't': 'т', 'U': 'У', 'u': 'у',
                'F': 'Ф', 'f': 'ф',
            }
        }
    
    
    def transliterate(self, text: str, direction: str) -> str:
        """Main transliteration function"""
        if direction not in self.language_maps:
            raise ValueError(f"Unknown direction: {direction}. Available: {list(self.language_maps.keys())}")
        
        mapping = self.language_maps[direction]
        
        # For multi-character mappings (like 'Shch' -> 'Щ')
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


# Usage examples
if __name__ == "__main__":
    # Create class instance
    translit = Transliterator()
    
    # Test existing directions
    print("=== Cyrillic to Latin test ===")
    print(translit.transliterate("АгроМагроКомбінат", 'cyr_to_lat'))
    print(translit.transliterate("Європа", 'cyr_to_lat'))
    print(translit.transliterate("Україна", 'cyr_to_lat'))
    
    print("\n=== Latin to Cyrillic test ===")
    print(translit.transliterate("The best grain", 'lat_to_cyr'))
    
    print(f"\nAvailable directions: {translit.get_available_directions()}")
    
    # Example of adding new language (Greek)
    greek_to_lat = {
        'Α': 'A', 'α': 'a', 'Β': 'B', 'β': 'b', 'Γ': 'G', 'γ': 'g',
        'Δ': 'D', 'δ': 'd', 'Ε': 'E', 'ε': 'e', 'Ζ': 'Z', 'ζ': 'z',
        'Η': 'H', 'η': 'h', 'Θ': 'Th', 'θ': 'th', 'Ι': 'I', 'ι': 'i',
        'Κ': 'K', 'κ': 'k', 'Λ': 'L', 'λ': 'l', 'Μ': 'M', 'μ': 'm',
        'Ν': 'N', 'ν': 'n', 'Ξ': 'X', 'ξ': 'x', 'Ο': 'O', 'ο': 'o',
        'Π': 'P', 'π': 'p', 'Ρ': 'R', 'ρ': 'r', 'Σ': 'S', 'σ': 's',
        'Τ': 'T', 'τ': 't', 'Υ': 'Y', 'υ': 'y', 'Φ': 'F', 'φ': 'f',
        'Χ': 'Ch', 'χ': 'ch', 'Ψ': 'Ps', 'ψ': 'ps', 'Ω': 'O', 'ω': 'o'
    }
    
    translit.add_language_map('greek_to_lat', greek_to_lat)
    print("\n=== Greek to Latin test ===")
    print(translit.transliterate("Αθήνα", 'greek_to_lat'))  # Athina
    



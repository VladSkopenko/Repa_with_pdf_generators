#!/usr/bin/env python3
"""
Тестовый скрипт для проверки DeepL API интеграции
"""

import os
from dotenv import load_dotenv
load_dotenv()
from main import translate_with_deepl, translate_contract_params

def test_deepl_translation():
    """Тестирует базовый перевод через DeepL"""
    
    # Проверяем наличие API ключа
    api_key = os.getenv('DEEPL_API_KEY')
    if not api_key:
        print("❌ DEEPL_API_KEY не найден в переменных окружения")
        print("Установите переменную окружения: set DEEPL_API_KEY=your-key")
        return False
    
    print("✅ API ключ найден")
    
    # Тестируем простой перевод
    test_text = "Hello, this is a test message"
    print(f"\n🔄 Тестируем перевод: '{test_text}'")
    
    try:
        # Перевод на русский
        ru_result = translate_with_deepl(test_text, 'ru', api_key)
        print(f"🇷🇺 Русский: {ru_result}")
        
        # Перевод на украинский
        uk_result = translate_with_deepl(test_text, 'uk', api_key)
        print(f"🇺🇦 Украинский: {uk_result}")
        
        print("\n✅ Базовый перевод работает!")
        
    except Exception as e:
        print(f"❌ Ошибка при тестировании: {e}")
        return False
    
    return True

def test_contract_translation():
    """Тестирует перевод параметров контракта"""
    
    api_key = os.getenv('DEEPL_API_KEY')
    if not api_key:
        print("❌ DEEPL_API_KEY не найден")
        return False
    
    print("\n🔄 Тестируем перевод параметров контракта...")
    
    try:
        # Тестируем перевод на русский
        print("\n🇷🇺 Перевод на русский:")
        ru_params = translate_contract_params('ru', api_key)
        
        print(f"  seller_name: {ru_params['seller_name']}")
        print(f"  goods_description: {ru_params['goods_description']}")
        print(f"  price_per_ton_text: {ru_params['price_per_ton_text']}")
        
        # Тестируем перевод на украинский
        print("\n🇺🇦 Перевод на украинский:")
        uk_params = translate_contract_params('uk', api_key)
        
        print(f"  seller_name: {uk_params['seller_name']}")
        print(f"  goods_description: {uk_params['goods_description']}")
        print(f"  price_per_ton_text: {uk_params['price_per_ton_text']}")
        
        print("\n✅ Перевод параметров контракта работает!")
        
    except Exception as e:
        print(f"❌ Ошибка при переводе контракта: {e}")
        return False
    
    return True

def main():
    """Основная функция тестирования"""
    print("🧪 Тестирование DeepL API интеграции")
    print("=" * 50)
    
    # Тест 1: Базовый перевод
    if not test_deepl_translation():
        print("\n❌ Базовый тест не прошел")
        return
    
    # Тест 2: Перевод контракта
    if not test_contract_translation():
        print("\n❌ Тест контракта не прошел")
        return
    
    print("\n🎉 Все тесты прошли успешно!")
    print("DeepL API интеграция работает корректно")


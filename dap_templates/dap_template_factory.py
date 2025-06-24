from dap_templates.dap_ukraine import DAPTemplateUkraine
from dap_templates.dap_english import DAPTemplateEnglish
from dap_templates.dap_rus import DAPTemplateRus
from deepl_translate_utils import ContractTranslator


class ContractTemplateFactory:
    template_map = {
        "uk": DAPTemplateUkraine,
        "en": DAPTemplateEnglish,
        "ru": DAPTemplateRus,
    }

    @classmethod
    def get_template(cls, lang, params):
        if lang not in cls.template_map:
            raise ValueError(f"Unsupported language: {lang}")
        params = ContractTranslator(language=lang).translate_contract(
            contract_params=params
        )
        return cls.template_map[lang](params)

    @classmethod
    def get_templates(cls, langs, params):
        if isinstance(langs, str):
            langs = [langs]
        return [cls.get_template(lang, params=params) for lang in langs]

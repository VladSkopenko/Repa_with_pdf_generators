params = {
    "contract_number": "1234567890",
    "date": "2024-01-01",
    "seller_name": 'LLC "Best Grain"',
    "seller_representative": "Ivan Ivanov",
    "buyer_name": 'LLC "AgroImport"',
    "buyer_representative": "John Smith",
    "goods_description": "Ukrainian wheat in bulk",
    "incoterms_year": "2024",
    "quantity": 1000,
    "tolerance": 5,
    "metrics": [
        "\nProtein: base 10.5%, not less than 9% (N x 5.7 on dry basis)\nThe Buyer applies a penalty of 1% of the delivered quantity / contract price for each reduction of 1% from the base protein ratio. No bonuses are provided for protein above 10.5%.",
        "\nMoisture: base 14.0%, max 15%\nThe Buyer applies a penalty of 1% of the delivered quantity / contract price for each excess of 1% of the base proportional moisture. No bonuses are provided for moisture below 14%.",
    ],
    "price_per_ton": 250,
    "price_per_ton_text": "two hundred and fifty",
    "total_value": 250000,
    "total_value_text": "two hundred and fifty thousand",
    "delivery_start_date": "01.01.2025",
    "delivery_end_date": "31.12.2025",
    "exporter_name": "_______________________",
    "edrpou_code": "________",
    "delivery_address": 'Odessa region, Odessa district, Yuzhny port, berth No. 17, LLC "TIS-MINDOBRIVA" or Yuzhny port, berth No. 16, LLC "TIS-MINDOBRIVA"',
    "first_payment_percent": 90,
    "first_payment_days": 3,
    "second_payment_percent": 10,
    "second_payment_days": 10,
    "seller_email": "seller@example.com",
    "buyer_email": "buyer@example.com",
}


if __name__ == "__main__":
    langs = ["uk", "en", "ru"]
    templates = ContractTemplateFactory.get_templates(langs, params=params)
    sections = [template.render_all_sections() for template in templates]
    pdf = ContractPDF(num_columns=len(langs))
    pdf.add_text(templates, *sections)
    pdf.output("contract_w.pdf")

from pprint import pprint
from t import split_sections

class ContractTemplateEnglish:
    def __init__(
        self,
        contract_number,
        date,
        seller_name,
        seller_representative,
        buyer_name,
        buyer_representative,
    ):
        self.contract_number = contract_number
        self.date = date
        self.seller_name = seller_name
        self.seller_representative = seller_representative
        self.buyer_name = buyer_name
        self.buyer_representative = buyer_representative

    def render_header(self):
        return (
            f"CONTRACT  № C-W {self.contract_number}\n"
            f"{self.date}"
        )

    def render_parties(self):
        return (
            f"The present Contract (hereinafter referred to as the \"Contract\") is concluded between the company"
            f"{self.buyer_name}(\"Buyer\") represented by {self.buyer_representative}, acting on the basis of Charter of the company, from one side, and {self.seller_name} (the \"Seller\") represented by the Director {self.seller_representative}, acting on the basis of the Company's Charter.\n\n"
            f"Taking into account the terms and conditions contained in this document, the parties have agreed as follows:"
        )

    def render_goods(self, product_description, production_year):
        return (
            "1.1. In the manner and under the terms and conditions specified in this Contract, the Seller sells, and the Buyer accepts and pays for agricultural products, namely:\n"
            f"{product_description}, {production_year} production years (hereinafter \"Goods\").\n"
        )
    
    def render_quantity_sections(self, quantity, tolerance):
        return [
            {"text": "2.1. The unit of quantity for the Goods is a metric ton (1000 kg).", "bold": False},
            {"text": f"2.2. The total quantity: {quantity} MT +/- {tolerance}% at Seller's choice.", "bold": False},
            {"text": "2.3. The weight of the delivered Goods is finally determined based on the results of weighing after arrival at the delivery location. Type of transport: cargo transport.", "bold": False},
            {"text": "2.4. The quantity of the Goods shall be determined by weight, respectively, during unloading of motor vehicles and/or railway wagons at the place of delivery: by the Terminal laboratory.  The Seller has the right to appoint its representatives, at its own expense, to monitor the quantity of the Goods during unloading. If the Seller does not ensure the timely presence of its representatives, the unloading of the cargo transport will be carried out without them, and the data on the quantity of the unloaded Goods determined by weighing at the delivery location will be recognized by both Parties to the Contract.", "bold": False},
            {"text": "2.5. If during the weighing of the wagon at the destination station a discrepancy between the gross weight in the railway consignment note and the overload weight of more than 0.5% is detected, the Buyer shall notify in writing of such discrepancy within 1 (one) hour by sending a message to the e-mail address specified in the Contract, and the wagon shall be unloaded only on the basis of a written permission, which the Seller shall provide within 4 (four) hours to the Buyer by sending a message to the e-mail address specified in this Contract. The Buyer shall have the right to agree to the place specified herein or to send its representative for the control weighing of the Goods, and the Seller's representative shall arrive within 12 hours from the moment of notification of the shortage.", "bold": False},
            {"text": "In the event of failure to deliver the agreed quantity of Goods, the Seller undertakes to:", "bold": False},
            {"text": "-     deliver the missing Goods within 3 days;", "bold": False},
            {"text": "-   if payment has been made, refund the Buyer within 3 days from the date of the corresponding demand by the Buyer.", "bold": False},
            {"text": "Additionally, the Buyer has the right to purchase the missing quantity of Goods from other counterparties. The Seller will be obligated to compensate the cost of such Goods and transportation and logistics expenses within 3 days from the date of the Buyer's written demand.\n", "bold": False},
        ]
    
    def render_quality_sections(self, metrics: list[str]):
        sections = [
            {"text": "\n3. QUALITY AND CONDITIONS OF THE GOODS:", "bold": True},
            {"text": "3.1. The quality of the Goods under this Contract shall correspond to the following indicators:\n", "bold": False},
        ]
   
        for metric in metrics:
            sections.append({"text": metric, "bold": False})

        sections.extend([
            {"text": "Ragweed is not accepted.", "bold": False},
            {"text": "All quality indicators must be calculated in accordance with ISO, ICC, and EU standards.", "bold": False},
            {"text": "\n3.2. The Goods must be of high quality, loyal, and suitable for sale, free of foreign/offensive odors, and without castor seeds or other toxic seeds. In addition, the Goods must not contain any unpleasant foreign bodies such as glass, metal, etc. The Goods must not contain GMOs in accordance with regulations and must comply with EU standards regarding pesticides/residues/heavy metals and mycotoxins. The Goods must be free of live insects, without foreign odors or contamination, while maintaining their natural order and color.", "bold": False},
            {"text": "3.3. The Buyer has the right to refuse the Goods in case of any deviation from the baseline. Acceptance of the Goods at a discount is at the discretion of the Buyer if such an option is feasible.", "bold": False},
            {"text": "3.4. In case of delivery by road, the Parties agree that if the quality of the Goods established by the Terminal's laboratory does not meet the permissible deviations, the results of the analysis of the Terminal's laboratory shall be final, not subject to appeal and binding on both Parties.", "bold": False},
            {"text": "3.5. In case of delivery by rail, in case of discrepancy between the actual quality indicators of the Goods and the quality indicators specified in the grain quality certificate issued upon unloading of the Goods by the Terminal laboratory and the quality requirements specified in DSTU, the Seller shall not unload the grain and shall notify the Client of the discrepancies by mail and take measures to arrange for the resolution of disputes.", "bold": False},
            {"text": "In case of disagreement of the Seller with the results of analyses by the laboratory of the Terminal, upon delivery by rail, the Seller shall declare its disagreement to the Buyer and inform about its further actions regarding such Goods. The Seller shall have the right to appoint its representative for repeated (arbitration) sampling and quality analysis of the Goods in the laboratory of the Terminal (arbitration) analysis of grain quality may be carried out in an accredited laboratory of the Grain Storage Company of Ukraine. The results of such analysis shall be final and not subject to appeal.", "bold": False},
            {"text": "The costs associated with arbitration to determine the quality of the disputed batch of Goods, including excessive downtime of wagons, shall be borne by and at the expense of the Seller.", "bold": False},
            {"text": "Regardless of the costs incurred, the Parties agree that the Buyer's liability shall be limited to downtime for three days inclusive. In any case, the Seller shall not have the right to abandon the wagons and shall bear all costs and losses during the time the wagons are on the railway tracks, including the time of independent laboratory tests, notwithstanding the results of such tests.", "bold": False},
            {"text": "3.6. The Buyer has the right to refuse any Goods that do not comply with the contractual quality parameters specified in this Contract. In the case of delivery of a substandard batch of Goods or non-compliance with the agreed parameters, the Buyer has the right to:", "bold": False},
            {"text": "- Reduce the price of the Goods according to the parameters determined in the laboratory's findings;", "bold": False},
            {"text": "- Discount the price of the delivered Goods. The parameters for discounting are defined in clause 3.1 of this Contract;", "bold": False},
            {"text": "- Compensate the Buyer for the cost of processing the Goods to meet the established quality parameters;", "bold": False},
            {"text": "- Deliver an additional quantity of Goods at a reduced price;", "bold": False},
            {"text": "- Supply/replace the Goods in accordance with the terms set forth in the Contract;", "bold": False},
            {"text": "- Refuse acceptance and payment for the Goods, as well as demand compensation for all costs, including but not limited to transport and logistics services, penalties, and financial sanctions imposed on the Buyer by counterparties (partners under subsequent Contracts for Goods supply) due to such shortfalls or poor-quality Goods. The Buyer may also claim compensation for damages incurred as a result of accepting substandard Goods.", "bold": False},
            {"text": "3.7. Replacement of Goods is carried out at the Seller's expense within 3 (three) business days from the date of the Buyer's claim.", "bold": False},
            {"text": "3.8.When discounting the Goods, a notice of price discounting shall be sent to the Seller's representative by e-mail or electronic communication channel specified in the Contract details. Upon receipt of the notification by e-mail about the need to discount the price, the Seller shall, within one (1) hour, agree to the discount if the Goods are delivered by road. If the delivery is carried out by rail, the Seller shall either agree to the price discount or notify the Seller of sending its representative to take joint samples and draw up the Certificate of Non-Conformity of the Goods. If the Seller does not respond within 1 hour after the Buyer sends an e-mail, the Buyer shall decide on the price discount at its sole discretion.", "bold": False},
            {"text": "3.9. In the event of agreement on price discounting by the Seller, the parties agree that the data used as the basis for price discounting due to non-compliance with quality and safety standards shall include laboratory test results conducted at the delivery location or an independent laboratory selected by the Buyer, along with data recorded in the Non-Conformity Report.", "bold": False},
            {"text": "3.10. If the Goods are accepted at a discounted price based on the Buyer's data, the Seller undertakes to issue the customs declaration (VMD) based on the discounted price data provided by the Buyer.", "bold": False},
            {"text": "3.11. In case of discrepancies in the Goods' quantity/quality, the Buyer has the right to withhold payment for the entire quantity of undelivered/substandard Goods until corrected documentation is provided:", "bold": False},
            {"text": " 3.11.1. Data indicated in the waybill (TTN), considering the Buyer's remarks, if any;", "bold": False},
            {"text": "  3.12.2. Laboratory test data, considering the price discounting.\n", "bold": False},
        ])
        return sections

    def render_price(self, price_per_ton, price_per_ton_text, total_value, total_value_text):
        return [
            {"text": "\n4. PRICE:", "bold": True},
            {"text": f"4.1. The price per one metric ton of the Goods is {price_per_ton} 00 US dollars ( {price_per_ton_text} USD).", "bold": False},
            {"text": f"4.2. The total value of the Goods under the Contract {total_value} 00 USD ({total_value_text} USD).", "bold": False},
        ]

    def render_all_sections(self, goods_description, incoterms_year, quantity, tolerance, metrics, price_per_ton, price_per_ton_text, total_value, total_value_text):
        sections = [
            {"text": self.render_parties().strip(), "bold": False},
            {"text": "\n1. GOODS: ", "bold": True},
            {"text": self.render_goods(goods_description, incoterms_year).strip(), "bold": False},
            {"text": "\n2. QUANTITY: ", "bold": True},
        ]
        sections.extend(self.render_quantity_sections(quantity, tolerance))
        sections.extend(self.render_quality_sections(metrics))
        sections.extend(self.render_price(price_per_ton, price_per_ton_text, total_value, total_value_text))
        return split_sections(sections)


contract_template_english = ContractTemplateEnglish(
    contract_number="1234567890",
    date="2024-01-01",
    seller_name="Best Grain LLC",
    seller_representative="Ivan Ivanov",
    buyer_name="AgroImport Ltd",
    buyer_representative="John Smith",
)

if __name__ == "__main__":
    sections_uk = contract_template_english.render_all_sections(
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
    pprint(sections_uk)
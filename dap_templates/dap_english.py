from pprint import pprint
from t import split_sections

class DAPTemplateEnglish:
    def __init__(self, contract_params):
        """
        contract_params = {
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
            'metrics': [...],
            'price_per_ton': 250,
            'price_per_ton_text': 'two hundred and fifty',
            'total_value': 250000,
            'total_value_text': 'two hundred and fifty thousand',
            'delivery_start_date': '01.01.2025',
            'delivery_end_date': '31.12.2025',
            'exporter_name': '_______________________',
            'edrpou_code': '________',
            'delivery_address': '...',
            'first_payment_percent': 90,
            'first_payment_days': 3,
            'second_payment_percent': 10,
            'second_payment_days': 10,
            'seller_email': 'seller@example.com',
            'buyer_email': 'buyer@example.com'
        }
        """  
        self.params = contract_params

    def render_header(self):
        return (
            f"CONTRACT  № C-W {self.params['contract_number']}\n"
            f"{self.params['date']}"
        )

    def render_parties(self):
        return [
            {"text": f"The present Contract (hereinafter referred to as the \"Contract\") is concluded between the company "
            f"{self.params['buyer_name']}(\"Buyer\") represented by {self.params['buyer_representative']}, acting on the basis of Charter of the company, from one side, and {self.params['seller_name']} (the \"Seller\") represented by the Director {self.params['seller_representative']}, acting on the basis of the Company's Charter.\n\n"
            f"Taking into account the terms and conditions contained in this document, the parties have agreed as follows:", "bold": False}
        ]

    def render_goods(self):
        return [
            {"text": "\n1. GOODS:", "bold": True},
            {"text": f"\n1.1. In accordance with the terms and conditions specified in this Contract, the Seller sells and the Buyer accepts and pays for agricultural products, namely: {self.params['goods_description']} according to Incoterms {self.params['incoterms_year']}.", "bold": False}
        ]
    
    def render_quantity_sections(self):
        return [
            {"text": "\n2. QUANTITY: ", "bold": True},
            {"text": "\n2.1. The unit of quantity for the Goods is a metric ton (1000 kg).", "bold": False},
            {"text": f"\n2.2. The total quantity: {self.params['quantity']} MT +/- {self.params['tolerance']}% at Seller's choice.", "bold": False},
            {"text": "\n2.3. The weight of the delivered Goods is finally determined based on the results of weighing after arrival at the delivery location. Type of transport: cargo transport.", "bold": False},
            {"text": "\n2.4. The quantity of the Goods shall be determined by weight, respectively, during unloading of motor vehicles and/or railway wagons at the place of delivery: by the Terminal laboratory.  The Seller has the right to appoint its representatives, at its own expense, to monitor the quantity of the Goods during unloading. If the Seller does not ensure the timely presence of its representatives, the unloading of the cargo transport will be carried out without them, and the data on the quantity of the unloaded Goods determined by weighing at the delivery location will be recognized by both Parties to the Contract.", "bold": False},
            {"text": "\n2.5. If during the weighing of the wagon at the destination station a discrepancy between the gross weight in the railway consignment note and the overload weight of more than 0.5% is detected, the Buyer shall notify in writing of such discrepancy within 1 (one) hour by sending a message to the e-mail address specified in the Contract, and the wagon shall be unloaded only on the basis of a written permission, which the Seller shall provide within 4 (four) hours to the Buyer by sending a message to the e-mail address specified in this Contract. The Buyer shall have the right to agree to the place specified herein or to send its representative for the control weighing of the Goods, and the Seller's representative shall arrive within 12 hours from the moment of notification of the shortage.", "bold": False},
            {"text": "\nIn the event of failure to deliver the agreed quantity of Goods, the Seller undertakes to:", "bold": False},
            {"text": "\n-     deliver the missing Goods within 3 days;", "bold": False},
            {"text": "\n-   if payment has been made, refund the Buyer within 3 days from the date of the corresponding demand by the Buyer.", "bold": False},
            {"text": "\nAdditionally, the Buyer has the right to purchase the missing quantity of Goods from other counterparties. The Seller will be obligated to compensate the cost of such Goods and transportation and logistics expenses within 3 days from the date of the Buyer's written demand.\n", "bold": False},
        ]
    
    def render_quality_sections(self):
        sections = [
            {"text": "\n3. QUALITY AND CONDITIONS OF THE GOODS:", "bold": True},
            {"text": "\n3.1. The quality of the Goods under this Contract shall correspond to the following indicators:\n", "bold": False},
        ]
   
        for metric in self.params['metrics']:
            sections.append({"text": metric, "bold": False})

        sections.extend([
            {"text": "\nRagweed is not accepted.", "bold": False},
            {"text": "\nAll quality indicators must be calculated in accordance with ISO, ICC, and EU standards.", "bold": False},
            {"text": "\n3.2. The Goods must be of high quality, loyal, and suitable for sale, free of foreign/offensive odors, and without castor seeds or other toxic seeds. In addition, the Goods must not contain any unpleasant foreign bodies such as glass, metal, etc. The Goods must not contain GMOs in accordance with regulations and must comply with EU standards regarding pesticides/residues/heavy metals and mycotoxins. The Goods must be free of live insects, without foreign odors or contamination, while maintaining their natural order and color.", "bold": False},
            {"text": "\n3.3. The Buyer has the right to refuse the Goods in case of any deviation from the baseline. Acceptance of the Goods at a discount is at the discretion of the Buyer if such an option is feasible.", "bold": False},
            {"text": "\n3.4. In case of delivery by road, the Parties agree that if the quality of the Goods established by the Terminal's laboratory does not meet the permissible deviations, the results of the analysis of the Terminal's laboratory shall be final, not subject to appeal and binding on both Parties.", "bold": False},
            {"text": "\n3.5. In case of delivery by rail, in case of discrepancy between the actual quality indicators of the Goods and the quality indicators specified in the grain quality certificate issued upon unloading of the Goods by the Terminal laboratory and the quality requirements specified in DSTU, the Seller shall not unload the grain and shall notify the Client of the discrepancies by mail and take measures to arrange for the resolution of disputes.", "bold": False},
            {"text": "\nIn case of disagreement of the Seller with the results of analyses by the laboratory of the Terminal, upon delivery by rail, the Seller shall declare its disagreement to the Buyer and inform about its further actions regarding such Goods. The Seller shall have the right to appoint its representative for repeated (arbitration) sampling and quality analysis of the Goods in the laboratory of the Terminal (arbitration) analysis of grain quality may be carried out in an accredited laboratory of the Grain Storage Company of Ukraine. The results of such analysis shall be final and not subject to appeal.", "bold": False},
            {"text": "\nThe costs associated with arbitration to determine the quality of the disputed batch of Goods, including excessive downtime of wagons, shall be borne by and at the expense of the Seller.", "bold": False},
            {"text": "\nRegardless of the costs incurred, the Parties agree that the Buyer's liability shall be limited to downtime for three days inclusive. In any case, the Seller shall not have the right to abandon the wagons and shall bear all costs and losses during the time the wagons are on the railway tracks, including the time of independent laboratory tests, notwithstanding the results of such tests.", "bold": False},
            {"text": "\n3.6. The Buyer has the right to refuse any Goods that do not comply with the contractual quality parameters specified in this Contract. In the case of delivery of a substandard batch of Goods or non-compliance with the agreed parameters, the Buyer has the right to:", "bold": False},
            {"text": "\n- Reduce the price of the Goods according to the parameters determined in the laboratory's findings;", "bold": False},
            {"text": "\n- Discount the price of the delivered Goods. The parameters for discounting are defined in clause 3.1 of this Contract;", "bold": False},
            {"text": "\n- Compensate the Buyer for the cost of processing the Goods to meet the established quality parameters;", "bold": False},
            {"text": "\n- Deliver an additional quantity of Goods at a reduced price;", "bold": False},
            {"text": "\n- Supply/replace the Goods in accordance with the terms set forth in the Contract;", "bold": False},
            {"text": "\n- Refuse acceptance and payment for the Goods, as well as demand compensation for all costs, including but not limited to transport and logistics services, penalties, and financial sanctions imposed on the Buyer by counterparties (partners under subsequent Contracts for Goods supply) due to such shortfalls or poor-quality Goods. The Buyer may also claim compensation for damages incurred as a result of accepting substandard Goods.", "bold": False},
            {"text": "\n3.7. Replacement of Goods is carried out at the Seller's expense within 3 (three) business days from the date of the Buyer's claim.", "bold": False},
            {"text": "\n3.8.When discounting the Goods, a notice of price discounting shall be sent to the Seller's representative by e-mail or electronic communication channel specified in the Contract details. Upon receipt of the notification by e-mail about the need to discount the price, the Seller shall, within one (1) hour, agree to the discount if the Goods are delivered by road. If the delivery is carried out by rail, the Seller shall either agree to the price discount or notify the Seller of sending its representative to take joint samples and draw up the Certificate of Non-Conformity of the Goods. If the Seller does not respond within 1 hour after the Buyer sends an e-mail, the Buyer shall decide on the price discount at its sole discretion.", "bold": False},
            {"text": "\n3.9. In the event of agreement on price discounting by the Seller, the parties agree that the data used as the basis for price discounting due to non-compliance with quality and safety standards shall include laboratory test results conducted at the delivery location or an independent laboratory selected by the Buyer, along with data recorded in the Non-Conformity Report.", "bold": False},
            {"text": "\n3.10. If the Goods are accepted at a discounted price based on the Buyer's data, the Seller undertakes to issue the customs declaration (VMD) based on the discounted price data provided by the Buyer.", "bold": False},
            {"text": "\n3.11. In case of discrepancies in the Goods' quantity/quality, the Buyer has the right to withhold payment for the entire quantity of undelivered/substandard Goods until corrected documentation is provided:", "bold": False},
            {"text": "\n 3.11.1. Data indicated in the waybill (TTN), considering the Buyer's remarks, if any;", "bold": False},
            {"text": "\n  3.12.2. Laboratory test data, considering the price discounting.\n", "bold": False},
        ])
        return sections
    
    def render_price(self):
        return [
        {"text": "\n4. PRICE:", "bold": True},
        {"text": f"\n4.1. The price per one metric ton of the Goods is {self.params['price_per_ton']} 00 US dollars ( {self.params['price_per_ton_text']} USD).", "bold": False},
        {"text": f"\n4.2. The total value of the Goods under the Contract {self.params['total_value']} 00 USD ({self.params['total_value_text']} USD).", "bold": False},
    ]

    def render_delivery_sections(self):
        sections = [
            {"text": "\n5. DELIVERY TERMS AND CONDITIONS:", "bold": True},
            {"text": "\n5.1. The Seller shall be deemed to have delivered the Goods when the Goods are placed at the disposal of the Buyer at the place determined by the Parties in this Contract, cleared of customs duties necessary for import, on the arrived means of transport, ready for unloading at the specified destination.", "bold": False},
            {"text": "\n5.2. The Seller bears all costs and risks associated with the delivery of the Goods to the destination and is obliged to perform the customs formalities necessary for import, pay any fees levied during import, as well as perform all customs formalities.", "bold": False},
            {"text": f"\n5.3. Supply of the Goods will be carried out on DAP terms. Delivery date: from {self.params['delivery_start_date']} to {self.params['delivery_end_date']} both dates inclusive. The Goods may be supplied in batches. One day before the delivery of the Goods, the Seller notifies the Buyer's email address about the delivery of the corresponding batch of Goods.", "bold": False},
            {"text": "\n5.4. Packaging: 100% bulk.", "bold": False},
            {"text": "\n5.5. Cargo motor transport must be accompanied by the following valid documents:", "bold": False},
            {"text": "\n→   properly executed motor (cargo-transport) waybill for each cargo motor transport, filled out by the Seller in accordance with the Buyer's instructions;", "bold": False},
            {"text": "\n5.6. Railway wagons must be accompanied by the following valid documents:", "bold": False},
            {"text": "\n→   Railway receipts/waybills for each railway wagon in accordance with the Buyer's instructions;", "bold": False},
            {"text": "\n→   Grain quality certificate (form 42), issued by the elevator or grain warehouse at the Goods shipment point.", "bold": False},
            {"text": "\n5.7. The Seller must:", "bold": False},
            {"text": "\na) conclude an appropriate agreement in the port with the Buyer's accredited customs broker and conduct customs clearance of the Goods at its own expense in accordance with the Buyer's instructions; Contact details of the Buyer's customs broker for clarification of customs clearance issues: +380952892570;", "bold": False},
            {"text": "\nb) at its own risk and expense obtain any export license, issue a certificate of origin of the Goods, as well as perform all customs formalities necessary for the export of the Goods.\nThe Seller provides the Forwarder and customs broker in the port for customs clearance of the Goods with all requested without exception documents within the time limits specified by the Forwarder (customs broker). Provided information or documents that have inaccuracies or provision of an incomplete package of documents are considered as not provided to the Forwarder (customs broker). The date of receipt of documents is considered the date of their delivery to the Forwarder (customs broker).", "bold": False},
            {"text": "\n5.8. The Buyer must provide the Seller with all necessary documentary instructions for filling out transport documents by sending by email;", "bold": False},
            {"text": "\n5.9. Implementation of supplies under this Contract is possible only after the Seller/Exporter passes accreditation with the Buyer.", "bold": False},
            {"text": "\n5.10. For supplies by rail transport:", "bold": False},
            {"text": "\nThe Seller sends the Buyer a shipment schedule by email.\nThe Buyer coordinates the provided schedule with the terminal at the delivery location and the Seller, in case of changes to this schedule.\nThe Seller undertakes to supply the Goods only in accordance with the agreed schedule. The shipment schedule must be proportional to the delivery period, unless otherwise agreed by the Parties.\nThe Seller authorizes its freight forwarder to provide the Buyer with the number of its application registered in the AS Mesplan 7 (seven) days before the start of shipment.\nThe Buyer is obliged to organize confirmation of this application in the AS Mesplan from the destination station and consignee/Terminal within 2 days from the date of providing the application number.\nIn case of non-coordination of the electronic application or coordination not in full, or convention introduced by the State Administration of Railway Transport of Ukraine (Ukrainian Railways) and published on the website https://uz.gov.ua/, the delivery time of the Goods is extended for the period of non-coordination and/or validity of the convention.", "bold": False},
            {"text": "\n5.11. The Seller daily sends to the Buyer's address by email a daily report on the shipped Goods (according to the sample provided together with the instructions) indicating the following information:", "bold": False},
            {"text": "\n- Number of this Contract;", "bold": False},
            {"text": "\n- Name of the Exporter;", "bold": False},
            {"text": "\n- Shipment date;", "bold": False},
            {"text": "\n- Station of departure and station of destination;", "bold": False},
            {"text": "\n- Wagon/car number;", "bold": False},
            {"text": "\n- Railway waybill/motor TTN number;", "bold": False},
            {"text": "\n- Name and weight (gross, tare, net) of cargo; Scanned copies of accompanying documents (Grain quality certificate (form 42).", "bold": False},
            {"text": f"\n5.12. Exporters of the Goods under this Contract: {self.params['exporter_name']}, EDRPOU code: {self.params['edrpou_code']}. Change of the Exporter occurs by agreement of both Parties by concluding an Additional Agreement to this Contract.\nThe Seller provides the Buyer with letters from the Exporters specified in this paragraph about their consent to carry out shipment and export of the Goods.\nIf the Seller is not a resident of Ukraine, the Seller confirms that the Goods supplied under this Contract were purchased directly from the Exporter.\nThe Seller provides a guarantee letter from the Exporters specified in this paragraph about the transfer of subsidiary liability from the Seller to the Forwarder in case of violation or non-fulfillment by the Buyer of its obligations under this Contract.", "bold": False},
            {"text": "\n5.13. In case of arrival by rail or motor transport to the Buyer's address of non-conforming Goods (loaded, baked Goods, presence of impurities) the Buyer ensures drawing up acts, on the basis of which the Seller reimburses additional costs associated with unloading, acceptance, storage and return of such Goods, including wagon downtime.\nWagons with residues of fumigants will not be accepted and must be redirected by the Seller within 3 (three) days from the moment of notification by the Buyer. In case of detection of wagons with fumigation residues, the Buyer has the right to issue an invoice for payment of a fine to the Seller in the amount of 300.00 (three hundred) US dollars per wagon per day, and the Seller is obliged to pay such fine within 5 (five) banking days from the date of issuing the invoice.\nThe Seller is obliged to dispose of non-conforming Goods within 3 (three) days from the moment of notification by the Buyer. In case of violation of the deadline established by this paragraph for disposal of non-conforming Goods, the Seller must pay the Buyer penalty sanctions in the amount of 300.00 (three hundred) US dollars for each wagon per day from the moment of connection and until the return of the Goods, and reimburse the Buyer for all incurred losses of documented expenses in connection with such violation.", "bold": False},
            {"text": "\n5.14. The Seller and Exporter guarantee that the Goods being supplied:", "bold": False},
            {"text": "\n- at the time of signing this Contract, as well as at the time of transfer of ownership of the Goods from the Seller to the Buyer, the competent authorities of the Seller do not accept and will not accept decisions on imposing any encumbrances on the Goods (its part), as well as decisions on alienation of the Goods;", "bold": False},
            {"text": "\n- at the time of signing this Contract, as well as at the time of transfer of ownership of the Goods from the Seller to the Buyer, the Goods are not and will not be in tax pledge, in dispute and under prohibition on alienation;", "bold": False},
            {"text": "\n- at the time of signing this Contract, as well as at the time of transfer of ownership of the Goods from the Seller to the Buyer, the Goods will not be sold, donated, assigned, exchanged, allocated from the composition of the Seller's assets or pledged, transferred to management, and will not be transferred for rent (use) in whole or in parts;", "bold": False},
            {"text": "\n- at the time of signing this Contract, as well as at the time of transfer of ownership of the Goods from the Seller to the Buyer, the Goods are in good condition and essentially correspond to the purposes for which it is intended, and does not contain any substances or materials that have defects or pose a risk to health or safety;", "bold": False},
            {"text": "\n- at the time of signing this Contract, as well as at the time of transfer of ownership of the Goods from the Seller to the Buyer, the Seller has no obligations, the term of which has come or will come in the future (including under previous contracts, offers, options, etc.) for alienation of the Goods, transfer of individual rights (right of use, right of disposal, right of ownership) to the Goods;", "bold": False},
            {"text": "\n- The Goods are free from any rights and claims of third parties, as well as from any other restrictions or encumbrances of any nature.", "bold": False},
            {"text": "\nThe Seller and Exporter also confirm that the origin of the Goods is not from Donetsk region, Luhansk region, Zaporizhzhia region, Kherson region, Autonomous Republic of Crimea and other temporarily occupied territories of Ukraine.", "bold": False},
            {"text": "\nThe Seller and Exporter are not registered and do not carry out economic activities in the specified temporarily occupied territories of Ukraine.", "bold": False},
            {"text": "\nIn case of detection of the fact that the Goods have origin from the specified regions, the Supplier and Exporter are obliged to fully reimburse the Buyer for all incurred costs and losses that may arise in connection with the supply of such Goods.", "bold": False},
            {"text": "\n5.15. The Supplier undertakes to register the PMD within 3 days from the date of the first event: supply or payment for each batch of Goods, but in any case 3 days before the end of the delivery period of the full batch of Goods.", "bold": False},
            {"text": f"\n5.16. The Supplier independently pays the cost of car registration in the amount of 500 UAH when shipping the Goods to {self.params['delivery_address']}", "bold": False},
        ]
        return sections

    def render_payment_conditions(self):
        sections = [
            {"text": "\n6. PAYMENT TERMS:", "bold": True},
            {"text": f"\n6.1. The Buyer is obliged to pay the cost of the Goods delivered to the place of delivery to the Seller's account by bank transfer in the following order:", "bold": False},
            {"text": f"\n- {self.params['first_payment_percent']}% of the cost of the Goods within {self.params['first_payment_days']} (three) banking days after delivery of the entire volume specified in the Contract and provision of documents defined in clause 6.2. of the Contract;", "bold": False},
            {"text": f"\n- {self.params['second_payment_percent']}% of the cost of the Goods the Buyer is obliged to pay within {self.params['second_payment_days']} days after the Seller's registration of the customs declaration.", "bold": False},
            {"text": "\n6.2. The Seller must provide the Buyer with the following documents:", "bold": False},
            {"text": "\n- Invoice for payment from the Seller indicating the total cost of the Goods in the amount of +5%;", "bold": False},
            {"text": "\n- Letter confirming shipment and signing of shipment instructions;", "bold": False},
            {"text": "\n- Customs registration card - certified copy (customs accreditation);", "bold": False},
            {"text": "\n- Foreign economic contract, appendix (if any) - each page of the Contract must be properly certified by the director or authorized person;", "bold": False},
            {"text": "\n- Proforma Invoice 1 copy original, then Invoice for registration of EK10DR (customs declaration) - original;", "bold": False},
            {"text": "\n- Extract from the State Register on the main type of enterprise activity - certified copy;", "bold": False},
            {"text": "\n- Certificate of origin of the Goods - original;", "bold": False},
            {"text": "\n- Contact person letter - original;", "bold": False},
            {"text": "\n- Letter confirming registration with the State Food and Consumer Service - certified copy;", "bold": False},
            {"text": "\n- Scanned copy of railway waybill (when delivering by rail in wagons).", "bold": False},
            {"text": "\n6.3. Settlements between the Buyer and the Seller are made in US dollars.", "bold": False},
            {"text": "\n6.4. The date of payment is considered to be the date of debiting funds from the Buyer's bank account to the Seller's bank account, subject to the Buyer providing a copy of the SWIFT.", "bold": False},
            {"text": "\n6.5. The price includes the cost of packaging, labeling, payment of all duties, customs fees, and charges during customs clearance, transportation, and cargo insurance.", "bold": False},
            {"text": "\n6.6. The basis for payment is the invoice issued by the Seller under the terms specified in clause 6.1 of the Contract.", "bold": False},
            {"text": "\n6.7. All banking expenses in the Buyer's country are borne by the Buyer, and all banking expenses in the Seller's country are borne by the Seller.", "bold": False},
        ]
        return sections

    def render_title_to_goods(self):
        sections = [
            {"text": "\n7. TITLE TO THE GOODS:", "bold": True},
            {"text": "\n7.1. The ownership of the goods shall be transferred from the Seller to the Buyer from the date of execution of the customs declaration type EK 10 DR.", "bold": False},
        ]
        return sections

    def render_sanctions(self):
        sections = [
            {"text": "\n8. SANCTIONS:", "bold": True},
            {"text": "\n8.1. Each party represents that it has not taken or refrained from taking any action that would cause itself, or the other party to be in contravention of the laws, regulations, resolutions, decrees or rules of any relevant jurisdictions relating to sanctions, trade embargoes, trade controls or boycotts. Each party also undertakes not to take or refrain from taking any action that would cause the above result.", "bold": False},
        ]
        return sections

    def render_claims(self):
        sections = [
            {"text": "\n9. CLAIMS:", "bold": True},
            {"text": "\n9.1. The Parties shall endeavor to resolve all disputes arising between them during the execution of this Contract through negotiations.", "bold": False},
            {"text": "\n9.2. For non-delivery (partial delivery)/untimely replacement of substandard Goods within the additional deadlines agreed upon by the Parties, the Seller shall pay the Buyer the following penalties and financial sanctions:", "bold": False},
            {"text": "\n- A penalty (fine) in the amount of 0.5% of the value of the Goods for each day of delay in delivery. If the delay exceeds 5 calendar days, in addition to the penalty, the Seller shall also pay the Buyer a fine of 20% of the value of the undelivered (partially delivered) Goods;", "bold": False},
            {"text": "\n- The Buyer may purchase the Goods from another Seller, in which case the Seller shall compensate the Buyer for the difference in the cost of the Goods.", "bold": False},
            {"text": "\nThe penalty and fine under this clause shall be paid by the Seller regardless of the Buyer's actual losses (penal compensation).", "bold": False},
            {"text": "\n9.3. In case of refusal to register the PMD, untimely registration of the PMD or violation of the procedure for filling out the PMD, the delivery of the Goods shall be deemed not to have taken place in full and penalties shall be applied as provided for in clause 9.2. of this Contract.", "bold": False},
            {"text": "\n9.4. If the Seller/exporter of the Seller fails to ensure timely customs clearance of the Goods to the vessel nominated by the Buyer, or the customs clearance of the Goods by the exporter/seller is impossible by the relevant decision of the judicial, fiscal or law enforcement authorities, The Seller shall reimburse the Buyer for all expenses, including but not limited to demurrage, excess storage, etc., related to or caused by the delay of the Goods at the Terminal/Port/Vessel within 5 business days from the date of the relevant invoice by the Buyer.", "bold": False},
            {"text": "\n9.5. In case of violation of the delivery period by more than 10 (ten) calendar days, the Buyer shall have the right to refuse to deliver the Goods under the Contract and demand from the Seller compensation for the damages caused and refund of the funds paid on a prepayment basis, which the Seller shall return in such case within 3 (three) banking days from the date of notification of the Buyer of the refusal of the Goods and refund.", "bold": False},
            {"text": "\n9.6. In the event of incomplete transfer of the shipping documents specified in clause 6.2 of the Contract, the Buyer has the right to withhold payment for the Goods until the Seller remedies the corresponding violation.", "bold": False},
            {"text": "\n9.7. In the event of the Seller violating any guarantees specified in clause 5.14. of this Contract (including, but not limited to, if the Goods are found to be pledged, including tax liens), the Seller shall compensate the Buyer for all losses incurred by the Buyer in full and shall pay the Buyer a fine of 30% of the value of such Goods. The fine is payable by the Seller regardless of the Buyer's actual losses.", "bold": False},
            {"text": "\n9.8. In addition, in case of delay in fulfilment of obligations, which caused the need to store grain at the Terminal beyond the agreed terms, the Supplier shall reimburse the Buyer for the actual costs of grain storage, confirmed by the relevant financial documents (invoices, acts of work performed, etc.), for the entire period of delay.", "bold": False},
            {"text": "\n9.9. In the event of delayed payment for the Goods, the Buyer shall pay the Seller a penalty of 0.02% of the unpaid amount of the Goods for each day of delay.", "bold": False},
            {"text": "\n9.10. The Seller and the Buyer shall be liable for any failure to fulfill their obligations under this Contract.", "bold": False},
        ]
        return sections

    def render_arbitration(self):
        sections = [
            {"text": "\n10. ARBITRATION:", "bold": True},
            {"text": "\n10.1. All disputes and disagreements that may arise during the performance of this Contract or in connection with it are resolved through negotiations between the Parties.", "bold": False},
            {"text": "\n10.2. The Seller and the Buyer make every effort to settle all disputes and disagreements that may arise under this Contract or in connection with it peacefully. In the event that the dispute could not be resolved through negotiations, all disputes and disagreements arising in connection with this Contract, as well as all claims related to the interpretation or performance of the terms of this Contract, are resolved in arbitration in accordance with the GAFTA Arbitration Rules, No. 125, in the version in force on the date of this Contract. The language of arbitration is English, the place of arbitration is London, England.", "bold": False},
        ]
        return sections

    def render_anti_bribery(self):
        sections = [
            {"text": "\n11. ANTI-BRIBERY MATTERS:", "bold": True},
            {"text": "\n11.1. Each of the Parties agrees and undertakes to the other that in accordance with this Contract, they will respectively comply with all laws, rules, regulations, decrees and/or official government orders concerning the fight against bribery and money laundering. Each of the Parties represents, warrants and undertakes to the other that it will not directly or indirectly", "bold": False},
            {"text": "\na) directly or indirectly carry out or attempt to carry out any actions aimed at providing a bribe, including through payment, offer, promise or other forms of providing benefits to any individuals or legal entities, including government officials;", "bold": False},
            {"text": "\nb) demand, consent to receive or accept bribes from any individual or legal entity;", "bold": False},
            {"text": "\nc) participate in any other similar transactions,", "bold": False},
            {"text": "\nin any case, if such violation is contrary to the legislation of any government regarding the fight against bribery and money laundering.", "bold": False},
        ]
        return sections

    def render_force_majeure(self):
        sections = [
            {"text": "\n12. FORCE MAJEURE:", "bold": True},
            {"text": "\n12.1. Neither Party shall be liable for partial or complete failure to perform obligations under this Contract if the failure is the result of force majeure circumstances that arose after the conclusion of the Contract and which could neither be foreseen nor prevented by reasonable measures (force majeure), if such were not known earlier at the time of conclusion of the Contract, such as, for example, Russia's aggression against Ukraine. Floods, fires, earthquakes, explosions, storms, soil subsidence, epidemics and other natural disasters, as well as war and military operations are considered as force majeure.", "bold": False},
            {"text": "\n12.2. In the event of the occurrence and termination of the circumstances specified in clause 12.1. of this Contract, the Party that is unable to fulfill its obligations under this Contract must send a written notice to the other Party within 5 (five) calendar days. If such Party cannot submit such notice in time, it is obliged to compensate the other Party for damages due to non-notification or late notification.", "bold": False},
            {"text": "\n12.3. In the event of force majeure, the term of performance of this Contract may be extended for the period of force majeure circumstances. If force majeure lasts more than 30 (thirty) calendar days, the Parties have the right to terminate the Contract, while they must issue a reconciliation act and make settlements under this Contract in its performed part.", "bold": False},
            {"text": "\n12.4. The occurrence of force majeure circumstances must be proven by the Chamber of Commerce and Industry of the country where such circumstances occurred.", "bold": False},
            {"text": "\n12.5. The Parties understand the significance of their actions and the consequences that may arise in the performance of this Contract, as the place of performance of the Contract is Ukraine, in a country where martial law is in force. At the time of conclusion of this Contract, the Parties understand that in accordance with the Decree of the President of Ukraine No. 64/2022 dated February 24, 2022 \"On the introduction of martial law in Ukraine\", from 5:30 a.m. on February 24, 2022, the military aggression of the Russian Federation has been taking place in Ukraine and therefore reference to these circumstances is not a force majeure within the meaning of this Contract and does not release the parties from the timely fulfillment of obligations under this Contract. An exception to this rule is the circumstances of martial law and military actions that will directly affect the ability of the Party to fulfill its contractual obligations.", "bold": False},
        ]
        return sections

    def render_other_conditions(self):
        sections = [
            {"text": "\n13. OTHER CONDITIONS:", "bold": True},
            {"text": "\n13.1. The Seller hereby guarantees that it owns and has good title to the Goods and that no Goods are the subject of any assignment or encumbrance. All the Goods are in the possession of, or under control of the Seller, or the Seller is entitled to take possession or control of such Goods as soon as reasonably practicable and such Goods are located in Ukraine.", "bold": False},
            {"text": "\n13.2. The Parties agreed that the text of the Contract, any materials and information or data related to this Contract are confidential and cannot be passed to any third parties without relevant written agreement of the other party of the Contract except of the situations when such information is to be provided in order to obtain official permissions and documents necessary for execution of the Contract or for payment of taxes and other obligatory fees.", "bold": False},
            {"text": "\n13.3. This Contract or any additions duly signed and sent by the Parties by facsimile means will be deemed valid until their paper originals are received.", "bold": False},
            {"text": "\n13.4. All additions are an integral part of this Contract.", "bold": False},
            {"text": "\n13.5. Parties can not transfer their rights under the contract to a third party without the written consent of the other party.", "bold": False},
            {"text": "\n13.6. This Contract is made in two originals, in Ukrainian and English, and one (1) original for each party. Both originals have equal legal force.", "bold": False},
            {"text": "\n13.7. The parties agreed that the Buyer will not re-export, which is the subject of this Contract, to the markets of third countries without the prior written consent of the Ministry of Economy and European Integration of Ukraine.", "bold": False},
            {"text": "\n13.8. The Parties agree that the documents, letters, requests, notifications sent to the e-mail addresses specified in this clause of the Contract shall be considered the official addresses for correspondence and exchange of information and documentation. All letters, requests, claims, copies of documents may be sent to the e-mail addresses specified below. Sent and delivered documents, letters, claims shall be deemed sent and received from the moment of receipt of the relevant notification in electronic form.", "bold": False},
            {"text": "\nThe Parties have agreed on the following e-mail addresses for quick exchange of documents:", "bold": False},
            {"text": f"\nBUYER: {self.params['buyer_email']}", "bold": False},
            {"text": f"\nSELLER: {self.params['seller_email']}", "bold": False},
            {"text": "\n13.9. The Parties have agreed that Saturday, Sunday and holidays that are officially or legally recognized as such in the countries of residence of the Parties shall be considered non-working days. If the deadline for performing a certain action or sending any notice expires on a non-working day, such deadline shall be extended until the first following working day. This clause does not apply to the Delivery Time.", "bold": False},
        ]
        return sections

    def render_signatures(self):
        sections = [
            {"text": "\n14. SIGNATURES OF THE PARTIES:", "bold": True},
            {"text": "\nBUYER:___________", "bold": False},
            {"text": "\nSELLER:___________", "bold": False},
        ]
        return sections



    def render_all_sections(self):
        sections = []
        sections.extend(self.render_parties())
        sections.extend(self.render_goods())
        sections.extend(self.render_quantity_sections())
        sections.extend(self.render_quality_sections())
        sections.extend(self.render_price())
        sections.extend(self.render_delivery_sections())
        sections.extend(self.render_payment_conditions())
        sections.extend(self.render_title_to_goods())
        sections.extend(self.render_sanctions())
        sections.extend(self.render_claims())
        sections.extend(self.render_arbitration())
        sections.extend(self.render_anti_bribery())
        sections.extend(self.render_force_majeure())
        sections.extend(self.render_other_conditions())
        sections.extend(self.render_signatures())
        return split_sections(sections)


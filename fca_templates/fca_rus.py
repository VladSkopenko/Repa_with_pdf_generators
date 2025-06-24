from src.app.common.docs_utils.service.section_spliter import SectionSplitter


class FCATemplateRus:
    def __init__(self, contract_params):
        self.params = contract_params

    def render_header(self):
        return (
            f"CONTRACT  № C-W {self.params['contract_number']}\n"
            f"{self.params['date']}"
        )

    def render_parties(self):
        return [
            {
                "text": f'The present Contract (hereinafter referred to as the "Contract") is concluded between the company '
                f"{self.params['buyer_name']}(\"Buyer\") represented by {self.params['buyer_representative']}, acting on the basis of Charter of the company, from one side, and {self.params['seller_name']} (the \"Seller\") represented by the Director {self.params['seller_representative']}, acting on the basis of the Company's Charter.\n\n"
                f"Taking into account the terms and conditions contained in this document, the parties have agreed as follows:",
                "bold": False,
            }
        ]

    def render_goods(self):
        return [
            {"text": "\n1. GOODS:", "bold": True},
            {
                "text": f"\n1.1. In the manner and under the terms and conditions specified in this Contract, the Seller sells, and the Buyer accepts and pays for agricultural products, namely: {self.params['goods_description']} according to Incoterms {self.params['incoterms_year']}.",
                "bold": False,
            },
        ]

    def render_quantity_sections(self):
        return [
            {"text": "\n2. QUANTITY: ", "bold": True},
            {
                "text": "\n2.1. The unit of quantity for the Goods is a metric ton (1000 kg).",
                "bold": False,
            },
            {
                "text": f"\n2.2. The total quantity: {self.params['quantity']} MT +/- {self.params['tolerance']}% at Seller's choice.",
                "bold": False,
            },
            {
                "text": "\n2.3. Type of transport: freight transport (road or rail).",
                "bold": False,
            },
            {
                "text": "\n2.4. If during the weighing of the wagon at the destination station a discrepancy between the gross weight in the railway consignment note and the overload weight of more than 0.5% is detected, the Buyer shall notify in writing of such discrepancy within 1 (one) hour by sending a message to the e-mail address specified in the Contract, and the wagon shall be unloaded only on the basis of a written permission, which the Seller shall provide within 4 (four) hours to the Buyer by sending a message to the e-mail address specified in this Contract. The Buyer shall have the right to agree to the place specified herein or to send its representative for the control weighing of the Goods, and the Seller's representative shall arrive within 12 hours from the moment of notification of the shortage.",
                "bold": False,
            },
            {
                "text": "\nIn the event of failure to deliver the agreed quantity of Goods, the Seller undertakes to:",
                "bold": False,
            },
            {"text": "- Deliver the missing Goods within 3 days;", "bold": False},
            {
                "text": "- If payment has been made, refund the Buyer within 3 days from the date of the corresponding demand by the Buyer.",
                "bold": False,
            },
            {
                "text": "Additionally, the Buyer has the right to purchase the missing quantity of Goods from other counterparties. The Seller will be obligated to compensate the cost of such Goods and transportation and logistics expenses within 3 days from the date of the Buyer's written demand.",
                "bold": False,
            },
        ]

    def render_quality_sections(self):
        sections = [
            {"text": "\n3. QUALITY AND CONDITIONS OF THE GOODS:", "bold": True},
            {
                "text": "\n3.1. The quality of the Goods under this Contract shall correspond to the following indicators:\n",
                "bold": False,
            },
        ]

        for metric in self.params["metrics"]:
            sections.append({"text": metric, "bold": False})

        sections.extend(
            [
                {
                    "text": "\nAll quality indicators must be calculated in accordance with ISO, ICC, and EU standards.",
                    "bold": False,
                },
                {
                    "text": "\n3.2. The Goods must be of high quality, loyal, and suitable for sale, free of foreign/offensive odors, and without castor seeds or other toxic seeds. Additionally, the Goods must not contain unpleasant foreign objects such as glass, metal, etc. The Goods must not contain GMOs in accordance with regulations and must comply with EU standards regarding pesticides/residues/heavy metals and mycotoxins.",
                    "bold": False,
                },
                {
                    "text": "The Goods must be free of live insects, without foreign odors or contamination, while maintaining their natural order and color.",
                    "bold": False,
                },
                {
                    "text": "\n3.3. The Buyer has the right to refuse the Goods in case of any deviation from the baseline. Acceptance of the Goods at a discount is at the discretion of the Buyer if such an option is feasible.",
                    "bold": False,
                },
                {
                    "text": "\n3.4. In the event that the Goods are found to be of substandard quality, the Buyer shall notify the Seller via email or telephone, stating that the Goods are non-compliant. The Seller must respond within one hour regarding their further actions, taking into account the conditions set forth in clause 3.5 of the Contract. Specifically, the Seller must indicate whether they will send their Representative to draft a Non-Conformity Report regarding the Goods’ compliance with the Contract terms or whether an independent accredited laboratory will be engaged for further inspection of the Goods. In any case, the laboratory conducting the testing must be agreed upon with the Buyer. If the Seller does not respond within one hour of receiving the Buyer’s notification, the Buyer shall independently decide on the respective batch of Goods — whether to accept or return the Goods to the Seller. The Buyer shall inspect the quality of the Goods within 5 (five) days from the date of arrival at the unloading location.",
                    "bold": False,
                },
                {
                    "text": "\n3.5. The final quality of the Goods shall be determined in accordance with the grain analysis cards issued by the certified laboratory of the Terminal at the place of unloading/delivery of the Goods.",
                    "bold": False,
                },
                {
                    "text": f"\nIf the Goods are delivered to the location at: {self.params.get('delivery_address')}, by road transport, the acceptance is conducted exclusively based on the results of the Terminal’s laboratory.",
                    "bold": False,
                },
                {
                    "text": "The Seller’s Representative and an independent representative shall not be called to draft a Non-Conformity Report regarding quantity and quality due to the Port Terminal’s inability to allocate waiting time for Representatives.",
                    "bold": False,
                },
                {
                    "text": "Thus, the Parties unconditionally agree that the results of the Terminal’s laboratory tests are final and unconditionally accepted by both Parties.",
                    "bold": False,
                },
                {
                    "text": "In case of delivery by road, the Parties agree that if the quality of the Goods established by the Terminal's laboratory does not meet the permissible deviations, the results of the analysis of the Terminal's laboratory shall be final, not subject to appeal and binding on both Parties.",
                    "bold": False,
                },
                {
                    "text": "3.6. In case of delivery by rail, in case of discrepancy between the actual quality indicators of the Goods and the quality indicators specified in the grain quality certificate issued upon unloading of the Goods by the Terminal laboratory and the quality requirements specified in DSTU, the Seller shall not unload the grain and shall notify the Client of the discrepancies by mail and take measures to arrange for the resolution of disputes.",
                    "bold": False,
                },
                {
                    "text": "3.7. In case of disagreement of the Seller with the results of analyses by the laboratory of the Terminal, upon delivery by rail, the Seller shall declare its disagreement to the Buyer and inform about its further actions regarding such Goods.",
                    "bold": False,
                },
                {
                    "text": "The Seller shall have the right to appoint its representative for repeated (arbitration) sampling and quality analysis of the Goods in the laboratory of the Terminal. Arbitration analysis of grain quality may be carried out in an accredited laboratory of the Grain Storage Company of Ukraine. The results of such analysis shall be final and not subject to appeal.",
                    "bold": False,
                },
                {
                    "text": "The costs associated with arbitration to determine the quality of the disputed batch of Goods, including excessive downtime of wagons, shall be borne by and at the expense of the Seller.",
                    "bold": False,
                },
                {
                    "text": "Regardless of the costs incurred, the Parties agree that the Buyer's liability shall be limited to downtime for three days inclusive. In any case, the Seller shall not have the right to abandon the wagons and shall bear all costs and losses during the time the wagons are on the railway tracks, including the time of independent laboratory tests, notwithstanding the results of such tests.",
                    "bold": False,
                },
                {
                    "text": "3.8. The Buyer has the right to refuse any Goods that do not comply with the contractual quality parameters specified in this Contract.",
                    "bold": False,
                },
                {
                    "text": "In the case of delivery of a substandard batch of Goods or non-compliance with the agreed parameters, the Buyer has the right to:",
                    "bold": False,
                },
                {
                    "text": "- Reduce the price of the Goods according to the parameters determined in the laboratory's findings;",
                    "bold": False,
                },
                {
                    "text": "- Discount the price of the delivered Goods. Indicators used for discounting are determined by the Parties in clause 3.1 of this Contract;",
                    "bold": False,
                },
                {
                    "text": "- Compensate the Buyer for the cost of processing the Goods to meet the established quality parameters;",
                    "bold": False,
                },
                {
                    "text": "- Deliver an additional quantity of Goods at a reduced price;",
                    "bold": False,
                },
                {
                    "text": "- Supply/replace the Goods in accordance with the terms set forth in the Contract;",
                    "bold": False,
                },
                {
                    "text": "- To refuse acceptance of the Goods and their payment, as well as to demand compensation for all costs incurred by the Buyer, including but not limited to transport and logistics services, penalties, and financial sanctions imposed on the Buyer by counterparties—partners under subsequent Contracts for the supply of Goods—due to such underdelivery or delivery of substandard Goods, as well as reimbursement for losses incurred in connection with the acceptance of substandard Goods by the Buyer.",
                    "bold": False,
                },
                {
                    "text": "Additionally, the Seller must compensate for the costs of transport and logistics services for the delivery and return of substandard Goods.",
                    "bold": False,
                },
                {
                    "text": "\n3.9. Replacement of Goods is carried out at the Seller's expense within 3 (three) calendar days from the date of the Buyer's claim.",
                    "bold": False,
                },
                {
                    "text": "3.10. In the case of discounting the Goods, the notification of price discounting is sent to the Seller's representative via email or electronic communication channel specified in the Contract details. Upon receiving the notification of the need for price discounting, the Seller must, within 3 (three) hours, either agree to the discounting or notify the Buyer of the dispatch of its representative for joint sampling and drafting of a Non-Conformity Report for the Goods, taking into account the requirements specified in clause 3.5 of the Contract. This notification is sent by the Seller to the Buyer's authorized representative via the email specified in the Contract details.",
                    "bold": False,
                },
                {
                    "text": "3.11. In the event of agreement on price discounting by the Seller, the Parties agree that the data used as the basis for price discounting due to non-compliance with quality and safety standards shall include laboratory test results conducted at the delivery location or an independent laboratory selected by the Buyer, along with data recorded in the Non-Conformity Report.",
                    "bold": False,
                },
                {
                    "text": "3.12. If the Goods are accepted at a discounted price based on the Buyer's data, the Seller undertakes to issue the customs declaration (VMD) based on the discounted price data provided by the Buyer.",
                    "bold": False,
                },
                {
                    "text": "3.13. In case of discrepancies in the Goods' quantity/quality, the Buyer has the right to withhold payment for the entire quantity of undelivered/substandard Goods until corrected documentation is provided:",
                    "bold": False,
                },
                {
                    "text": "3.13.1. Data indicated in the waybill (TTN), considering the Buyer's remarks, if any;",
                    "bold": False,
                },
                {
                    "text": "3.13.2. Laboratory test data, considering the price discounting.",
                    "bold": False,
                },
            ]
        )
        return sections

    def render_price(self):
        return [
            {"text": "\n4. PRICE:", "bold": True},
            {
                "text": f"\n4.1. The price per one metric ton of the Goods is {self.params['price_per_ton']} US dollars ( {self.params['price_per_ton_text']} USD).",
                "bold": False,
            },
            {
                "text": f"\n4.2. The total value of the Goods under the Contract {self.params['total_value']} USD ({self.params['total_value_text']} USD).",
                "bold": False,
            },
        ]

    def render_delivery_sections(self):
        sections = [
            {"text": "\n5. DELIVERY TERMS AND CONDITIONS:", "bold": True},
            {
                "text": "\n5.1. When delivering under FCA terms: Within the timeframe specified in the Contract, the Seller must prepare and load the agreed Goods of proper quality and quantity into the transport vehicle provided by the Buyer, hand over the Goods to the carrier/forwarder, and provide the documents stipulated in the Contract. Title to the Goods shall pass to the Buyer upon delivery of the Goods to the carrier nominated by the Buyer at the agreed place of delivery in accordance with the terms of the FCA. The Buyer independently covers the transportation (or redirection) costs of the Goods. By agreement between the Parties, these costs may be initially paid by the Supplier, with subsequent reimbursement by the Buyer within 3 days of receiving the corresponding invoice from the Seller.",
                "bold": False,
            },
            {
                "text": "\n5.2. The Seller must prepare the Goods, cleared of import duties, within the timeframe specified by the Parties in the Contract, prior to shipment and handover to the Carrier in accordance with the instructions provided by the Buyer.",
                "bold": False,
            },
            {
                "text": "\n5.3. The Seller is obligated to complete the customs formalities required for import, pay any duties levied upon import, and fulfill all necessary customs requirements.",
                "bold": False,
            },
            {
                "text": f"\n5.4. The delivery of the Goods will be carried out under FCA term {self.params.get('delivery_address')}",
                "bold": False,
            },
            {
                "text": f"\nDelivery dates: from {self.params.get('delivery_start_date')} to {self.params.get('delivery_end_date')}, inclusive. The Goods may be delivered in batches. The Seller shall notify the Buyer via email about the delivery of each batch of Goods at least one day prior to delivery.",
                "bold": False,
            },
            {"text": "\n5.5. Packaging: 100% in bulk.", "bold": True},
            {
                "text": "\nThe cargo transport must be accompanied by the following valid documents:",
                "bold": False,
            },
            {
                "text": "\n⮚ A properly completed auto (CMR) waybill for each cargo transport, filled out by the Seller in accordance with the Buyer's instructions.",
                "bold": False,
            },
            {
                "text": "\n5.6. Railway wagons shall be accompanied by the following valid documents:",
                "bold": True,
            },
            {
                "text": "\n⮚ Railway receipts/waybills for each day's railway wagon in accordance with the Buyer's instructions;",
                "bold": False,
            },
            {"text": "\n⮚ Certificate of grain quality.", "bold": False},
            {
                "text": "\n5.7. All export duties, taxes, fees, as well as costs associated with the customs clearance of the Goods for export, including the costs of obtaining the necessary permits, certificates and control procedures, are the responsibility of the Seller.",
                "bold": False,
            },
            {
                "text": "The Seller shall ensure that the Goods are exported in accordance with the requirements of the legislation of the country of export.",
                "bold": False,
            },
            {
                "text": "Drafts of all shipping documents must be sent to the buyer for preliminary review prior to finalization.",
                "bold": False,
            },
            {
                "text": "All shipping documents must be in English or in two/multiple languages, one of which is English.",
                "bold": False,
            },
            {
                "text": "The documents must be executed in full compliance with the documentary instructions provided by the buyer, but not contrary to the terms of the contract.",
                "bold": False,
            },
            {"text": "\n5.8. For deliveries by rail:", "bold": True},
            {
                "text": "The Seller shall send the Buyer a shipment schedule by e-mail.",
                "bold": False,
            },
            {
                "text": "The Buyer shall coordinate the provided schedule with the terminal at the place of delivery and the Seller in case of changes to this schedule.",
                "bold": False,
            },
            {
                "text": "The Seller undertakes to deliver the Goods only in accordance with the agreed schedule.",
                "bold": False,
            },
            {
                "text": "The shipment schedule shall be proportional to the delivery period, unless otherwise agreed by the Parties.",
                "bold": False,
            },
            {"text": "\n5.9. The Buyer must:", "bold": True},
            {
                "text": "а) provide the Seller with all necessary documentary instructions for completing transport documents by sending them via email.\n"
                "The Seller shall provide the Forwarder and the customs broker at the port for customs clearance of the Goods with all documents requested without exception within the terms specified by the Forwarder (customs broker). "
                "The provided information or documents that have inaccuracies or an incomplete package of documents shall be deemed not to have been provided to the Forwarder (customs broker). The date of receipt of documents shall be the date of their delivery to the Forwarder (customs broker).",
                "bold": False,
            },
            {
                "text": "\n5.10. Delivery under this Contract is possible only after the Seller/Exporter has passed accreditation with the Buyer.",
                "bold": True,
            },
            {
                "text": "\n5.11. The Seller and the Exporter warrant that the Goods supplied:",
                "bold": True,
            },
            {
                "text": "- at the time of signing this Contract, as well as at the time of transfer of ownership of the Goods from the Seller to the Buyer, the competent authorities of the Seller have not made and will not make decisions on imposing any encumbrances on the Goods (part of it), as well as decisions on the alienation of the Goods;",
                "bold": False,
            },
            {
                "text": "- at the time of signing this Contract, as well as at the time of transfer of ownership of the Goods from the Seller to the Buyer, the Goods are not and will not be in a tax lien, in a dispute and under a ban on alienation;",
                "bold": False,
            },
            {
                "text": "- at the time of signing this Contract, as well as at the time of transfer of ownership of the Goods from the Seller to the Buyer, the Goods will not be sold, donated, assigned, exchanged, allocated from the Seller's assets or pledged, transferred to management, and will not be leased (used) in whole or in part;",
                "bold": False,
            },
            {
                "text": "- at the time of signing this Contract, as well as at the time of transfer of ownership of the Goods from the Seller to the Buyer, the Goods are in good condition and substantially fit for the purpose for which they are intended and do not contain any substances or materials that are defective or pose a risk to health or safety;",
                "bold": False,
            },
            {
                "text": "- at the time of signing this Contract, as well as at the time of transfer of ownership of the Goods from the Seller to the Buyer, the Seller has no obligations that have matured or will mature in the future (including under previous contracts, offers, options, etc.) to alienate the Goods, transfer certain rights (right to use, right to dispose of, right to possession) to the Goods;",
                "bold": False,
            },
            {
                "text": "The Goods are free from any rights and claims of third parties, as well as from any other restrictions or encumbrances of any nature.",
                "bold": False,
            },
            {
                "text": "The Seller and the Exporter warrant that the Goods supplied are free from any rights and claims of third parties, as well as from any other restrictions or encumbrances of any nature. The Seller and the Exporter also confirm that the Goods do not originate from Donetsk region, Luhansk region, Zaporizhzhia region, Kherson region, the Autonomous Republic of Crimea and other temporarily occupied territories of Ukraine.",
                "bold": False,
            },
            {
                "text": "In addition, the Seller and the Exporter shall not be registered or carry out business activities in the said temporarily occupied territories of Ukraine. In case of detection of the fact that the Goods originate from the said regions, the Supplier and the Exporter shall fully reimburse the Buyer for all costs and losses incurred and that may arise in connection with the supply of such Goods.",
                "bold": False,
            },
            {
                "text": "\n5.12. The Supplier is obligated to register the customs declaration (PMD) within 3 days of the occurrence of the first event: delivery or payment for each batch of Goods, but in any case, no later than 3 days before the expiration of the delivery period for the full batch of Goods.",
                "bold": True,
            },
            {
                "text": f"\n5.13. Exporters of the Goods under this Contract:\n{self.params.get('exporter_name')},\nCode: {self.params.get('edrpou_code')},\nThe change of the Exporter shall be made with the consent of both Parties by concluding an Additional Agreement to this Contract.\n"
                "If the Seller is not a resident of Ukraine, the Seller confirms that the Goods delivered under this Contract were purchased directly from the Exporter.\n"
                "The Seller shall provide a letter of guarantee from the Exporters referred to in this clause on the transfer of subsidiary liability from the Seller to the Freight Forwarder in case of violation or non-fulfilment by the Buyer of its obligations under this Contract.",
                "bold": True,
            },
            {
                "text": "\n5.14. In case of arrival of substandard Goods (unloaded, sintered Goods, presence of impurities) by rail or road to the Buyer's address, the Buyer shall ensure the preparation of acts on the basis of which the Seller shall reimburse additional costs associated with the unloading, acceptance, storage and return of such Goods, including the demurrage of wagons.",
                "bold": True,
            },
            {
                "text": "Wagons with residual amounts of fumigants will not be accepted and must be forwarded by the Seller within 3 (three) days from the date of notification by the Buyer. In case of detection of wagons with fumigation residues, the Buyer shall have the right to invoice the Seller for payment of a fine in the amount of USD 300.00 (three hundred) per wagon per day, and the Seller shall be obliged to pay such fine within 5 (five) banking days from the date of invoice.",
                "bold": False,
            },
            {
                "text": "The Seller shall dispose of the non-conditional Goods within 3 (three) days from the date of notification by the Buyer. In case of violation of the term established by this clause for the disposal of substandard Goods, the Seller shall pay the Buyer penalties in the amount of USD 300.00 (three hundred) per car per day from the moment of connection and until the return of the Goods, and reimburse the Buyer for all losses incurred and documented expenses in connection with such violation.",
                "bold": False,
            },
        ]

        return sections

    def render_payment_conditions(self):
        sections = [
            {"text": "\n6. PAYMENT TERMS:", "bold": True},
            {
                "text": "\n6.1. The Buyer is obligated to pay for the Goods delivered to the place of delivery to the Seller’s account via bank transfer as follows:",
                "bold": False,
            },
            {
                "text": "\nBuyer shall effect payment in two instalments as follows:",
                "bold": False,
            },
            {"text": f"\n{self.params['first_payment_condition']}", "bold": False},
            {"text": "\nDocuments required for the first payment:", "bold": False},
            {"text": "\n- Signed commercial invoice;", "bold": False},
            {
                "text": "\n- Transport document (CMR/railway bill/BL) signed by the carrier;",
                "bold": False,
            },
            {
                "text": "\n- Loading certificate and/or weight/quality certificates.",
                "bold": False,
            },
            {"text": f"\n{self.params['second_payment_condition']}", "bold": False},
            {"text": "\nDocuments required for the remaining payment:", "bold": False},
            {
                "text": "\n- Presentation of original documents (if applicable);",
                "bold": False,
            },
            {
                "text": "\n- Receipt of final quality and quantity inspection certificates (if agreed);",
                "bold": False,
            },
            {
                "text": "\n- And/or signing of the acceptance act (if applicable).",
                "bold": False,
            },
            {
                "text": "\n6.2. Settlements between the Buyer and the Seller are conducted in US dollars.",
                "bold": False,
            },
            {
                "text": "\n6.3. Settlements between the Buyer and the Seller are conducted in US dollars.",
                "bold": False,
            },
            {
                "text": "\n6.4. The price includes the cost of packaging, labeling, payment of all duties, customs fees, and charges during customs clearance, transportation, and cargo insurance.",
                "bold": False,
            },
            {
                "text": "\n6.5. The basis for payment is the invoice issued by the Seller under the terms specified in clause 6.1 of the Contract.",
                "bold": False,
            },
            {
                "text": "\n6.6. All banking expenses in the Buyer’s country are borne by the Buyer, and all banking expenses in the Seller’s country are borne by the Seller.",
                "bold": False,
            },
        ]
        return sections

    def render_title_to_goods(self):
        sections = [
            {"text": "\n7. TITLE TO THE GOODS:", "bold": True},
            {
                "text": "\n7.1. The ownership of the goods passes from the Seller to the Buyer after issuance of VMD.",
                "bold": False,
            },
        ]
        return sections

    def render_sanctions(self):
        sections = [
            {"text": "\n8. SANCTIONS:", "bold": True},
            {
                "text": "\n8.1. Each party represents that it has not taken or refrained from taking any action that would cause itself, or the other party to be in contravention of the laws, regulations, resolutions, decrees or rules of any relevant jurisdictions relating to sanctions, trade embargoes, trade controls or boycotts. Each party also undertakes not to take or refrain from taking any action that would cause the above result.",
                "bold": False,
            },
        ]
        return sections

    def render_claims(self):
        sections = [
            {"text": "\n9. RESPONSIBILITY OF THE PARTIES:", "bold": True},
            {
                "text": "\n9.1. The Parties shall endeavor to resolve all disputes arising between them during the execution of this Contract through negotiations.",
                "bold": False,
            },
            {
                "text": "\n9.2. For non-delivery (partial delivery)/untimely replacement of substandard Goods within the additional deadlines agreed upon by the Parties, the Seller shall pay the Buyer the following penalties and financial sanctions:",
                "bold": False,
            },
            {
                "text": "- A penalty (fine) in the amount of 0.5% of the value of the Goods for each day of delay in delivery. If the delay exceeds 5 calendar days, in addition to the penalty, the Seller shall also pay the Buyer a fine of 20% of the value of the undelivered (partially delivered) Goods.",
                "bold": False,
            },
            {
                "text": "- The Buyer may purchase the Goods from another Seller, in which case the Seller shall compensate the Buyer for the difference in the cost of the Goods аnd transport and logistics services.",
                "bold": False,
            },
            {
                "text": "The penalty and fine under this clause shall be paid by the Seller regardless of the Buyer’s actual losses (penal compensation).",
                "bold": False,
            },
            {
                "text": "\n9.3. If the Seller/exporter of the Seller fails to ensure timely customs clearance of the Goods to the vessel nominated by the Buyer, or the customs clearance of the Goods by the exporter/seller is impossible by the relevant decision of the judicial, fiscal or law enforcement authorities,",
                "bold": False,
            },
            {
                "text": "The Seller shall reimburse the Buyer for all expenses, including but not limited to demurrage, excess storage, etc., related to or caused by the delay of the Goods at the Terminal/Port/Vessel within 5 business days from the date of the relevant invoice by the Buyer.",
                "bold": False,
            },
            {
                "text": "\n9.4. In case of violation of the delivery period by more than 10 (ten) calendar days, the Buyer shall have the right to refuse to deliver the Goods under the Contract and demand from the Seller compensation for the damages caused and refund of the funds paid on a prepayment basis, which the Seller shall return in such case within 3 (three) banking days from the date of notification of the Buyer of the refusal of the Goods and refund.",
                "bold": False,
            },
            {
                "text": "\n9.5. In the event of incomplete transfer of the shipping documents specified in clause 6.1. of the Contract, the Buyer has the right to withhold payment for the Goods until the Seller remedies the corresponding violation.",
                "bold": False,
            },
            {
                "text": "\n9.6. In the event of the Seller violating any guarantees specified in clause 5.9. of this Contract (including, but not limited to, if the Goods are found to be pledged, including tax liens), the Seller shall compensate the Buyer for all losses incurred by the Buyer in full and shall pay the Buyer a fine of 30% of the value of such Goods. The fine is payable by the Seller regardless of the Buyer’s actual losses.",
                "bold": False,
            },
            {
                "text": "\n9.7. In the event of delayed payment for the Goods, the Buyer shall pay the Seller a penalty of 0.02% of the unpaid amount of the Goods for each day of delay.",
                "bold": False,
            },
            {
                "text": "\n9.9. The Seller and the Buyer shall be liable for any failure to fulfill their obligations under this Contract.",
                "bold": False,
            },
        ]
        return sections

    def render_arbitration(self):
        sections = [
            {"text": "\n10. ARBITRATION CLAUSE:", "bold": True},
            {
                "text": "\n10.1. All disputes and disagreements that may arise during the execution of this Contract or"
                        " in connection with it shall be resolved through negotiations between the Parties.",
                "bold": False,
            },
            {
                "text": "\n10.2. The Seller and the Buyer shall make every effort to resolve any disputes and"
                        " disagreements arising from or in connection with this Contract amicably. In the event that the"
                        " dispute is not settled by negotiation, all disputes and disagreements arising out of or relating"
                        " to this Contract, as well as all claims relating to the interpretation or performance of the terms of this Contract, shall be settled by arbitration in accordance with the GAFTA Arbitration Rules, No. 125, as in effect on the date of this Contract. The language of arbitration shall be English and the place of arbitration shall be London, England.",
                "bold": False,
            },
        ]
        return sections

    def render_anti_bribery(self):
        sections = [
            {"text": "\n11. ANTI-BRIBERY:", "bold": True},
            {
                "text": "\n11.1. The Parties each agree and undertake to the other that in connection with this Contract, they will respectively comply with all applicable laws, rules, regulations, decrees and/or official government orders relating to anti-bribery and anti-money laundering. The Parties each represent, warrant and undertake to the other that they shall not, directly or indirectly",
                "bold": False,
            },
            {
                "text": "a) will not, directly or indirectly, perform or attempt to perform any act aimed at providing a bribe, including through payment, offer, promise or other forms of providing a benefit to any person or entity, including public officials;",
                "bold": False,
            },
            {
                "text": "b) request, agree to receive or accept a bribe from any person individual or entity;",
                "bold": False,
            },
            {"text": "c) engage in any other transactions,", "bold": False},
            {
                "text": "in each case if this is in violation of or inconsistent with the anti-bribery and anti-money laundering legislation of any government.",
                "bold": False,
            },
        ]
        return sections

    def render_force_majeure(self):
        sections = [
            {"text": "\n12. FORCE – MAJEURE:", "bold": True},
            {
                "text": "\n12.1. Neither party shall bear responsibility for the partial or complete non-performance of the obligations under the present Contract, if the non-performance results from force-majeure circumstances arisen after signing of the Contract which could not be either foreseen or prevented by prudent measures (force-majeure) if they were not previously known.",
                "bold": False,
            },
            {
                "text": "Flood, fire, earth-quakes, explosion, storm, floor convergence, epidemic or other acts of God as well as war and military operations shall consider force-majeure.",
                "bold": False,
            },
            {
                "text": "\n12.2. Upon occurrence and cessation of the circumstances stipulated in p. 10.1. of the present Contract, the party which is unable to fulfill its obligations under the present Contract shall serve a written notice to the other party within 5 (five) calendar days. If the party fails to serve such notice in time it shall reimburse to other party losses resulted from not notifying or late notifying.",
                "bold": False,
            },
            {
                "text": "\n12.3. Upon occurrence of force-majeure the period of performance of the present Contract shall be prolonged for the period of force-majeure. Should force-majeure lasts more than 30 (thirty) calendar days the Parties have the right to terminate the Contract, at that they have to issue an act of verification of accounts and to settle payments under the present Contract in its performed portion.",
                "bold": False,
            },
            {
                "text": "\n12.4. Occurrence of force-majeure circumstances shall be proved by Chamber of Commerce and Industry of the country where these circumstances have occurred.",
                "bold": False,
            },
            {
                "text": "\n12.5. The Parties understand the significance of their actions and the consequences that may arise in the performance of this Contract, as the place of performance of the Contract is Ukraine, in a country where martial law is in force.",
                "bold": False,
            },
            {
                "text": "At the time of conclusion of this Contract, the Parties understand that in accordance with the Decree of the President of Ukraine No. 64/2022 dated February 24, 2022 “On the introduction of martial law in Ukraine”, from 5:30 a.m. on February 24, 2022, the military aggression of the Russian Federation has been taking place in Ukraine and therefore reference to these circumstances is not a force majeure within the meaning of this Contract and does not release the Parties from the timely fulfillment of obligations under this Contract.",
                "bold": False,
            },
            {
                "text": "An exception to this rule is the circumstances of martial law and military actions that will directly affect the ability of the Party to fulfill its contractual obligations.",
                "bold": False,
            },
        ]
        return sections

    def render_other_conditions(self):
        sections = [
            {"text": "\n13. OTHER CONDITIONS:", "bold": True},
            {
                "text": "\n13.1. The Seller hereby guarantees that it owns and has good title to the Goods and that no Goods are the subject of any assignment or encumbrance. All the Goods are in the possession of, or under control of the Seller, or the Seller is entitled to take possession or control of such Goods as soon as reasonably practicable and such Goods are located in Ukraine.",
                "bold": False,
            },
            {
                "text": "\n13.2. The Parties agreed that the text of the Contract, any materials and information or data related to this Contract are confidential and cannot be passed to any third parties without relevant written agreement of the other party of the Contract except of the situations when such information is to be provided in order to obtain official permissions and documents necessary for execution of the Contract or for payment of taxes and other obligatory fees.",
                "bold": False,
            },
            {
                "text": "\n13.3. This Contract or any additions duly signed and sent by the Parties by facsimile means will be deemed valid until their paper originals are received.",
                "bold": False,
            },
            {
                "text": "\n13.4. All additions are an integral part of this Contract.",
                "bold": False,
            },
            {
                "text": "\n13.5. Parties can not transfer their rights under the contract to a third party without the written consent of the other party.",
                "bold": False,
            },
            {
                "text": "\n13.6. This Contract is made in two originals, in Ukrainian and English, and one (1) original for each party.. Both originals have equal legal force.",
                "bold": False,
            },
            {
                "text": "\n13.8. The Parties agree that the documents, letters, requests, notifications sent to the e-mail addresses specified in this clause of the Contract shall be considered the official addresses for correspondence and exchange of information and documentation. All letters, requests, claims, copies of documents may be sent to the e-mail addresses specified below. Sent and delivered documents, letters, claims shall be deemed sent and received from the moment of receipt of the relevant notification in electronic form.",
                "bold": False,
            },
            {
                "text": f"\nThe Parties have agreed on the following e-mail addresses for quick exchange of documents:",
                "bold": False,
            },
            {"text": f"\nBUYER: {self.params['buyer_email']}", "bold": False},
            {"text": f"\nSELLER: {self.params['seller_email']}", "bold": False},
            {
                "text": "\n13.9. The Parties have agreed that Saturday, Sunday and holidays that are officially or legally recognized as such in the countries of residence of the Parties shall be considered non-working days. If the deadline for performing a certain action or sending any notice expires on a non-working day, such a deadline shall be extended until the first following working day. This clause does not apply to the Delivery Time",
                "bold": False,
            },
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
        return SectionSplitter.split_sections(sections)

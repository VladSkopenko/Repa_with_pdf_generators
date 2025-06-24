from src.app.common.docs_utils.service.section_spliter import SectionSplitter


class FCATemplateUkraine:
    def __init__(self, contract_params):
        self.params = contract_params

    def render_header(self):
        return (
            f"КОНТРАКТ № C-W {self.params['contract_number']}\n"
            f"{self.params['date']}"
        )

    def render_parties(self):
        return [
            {
                "text": (
                    f"Цей Контракт (далі «Контракт») укладено між компанією "
                    f"{self.params['buyer_name']} («Покупець») в особі {self.params['buyer_representative']}, "
                    f"що діє на підставі Статуту компанії, з одного боку, та "
                    f"{self.params['seller_name']} («Продавець») в особі директора {self.params['seller_representative']}, "
                    f"діючого на підставі Статуту.\n\n"
                    f"Беручи до уваги умови та положення, що містяться в цьому документі, сторони домовилися про таке:"
                ),
                "bold": False,
            }
        ]

    def render_goods(self):
        return [
            {"text": "\n1. ТОВАР:", "bold": True},
            {
                "text": (
                    f"\n1.1. У порядку та на умовах, визначених цим Контрактом, Продавець продає, а Покупець "
                    f"приймає та оплачує {self.params['goods_description']}."
                ),
                "bold": False,
            },
        ]

    def render_quantity_sections(self):
        return [
            {"text": "\n2. КІЛЬКІСТЬ:", "bold": True},
            {
                "text": "\n2.1. Одиниця виміру товару є метрична тонна (1000 кг).",
                "bold": False,
            },
            {
                "text": f"\n2.2. Загальна кількість товару: {self.params['quantity']} MT +/- {self.params['tolerance']}% за вибором Продавця.",
                "bold": False,
            },
            {
                "text": "\n2.3. Вид транспорту: вантажний транспорт (автомобільний або залізничний).",
                "bold": False,
            },
            {
                "text": "\n2.4. У разі, якщо під час зважування вагона на станції призначення виявлено розходження між вагою брутто у залізничній накладній та вагою перевантаження більше ніж на 0,5 %, Покупець має письмово повідомити про таку розбіжність протягом 1 (однієї) години шляхом надсилання повідомлення на електронну адресу, яка зазначена в Контракті, при цьому вивантаження вагону здійснюється тільки на підставі письмового дозволу, який Продавець повинен надати протягом 4 (чотирьох) годин Покупцю шляхом надсилання повідомлення на електронну адресу, зазначену в цьому Контракті. Покупець має право погодитись з визначеною в цьому місці або надіслати свого представника для контрольного зважування Товару, а представник Продавця повинен прибути протягом 12 годин з моменту повідомлення про виявлення нестачі.",
                "bold": False,
            },
            {
                "text": "\nУ випадку непоставки Товару в погодженій кількості Продавець зобов'язується:",
                "bold": False,
            },
            {"text": "- здійснити допоставку Товару протягом 3-х днів;", "bold": False},
            {
                "text": "- у випадку, якщо були сплачені грошові кошти, повернути їх Покупцю протягом 3-х днів від дати відповідної вимоги Покупця.",
                "bold": False,
            },
            {
                "text": "Також Покупець має право докупити ту кількість Товару, якої Продавець не допоставив у інших контрагентів і останній повинен буде компенсувати вартість такого Товару та транспортно-логістичні витрати протягом 3-х днів від дати письмової вимоги Покупця.",
                "bold": False,
            },
        ]

    def render_quality_sections_uk(self):
        sections = [
            {"text": "\n3. ЯКІСТЬ ТА СТАН ТОВАРУ:", "bold": True},
            {
                "text": "\n3.1. Якість Товару за цим Контрактом має відповідати наступним показникам:\n",
                "bold": False,
            },
        ]

        # Добавляем метрики, которые приходят из params['metrics']
        for metric in self.params.get("metrics", []):
            sections.append({"text": metric, "bold": False})

        sections.extend(
            [
                {
                    "text": "\nУсі показники якості мають бути розраховані відповідно до стандартів ISO, ICC та ЄС.",
                    "bold": False,
                },
                {
                    "text": "\n3.2. Товар повинен бути якісним, лояльним і придатним для продажу, без сторонніх/поганих запахів, без насіння рицини та іншого отруйного насіння. Крім того, у товарах не повинно бути таких неприємних сторонніх тіл, як скло, метал тощо. Товари не повинні містити ГМО відповідно до нормативів та відповідати нормативам ЄС щодо пестицидів/залишків/важких металів та мікотоксинів. "
                    "Товар має бути вільним від живих комах, без стороннього запаху чи забруднення природного порядку та кольору.",
                    "bold": False,
                },
                {
                    "text": "\n3.3. Покупець має право відмовитися від Товару за будь-якого відхилення від базису. Прийняття товару з дисконтом є прерогативою Покупця за такої можливості.",
                    "bold": False,
                },
                {
                    "text": "\n3.4. У випадку, якщо Товар виявиться неякісним, Покупець повідомляє Продавця електронною поштою, телефоном, що Товар є неякісний, а Продавець протягом години повинен надати відповідь з приводу своїх подальших дій, з урахуванням умов викладених в п. 3.5. Контракту, а саме чи буде надсилати свого Представника для складання Акту про невідповідність Товару умовам Контракту чи буде залучено незалежну акредитовану лабораторію для подальшого приймання Товару. В будь-якому разі повинно буде погоджено з Покупцем лабораторія, яка буде проводити лабораторні дослідження. У випадку не надання відповіді протягом години з моменту отримання повідомлення від Покупця, останній самостійно приймає рішення стосовно такої Партії Товару, а саме чи приймати Товар чи повертати Товар Продавцю. Покупець перевіряє якість Товару протягом 5 (п’яти) діб з дати надходження в місця вивантаження Товару.",
                    "bold": False,
                },
                {
                    "text": "\n3.5. Остаточна якість Товару визначається відповідно до карток аналізу зерна, виданих сертифікованою лабораторією Терміналу в місці вивантаження/доставки Товару. "
                    f"Якщо доставка Товару здійснюється на термінал за адресою: {self.params.get('delivery_address')}, "
                    "автомобільним транспортом, то приймання здійснюється виключно по результатам лабораторії Терміналу. "
                    "Виклик Представника Продавця та залучення незалежного представника для складання Акту про невідповідність кількості та якості не здійснюється у зв’язку із неможливістю Портового Терміналу забезпечити час на очікування Представників. "
                    "Отже Сторони беззастережно погодили, що результати лабораторних досліджень Терміналу є остаточними і безспірно приймаються Сторонами. "
                    "При постачанні автомобільним транспортом Сторони погоджуються, що у разі невідповідності якості Товару, встановленої лабораторією Терміналу, допустимим відхиленням, результати аналізу лабораторії Терміналу є остаточними, не підлягають оскарженню та є обов’язковими для обох Сторін.",
                    "bold": False,
                },
                {
                    "text": "\n3.6. При постачанні залізничним транспортом у разі виявлення невідповідності фактичних якісних показників Товару якісним показникам, зазначеним у посвідченні про якість зерна виданому при розвантаженні Товару лабораторією Терміналу та вимогам щодо якості зазначеним у ДСТУ, Продавець не вивантажує зерно та зобов'язаний проінформувати про виявлені розбіжності поштою та вжити заходів для організації вирішення спірних питань.",
                    "bold": False,
                },
                {
                    "text": "\n3.7. У разі незгоди Продавця з результатами аналізів лабораторією Терміналу, при постачанні залізничним транспортом, Продавець заявляє Покупцю про свою незгоду та повідомляє про подальші свої дії щодо такого Товару. "
                    "Продавець має право призначити свого представника на повторний (арбітражний) відбір зразків та аналіз якості Товару у лабораторії Терміналу  (арбітражний) аналіз якості зерна може бути здійснений в акредитованій лабораторії СЖС Україна. "
                    "Результати такого аналізу визначаються остаточними та не підлягають оскарженню. "
                    "Витрати, пов'язані з арбітражем визначенням якості спірної партії Товару, в тому числі наднормативний простій вагонів - покладаються на Продавця та за його рахунок. "
                    "Незалежно від понесених витрат Сторони погодились, що відповідальність Покупця обмежується простоєм за три дні включно. "
                    "У будь-якому випадку Продавець не має права кидати вагони та бере на себе всі витрати та збитки під час перебування вагонів на залізничних коліях, включаючи час незалежних лабораторних випробувань, незважаючи на результати таких випробувань.",
                    "bold": False,
                },
                {
                    "text": "\n3.8. Покупець має право відмовитися від будь-якого Товару, який не відповідає договірним параметрам якості, зазначеним у цьому Контракті.",
                    "bold": False,
                },
                {
                    "text": "\nУ випадку поставки неякісної партії Товару або у невідповідності до погоджених Сторонами показників Покупець має право на:",
                    "bold": False,
                },
                {
                    "text": "- На зменшення ціни за Товар у відповідності до тих показників, які визначені в висновку лабораторії;",
                    "bold": False,
                },
                {
                    "text": "- дисконтування ціни на поставлений Товар. Показники, які застосовуються для дисконтування визначаються Сторонами у п.3.1. даного Контракту;",
                    "bold": False,
                },
                {
                    "text": "- на компенсацію Покупцеві вартості доробки Товару до встановлених показників якості;",
                    "bold": False,
                },
                {
                    "text": "- поставки більшої кількості Товару по зменшеній ціні;",
                    "bold": False,
                },
                {
                    "text": "- допоставки/ заміни Товару у відповідності до умов визначених в Контракті;",
                    "bold": False,
                },
                {
                    "text": "- відмовитися від прийняття Товару та його оплати, а також вимагати компенсування Покупцеві всіх витрати в тому числі, але не обмежуючись транспортно-логістичні послуги, штрафні та фінансові санкції, які будуть застосовані до Покупця зі Сторони контрагентів – партнерів по подальшим Контрактам на поставку Товару у зв’язку з такою недопоставкою або поставкою неякісного Товару, а також відшкодування збитків понесених у зв’язку з прийняттям Покупцем Товару неналежної якості.",
                    "bold": False,
                },
                {
                    "text": "\nТакож Продавець повинен буде компенсувати витрати на транспортно-логістичні послуги на доставку, повернення неякісного Товару.",
                    "bold": False,
                },
                {
                    "text": "\n3.9. Заміна товару здійснюється за рахунок Продавця впродовж 3 (трьох) календарних днів з моменту пред’явлення рекламації Покупцем.",
                    "bold": False,
                },
                {
                    "text": "\n3.10. При дисконтуванні Товару, повідомлення про дисконтування ціни направляється представнику Продавця на електронну адресу або на електронний канал зв’язку, що вказані у реквізитах Контракту. Після отримання повідомлення про необхідність дисконтування ціни, Продавець протягом 3-х (трьох) годин зобов’язаний або надати згоду на дисконтування, або повідомити про направлення свого представника для спільного відбору проб та складання Акту про невідповідність Товару, з урахуванням вимог визначених в п. 3.5. Контракту. Вказане повідомлення Продавець направляє уповноваженому представнику Покупця на електронну адресу, що вказана в реквізитах Контракту.",
                    "bold": False,
                },
                {
                    "text": "\n3.11. У випадку отримання згоди про дисконтування ціни від Продавця, Сторони погоджуються, що вихідними даними для дисконтування ціни, у зв’язку із невідповідністю Товару якісним характеристикам, передбаченим по якості та безпечності, є дані лабораторних досліджень, що проводяться лабораторією по місцю поставки або незалежною лабораторією за вибором Покупця, та даними, що фіксуються у Акті про невідповідність Товару.",
                    "bold": False,
                },
                {
                    "text": "\n3.12. У випадку прийняття Товару із дисконтованою ціною по даним Покупця, Продавець зобов’язується направити ВМД на підставі отриманих від Покупця даних про дисконтування ціни.",
                    "bold": False,
                },
                {
                    "text": "\n3.13. У випадку виявлення невідповідності Товару за кількістю/якістю, Покупець має право не здійснювати оплату всієї кількості недопоставленого/неякісного Товару до моменту отримання відкоригованих документів:",
                    "bold": False,
                },
                {
                    "text": "3.13.1. даним, зазначеним у ТТН з урахування відмітки Покупця за наявності;",
                    "bold": False,
                },
                {
                    "text": "3.13.2. даним лабораторних досліджень з урахуванням дисконтування ціни.",
                    "bold": False,
                },
            ]
        )

        return sections

    def render_price(self):
        return [
            {"text": "\n4. ЦІНА:", "bold": True},
            {
                "text": f"\n4.1. Ціна за одну метричну тонну Товару становить {self.params['price_per_ton']} доларів США ({self.params['price_per_ton_text']} доларів США).",
                "bold": False,
            },
            {
                "text": f"\n4.2. Загальна вартість Товару за Контрактом {self.params['total_value']} доларів США ({self.params['total_value_text']} доларів США).",
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
            {
                "text": "\n5.9. The Seller and the Exporter warrant that the Goods supplied:",
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
                "text": "In case of detection of the fact that the Goods originate from the said regions, the Supplier and the Exporter shall fully reimburse the Buyer for all costs and losses incurred and that may arise in connection with the supply of such Goods.",
                "bold": False,
            },
            {
                "text": "\n5.10. In case of arrival of substandard Goods (unloaded, sintered Goods, presence of impurities) by rail or road to the Buyer's address,",
                "bold": True,
            },
            {
                "text": "the Buyer shall ensure the preparation of acts on the basis of which the Seller shall reimburse additional costs associated with the unloading, acceptance, storage and return of such Goods, including the demurrage of wagons.",
                "bold": False,
            },
            {
                "text": "Wagons with residual amounts of fumigants will not be accepted and must be forwarded by the Seller within 3 (three) days from the date of notification by the Buyer.",
                "bold": False,
            },
            {
                "text": "In case of detection of wagons with fumigation residues, the Buyer shall have the right to invoice the Seller for payment of a fine in the amount of USD 300.00 (three hundred) per wagon per day, and the Seller shall be obliged to pay such fine within 5 (five) banking days from the date of invoice.",
                "bold": False,
            },
            {
                "text": "The Seller shall dispose of the non-conditional Goods within 3 (three) days from the date of notification by the Buyer.",
                "bold": False,
            },
            {
                "text": "In case of violation of the term established by this clause for the disposal of substandard Goods, the Seller shall pay the Buyer penalties in the amount of USD 300.00 (three hundred) per car per day from the moment of connection and until the return of the Goods, and reimburse the Buyer for all losses incurred and documented expenses in connection with such violation.",
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
                "text": "\n6.3. The price includes the cost of packaging, labeling, payment of all duties, customs fees, and charges during customs clearance, transportation, and cargo insurance.",
                "bold": False,
            },
            {
                "text": "\n6.4. The basis for payment is the invoice issued by the Seller under the terms specified in clause 6.1 of the Contract.",
                "bold": False,
            },
        ]
        return sections

    def render_title_to_goods(self):
        sections = [
            {"text": "\n7. TITLE TO THE GOODS:", "bold": True},
            {
                "text": "\n7.1. Title to the Goods, as well as all risks of accidental loss or damage to the Goods, shall pass from the Seller to the Buyer upon delivery of the Goods to the carrier nominated by the Buyer at the agreed place of delivery in accordance with the terms of the FCA (Incoterms 2020).",
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
                "text": "\n10.1. All disputes and disagreements that may arise during the execution of this Contract or in connection with it shall be resolved through negotiations between the Parties.",
                "bold": False,
            },
            {
                "text": "\n10.2. The Seller and the Buyer shall make every effort to resolve any disputes and disagreements arising from or in connection with this Contract amicably. In the event that the dispute is not settled by negotiation, all disputes and disagreements arising out of or relating to this Contract, as well as all claims relating to the interpretation or performance of the terms of this Contract, shall be settled by arbitration in accordance with the GAFTA Arbitration Rules, No. 125, as in effect on the date of this Contract. The language of arbitration shall be English and the place of arbitration shall be London, England.",
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
                "text": "\n13.9. The Parties have agreed that Saturday, Sunday and holidays that are officially or legally recognized as such in the countries of residence of the Parties shall be considered non-working days. If the deadline for performing a certain action or sending any notice expires on a non-working day, such a deadline shall be extended until the first following working day. This clause does not apply to the Delivery T",
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

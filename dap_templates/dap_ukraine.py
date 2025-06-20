from section_spliter import SectionSplitter

class DAPTemplateUkraine:
    def __init__(self, contract_params):
        """
        contract_params = {
            'contract_number': '1234567890',
            'date': '2024-01-01',
            'seller_name': 'ТОВ "Кращий Зерно"',
            'seller_representative': 'Іван Іванов',
            'buyer_name': 'ТОВ "АгроІмпорт"',
            'buyer_representative': 'Джон Сміт',
            'goods_description': 'Пшениця українська навалом',
            'incoterms_year': '2024',
            'quantity': 1000,
            'tolerance': 5,
            'metrics': [...],
            'price_per_ton': 250,
            'price_per_ton_text': 'двісті п\'ятдесят',
            'total_value': 250000,
            'total_value_text': 'двісті п\'ятдесят тисяч',
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
            f"КОНТРАКТ № C-W {self.params['contract_number']}\n"
            f"{self.params['date']}"
        )

    def render_parties(self):
        return [
            {"text": f"Цей Контракт (надалі — \"Контракт\") укладено між компанією "
            f"{self.params['buyer_name']}(\"Покупець\") в особі {self.params['buyer_representative']}, що діє на підставі Статуту компанії, з однієї сторони, та {self.params['seller_name']} (\"Продавець\") в особі директора {self.params['seller_representative']}, що діє на підставі Статуту компанії.\n\n"
            f"Беручи до уваги умови, викладені в цьому документі, сторони домовилися про наступне:", "bold": False}
        ]

    def render_goods(self):
        return [
            {"text": "\n1. ТОВАР:", "bold": True},
            {"text": f"\n1.1. У порядку та на умовах, визначених цим Контрактом, Продавець продає, а Покупець приймає та оплачує сільськогосподарську продукцію, а саме: {self.params['goods_description']}, {self.params['incoterms_year']} року виробництва (надалі — \"Товар\").", "bold": False}
        ]

    def render_quantity_sections(self):
        return [
            {"text": "\n2. КІЛЬКІСТЬ: ", "bold": True},
            {"text": "\n2.1. Одиниця виміру кількості Товару — метрична тонна (1000 кг).", "bold": False},
            {"text": f"\n2.2. Загальна кількість: {self.params['quantity']} МТ +/- {self.params['tolerance']}% на вибір Продавця.", "bold": False},
            {"text": "\n2.3. Вага поставленого Товару остаточно визначається за результатами зважування після прибуття на місце доставки. Вид транспорту: вантажний транспорт.", "bold": False},
            {"text": "\n2.4. Кількість Товару визначається за вагою під час розвантаження автотранспорту та/або залізничних вагонів на місці доставки: лабораторією Терміналу. Продавець має право призначити своїх представників, за власний рахунок, для контролю кількості Товару під час розвантаження. Якщо Продавець не забезпечить своєчасну присутність своїх представників, розвантаження вантажного транспорту буде здійснено без них, а дані про кількість розвантаженого Товару, визначені зважуванням на місці доставки, визнаються обома Сторонами Контракту.", "bold": False},
            {"text": "\n2.5. Якщо під час зважування вагона на станції призначення виявлено розбіжність між брутто-вагою у залізничній накладній та перевантаженою вагою понад 0,5%, Покупець повідомляє про таку розбіжність письмово протягом 1 (однієї) години, надіславши повідомлення на електронну адресу, зазначену в Контракті, а вагон розвантажується лише на підставі письмового дозволу, який Продавець надає протягом 4 (чотирьох) годин Покупцю, надіславши повідомлення на електронну адресу, зазначену в цьому Контракті. Покупець має право погодитися на місце, зазначене тут, або направити свого представника для контрольного зважування Товару, а представник Продавця прибуде протягом 12 годин з моменту повідомлення про нестачу.", "bold": False},
            {"text": "\nУ разі недопоставки погодженої кількості Товару Продавець зобов'язується:", "bold": False},
            {"text": "\n-     поставити відсутній Товар протягом 3 днів;", "bold": False},
            {"text": "\n-   якщо оплата здійснена, повернути Покупцю кошти протягом 3 днів з дати відповідної вимоги Покупця.", "bold": False},
            {"text": "\nДодатково Покупець має право придбати відсутню кількість Товару у інших контрагентів. Продавець зобов'язаний компенсувати вартість такого Товару та транспортно-логістичні витрати протягом 3 днів з дати письмової вимоги Покупця.\n", "bold": False},
        ]

    def render_quality_sections(self):
        sections = [
            {"text": "\n3. ЯКІСТЬ І СТАН ТОВАРУ:", "bold": True},
            {"text": "\n3.1. Якість Товару за цим Контрактом повинна відповідати наступним показникам:", "bold": False},
        ]
        for metric in self.params['metrics']:
            sections.append({"text": metric, "bold": False})
        sections.extend([
            {"text": "\nАмброзія не приймається.", "bold": False},
            {"text": "\nВсі показники якості повинні визначатися відповідно до стандартів ISO, ICC та ЄС.", "bold": False},
            {"text": "\n3.2. Товар повинен бути високоякісним, лояльним і придатним для продажу, без сторонніх/неприємних запахів, без рицини або інших токсичних насіння. Крім того, Товар не повинен містити сторонніх тіл, таких як скло, метал тощо. Товар не повинен містити ГМО відповідно до нормативних актів і повинен відповідати стандартам ЄС щодо пестицидів/залишків/важких металів і мікотоксинів.\nТовар повинен бути без живих комах, без сторонніх запахів або забруднень, зберігаючи свій природний вигляд і колір.", "bold": False},
            {"text": "\n3.3. Покупець має право відмовитися від Товару у разі будь-якого відхилення від базових показників. Прийняття Товару зі знижкою — на розсуд Покупця, якщо така опція можлива.", "bold": False},   
            {"text": "\n3.4. У разі доставки автотранспортом Сторони погоджуються, що якість Товару, встановлена лабораторією Терміналу, не відповідає допустимим відхиленням, результати аналізу лабораторії Терміналу є остаточними, не підлягають оскарженню і є обов'язковими для обох Сторін.", "bold": False},
            {"text": "\n3.5. У разі доставки залізницею, у разі невідповідності фактичних показників якості Товару та показників якості, зазначених у сертифікаті якості зерна, виданому при розвантаженні Товару лабораторією Терміналу, та вимогам якості, зазначеним у ДСТУ, Продавець не розвантажує зерно і повідомляє Клієнта про розбіжності поштою та вживає заходів для врегулювання спорів.", "bold": False},
            {"text": "\nУ разі незгоди Продавця з результатами аналізу лабораторії Терміналу при доставці залізницею, Продавець заявляє про свою незгоду Покупцю та інформує про подальші дії щодо такого Товару. Продавець має право призначити свого представника для повторного (арбітражного) відбору проб і аналізу якості Товару в лабораторії Терміналу (арбітражний аналіз якості зерна може бути проведений в акредитованій лабораторії Зернової компанії України). Результати такого аналізу є остаточними і не підлягають оскарженню.", "bold": False},
            {"text": "\nВитрати, пов'язані з арбітражем для визначення якості спірної партії Товару, включаючи надмірний простій вагонів, несе і оплачує Продавець.", "bold": False},
            {"text": "\nНезалежно від понесених витрат, Сторони погоджуються, що відповідальність Покупця обмежується простоєм на три дні включно. У будь-якому випадку Продавець не має права залишати вагони і несе всі витрати та збитки за час перебування вагонів на залізничних коліях, включаючи час незалежних лабораторних досліджень, незалежно від результатів таких досліджень.", "bold": False},
            {"text": "\n3.6. Покупець має право відмовитися від будь-якого Товару, що не відповідає договірним параметрам якості, зазначеним у цьому Контракті.\nУ разі поставки неякісної партії Товару або невідповідності погодженим параметрам Покупець має право:", "bold": False},
            {"text": "\n- Зменшити ціну Товару відповідно до параметрів, визначених у висновку лабораторії;", "bold": False},
            {"text": "\n- Застосувати знижку до ціни поставленого Товару. Параметри для знижки визначені у пункті 3.1 цього Контракту;", "bold": False},
            {"text": "\n- Компенсувати Покупцю витрати на доопрацювання Товару до встановлених параметрів якості;", "bold": False},
            {"text": "\n- Поставити додаткову кількість Товару за зниженою ціною;", "bold": False},
            {"text": "\n- Поставити/замінити Товар відповідно до умов, викладених у Контракті;", "bold": False},
            {"text": "\n- Відмовитися від приймання та оплати Товару, а також вимагати компенсації всіх витрат, включаючи, але не обмежуючись, транспортно-логістичними послугами, штрафами та фінансовими санкціями, накладеними на Покупця контрагентами (партнерами за наступними Контрактами на поставку Товару) через такі недоліки або неякісний Товар. Покупець також може вимагати компенсації збитків, понесених у результаті приймання неякісного Товару.", "bold": False},
            {"text": "\n3.7. Заміна Товару здійснюється за рахунок Продавця протягом 3 (трьох) робочих днів з дати претензії Покупця.", "bold": False},
            {"text": "\n3.8. При застосуванні знижки на Товар повідомлення про знижку надсилається представнику Продавця електронною поштою або електронним каналом зв'язку, зазначеним у реквізитах Контракту. Після отримання повідомлення електронною поштою про необхідність застосування знижки Продавець протягом однієї (1) години погоджує знижку, якщо Товар доставляється автотранспортом. Якщо доставка здійснюється залізницею, Продавець або погоджує знижку, або повідомляє Продавцю про направлення свого представника для спільного відбору проб і складання Акту невідповідності Товару. Якщо Продавець не відповідає протягом 1 години після відправлення електронного листа Покупцем, Покупець самостійно приймає рішення щодо знижки.", "bold": False},
            {"text": "\n3.9. У разі погодження знижки Продавцем сторони погоджуються, що даними, які використовуються для знижки через невідповідність якості та безпеки, є результати лабораторних досліджень, проведених на місці доставки або в незалежній лабораторії, обраній Покупцем, а також дані, зафіксовані в Акті невідповідності.", "bold": False},
            {"text": "\n3.10. Якщо Товар приймається за зниженою ціною на підставі даних Покупця, Продавець зобов'язується оформити митну декларацію (ВМД) на підставі даних про знижку, наданих Покупцем.", "bold": False},
            {"text": "\n3.11. У разі розбіжностей у кількості/якості Товару Покупець має право утримати оплату за всю кількість недопоставленого/неякісного Товару до надання виправлених документів:", "bold": False},
            {"text": "\n 3.11.1. Дані, зазначені у товарно-транспортній накладній (ТТН), з урахуванням зауважень Покупця, якщо такі є;", "bold": False},
            {"text": "\n  3.12.2. Дані лабораторних досліджень, з урахуванням знижки.", "bold": False},
        ])
        return sections
    
    def render_price(self):
        return [
            {"text": "\n4. ЦІНА:", "bold": True},
            {"text": f"\n4.1. Ціна за одну метричну тонну Товару становить {self.params['price_per_ton']} 00 доларів США ( {self.params['price_per_ton_text']} USD).", "bold": False},
            {"text": f"\n4.2. Загальна вартість Товару за Контрактом {self.params['total_value']} 00 USD ({self.params['total_value_text']} USD).", "bold": False},
        ]

    def render_delivery_sections(self):
        sections = [
            {"text": "\n5. УМОВИ І ТЕРМІНИ ПОСТАВКИ:", "bold": True},
            {"text": "\n5.1. Продавець вважається таким, що здійснив поставку Товару, коли Товар надано в розпорядження Покупця в місці визначеному Сторонами в даному Контракті, очищений від митних зборів, необхідних для ввезення, на прибулому транспортному засобі, готовому до розвантаження в зазначеному місці призначення.", "bold": False},
            {"text": "\n5.2. Продавець несе всі витрати і ризики, пов'язані з доставкою Товару в місце призначення, і зобов'язаний виконати митні формальності, необхідні для ввезення, сплатити будь-які збори, що стягуються під час ввезення, а також виконати всі митні формальності.", "bold": False},
            {"text": f"\n5.3. Постачання Товару буде здійснено на умовах  DAP. Дата поставки : з {self.params['delivery_start_date']} р. по {self.params['delivery_end_date']} р. обидві дати включно. Товар може поставлятися партіями. За день до поставки Товару Продавець повідомляє на електронну адресу Покупця про поставку відповідної партії Товару.", "bold": False},
            {"text": "\n5.4. Упаковка: 100% насипом.", "bold": False},
            {"text": "\n5.5. Вантажний автотранспорт повинен супроводжуватись наступними діючими документами:", "bold": False},
            {"text": "→   належно оформлена авто (товарно-транспортна) на кожен вантажний автотранспорт, заповнена Продавцем відповідно до інструкцій Покупця;", "bold": False},
            {"text": "\n5.6. Залізничні вагони повинні супроводжуватись наступними діючими документами:", "bold": False},
            {"text": "→   Залізничні квитанції/накладні на кожен день залізничний вагон відповідно до інструкції Покупця;", "bold": False},
            {"text": "→   Посвідчення про якість зерна (форма 42), виданий елеватором або зерновим складом в Пункті відвантаження Товару.", "bold": False},
            {"text": "\n5.7. Продавець повинен:", "bold": False},
            {"text": "a) укласти відповідний договір у порту з акредитованим митним брокером Покупця та проводити митне оформлення Товару за свій рахунок відповідно до інструкцій Покупця; Контактні дані митного брокера Покупця для з'ясування питань щодо митного оформлення: +380952892570;", "bold": False},
            {"text": "b) на власний страх і ризик і власним коштом отримати будь-яку експортну ліцензію, оформити сертифікат походження Товару, а також виконати всі митні формальності, необхідні для експорту Товару.\nПродавець надає Експедитору та митному брокеру в порту для митного оформлення Товару всі запитувані без виключення документи в терміни, які вказує Експедитор (митний брокер). Надані відомості або документи, які мають неточності або надання неповного пакету документів вважаються такими, що не надані Експедитору (митному брокеру). Датою одержання документів вважається дата їх вручення Експедитору (митному брокеру).", "bold": False},
            {"text": "\n5.8. Покупець повинен надати Продавцю всі необхідні документарні інструкції для заповнення транспортних документів шляхом надсилання електронною поштою;", "bold": False},
            {"text": "\n5.9. Здійснення поставок за даним Контрактом можливе лише після проходження Продавцем/Експортером акредитації у Покупця.", "bold": False},
            {"text": "\n5.10. Для поставок залізничним транспортом:", "bold": False},
            {"text": "\nПродавець по електронній пошті направляє Покупцю графік відвантаження.\nПокупець узгоджує наданий графік з терміналом в місці поставки та Продавцем, у випадку внесення змін у цей графік.\nПродавець зобов'язується здійснювати поставку Товару лише у відповідності до узгодженого графіку. Графік відвантаження має бути пропорційним до періоду поставки, якщо інше не погодять Сторони.\nПродавець уповноважує свого вантажовідправника надати Покупцю номер своєї заявки, зареєстрованої в АС Месплан за 7 (сім) днів до початку відвантаження.\nПокупець зобов'язаний організувати підтвердження даної заявки в АС Месплан з боку станції призначення та вантажоодержувача/Терміналу протягом 2 днів з моменту надання номера заявки.\nУ разі непогодження електронної заявки або погодження не в повному обсязі, або конвенції, введеної Державною адміністрацією залізничного транспорту України (Українські залізниці) та опубліковані на сайті https://uz.gov.ua/, сроки поставки Товару продовжуються на строк не погодження та/або дії конвенції.", "bold": False},
            {"text": "\n5.11. Продавець щоденно направляє на адресу Покупця електронною поштою добовий звіт про відвантажений Товар (згідно зразка, наданого разом з інструкціями) із зазначенням наступної інформації:", "bold": False},
            {"text": "\n- Номер даного Контракту;", "bold": False},
            {"text": "\n- Назву Експортера;", "bold": False},
            {"text": "\n- Дата відвантаження;", "bold": False},
            {"text": "\n- Станція відправлення та станція призначення;", "bold": False},
            {"text": "\n- Номер вагона/автомобіля;", "bold": False},
            {"text": "\n- Номер залізничної накладної/авто ТТН;", "bold": False},
            {"text": "\n- Назву та вагу (брутто, тара, нетто) вантажу; Скановані копії супровідних документів (Посвідчення про якість зерна (форма 42).", "bold": False},
            {"text": f"\n5.12. Експортери Товару за даним Контрактом: {self.params['exporter_name']}, код ЄДРПОУ:{self.params['edrpou_code']}. Зміна Експортера відбувається за згодою обох Сторін шляхом укладання Додаткової угоди до даного Контракту.\nПродавець надає Покупцю листи від зазначених у цьому пункті Експортерів про їх згоду здійснити відвантаження та експорт Товару.\nЯкщо Продавець не є резидентом України, Продавець підтверджує, що Товар, поставлений за цим Контрактом, було придбано безпосередньо в Експортера.\nПродавець надає гарантійний лист від зазначених у цьому пункті Експортерів про перехід субсидіарної відповідальності від Продавця до Експедитора у разі порушення або невиконання Покупцем своїх зобов'язань за даним Контрактом.", "bold": False},
            {"text": "\n5.13.У разі прибуття залізничним або автомобільним транспортом на адресу Покупця некондиційного Товару (завантажений, спечений Товар, наявність домішок) Покупець забезпечує складання актів, на підставі яких Продавець відшкодовує додаткові витрати, пов'язані з вивантаженням, прийманням, зберіганням та повернення такого Товару, включаючи простій вагонів.\nВагони із залишками кількостей фумігантів прийматися не будуть і повинні бути переадресовані Продавцем протягом 3 (трьох) діб  з моменту повідомлення Покупцем. У разі виявлення вагонів із залишками фумігації Покупець має право виставити рахунок на сплату штрафу Продавцю у розмірі 300, 00(триста) доларів США за вагон на добу, а Продавець зобов'язаний сплатити такий штраф протягом 5 (п'яти) банківських днів з моменту виставлення рахунку.\nПродавець зобов'язаний розпорядитися неконденційним Товаром протягом 3 ( трьох) днів з моменту повідомлення Покупцем. У разі порушення встановленого цим пунктом терміну для розпорядження некондинційним Товаром Продавець повинен сплатити Покупець штрафні санкції у сумі 300,00 (триста) доларів США за кожен вагон на добу з моменту сполучення та до повернення Товару, та відшкодувати Покупцю всі понесені збитки  документально підтверджених витрат у зв'язку з таким порушенням.", "bold": False},
            {"text": "\n5.14. Продавець та Експортер гарантує, що Товар який постачається :", "bold": False},
            {"text": "\n- на момент підписання цього Контракту, а також на момент переходу права власності на Товар від Продавця до Покупця, компетентними органами Продавця не приймаються і не будуть прийматися рішення про накладення будь-яких обтяжень на Товар (його частину), а також рішення щодо відчуження Товару;", "bold": False},
            {"text": "\n- на момент підписання цього Контракту, а також на момент переходу права власності на Товар від Продавця до Покупця, Товар не знаходиться та не буде знаходитися в податковій заставі, у спорі і під забороною на відчуження;", "bold": False},
            {"text": "\n- на момент підписання цього Контракту, а також на момент переходу права власності на Товар від Продавця до Покупця, Товар не буде продано, подаровано, відступлено, обміняно, виділено зі складу активів Продавця або закладено, передано в управління, а також не буде передано в оренду (користування) цілком або частинами;", "bold": False},
            {"text": "\n- на момент підписання цього Контракту, а також на момент переходу права власності на Товар від Продавця на Покупця, Товар перебуває в доброму стані та по-суті відповідає цілям, для яких воно призначено, та не містить жодних речовин або матеріалів, що мають недоліки або становлять ризик для здоров'я або безпеки;", "bold": False},
            {"text": "\n- на момент підписання цього Контракту, а також на момент переходу права власності на Товар від Продавця до Покупця, у Продавця відсутні які-небудь зобов'язання, термін яких наступив або наступить у майбутньому (у т.ч. по попередніх контрактах, офертах, опціонах тощо) по відчуженню Товару, передачі окремих прав (право користування, право розпорядження, право володіння) на Товар;", "bold": False},
            {"text": "\n- Товар є вільним від будь-яких прав та претензій третіх осіб, а також від будь-яких інших обмежень чи обтяжень будь-якого характер.", "bold": False},
            {"text": "\nПродавець та Експортер також підтверджує, що походження Товару не є з Донецької області, Луганської області, Запорізької області, Херсонської області, Автономної Республіки Крим та інших тимчасово окупованих територій України.", "bold": False},
            {"text": "Продавець та Експортер не зареєстровані та не здійснюють господарську діяльність на зазначених тимчасово окупованих територіях України.", "bold": False},
            {"text": "\nУ разі виявлення факту, що Товар має походження з вказаних регіонів, Постачальник та Експортер зобов'язані повністю відшкодувати Покупцю всі понесені витрати та збитки, що можуть виникнути у зв'язку з постачанням такого Товару.", "bold": False},
            {"text": "\n5.15. Постачальник зобов'язується зареєструвати ПМД протягом 3-х днів з дати настання першої події: постачання або оплати за кожну партію Товару, але в будь якому випадку за 3 дні до закінчення терміну поставки повної партії Товару.", "bold": False},
            {"text": f"\n5.16. Постачальник самостійно оплачує вартість реєстрації автомобілю у розмірі 500 грн., при відвантаженні Товару до {self.params['delivery_address']}", "bold": False},
        ]
        return sections
    
    def render_payment_conditions(self):
        sections = [
            {"text": "\n6. УМОВИ ОПЛАТИ:", "bold": True},
            {"text": f"\n6.1. Покупець зобов'язаний сплатити вартість Товару, поставленого на місце поставки, на рахунок Продавця банківським переказом у наступному порядку:", "bold": False},
            {"text": f"\n- {self.params['first_payment_percent']}% вартості Товару протягом {self.params['first_payment_days']} (трьох) банківських днів після поставки всього об'єму зазначеного у Контракті та наданні документів визначених в п. 6.2. Контракту;", "bold": False},
            {"text": f"\n- {self.params['second_payment_percent']}% вартість Товару Покупець зобов'язаний сплатити протягом {self.params['second_payment_days']} днів після оформлення Продавцем ВМД.", "bold": False},
            {"text": "\n6.2. Продавець повинен надати Покупцю наступні документи:", "bold": False},
            {"text": "\n- Інвойсу на оплату від Продавця із зазначенням загальної вартості Товару у розмірі +5%;", "bold": False},
            {"text": "\n- Лист на підтвердження відвантаження та підписання інструкції на відвантаження;", "bold": False},
            {"text": "\n- Картка обліку на митниці – копія завірена (акредитація у митниці);", "bold": False},
            {"text": "\n- Зовнішньоекономічний контракт, додаток (якщо він є) – кожна сторінка Контракта повинна бути належним чином завірена директором, або уповноваженою особою;", "bold": False},
            {"text": "\n- Рахунок-Проформа 1 екз. оригінал, потім Рахунок-фактура для оформлення ЕК10ДР (ГТД/ВМД/ДР) – оригінал;", "bold": False},
            {"text": "\n- Виписка з Держреєстра про головний вид діяльності підприємства - копія завірена;", "bold": False},
            {"text": "\n- Довідка про походження Товару – оригінал;", "bold": False},
            {"text": "\n- Лист контактної особи – оригінал;", "bold": False},
            {"text": "\n- Лист-підтвердження реєстрації в Держпродспожив службі - копія завірена;", "bold": False},
            {"text": "\n- Скановану копію залізничної накладної (при поставці залізничним транспортом у вагонах).", "bold": False},
            {"text": "\n6.3. Розрахунки між Покупцем і Продавцем здійснюються в доларах США.", "bold": False},
            {"text": "\n6.4. Датою оплати вважається дата списання грошових коштів з банківського рахунку Покупця на банківський рахунок Продавця, при умові наданням Покупцем копії SWIFT.", "bold": False},
            {"text": "\n6.5. До ціни включається вартість упаковки, маркування, оплата всіх зборів і митних зборів і платежів під час розмитнення, транспортування та страхування вантажу.", "bold": False},
            {"text": "\n6.6. Підставою для оплати є рахунок-фактура (інвойс), виставлений Продавцем, на умовах викладених в п.6.1.Контракту.", "bold": False},
            {"text": "\n6.7. Усі банківські витрати в країні Покупця здійснюються за рахунок Покупця, усі банківські витрати в країні Продавця – за рахунок Продавця.", "bold": False},
        ]
        return sections

    def render_title_to_goods(self):
        sections = [
            {"text": "\n7. ПРАВО ВЛАСНОСТІ НА ТОВАР:", "bold": True},
            {"text": "\n7.1. Право власності на Товар переходить від Продавця до Покупця з дати оформлення митної декларації типу ЕК 10 ДР.", "bold": False},
        ]
        return sections

    def render_sanctions(self):
        sections = [
            {"text": "\n8. САНКЦІЇ:", "bold": True},
            {"text": "\n8.1. Кожна із Сторін заявляє, що не приймає чи утримуватиметься від будь-яких дій, які можуть призвести до порушення нею чи іншою Стороною законів, правил, постанов, указів чи правил будь-якої відповідної юрисдикції, пов'язані з санкціями, ембарго, контролем торгівлі чи бойкотом. Кожна Сторона також зобов'язується не приймати або утримуватись від будь-яких дій, які можуть призвести до вказаного вище результату.", "bold": False},
        ]
        return sections

    def render_claims(self):
        sections = [
            {"text": "\n9. ПРЕТЕНЗІЇ:", "bold": True},
            {"text": "\n9.1. Сторони намагатимуться вирішувати всі суперечки, що виникають між ними під час виконання цього Контракту шляхом переговорів.", "bold": False},
            {"text": "\n9.2. За непоставку (недопоставку)/несвоєчасну заміну неякісного Товару в строки додатково погоджені Сторонами, Продавець зобов'язується сплатити Покупцю наступні штрафні та фінансові санкції, а саме:", "bold": False},
            {"text": "\n- пеню (штрафну санкцію) в розмірі 0,5% від вартості Товару, поставку якого була прострочена, за кожен день прострочення такої поставки. За прострочення поставки більш ніж на 5 календарних днів Продавця, крім пені (додатково) зобов'язується також сплачувати Покупцю штраф в розмірі 20 % від вартості непоставленого (недопоставленого) Товару;", "bold": False},
            {"text": "\n- також Покупець може перекупити товар у іншого Продавця, тоді Продавець компенсує Покупцю різницю у вартості товару.", "bold": False},
            {"text": "\nПеня та штраф за цим пунктом сплачується Продавцем незалежно від заподіяних Покупцю збитків (штрафна неустойка).", "bold": False},
            {"text": "\n9.3. У разі відмови від реєстрації ПМД, несвоєчасної реєстрації ПМД або порушення порядку заповнення ПМД, поставка Товару є такою що не відбулась в повному обсязі та застосовуються штрафні санкції передбачені п. 9.2. цього Контракту.", "bold": False},
            {"text": "\n9.4. Якщо Продавець/ Експортер Продавця не забезпечить своєчасне митне оформленням Товару на судно, номіноване Покупцем, а митне оформленням Товару Експортером/Продавцем буде неможливе відповідним рішенням судових, фіскальних чи правоохоронних органів, Продавець зобов'язаний відшкодувати Покупцю всі витрати, включаючи, але не обмежуючись простоєм судна (демередж), понаднормове зберігання, тощо, пов'язані або спричинені затримкою Товару на Терміналі/Порту/Судні протягом 5 робочих днів з дня виставлення відповідного рахунку Покупцем.", "bold": False},
            {"text": "\n9.5. У випадку порушення строку поставки більш ніж на 10 (десять) календарних днів, Покупець має право відмовитись від поставки Товару по Контракту і вимагати від Продавця відшкодування заподіяних збитків та повернення грошових коштів, що були сплачені на умовах попередньої оплати, які Продавець зобов'язаний повернути в такому випадку протягом 3 (трьох) банківських днів з моменту повідомлення Покупця про відмову від Товару та повернення коштів.", "bold": False},
            {"text": "\n9.6. У разі неповної передачі Покупцеві товаросупровідної документації, передбаченої пп.6.2. Контракту, Покупець вправі застосувати до Продавця затримку оплати Товару до моменту усунення Продавцем відповідного порушення.", "bold": False},
            {"text": "\n9.7. У випадку порушення Продавцем будь-яких гарантій, передбачених п.5.14. цього Контракту (зокрема, у разі виявлення, що Товар є предметом застави, в тому числі, податкової, зобов'язується відшкодувати Покупцю збитки, понесені Покупцем, в повному обсязі, а також сплатити Покупцю штраф в розмірі 30 % від вартості такого Товару. Штраф сплачується Продавцем незалежно від наявності збитків.", "bold": False},
            {"text": "\n9.8. Окрім того, у разі прострочення виконання зобов'язань, що спричинило необхідність зберігання зерна на складі Терміналу понад узгоджені строки, Постачальник відшкодовує Покупцеві фактичні витрати на зберігання зерна, підтверджені відповідними фінансовими документами (рахунки, акти виконаних робіт тощо), за весь період прострочення.", "bold": False},
            {"text": "\n9.9. У разі затримки оплати за Товар Покупець сплачує Продавцю штрафні санкції у розмірі 0.02% від суми неоплаченого Товару за кожен день затримки.", "bold": False},
            {"text": "\n9.10. Продавець та Покупець повинні бути відповідальними за будь-яке невиконання своїх зобов'язань за цим Контрактом.", "bold": False},
        ]
        return sections

    def render_arbitration(self):
        sections = [
            {"text": "\n10. АРБІТРАЖ:", "bold": True},
            {"text": "\n10.1. Усі спори та розбіжності, які можуть виникнути під час виконання цього Контракту або у зв'язку з ним, вирішуються шляхом переговорів між Сторонами.", "bold": False},
            {"text": "\n10.2. Продавець і Покупець докладають усіх зусиль для врегулювання всіх спорів і розбіжностей, що можуть виникнути з цього Контракту або у зв'язку з ним, мирним шляхом. У випадку, якщо спір не вдалося розв'язати шляхом переговорів, всі спори та розбіжності, що виникають у зв'язку з цим Контрактом, а також усі претензії, пов'язані із тлумаченням або виконанням умов цього Контракту, вирішуються в арбітражному порядку у відповідності із Арбітражними Правилами ГАФТА, № 125, в редакції, чинній на дату цього Контракту. Мова арбітражу - Англійська, місце арбітражу - м. Лондон Англія.", "bold": False},
        ]
        return sections

    def render_anti_bribery(self):
        sections = [
            {"text": "\n11. АНТИКОРУПЦІЙНІ ПИТАННЯ:", "bold": True},
            {"text": "\n11.1. Кожна із Сторін погоджується та зобов'язується перед іншою, що згідно з цим Контрактом, вони відповідно дотримуватимуться всіх законів, правил, положень, указів та/або офіційних урядових розпоряджень, що стосуються боротьби з хабарництвом та відмиванням грошей. Кожна із Сторін представляє, гарантує та зобов'язується іншою, не буде прямо чи опосередковано", "bold": False},
            {"text": "\na) не буде прямо або опосередковано здійснювати або намагатися здійснити будь-які дії, спрямовані на надання хабар, у тому числі через платіж, пропозицію, обіцянку чи інші форми надання вигоди будь-яким фізичним або юридичним особам, включаючи державних посадових осіб;", "bold": False},
            {"text": "\nb) вимагати, давати згоду на отримання чи приймати хабар від будь-якої фізичної чи юридичної особи;", "bold": False},
            {"text": "\nc) брати участь у будь-яких інших подібних транзакціях,", "bold": False},
            {"text": "\nу будь-якому випадку, якщо це порушення суперечить законодавству будь-якого уряду щодо боротьби з хабарництвом та відмиванням грошей.", "bold": False},
        ]
        return sections

    def render_force_majeure(self):
        sections = [
            {"text": "\n12. ФОРС-МАЖОР:", "bold": True},
            {"text": "\n12.1. Жодна із Сторін не несе відповідальності за часткове або повне невиконання зобов'язань за цим Контрактом, якщо невиконання є результатом обставин непереборної сили, що виникли після укладення Контракту і які не можна було ні передбачити, ні запобігти розумним заходам (форс-мажор), якщо такі не були відомі раніше на момент укладання Контракту, як, наприклад, агресія Росії проти України. Повені, пожежі, землетруси, вибухи, бурі, осідання грунту, епідемії та інші стихійні лиха, а також війна та військові операції розглядаються як форс-мажор.", "bold": False},
            {"text": "\n12.2. У разі настання та припинення обставин, зазначених у пункті 12.1. цього Контракту, Сторона, яка не в змозі виконати свої зобов'язання за цим Контрактом, повинна надіслати письмове повідомлення іншій Стороні протягом 5 (п'яти) календарних днів. Якщо така Сторона не може подати таке повідомлення вчасно, вона зобов'язана відшкодувати збитки іншій Стороні через неповідомлення або пізнє повідомлення.", "bold": False},
            {"text": "\n12.3. У разі настання форс-мажору термін виконання цього Контракту може бути продовжений на період дії обставин форс-мажору. Якщо форс-мажор триває понад 30 (тридцять) календарних днів Сторони мають право розірвати Контракт, при цьому вони повинні випустити акт звіряння та провести розрахунки за цим Контрактом у його виконаній частині.", "bold": False},
            {"text": "\n12.4. Виникнення обставин форс-мажору має бути доведено Торгово-промисловою палатою країни, де такі обставини мали місце.", "bold": False},
            {"text": "\n12.5. Сторони розуміють значення своїх дій та наслідки, які можуть виникнути при виконанні даного Контракту, адже місце виконання Контракту Україна, в країні, якій діє воєнний стан. На момент укладання цього Контракту, Сторони розуміють, що згідно до Указу Президента України №64/2022 від 24 лютого 2022 року \"Про введення воєнного стану в Україні\", із 5 години 30 хвилин 24 лютого 2022 року в Україні відбувається військова агресія Російської Федерації і тому посилання на ці обставини не є форс-мажорними обставинами у розумінні цього Контракту і не звільняє сторони від своєчасного виконання зобов'язань по цьому Контракту. Винятком з цього правила є обставини воєнного стану та військові дії, які безпосередньо вплинуть на можливість для Сторони виконати свої договірні зобов'язання.", "bold": False},
        ]
        return sections

    def render_other_conditions(self):
        sections = [
            {"text": "\n13. ІНШІ УМОВИ:", "bold": True},
            {"text": "\n13.1. Продавець цим гарантує, що він має і мав дійсне право власності на Товар і Товар не є предметом відчуження або обтяження. Весь товар знаходиться у власності або під контролем Продавця, або Продавець має право володіти Товаром або контролювати його, як тільки це буде практично можливим, і такий товар знаходиться в Україні.", "bold": False},
            {"text": "\n13.2. Сторони домовилися, що текст Контракту, будь-які матеріали, інформація та дані щодо Контракту є конфіденційними та не можуть передаватися третім особам без попередньої письмової згоди іншої сторони Контракту, крім випадків, коли така передача пов'язана з отриманням офіційних дозволів та документів, необхідних для виконання Контракту чи сплати податків та інших обов'язкових платежів.", "bold": False},
            {"text": "\n13.3. Цей Контракт або будь-які доповнення належним чином підписані та надіслані Сторонами засобами факсимільного зв'язку будуть вважатися дійсними, доки їх паперові оригінали не будуть отримані.", "bold": False},
            {"text": "\n13.4. Усі доповнення є невід'ємною частиною цього Контракту.", "bold": False},
            {"text": "\n13.5. Сторони не можуть передавати свої права згідно з Контрактом третій стороні без письмової згоди іншої сторони.", "bold": False},
            {"text": "\n13.6. Цей Контракт складено у двох оригіналах, українською та англійською мовами, 1 (один) оригінал для кожної із сторін. Обидва оригінали мають рівну юридичну силу.", "bold": False},
            {"text": "\n13.7. Сторони погодилися, що Покупець не здійснюватиме реекспорт, що є предметом цього Контракту, на ринки третіх країн без попередньої письмової згоди Міністерства економіки та європейської інтеграції України.", "bold": False},
            {"text": "\n13.8. Сторони домовилися, що надіслані документи, листи, вимоги, повідомлення на електронні адреси визначені в даному пункті Контракту вважаються офіційним адресами для ведення листування і обміном інформації та документації. Всі листи, вимоги, претензії, копії документів можуть направлятися на вказані нижче електронні адреси. Відправлені і доставлені документи, листи, вимоги вважаються відправленими і отриманими з моменту отримання відповідного повідомлення в електронному вигляді.", "bold": False},
            {"text": "\nДля швидкого обміну документацією Сторони погодили наступні електронні адреси:", "bold": False},
            {"text": f"\nВід Постачальника: {self.params['seller_email']};", "bold": False},
            {"text": f"\nВід Покупця: {self.params['buyer_email']}.", "bold": False},
            {"text": "\n13.9. Сторони погодили, що субота, неділя та свята, що офіційно або відповідно до закону визнаються такими у країнах резиденції Сторін, вважаються неробочими днями. Якщо строк вчинення певної дії або направлення будь-якого повідомлення спливає у неробочий день, такий строк продовжується до першого наступного робочого дня. Цей пункт не стосується Строку поставки.", "bold": False},
        ]
        return sections

    def render_signatures(self):
        sections = [
            {"text": "\n14. ПІДПИСИ СТОРІН:", "bold": True},
            {"text": "\nПОКУПЕЦЬ /BUYER:___________", "bold": False},
            {"text": "\nПРОДАВЕЦЬ /SELLER:___________", "bold": False},
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



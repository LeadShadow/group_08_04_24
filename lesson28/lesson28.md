# Software Engineering та принципи SOLID

## Software Engineering як процес

Програмна інженерія (Software Engineering) - це інженерна галузь, пов'язана з розробкою програмного продукту з використанням чітко визначених наукових принципів, методів та процедур. Результатом розробки програмного забезпечення є ефективний та надійний програмний продукт.

### Причини виникнення

Приблизно кожні 5 років кількість розробників подвоюється. Очевидний наслідок цього факту — в будь-який момент часу половина всіх розробників на ринку мають менше 5 років досвіду та недостатній рівень кваліфікації, щоб створювати якісний програмний продукт.

Зараз будь-яку людину на нашій планеті оточує мінімум 5 обчислювальних пристроїв різного рівня складності, які виконують кимось написаний код. Наше життя дуже залежить від того, що код в навколишніх пристроях працює без збоїв та помилок.

Поєднання цих двох факторів призводить до того, що вимоги до якості програмного забезпечення постійно зростають, але недостатній рівень кваліфікації більшості розробників не дозволяє відповідати цим вимогам.

В результаті ми отримуємо сучасну бізнес-модель розробки ПЗ, коли користувачі перших "стабільних" версій виступають фактично тестувальниками для неякісного, неналагодженого та випущеного поспіхом програмного продукту.

Фактично, зараз, на початку 2020-х, індустрія розробки програмного забезпечення переживає кризу становлення.

Перші ознаки кризи, що насувається, проявилися наприкінці 1960-х років. Багато програмних проектів зазнали невдачі і вийшли за межі бюджету. На виході вийшло ненадійне програмне забезпечення, обслуговування якого вимагає високих витрат. Програмне забезпечення більшого розміру стало досить дорогим в обслуговуванні. Це призводило до того, що програмне забезпечення не здатне було задовольнити зростаючі вимоги замовника, а попит на нове програмне забезпечення збільшувався швидше, ніж можливість створення нового програмного забезпечення.

Вирішенням проблеми було перетворення неорганізованого програмування на дисципліну програмної інженерії. Ці інженерні моделі покликані допомогти компаніям оптимізувати операції та надати програмне забезпечення, яке відповідає вимогам клієнтів.

З кінця 1970-х років настає початок розробки та широкого використання різних підходів та принципів програмної інженерії. У 1980-х роках відбулася автоматизація процесу розробки програмного забезпечення та зростання автоматизованої розробки програмного забезпечення. 1990-ті роки стали часом підвищеної уваги до «управлінських» аспектів проектів, стандартів якості та процесів, таких як ISO 9001. На початку 2000-х років дуже швидкими темпами наростає популярність гнучких підходів (Agile) до розробки ПЗ та стає практично стандартом навіть у тих сферах, де не зовсім підходить. У 2010-х тривале зростання складності ПЗ виводить на перше місце чисто управлінську проблему складності розробки ПЗ паралельно декількома командами розробників в межах одного продукту. Популярним вирішенням проблеми паралельної розробки стає мікросервісна архітектура, постійна інтеграція мікросервісів (CI) та постійна доставка (CD).

### Основні проблеми, які стоять перед розробниками ПЗ

- **Розмір та складність програмного забезпечення.** У реальному житті рідко зустрінеш реальний продукт із кодовою базою менше 100000 рядків.
- **Масштабованість.** Успішний продукт може зростати експоненційно та розробники повинні закладати можливість швидко та легко налаштовувати ПЗ, щоб воно справлялося з тисячократно збільшеним навантаженням.
- **Адаптивність.** Вимоги бізнесу до програмного продукту постійно змінюються та продукт повинен бути досить гнучким, щоб швидко та дешево задовольняти вимогам, що змінюються.
- **Вартість.** Розвиток промисловості та масове виробництво знизило вартість комп'ютерів та електронного обладнання, і тепер основна частина вартості більшості сучасних продуктів — це їхнє ПЗ. У свою чергу, це породжує вимогу знизити накладні витрати на розробку ПЗ, збільшивши ефективність розробки, щоб успішно конкурувати на ринку.
- **Управління якістю та ціною якості ПЗ.** Бізнес хоче мати можливість гнучко контролювати накладні витрати на виробництво ПЗ та розуміти, яку якість він отримає за яку вартість.

### Методології програмної інженерії

- Підходи до управління процесом розробки (Agile, Scrum, Kanban та ін.)
- Принципи проектування (SOLID, аспекти, Domain Driven Design та ін.)
- Архітектурні принципи (мікросервісна архітектура, event-driven архітектура).
- Підходи до розробки (Test Driven Design, парне програмування та ін.)
- Патерни проектування

## Важливість використання підходів та методологій програмної інженерії

### Знижує складність

Велике програмне забезпечення — це завжди складно, і його складно розвивати та підтримувати. У програмної інженерії є чудове рішення, яке дозволяє знизити складність будь-якого проекту. Програмна інженерія розділяє великі проблеми на різні дрібні. А потім починає вирішувати кожну невелику проблему по черзі. Всі ці маленькі проблеми вирішуються незалежно одна від одної.

### Зводить до мінімуму вартість

Програмне забезпечення вимагає багато зусиль, а програмісти — високооплачувані спеціалісти. Для розробки програмного забезпечення з великою кількістю рядків коду потрібно багато робочої сили. Але при розробці програмного забезпечення програмісти все проектують і цим зменшують кількість непотрібних речей. У свою чергу, вартість виробництва програмного забезпечення стає меншою у порівнянні з будь-яким програмним забезпеченням, в якому не використовується метод програмної інженерії.

### Скорочує час

Все, що зроблено не відповідно до проекту, завжди призводить до марнування часу. І дуже трудомістка процедура — отримати остаточний робочий код. Якщо з нею не впоратися належним чином, це може зайняти багато часу. Тому, якщо ви створюєте своє програмне забезпечення відповідно до методу розробки програмного забезпечення, це значно скоротить вам час.

### Робота з великими проектами

Великі проекти не виконуються за декілька днів, і вони вимагають великого терпіння, планування та управління. А щоб інвестувати шість або сім місяців у будь-який проект, потрібно багато планування, управління, тестування та обслуговування. Ніхто не хоче, щоб на виконання проекту було заплановано чотири місяці, а після цього часу виявилося, що проект все ще перебуває на першій стадії. Компанія виділила багато ресурсів на план, і він повинен бути виконаний. Таким чином, щоб без проблем впоратися з великим проектом, компанія повинна вдатися до методів розробки програмного забезпечення.

### Надійність

Програмне забезпечення повинно бути надійним. Якщо ви поставили програмне забезпечення кінцевому споживачеві, воно повинно працювати, принаймні, прот
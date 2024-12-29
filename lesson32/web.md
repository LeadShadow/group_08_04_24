## Робота мережі

Робота мережі полягає у передачі даних від одного комп'ютера до іншого. У цьому процесі можна виділити декілька окремих завдань:

1. розпізнати дані;
2. розбити дані на керовані блоки;
3. додати інформацію до кожного блоку, щоб;
4. вказати місце знаходження даних;
5. вказати одержувача;
6. додати інформацію синхронізації та інформацію для перевірки помилок;
7. помістити дані в мережу та надіслати їх за заданою адресою.


Мережева операційна система при виконанні всіх завдань дотримується суворого набору процедур. Ці процедури називаються протоколами або правилами поведінки. Протоколи регламентують кожну мережеву операцію.



Стандартні протоколи дозволяють програмному та апаратному забезпеченню різних виробників нормально взаємодіяти. Існує стандарт – модель OSI.



## Модель OSI


У 1978 році International Standards Organization (ISO) випустила набір специфікацій, що описують архітектуру мережі з неоднорідними пристроями. 



Вихідний документ стосувався відкритих систем, щоб усі вони могли використовувати однакові протоколи та стандарти для обміну інформацією.



В 1984 ISO випустила нову версію своєї моделі, названу еталонною моделлю взаємодії відкритих систем (Open System Interconnection reference model, OSI). 



Версія 1984 стала міжнародним стандартом: її специфікації використовують виробники при розробці мережевих продуктів, вона є основою побудови різних мереж.



Ця модель — поширений метод опису мережевих середовищ. Будучи багаторівневою системою, вона відображає взаємодію програмного та апаратного забезпечення при здійсненні сеансу зв'язку, а також допомагає розв'язувати різноманітні проблеми.



## Багаторівнева архітектура​



У моделі OSI мережеві функції розподілені між сімома рівнями. Кожному рівню відповідають різні мережеві операції, обладнання та протоколи.

На кожному рівні виконуються певні мережеві функції, які взаємодіють із функціями сусідніх рівнів, що знаходяться вище і нижче. Наприклад, Сеансовий рівень повинен взаємодіяти лише з Представницьким та Транспортним рівнем тощо. Усі ці функції детально описані.

Нижні рівні – 1-й та 2-й – визначають фізичне середовище передачі даних та супутні завдання (такі як передача бітів даних через плату мережного адаптера та кабель). Найвищі рівні визначають, яким способом здійснюється доступ застосунків до послуг зв'язку. Що вищий рівень, то складніше завдання він вирішує.



Кожен рівень надає кілька послуг (тобто виконує кілька операцій), які готують дані для доставки мережею на інший комп'ютер. Рівні відокремлюються між собою межами — інтерфейсами. Всі запити від одного рівня до іншого передаються через інтерфейс. Кожен рівень використовує послуги нижчого рівня.



Докладніше про взаємодію рівнів моделі OSI перегляньте [додаткові матеріали](https://dou.ua/forums/topic/46215/).

# Як влаштований інтернет



## Основні поняття

​

**Хостинг** — послуга з надання обчислювальних потужностей для розміщення інформації на сервері, яка постійно знаходиться в мережі. Хостингом також називається послуга з розміщення обладнання клієнта на території провайдера із забезпеченням підключення його до каналів зв'язку з високою пропускною здатністю. Зазвичай хостинг входить до пакету з обслуговування сайту та вважається як мінімум послуга розміщення файлів сайту на сервері, на якому запущено ПЗ, необхідне для обробки запитів до цих файлів (веб-сервер). Як правило, до обслуговування вже входить надання місця для поштової кореспонденції, баз даних, DNS, файлового сховища на спеціально виділеному файл-сервері тощо, а також підтримка функціонування відповідних сервісів.

**Сервер DNS** — програмно-апаратний комплекс, що забезпечує трансляцію доменних імен на мережеві адреси (IP-адреси).

**Координатор** — уповноважена юридична особа, яка здійснює управління доменами .ua.

**Доменне ім'я** — символьне позначення, призначене для мережної адресації, в якій використовується система доменних імен.

**Стоп-лист** — перелік символьних позначень, реєстрація яких у якості доменних імен недоступна.

**Реєстратор** — юридична особа, акредитована Координатором для реєстрації доменних імен у доменах .ua

## Протокол HTTP

Сервер та браузер спілкуються, надсилаючи один одному запити за особливим протоколом – HTTP (RFC-2616). З'єднання може ініціювати лише браузер. Він посилає серверу запит - показати такий-то файл.

**HTTP** є синхронним протоколом. Це означає, що клієнт надіслав запит серверу і поки чекає від нього відповідь, наступні запити надіслати не може. Також варто відзначити, що HTTP — протокол без стану. Тобто сервер не зберігає інформацію про користувача між запитами.

**Протокол HTTP** — це протокол передачі даних, спочатку призначений для передачі гіпертекстових документів (тобто документів, які можуть містити посилання, що дозволяють організувати перехід до інших документів).

По суті є дуже простим текстовим протоколом. Заснований на обробці спеціальних символів та ключових слів у повідомленнях.



Для збереження стану користувача в системі використовується механізм **cookie** або **сесій**.

Запит відбувається у кілька етапів:


1. DNS-запит — пошук найближчого DNS-сервера, щоб перетворити URI (наприклад, google.com) на його числове представлення - IP-адреса (74.125.87.99, прим. - Отримано за допомогою команди ping). Це адреса і буде реальною адресою сайту в Інтернет.
2. з'єднання — встановлення з'єднання з сервером за отриманою IP-адресою;
3. відправлення даних;
4. очікування відповіді - в цей момент чекаємо, доки пакети даних дійдуть до сервера, він їх обробить і відповідь повернеться назад;
5. отримання даних.


Якщо якийсь елемент веб-сторінки розміщено на іншому хості, для запиту цього елемента встановлюється нове з'єднання, починаючи з DNS-запиту.

Основою HTTP є технологія "клієнт-сервер", тобто передбачається існування:

* Споживачів (клієнтів), які ініціюють з'єднання та надсилають запит;
* Постачальників (серверів), які очікують на з'єднання для отримання запиту, роблять необхідні дії та повертають назад повідомлення з результатом.


Основним об'єктом маніпуляції в HTTP є ресурс, який вказує URI (Uniform Resource Identifier) ​​у запиті клієнта. Особливістю протоколу HTTP є можливість вказати в запиті та відповіді спосіб представлення одного і того самого ресурсу за різними параметрами: форматом, кодуванням, мовою тощо (зокрема для цього використовується HTTP-заголовок). Саме завдяки можливості зазначення способу кодування повідомлення, клієнт та сервер можуть обмінюватися двійковими даними, хоча цей протокол є текстовим.
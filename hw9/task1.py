# Ваша компанія веде блог. Треба реалізувати функцію find_articles для пошуку за статтями
# цього блогу. Є список articles_dict, в якому міститься опис статей блогу. Кожен елемент
# цього списку є словником з наступними ключами: прізвища авторів - ключ 'author',
# назва статті - ключ 'title', рік видання - ключ 'year'.
#
# Реалізуйте функцію find_articles,
#
# Параметр key функції визначає поєднання букв для пошуку. Наприклад,
# при key="Python" функція шукає, чи є у списку articles_dict статті, у назві чи
# іменах авторів яких зустрічається це поєднання літер. Якщо такі елементи списку були
# знайдені, треба повернути новий список зі словників, що містять прізвища авторів,
# назву та рік видання всіх таких статей.
#
# Другий ключовий параметр функції letter_case визначає, чи треба враховувати під час
# пошуку регістр літер. За умовчанням він дорівнює False і регістр немає значення тобто
# пошук в тексті "Python" і "python" це те ж саме. Інакше потрібно шукати повний збіг.

articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    mathing_articles = []
    search_key = key.lower() if not letter_case else key

    for article in articles_dict:
        title = article['title']
        author = article['author']

        title_to_check = title.lower() if not letter_case else title
        author_to_check = author.lower() if not letter_case else author

        if search_key in title_to_check or search_key in author_to_check:
            mathing_articles.append({
                'author': author,
                'title': title,
                'year': article['year']
            })
    return mathing_articles


print(find_articles('Artur'))
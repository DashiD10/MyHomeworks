# Dataset
# small_dict = {
#     'Человек-муравей и Оса: Квантомания': 2023,
#     'Стражи Галактики. Часть 3': 2023,
#     'Капитан Марвел 2': 2023,
#     'Дэдпул 3': 2024,
#     'Капитан Америка: Дивный новый мир': 2024,
#     'Громовержцы': 2024,
#     'Блэйд': 2025,
#     'Фантастическая четвёрка': 2025,
#     'Мстители: Династия Канга': 2026,
#     'Мстители: Секретные войны': 2027,
#     'Безымянный фильм о Человеке-пауке': None,
#     'Безымянный фильм о Шан-Чи': None,
#     'Безымянный фильм о Вечных': None,
#     'Безымянный фильм о мутантах': None
# }
from marvel import small_dict


def search_movies():
    search_term = input("Введите название фильма или его часть: ").lower()
    found_movies = []

    for movie in small_dict.keys():
        if search_term in movie.lower():
            found_movies.append(movie)

    if found_movies:
        print("\nНайденные фильмы:")
        for movie in found_movies:
            print(f"- {movie}")
    else:
        print("Фильмы не найдены")


def filter_movies_after_2024():

    print("\nФильмы после 2024 года:")
    for movie, year in small_dict.items():
        if isinstance(year, (int, float)) and year > 2024:
            print(f"- {movie}")

    filtered_titles = [
        movie
        for movie, year in small_dict.items()
        if isinstance(year, (int, float)) and year > 2024
    ]

    filtered_dict = {
        movie: year
        for movie, year in small_dict.items()
        if isinstance(year, (int, float)) and year > 2024
    }

    filtered_list_of_dicts = [
        {movie: year}
        for movie, year in small_dict.items()
        if isinstance(year, (int, float)) and year > 2024
    ]

    print("\nСписок названий:", filtered_titles)
    print("\nОтфильтрованный словарь:", filtered_dict)
    print("\nСписок словарей:", filtered_list_of_dicts)


search_movies()
filter_movies_after_2024()

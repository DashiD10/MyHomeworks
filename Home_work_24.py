from typing import Dict, List, Set, Any, Optional, Union
from pprint import pprint
from marvel import full_dict


def get_user_input() -> List[Optional[int]]:
    user_input = input("Введите цифры, разделенные пробелом: ")
    return list(map(lambda x: int(x) if x.isdigit() else None, user_input.split()))

def repack_to_list() -> List[Dict[str, Any]]:
    return [{**{"id": k}, **v} for k, v in full_dict.items()]

def filter_by_ids(ids: List[Optional[int]]) -> List[Dict[str, Any]]:
    return list(filter(lambda x: x["id"] in ids, repack_to_list()))

def get_unique_directors() -> Set[str]:
    return {
        movie["director"] for movie in full_dict.values() if movie["director"] != "TBA"
    }

def convert_years_to_str() -> Dict[int, Dict[str, Any]]:
    return {k: {**v, "year": str(v["year"])} for k, v in full_dict.items()}

def filter_ch_movies() -> List[Dict[str, Any]]:
    return list(
        filter(lambda x: x["title"] and x["title"].startswith("Ч"), full_dict.values())
    )

def sort_by_year() -> Dict[int, Dict[str, Any]]:
    sorted_items = sorted(
        full_dict.items(),
        key=lambda x: x[1]["year"] if isinstance(x[1]["year"], int) else float("inf"),
    )
    return dict(sorted_items)

def sort_by_year_and_title() -> Dict[int, Dict[str, Any]]:
    sorted_items = sorted(
        full_dict.items(),
        key=lambda x: (
            x[1]["year"] if isinstance(x[1]["year"], int) else float("inf"),
            x[1]["title"] if x[1]["title"] else "",
        ),
    )
    return dict(sorted_items)

def filter_and_sort_oneliner() -> Dict[int, Dict[str, Any]]:
    return dict(
        sorted(
            filter(
                lambda x: isinstance(x[1]["year"], int) and x[1]["year"] > 2020,
                full_dict.items(),
            ),
            key=lambda x: x[1]["year"],
        )
    )


def main():
   
    print("\n=== Ввод пользователя ===")
    user_ids = get_user_input()
    pprint(user_ids)

    print("\n=== Перепаковка `full_dict` в список словарей ===")
    pprint(repack_to_list()[:2])  

    print("\n=== Использование фильтрации по `ids` ===")
    pprint(filter_by_ids(user_ids))

    print("\n=== Множество с помощью `set comprehension`, уникальные значения ключа `director` из словаря ===")
    pprint(get_unique_directors())

    print("\n=== Преобразование Years as Strings ===")
    pprint(list(convert_years_to_str().items())[:2])  

    print("\n=== Получаем фильмы на 'Ч' ===")
    pprint(filter_ch_movies())

    print("\n=== Отсортировка словаря `full_dict` по одному параметру с использованием `lambda` ===")
    pprint(list(sort_by_year().items())[:2])  

    print("\n=== Отсортировка словаря `full_dict` по двум параметрам с использованием `lambda` ===")
    pprint(list(sort_by_year_and_title().items())[:2])  

    print("\n=== Фильтрация и сортировка `full_dict` с использованием `filter` и `sorted` ===")
    pprint(filter_and_sort_oneliner())


if __name__ == "__main__":
    main()
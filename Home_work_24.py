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
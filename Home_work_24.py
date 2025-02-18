from typing import Dict, List, Set, Any, Optional, Union
from pprint import pprint
from marvel import full_dict


def get_user_input() -> List[Optional[int]]:
    user_input = input("Введите цифры, разделенные пробелом: ")
    return list(map(lambda x: int(x) if x.isdigit() else None, user_input.split()))

def repack_to_list() -> List[Dict[str, Any]]:
    return [{**{"id": k}, **v} for k, v in full_dict.items()]
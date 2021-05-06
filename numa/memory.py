from numa.init import *
from typing import List, Optional


def get_interleave_nodes() -> List[int]:
    return []


def set_interleave_nodes(*nodes) -> None:
    pass


def set_local_alloc(strict_policy: Optional[bool] = False) -> None:
    pass


def set_membind_nodes(strict_policy: Optional[bool] = False, *nodes) -> None:
    pass


def get_membind_nodes(*nodes) -> List[int]:
    return []


def set_membind_policy(strict_policy: Optional[bool] = False) -> None:
    pass


def allocation_allowed_nodes() -> List[int]:
    return []

from numa import LIBNUMA
from typing import List, Optional
from ctypes import c_longlong

__all__ = ["get_allocation_allowed_nodes", "set_interleave_nodes", "set_local_alloc", "set_membind_nodes",
           "get_membind_nodes", "get_interleave_nodes", "set_membind_policy"]


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


def get_allocation_allowed_nodes() -> List[int]:
    return []


def node_memory_info(node: int) -> tuple:
    free_size = c_longlong()
    total_size = LIBNUMA.numa_node_size64(node, free_size)
    return total_size, free_size.value

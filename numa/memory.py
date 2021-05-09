from numa import LIBNUMA
from typing import List
from ctypes import c_longlong
import numa.utils as numa_utils

__all__ = ["get_allocation_allowed_nodes", "set_interleave_nodes", "set_local_alloc", "set_membind_nodes",
           "get_membind_nodes", "get_interleave_nodes"]


def get_interleave_nodes() -> List[int]:
    result_nodes_pointer = LIBNUMA.numa_get_interleave_mask()
    try:
        result_nodes_pointer.contents
    except ValueError:
        raise Exception(f"get interleave nodes info failed")
    return numa_utils.get_bitset_list(result_nodes_pointer)


def set_interleave_nodes(*nodes) -> None:
    nodes = list(set(nodes))
    res = ",".join(list(map(str, nodes)))
    c_string = bytes(res, "ascii")
    bitmask = LIBNUMA.numa_parse_nodestring(c_string)
    op_res = LIBNUMA.numa_set_interleave_mask(bitmask)
    if op_res == -1:
        raise Exception(f"set interleave_nodes {res} failed")


def set_local_alloc() -> None:
    LIBNUMA.numa_set_localalloc()


def set_membind_nodes(*nodes) -> None:
    nodes = list(set(nodes))
    res = ",".join(list(map(str, nodes)))
    c_string = bytes(res, "ascii")
    bitmask = LIBNUMA.numa_parse_nodestring(c_string)
    op_res = LIBNUMA.numa_set_membind(bitmask)
    if op_res == -1:
        raise Exception(f"set membind nodes {res} failed")


def get_membind_nodes() -> List[int]:
    result_nodes_pointer = LIBNUMA.numa_get_membind()
    try:
        result_nodes_pointer.contents
    except ValueError:
        raise Exception(f"get membind nodes info failed")
    return numa_utils.get_bitset_list(result_nodes_pointer)


'''
def set_membind_policy(strict_policy: Optional[bool] = False) -> None:
    if strict_policy == False:
        strict_policy = 0
    else:
        strict_policy = 1
    LIBNUMA.numa_set_bind_policy(strict_policy)
'''


def get_allocation_allowed_nodes() -> List[int]:
    result_nodes_pointer = LIBNUMA.numa_get_mems_allowed()
    try:
        result_nodes_pointer.contents
    except ValueError:
        raise Exception(f"get allocation allowed nodes info failed")
    return numa_utils.get_bitset_list(result_nodes_pointer)


def node_memory_info(node: int) -> tuple:
    free_size = c_longlong()
    total_size = LIBNUMA.numa_node_size64(node, free_size)
    return total_size, free_size.value

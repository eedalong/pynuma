from init import *
from typing import List


def clear_node_mask(node_mask: nodemask_t):
    tmp = bitmask_t()
    tmp.maskp = cast(byref(node_mask), POINTER(c_ulong))
    tmp.size = sizeof(nodemask_t) * 8
    LIBNUMA.numa_bitmask_clearall(byref(tmp))


def node_list_to_node_mask(node_lst: List[int]):
    """
    Convert node list to node mask
    :param node_lst: node list
    :return: nodemask_t
    """
    res = nodemask_t()
    valid_node_list = list(filter(lambda x: x <= MAX_NUMANODES, node_lst))
    clear_node_mask(res)
    for node in valid_node_list:
        res.n[node/8/sizeof(c_ulong)] |= 1 << (node % (8 * sizeof(c_ulong)))
    return res


def get_bitset_list(bitmask: bitmask_t) -> List[int]:
    return list(filter(lambda node: LIBNUMA.numa_bitmask_isbitset(bitmask, node) != 0, range(bitmask.size)))


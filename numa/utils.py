from numa import bitmask_t, LIBNUMA
from typing import List


def get_bitset_list(bitmask: bitmask_t) -> List[int]:
    return list(filter(lambda node: LIBNUMA.numa_bitmask_isbitset(bitmask, node) != 0, range(bitmask.contents.size)))

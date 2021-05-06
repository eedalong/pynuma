from init import *

def numa_avaliable():
    """
    :return: bool
    """
    return NUMA_AVALIABLE


def get_max_node() -> int:
    return LIBNUMA.numa_max_node()






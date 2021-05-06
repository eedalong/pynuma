from numa.init import LIBNUMA, NUMA_AVALIABLE
from typing import Dict, List
from ctypes import byref, c_longlong


__all__ = ["numa_avaliable", "get_max_node", "get_max_possible_node", "get_num_configured_nodes",
           "get_num_configured_cpus", "numa_distance", "numa_hardware_info"]


def numa_avaliable():
    """
    :return: bool
    """
    return NUMA_AVALIABLE


def get_max_node() -> int:
    return LIBNUMA.numa_max_node()


def get_max_possible_node() -> int:
    pass


def get_num_configured_nodes() -> int:
    pass


def get_num_configured_cpus() -> int:
    pass


def numa_distance(node1: int, node2: int) -> int:
    pass


def numa_hardware_info() -> Dict:
    """
    :return: Dict(numa_node_distance:List[List[int]], node_cpu_info:Dict(node:List[int]))
    """
    pass


def node_to_cpus(node: int) -> List[int]:
    pass


def cpu_to_node(cpu: int) -> int:
    pass





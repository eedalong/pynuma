from typing import List
from numa import LIBNUMA
import numa.utils as numa_utils

__all__ = ["run_on_nodes", "run_on_all_nodes", "run_on_cpus", "run_on_all_cpus", "get_affinitive_cpus",
           "get_affinitive_nodes", "get_preferred_node", "set_preferred_node", "get_allowed_nodes_num",
           "get_allowed_cpus_num", "bind"]


def run_on_nodes(*nodes):
    """
    :param nodes: numa node to run
    :return:
    """
    nodes = list(set(nodes))
    if len(nodes) == 0:
        bitmask = LIBNUMA.numa_parse_nodestring(b"all")
        op_res = LIBNUMA.numa_run_on_node_mask(bitmask)
        if op_res == -1:
            raise Exception("attempt to run on all nodes failed")
    else:
        res = ",".join(list(map(str, nodes)))
        c_string = bytes(res, "ascii")
        bitmask = LIBNUMA.numa_parse_nodestring(c_string)
        op_res = LIBNUMA.numa_run_on_node_mask(bitmask)
        if op_res == -1:
            raise Exception(f"attempt to run on {res} failed")


def run_on_all_nodes():
    run_on_nodes()


def run_on_cpus(pid: int, *cpus):
    """
    :param cpus: cpu list
    :param pid: process id
    :return:
    """
    cpus = list(set(cpus))
    if len(cpus) == 0:
        bitmask = LIBNUMA.numa_parse_cpustring(b"all")
        op_res = LIBNUMA.numa_sched_setaffinity(pid, bitmask)
        if op_res == -1:
            raise Exception("attempt to run on all nodes failed")
    else:
        res = ",".join(list(map(str, cpus)))
        c_string = bytes(res, "ascii")
        bitmask = LIBNUMA.numa_parse_cpustring(c_string)
        op_res = LIBNUMA.numa_sched_setaffinity(pid, bitmask)
        if op_res == -1:
            raise Exception(f"attempt to run on {res} failed")


def run_on_all_cpus(pid: int):
    run_on_cpus(pid)


# TODO Quite Confused about this api
def get_affinitive_nodes() -> List[int]:
    result_mask_pointer = LIBNUMA.numa_get_run_node_mask()
    try:
        result_mask_pointer.contents
    except ValueError:
        raise Exception(f"get run nodes info failed")
    return numa_utils.get_bitset_list(result_mask_pointer)


def get_affinitive_cpus(pid: int) -> List[int]:
    cpu_mask = LIBNUMA.numa_allocate_cpumask()
    LIBNUMA.numa_bitmask_clearall(cpu_mask)
    LIBNUMA.numa_sched_getaffinity(pid, cpu_mask)
    return numa_utils.get_bitset_list(cpu_mask)


def bind(*nodes):
    nodes = list(set(nodes))
    res = ",".join(list(map(str, nodes)))
    c_string = bytes(res, "ascii")
    bitmask = LIBNUMA.numa_parse_nodestring(c_string)
    LIBNUMA.numa_run_on_node_mask(bitmask)
    LIBNUMA.numa_set_membind(bitmask)


def get_preferred_node() -> int:
    return LIBNUMA.numa_preferred()


def set_preferred_node(node: int) -> None:
    LIBNUMA.numa_set_preferred(node)


def get_allowed_cpus_num() -> int:
    return LIBNUMA.numa_num_task_cpus()


def get_allowed_nodes_num() -> int:
    return LIBNUMA.numa_num_task_nodes()

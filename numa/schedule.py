from init import *
import numa.utils as utils


def run_on_nodes(*nodes):
    """
    :param nodes: numa node to run
    :return:
    """
    nodes = list(nodes)
    if len(nodes) == 1:
        return LIBNUMA.numa_run_on_node(nodes[0])
    if len(nodes) > 1:
        node_mask = utils.node_list_to_node_mask(nodes)
        bitmask = LIBNUMA.numa_allocate_nodemask()
        LIBNUMA.copy_nodemask_to_bitmask(byref(node_mask), bitmask)
        res = LIBNUMA.numa_run_on_node_mask(byref(bitmask))
        LIBNUMA.numa_bitmask_free(bitmask)
        



def run_on_all_nodes():
    pass





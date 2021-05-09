from ctypes import *
from ctypes.util import find_library


def roundup(a: int, b: int) -> int:
    assert b > 0
    return (a + b - 1) // b


LIBNUMA = CDLL(find_library("numa"))

MAX_NUMANODES = LIBNUMA.numa_num_possible_nodes()
NR_CPUS = LIBNUMA.numa_num_possible_cpus()


class bitmask_t(Structure):
    _fields_ = [
            ('size', c_ulong),
            ('maskp', POINTER(c_ulong)),
            ]


class nodemask_t(Structure):
    _fields_ = [('n', c_ulong * roundup(MAX_NUMANODES, sizeof(c_ulong) * 8))]


class cpu_set_t(Structure):
    _fields_ = [('__bits', c_ulong * roundup(NR_CPUS, sizeof(c_ulong) * 8))]


LIBNUMA.numa_available.argtypes = []
LIBNUMA.numa_available.restype = c_int

LIBNUMA.numa_max_node.argtypes = []
LIBNUMA.numa_max_node.restype = c_int

LIBNUMA.numa_preferred.argtypes = []
LIBNUMA.numa_preferred.restype = c_int

LIBNUMA.numa_node_to_cpus.argtypes = [c_int, POINTER(bitmask_t)]
LIBNUMA.numa_node_to_cpus.restype = c_int

LIBNUMA.numa_set_interleave_mask.argtypes = [POINTER(bitmask_t)]
LIBNUMA.numa_set_interleave_mask.restype = c_void_p

LIBNUMA.numa_get_interleave_mask.argtypes = []
LIBNUMA.numa_get_interleave_mask.restype = POINTER(bitmask_t)

LIBNUMA.numa_bitmask_clearall.argtypes = [POINTER(bitmask_t)]
LIBNUMA.numa_bitmask_clearall.restype = POINTER(bitmask_t)

LIBNUMA.numa_allocate_nodemask.argtypes = []
LIBNUMA.numa_allocate_nodemask.restype = POINTER(bitmask_t)

LIBNUMA.numa_bind.argtypes = [POINTER(bitmask_t)]
LIBNUMA.numa_bind.restype = c_void_p

LIBNUMA.numa_set_membind.argtypes = [POINTER(bitmask_t)]
LIBNUMA.numa_set_membind.restype = c_void_p

LIBNUMA.numa_get_membind.argtypes = []
LIBNUMA.numa_get_membind.restype = POINTER(bitmask_t)

LIBNUMA.numa_set_preferred.argtypes = [c_int]
LIBNUMA.numa_set_preferred.restype = c_void_p

LIBNUMA.numa_set_localalloc.argtypes = []
LIBNUMA.numa_set_localalloc.restype = c_void_p

LIBNUMA.numa_get_run_node_mask.argtypes = []
LIBNUMA.numa_get_run_node_mask.restype = POINTER(bitmask_t)

LIBNUMA.numa_run_on_node_mask.argtypes = [POINTER(bitmask_t)]
LIBNUMA.numa_run_on_node_mask.restype = c_int

LIBNUMA.numa_distance.argtypes = [c_int, c_int]
LIBNUMA.numa_distance.restype = c_int

LIBNUMA.numa_parse_nodestring.argtypes = [c_char_p]
LIBNUMA.numa_parse_nodestring.restype = POINTER(bitmask_t)

LIBNUMA.numa_parse_cpustring.argtypes = [c_char_p]
LIBNUMA.numa_parse_cpustring.restype = POINTER(bitmask_t)

LIBNUMA.numa_node_size64.argtypes = [c_int, POINTER(c_longlong)]
LIBNUMA.numa_node_size64.restype = c_longlong

LIBNUMA.numa_allocate_cpumask.argtypes = []
LIBNUMA.numa_allocate_cpumask.restype = POINTER(bitmask_t)

LIBNUMA.numa_set_localalloc.argtypes = []
LIBNUMA.numa_set_localalloc.restype = c_void_p

LIBNUMA.numa_set_bind_policy.argtypes = [c_int]
LIBNUMA.numa_set_bind_policy.restype = c_void_p

LIBNUMA.numa_get_mems_allowed.argtypes = []
LIBNUMA.numa_get_mems_allowed.restype = POINTER(bitmask_t)

LIBNUMA.numa_distance.argtypes = [c_int, c_int]
LIBNUMA.numa_distance.restype = c_int

LIBNUMA.numa_node_of_cpu.argtypes = [c_int]
LIBNUMA.numa_node_of_cpu.restype = c_int

LIBNUMA.numa_node_to_cpus.argtypes = [c_int, POINTER(bitmask_t)]
LIBNUMA.numa_node_to_cpus.restype = c_int


from . import memory
from . import schedule
from . import info

__all__ = ["info", "memory", "schedule", "LIBNUMA", "bitmask_t"]

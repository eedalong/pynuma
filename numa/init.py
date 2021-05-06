from ctypes import *
from ctypes_configure import configure
from ctypes.util import find_library

def __setup__():
    class CConfigure(object):
        _compilation_info_ = configure.ExternalCompilationInfo(
            includes=['sched.h', 'numa.h'],
            libraries=[]
            )

    for cname in ['NUMA_NUM_NODES', '__CPU_SETSIZE', '__NCPUBITS']:
        if cname.startswith('__'):
            pyname = cname[2:]
        else:
            pyname = cname
        setattr(CConfigure, pyname, configure.ConstantInteger(cname))

    return configure.configure(CConfigure)


# setup
globals().update(__setup__())


class bitmask_t(Structure):
    _fields_ = [
            ('size', c_ulong),
            ('maskp', POINTER(c_ulong)),
            ]


class nodemask_t(Structure):
    _fields_ = [('n', c_ulong * (NUMA_NUM_NODES/(sizeof(c_ulong)*8)))]


class cpu_set_t(Structure):
    _fields_ = [('__bits', c_ulong * (CPU_SETSIZE / NCPUBITS))]


LIBNUMA = CDLL(find_library("numa"))


LIBNUMA.numa_available.argtypes = []
LIBNUMA.numa_available.restype = c_int

LIBNUMA.numa_max_node.argtypes = []
LIBNUMA.numa_max_node.restype = c_int

LIBNUMA.numa_node_size64.argtypes = [c_int, POINTER(c_longlong)]
LIBNUMA.numa_node_size64.restype = c_longlong

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

LIBNUMA.copy_bitmask_to_nodemask.argtypes = [POINTER(bitmask_t), POINTER(nodemask_t)]
LIBNUMA.copy_bitmask_to_nodemask.restype = c_void_p

LIBNUMA.copy_nodemask_to_bitmask.argtypes = [POINTER(nodemask_t), POINTER(bitmask_t)]
LIBNUMA.copy_nodemask_to_bitmask.restype = c_void_p

LIBNUMA.numa_bitmask_free.argtypes = [POINTER(bitmask_t)]
LIBNUMA.numa_bitmask_free.restype = c_void_p

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



# some global variables
NUMA_AVALIABLE: bool = (LIBNUMA.numa_avaliable() != -1)
if not NUMA_AVALIABLE:
    raise Exception("numa not avaliable")
MAX_NODE: int = LIBNUMA.numa_max_node()


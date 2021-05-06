import platform

from ctypes import *
from ctypes_configure import configure


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


libnuma = CDLL("libnuma" + (".dylib" if platform.system() == "Darwin" else ".so"), use_errno=True)

libnuma.numa_available.argtypes = []
libnuma.numa_available.restype = c_int

libnuma.numa_max_node.argtypes = []
libnuma.numa_max_node.restype = c_int

libnuma.numa_node_size64.argtypes = [c_int, POINTER(c_longlong)]
libnuma.numa_node_size64.restype = c_longlong

libnuma.numa_preferred.argtypes = []
libnuma.numa_preferred.restype = c_int

libnuma.numa_node_to_cpus.argtypes = [c_int, POINTER(bitmask_t)]
libnuma.numa_node_to_cpus.restype = c_int

libnuma.numa_set_interleave_mask.argtypes = [POINTER(bitmask_t)]
libnuma.numa_set_interleave_mask.restype = c_void_p

libnuma.numa_get_interleave_mask.argtypes = []
libnuma.numa_get_interleave_mask.restype = POINTER(bitmask_t)

libnuma.numa_bitmask_clearall.argtypes = [POINTER(bitmask_t)]
libnuma.numa_bitmask_clearall.restype = POINTER(bitmask_t)

libnuma.copy_bitmask_to_nodemask.argtypes = [POINTER(bitmask_t), POINTER(nodemask_t)]
libnuma.copy_bitmask_to_nodemask.restype = c_void_p

libnuma.copy_nodemask_to_bitmask.argtypes = [POINTER(nodemask_t), POINTER(bitmask_t)]
libnuma.copy_nodemask_to_bitmask.restype = c_void_p

libnuma.numa_bitmask_free.argtypes = [POINTER(bitmask_t)]
libnuma.numa_bitmask_free.restype = c_void_p

libnuma.numa_allocate_nodemask.argtypes = []
libnuma.numa_allocate_nodemask.restype = POINTER(bitmask_t)

libnuma.numa_bind.argtypes = [POINTER(bitmask_t)]
libnuma.numa_bind.restype = c_void_p

libnuma.numa_set_membind.argtypes = [POINTER(bitmask_t)]
libnuma.numa_set_membind.restype = c_void_p

libnuma.numa_get_membind.argtypes = []
libnuma.numa_get_membind.restype = POINTER(bitmask_t)

libnuma.numa_set_preferred.argtypes = [c_int]
libnuma.numa_set_preferred.restype = c_void_p

libnuma.numa_set_localalloc.argtypes = []
libnuma.numa_set_localalloc.restype = c_void_p

libnuma.numa_get_run_node_mask.argtypes = []
libnuma.numa_get_run_node_mask.restype = POINTER(bitmask_t)

libnuma.numa_run_on_node_mask.argtypes = [POINTER(bitmask_t)]
libnuma.numa_run_on_node_mask.restype = c_int

libnuma.numa_distance.argtypes = [c_int, c_int]
libnuma.numa_distance.restype = c_int

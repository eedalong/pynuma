from numa.init import *

res = LIBNUMA.numa_parse_nodestring("0")
print(type(res))


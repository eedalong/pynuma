import numa
import os
numa.schedule.run_on_nodes(0)
res = numa.schedule.get_preferred_node()
print(f"preferred node is {res}")
print(numa.schedule.get_allowed_cpus_num())
print(numa.schedule.get_allowed_nodes_num())

numa.schedule.run_on_cpus(os.getpid(), 0, 1, 2, 3)
print(numa.schedule.get_affinitive_cpus(os.getpid()))

numa.schedule.run_on_all_cpus(os.getpid())
print(numa.schedule.get_affinitive_cpus(os.getpid()))

print(numa.memory.node_memmory_info(0))
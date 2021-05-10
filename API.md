API Doc For PyNuma
--
### numa.memory

| api name                     | parameters | notes                                                        | use example                                            |
| ---------------------------- | ---------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| get_interleave_nodes         | null       | get the current interleave nodes                             | nodes_get = numa.memory.get_interleave_nodes()         |
| set_interleave_nodes         | *nodes     | set memory interleave nodes for current task                 | numa.memory.set_interleave_nodes(0, 1)                 |
| set_local_alloc              | null       | set the memory allocation policy for the calling task to local allocation | numa.memory.set_local_alloc()                          |
| set_membind_nodes            | *nodes     | set the memory allocation nodes                              | numa.memory.set_membind_nodes(0, 1)                    |
| get_membind_nodes            | null       | get nodes from which memory can currently be allocated       | nodes_get = numa.memory.get_membind_nodes()            |
| get_allocation_allowed_nodes | null       | get nodes from which the process is allowed to allocate memory in its current cpuset context | nodes_get = numa.memory.get_allocation_allowed_nodes() |
| node_memory_info             | node       | get the memory size of the node and the amount of free memory on the node | node_info = numa.memory.node_memory_info(0)            |

### numa.schedule

| api name      | parameters | notes | use example|
| ----------- | ----------- | ----------- | ----------- |
| run_on_nodes      | *nodes       | set node affinity for process      | numa.schedule.run_on_nodes(0, 1) |



### numa.info
| api name      | parameters | notes | use example|
| :-----------: | :-----------: | ----------- | ----------- |
| numa_available      | void       | check whether numa is available       | numa.info.numa_available() |
| get_max_node      | void       | returns max id of numa nodes      | numa.info.get_max_node() |
| get_max_possible_node      | void       | returns max possible number of numa nodes      | numa.info.get_max_possible_node() |
| get_num_configured_nodes      | void       | returns the number of memory nodes in the system       | numa.info.get_num_configured_nodes() |
| get_num_configured_cpus      | void       | returns the number of cpus in the system       | numa.info.get_num_configured_cpus() |
| numa_distance      | int, int       | returns the distance in the machine topology between two nodes       | numa.info.numa_distance(0, 1) |
| numa_hardware_info      | void       | returns hardware info of system, include numa node distance and node cpu info      | numa.info.numa_hardware_info() |
| cpu_to_node      | int       | returns the node that a cpu belongs to       | numa.info.cpu_to_node(0) |
| node_to_cpus      | int       | converts a node number to list of CPUs which belong to this node    | numa.info.node_to_cpus(0) |


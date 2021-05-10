API Doc For PyNuma
--
### numa.memory

| api name                     | parameters | nodes                                                        | use example                                            |
| ---------------------------- | ---------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| get_interleave_nodes         | null       | get the current interleave nodes                             | nodes_get = numa.memory.get_interleave_nodes()         |
| set_interleave_nodes         | *nodes     | set memory interleave nodes for current task                 | numa.memory.set_interleave_nodes(0, 1)                 |
| set_local_alloc              | null       | set the memory allocation policy for the calling task to local allocation | numa.memory.set_local_alloc()                          |
| set_membind_nodes            | *nodes     | set the memory allocation nodes                              | numa.memory.set_membind_nodes(0, 1)                    |
| get_membind_nodes            | null       | get nodes from which memory can currently be allocated       | nodes_get = numa.memory.get_membind_nodes()            |
| get_allocation_allowed_nodes | null       | get nodes from which the process is allowed to allocate memory in its current cpuset context | nodes_get = numa.memory.get_allocation_allowed_nodes() |
| node_memory_info             | node       | get the memory size of the node and the amount of free memory on the node | node_info = numa.memory.node_memory_info(0)            |

### numa.schedule

| api name      | parameters | nodes | use example|
| ----------- | ----------- | ----------- | ----------- |
| run_on_nodes      | *nodes       | set node affinity for process      | numa.schedule.run_on_nodes(0, 1) |



### numa.info
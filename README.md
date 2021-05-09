# py-libnuma
py-libnuma is python3 interface to numa Linux library so that you can set task affinity and memory affinity in python
level for your process which can help you to improve your code's performence.

# Installation
    pip install py-libnuma

# Usage
py-libnuma categorize libnuma's apis into 3 groups :`memory`, `schedule` and `info`. You can set your tasks' cpu affinity, memory affinity and get information about your
systems's hardware with these 3 modules respectively. For more information about APIs, you can refer to [API.md](https://github.com/eedalong/pynuma/blob/main/API.md) in github


## schedule

`numa.schedule` helps you to set cpu affinity for your process, if you have multiple numa nodes, and you want your process to be scheduled on cpus from node1 and node2, you can use `numa.schedule` like this

    from numa import schedule
    schedule.run_on_nodes(1,2)

If you want a certain process with `pid` to run on specific cpus, you can use `numa.schedule` like this

    from numa import schedule
    schedule.run_on_cpus(pid, 1,3,4,6)


## memory

`numa.memory` helps you to set memory policy for your process, if you want your current process to allocate memory from multiple numa nodes
to balance local and remote memory access, you can use `numa.memory` like this:
    
    from numa import memory    
    memory.set_interleave_nodes(0,1)

or you can make your process to allocate from certain nodes by 

    from numa import memory    
    memory.set_membind_nodes(1)

## Info

`numa.info` helps you to get information about your numa hardware, you can check hardware information by:
    
    from numa import info    
    info.numa_hardware_info()

This will tell you distance between different numa nodes and node-cpu relation. You can also check cpu set for certain nodes by:

    from numa import info    
    info.node_to_cpus(1)

or check which node is a certain cpu belongs to by:

    from numa import info    
    info.cpu_to_node(1)

For more information about APIs, you can refer to [API.md](https://github.com/eedalong/pynuma/blob/main/API.md) in github

## Feedback

If you have any problems with using this package, feel free to create issues and you will get answered in no more than 24 hours




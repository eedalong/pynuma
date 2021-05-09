# py3-libnuma
py3-libnuma is python3 interface to numa Linux library so that you can set task affinity and memory affinity in python
level for your process which can help you to improve your code's performence.

# Installation
    pip install py3-libnuma

# Usage
py3-libnuma categorize libnuma's apis into 3 groups :`memory`, `schedule` and `info`. You can set your tasks' cpu affinity, memory affinity and get information about your
systems's hardware with these 3 modules respectively.

## schedule
if you have multiple numa nodes, and you want your process to be scheduled on cpus from node1 and node2, you can use `numa.schedule` like this

    from numa import schedule
    schedule.run_on_nodes(1,2)

If you want a certain process with `pid` to run on specific cpus, you can use `numa.schedule` like this

    from numa import schedule
    scedule.run_on_cpus(pid, 1,3,4,6)

For more information about APIs, you can refer to [API.md](https://github.com/eedalong/pynuma/blob/main/API.md) in github


import unittest
import os
from numa import schedule, info, memory

# (From Dalong) unit test command: python -m unittest tests/test.py


class TestSchedule(unittest.TestCase):
    def setUp(self):
        schedule.run_on_all_nodes()
        schedule.run_on_all_cpus(os.getpid())
        self.max_node = info.get_max_node()
        self.total_cpu_num = os.cpu_count()

    def tearDown(self):
        schedule.run_on_all_nodes()
        schedule.run_on_all_cpus(os.getpid())

    def test_run_on_nodes(self):
        schedule.run_on_nodes(self.max_node)
        preferred_nodes = schedule.get_affinitive_nodes()
        self.assertEqual(preferred_nodes, [self.max_node])

    def test_preferred_nodes(self):
        schedule.set_preferred_node(self.max_node)
        preferred_node = schedule.get_preferred_node()
        self.assertEqual(preferred_node, self.max_node)

    def test_run_on_cpus(self):
        cpus_set = list(filter(lambda x: x % 2 == 1, list(range(self.total_cpu_num))))
        schedule.run_on_cpus(os.getpid(), *cpus_set)
        cpus_get = schedule.get_affinitive_cpus(os.getpid())
        self.assertEqual(cpus_get, cpus_set)

    def test_bind(self):
        schedule.bind(self.max_node)
        preferred_node = schedule.get_preferred_node()
        self.assertEqual(preferred_node, self.max_node)

class TestInfo(unittest.TestCase):
    def setUp(self):
        self.max_node = info.get_max_node()
        self.total_cpu_num = os.cpu_count()

    def test_numa_avaliable(self):
        assert info.numa_avaliable()

    def test_get_max_node(self):
        print('NUMA max node: {}'.format(info.get_max_node()))
    
    def test_get_max_possible_node(self):
        print('NUMA max possible node: {}'.format(info.get_max_possible_node()))

    def test_get_num_configured_nodes(self):
        print('NUMA num configured nodes: {}'.format(info.get_num_configured_nodes()))

    def test_get_num_configured_cpus(self):
        print('NUMA num configured cpus: {}'.format(info.get_num_configured_cpus()))

    def test_numa_distance(self):
        for i in range(self.max_node + 1):
            for j in range(self.max_node + 1):
                print('NUMA distance node {} to node {}: {}'.format(i, j, info.numa_distance(i, j)))

    def test_numa_hardware_info(self):
        res = info.numa_hardware_info()
        print('NUMA hardware info: numa_node_distance: {}, node_cpu_info: {}'.format(res['numa_node_distance'], res['node_cpu_info']))

    def test_cpu_to_node(self):
        for i in range(self.total_cpu_num):
            print('NUMA cpu to node: cpu{} -> node{}'.format(i, info.cpu_to_node(i)))

    def test_node_to_cpus(self):
        for i in range(self.max_node + 1):
            print('NUMA node to cpus: node{} -> cpus: {}'.format(i, info.node_to_cpus(i)))


if __name__ == "__main__":
    unittest.main()






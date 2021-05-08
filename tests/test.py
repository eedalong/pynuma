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

    # TODO bind seems doesnt take effect
    def test_bind(self):
        pass
        #schedule.bind(self.max_node)
        #preferred_node = schedule.get_preferred_node()
        #self.assertEqual(preferred_node, self.max_node)

    def test_interleave_nodes(self):
        nodes_set = list(filter(lambda x: x % 2 == 1, list(range(self.max_node + 1))))
        memory.set_interleave_nodes(*nodes_set)
        nodes_get = memory.get_interleave_nodes()
        self.assertEqual(nodes_set, nodes_get)
    
    def test_membind_nodes(self):
        nodes_set = list(filter(lambda x: x % 2 == 1, list(range(self.max_node + 1))))
        memory.set_membind_nodes(False, *nodes_set)
        nodes_get = memory.get_membind_nodes()
        self.assertEqual(nodes_set, nodes_get)
    
    def test_local_alloc(self):
        schedule.set_preferred_node(self.max_node)
        self.assertEqual(schedule.get_preferred_node(), self.max_node)
        memory.set_local_alloc(0)
        preferred_node = schedule.get_preferred_node()
        local_node = 0
        self.assertEqual(preferred_node, local_node)

    def test_get_mem_allowed(self):
        nodes_get = memory.get_allocation_allowed_nodes()
        nodes = list(range(self.max_node+1))
        self.assertEqual(nodes_get, nodes)
    
    def test_node_info(self):
        node_info = memory.node_memory_info(0)
        for i in range(self.max_node + 1):
            self.assertFalse(node_info[i] == -1)

    def test_set_policy(self):
        memory.set_membind_nodes(True, *[self.max_node])
        nodes_get = memory.get_membind_nodes()
        self.assertEqual([self.max_node], nodes_get)



if __name__ == "__main__":
    unittest.main()


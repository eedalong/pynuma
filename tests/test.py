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


if __name__ == "__main__":
    unittest.main()






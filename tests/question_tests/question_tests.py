#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

from src.question_b import question_b as qb

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

class Test_GlobalVariable(unittest.TestCase):
    def test_use_global_increments_global(self):
        # ensure a known starting state
        qb.global_counter = 0
        returned = qb.use_global()        # modify the global via the function
        # assert the function returned the new value and the module global changed
        self.assertEqual(returned, 1)
        self.assertEqual(qb.global_counter, 1)

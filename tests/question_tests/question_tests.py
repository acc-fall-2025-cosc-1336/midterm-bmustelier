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

from src.question_c import question_c as qc

class Test_AssessmentAndTax(unittest.TestCase):
    def test_get_assessment_value(self):
        # assessment is 60% of actual value
        self.assertAlmostEqual(qc.get_assessment_value(10000), 6000)
        self.assertAlmostEqual(qc.get_assessment_value(20000), 12000)

    def test_get_tax_assessed(self):
        # tax is $0.72 per $100 -> 0.0072 * assessment_value
        self.assertAlmostEqual(qc.get_tax_assessed(6000), 43.20, places=2)
        self.assertAlmostEqual(qc.get_tax_assessed(10000), 72.00, places=2)

import unittest

from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):

    def test_roll(self):
        die = Die()
        
        for _ in range(2):
            die.roll()
            roll_value = die.get_rolled_value()
            self.assertEqual(1 <= roll_value <= 6, True)
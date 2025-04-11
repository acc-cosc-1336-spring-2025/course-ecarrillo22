#
import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory,remove_inventory

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        my_dict = {}
        
        add_inventory(my_dict, 'Widget1', 10)
        self.assertEqual(my_dict['Widget1'], 10)

        my_dict = {'Widget1':25}
        add_inventory(my_dict, 'Widget1', 35)
        self.assertEqual(my_dict['Widget1'], 35)

        my_dict = {'Widget1':-10}
        add_inventory(my_dict, 'Widget1', 25)
        self.assertEqual(my_dict['Widget1'], 25)

    def test_remove_inventory(self):
        my_dict = {'widget1':30, 'widget2':55}
        remove_inventory(my_dict, 'widget1')
        self.assertEqual(len(my_dict), 1)
        self.assertEqual('widget2' in my_dict, True)
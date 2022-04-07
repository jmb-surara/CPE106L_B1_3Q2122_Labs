"""
Author: Julian Marc B. Surara 
Filename: test_oxo_dialog_ui.py
This program performs the unit testing method to check the following functions:
-startGame()
-quit()
This is to test that these functions are working accurately and properly.
"""

import unittest
import oxo_dialog_ui

class TestOxoLogic(unittest.TestCase):
    def test_startGame(self):
        self.assertEqual(oxo_dialog_ui.startGame(),list(" " * 9))
    def test_quit(self):
        self.assertRaises(SystemExit, oxo_dialog_ui.quit)
    
if __name__ == '__main__':
    unittest.main()

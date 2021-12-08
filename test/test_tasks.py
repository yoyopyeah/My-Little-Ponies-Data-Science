import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)
from src.compile_word_counts import *
from src.compute_pony_lang import *


class TasksTest(unittest.TestCase):
    def setUp(self):
        dir = os.path.dirname(__file__)
        self.mock_dialog = os.path.join(dir, 'fixtures', 'mock_dialog.csv')
        self.true_word_counts = os.path.join(dir, 'fixtures', 'word_counts.true.json')
        self.true_tf_idfs = os.path.join(dir, 'fixtures', 'tf_idfs.true.json')
        
        
    def test_task1(self):
        # use  self.mock_dialog and self.true_word_counts; REMOVE self.assertTrue(True) and write your own assertion, i.e. self.assertEquals(...)
        print(f"\nTesting functionality of compile_word_counts.py")
        wcounts = count_word(self.mock_dialog)
        with open(self.true_word_counts) as f:
            wc_true = json.load(f)
        self.assertEqual(wcounts, wc_true)
        print("OK")


    def test_task2(self):
        # use self.true_word_counts self.true_tf_idfs; REMOVE self.assertTrue(True) and write your own assertion, i.e. self.assertEquals(...)
        print(f"\nTesting functionality of compute_pony_lang.py")
        with open(self.true_word_counts) as f:
            wcounts = json.load(f)
        tfidf = analyze_lang(wcounts, 5)
        with open(self.true_tf_idfs) as f:
            tfidf_true = json.load(f)
        self.assertEqual(tfidf, tfidf_true)
        print("OK")
        
    
if __name__ == '__main__':
    unittest.main()
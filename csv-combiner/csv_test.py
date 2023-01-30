import unittest
import csv_combiner
import io
import sys 
import os
import generatefixtures
import pandas as pd
from functools import reduce

class TestMain(unittest.TestCase):
    def setUp(self):
        generatefixtures.main()
        sys.stdout = io.StringIO()
    
    def tearDown(self):
        os.remove('./fixtures/accessories.csv')
        os.remove('./fixtures/clothing.csv')
        os.remove('./fixtures/household_cleaners.csv')
        
        sys.stdout = sys.__stdout__
    
    def test_main(self):
        csv_combiner.main(['./fixtures/clothing.csv', './fixtures/accessories.csv', './fixtures/household_cleaners.csv'])
        
        output = sys.stdout.getvalue()
        
        acc_df = pd.read_csv('./fixtures/accessories.csv', lineterminator='\n')
        clo_df = pd.read_csv('./fixtures/clothing.csv', lineterminator='\n')
        hc_df = pd.read_csv('./fixtures/household_cleaners.csv', lineterminator='\n')
        
        

        #define list of DataFrames
        dfs = [acc_df, clo_df, hc_df]

        #merge all DataFrames into one
        expected_df = reduce(lambda  left,right: pd.merge(left,right,on=['email_hash'],
                                            how='outer'), dfs)
        
        self.assertEqual(len(expected_df), len(output))
        
if __name__ == "__main__":
    unittest.main()

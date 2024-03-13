import unittest
import pandas as pd
import re
import datetime

from Task1 import typeconversion
class TestDataValidation(unittest.TestCase):
    # def test_validate_data(self):
    #     self.assertTrue(validate(self.df))
    
    def test_valid_data(self):
        data = {'datetime' : "2014-02-03 00:00:00" , 'close': 103.45 , 'high': 109.4, 'low': 103.0 , 'open': 109.0, 'volume': 5572627, 'instrument': "HINDALCO"}
        df = pd.DataFrame(data,index=[0])
        df = typeconversion(df)
        # df.info()
        self.assertEqual('int64', df['volume'].dtype)
        self.assertEqual('float64', df['open'].dtype)  
        self.assertEqual('float64', df['high'].dtype)  
        self.assertEqual('float64', df['low'].dtype)  
        self.assertEqual('float64', df['close'].dtype)
        self.assertEqual('string', df['instrument'].dtype)  
        self.assertEqual('datetime64[ns]', df['datetime'].dtype)  
    

if __name__ == '__main__':
    unittest.main()

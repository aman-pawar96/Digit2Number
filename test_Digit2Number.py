import unittest
import Digit2Number


TestCases={"123.45":"one Hundred twenty three Rupee forty five Paise Only","123ww.23":"Not a Valid Number","1000000.00":"Number Exceding Max range (0-999999.99), Try with number in range","-99":"Number Below Min range (0-999999.99), Try with number in range","23765.23":"twenty three Thousand seven Hundred sixty five Rupee twenty three Paise Only","234.100":"Decimal Value cannot be greater than 99, Invalid Input","13227.34":"thirteen Thousand two Hundred twenty seven Rupee thirty four Paise Only"}

class TestDigit2Number(unittest.TestCase):
    
    def test_CheckNumber(self):
        i=1
        for Keys in TestCases.keys():
            print("TestCase:"+str(i))
            print("Input value: "+Keys)
            print("ExpectedResult: "+TestCases[Keys])
            self.assertEqual(Digit2Number.CheckNumber(Keys),TestCases[Keys])
            i=i+1
if __name__=="__main__":
    unittest.main()
import unittest
def duplicate_count(text):
    text= text.lower()
    res=0
    char=set(text)
    print(char)
    for i in char:
        if(text.count(i)>1):
            res+=1
    return res            
        



class TestSum(unittest.TestCase):
    def test1(self):
        self.assertEqual(duplicate_count(""), 0)
    def test2(self):
        self.assertEqual(duplicate_count("abcde"), 0)
    def test3(self):
        self.assertEqual(duplicate_count("abcdeaa"), 1)
    def test4(self):
        self.assertEqual(duplicate_count("abcdeaB"), 2)
    def test5(self):
        self.assertEqual(duplicate_count("Indivisibilities"), 2)
if __name__ == '__main__':
    unittest.main()
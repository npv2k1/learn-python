# nhập thư viên unittest
import unittest


# hàm cần test
def sums(*a):
    res=0
    for i in a:
        res+=i
    return res

# khởi tạo class test
class TestSum(unittest.TestCase):

    def sumTwoNumber(self):
        self.assertEqual(sums(1,2), 3)

    def sumThreeNumber(self):
        self.assertEqual(sums(1,2,3), 6)


# chạy test
if __name__ == '__main__':
    unittest.main()

import unittest

class Calculator:
    def __init__(self):
        self._fact_memory = { 0: 1 }
    
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mult(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    def fact(self, n):
        if n in self._fact_memory:
            return self._fact_memory[n]
        
        if n < 0:
            raise ValueError('Negative argument value of factorial')
        else:
            for i in range(max(self._fact_memory.keys()) + 1, n + 1):
                self._fact_memory[i] = i * self._fact_memory[i - 1]
                
            return self._fact_memory[n]
        

class TestCalculator(unittest.TestCase):
    # def __init__(self):
    #     super().__init__()
    #     self.calc = Calculator()
    def setUp(self):
        super(TestCalculator, self).setUp()
        self.calc = Calculator()

    @unittest.expectedFailure
    def test_small_nums_add(self):
        self.assertEqual(self.calc.add(0.0000001, 0.00000007), 0.00000017)

    def test_big_nums_add(self):
        self.assertEqual(self.calc.add(123123123, 123123123), 246246246)

    def test_zero_div(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(123123123, 0)

    def test_zero_mult(self):
        self.assertEqual(self.calc.mult(123123123, 0), 0)

    @unittest.expectedFailure
    def test_negative_fact(self):
        self.assertRaises(ValueError, self.calc.fact(-20))

    def test_big_nums_fact(self):
        self.assertIsInstance(self.calc.fact(100), int)


if __name__ == "__main__":
    unittest.main()
    # test = TestCalculator()
    # test.small_nums_add()
    # test.big_nums_add()
    # test.zero_div()
    # test.zero_mult()
    # test.negative_fact()
    # test.big_nums_fact()
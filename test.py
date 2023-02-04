from array import array
import unittest
from perceptron import Perceptron


class TestCreate(unittest.TestCase):

    def test_create(self):
        perc = Perceptron(2, 1)
        self.assertEqual(len(perc.b), 1)
        self.assertEqual(len(perc.w), 1)
        self.assertEqual(len(perc.w[0]), 2)

class TestEvaluate(unittest.TestCase):

    def test_evaluate_1(self):
        perc = Perceptron(2, 1)
        perc.b = array('d', [1])
        perc.w = [[1.0, 2.0]]
        x = array('d', [1.0, 2.0])
        y = perc.evaluate(x)
        self.assertEqual(y[0], 1)

    def test_evaluate_0(self):
        perc = Perceptron(2, 1)


class TesstLearn(unittest.TestCase):

    def test_simple(self):
        r, s = 2, 1
        p = Perceptron(r, s)
        x = array('d', [1.8, 2.9])
        for _ in range(1_000_000):
            p.learn(0, x, 1)
        print(p.w, p.b)

if __name__ == '__main__':
    unittest.main()

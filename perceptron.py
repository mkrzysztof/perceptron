from array import array
from random import uniform, randint

def heviside(x):
    if x < 0:
        return 0.0
    else:
        return 1.0

class Perceptron:
    def __init__(self, r, s):
        """r - number of inputs
        s - number of outputs (number of class"""
        self.b = array('d')
        self.w = []
        for neuron_number in range(s):
            b_0, w_i = self._create_neuron(r)
            self.b.append(b_0)
            self.w.append(w_i)

    def _create_neuron(self, r):
        """this cfreate touple (b, array() of size r
        b have random value {0, 1} and each element of array has random value
        U(-1, 1)"""
        b = uniform(-1.0, 1.0)
        arr = array('d', [uniform(-1.0, 1.0) for i in range(r)])
        return b, arr

    def evaluate(self, x):
        """ evaluate x array through perceptron"""
        y=[]
        for w_i, b_i in zip(self.w, self.b):
            u_i = b_i
            for b_ij, x_j in zip(w_i, x):
                u_i += b_ij * x_j
            g_i = heviside(u_i)
            y.append(g_i)
        return y

    def evaluate_n(self, neuron_number, x):
        w_n = self.w[neuron_number]
        b_n = self.b[neuron_number]
        u_n = b_n
        for b_nj, x_j in zip(w_n, x):
            u_n += b_nj * x_j
        return heviside(u_n)
            
    def learn(self, neur_number, x, t):
        """ training of each neurons acts independently"""
        y = self.evaluate_n(neur_number, x)
        e = t - y
        if e == 1:
            for i, x_i in enumerate(x):
                self.w[neur_number][i] += x_i 
            self.b[neur_number] += 1
        elif e == -1:
            for i, x_i in enumerate(x):
                self.w[neur_number][i] -= x_i 
            self.b[neur_number] -= 1

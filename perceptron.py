from array import array
from itertools import product
from random import uniform, randint
from math import sqrt
import os
import pickle
import sys

def heviside(x):
    if x < 0:
        return 0.0
    else:
        return 1.0

class DataLearn:
    def __init__(self):
        self.data = []

    def read(self, file):
        read_data = file.read().split()
        case_num = int(read_data[0])
        num_squares = int(read_data[1])
        dimension = int(sqrt(num_squares))
        vector = array('d', map(int, read_data[2:]))
        case = (case_num, vector)
        self.data.append(case)
        

class Perceptron:
    def __init__(self, r, s):
        """r - number of inputs
        s - number of outputs (number of class"""
        self.b = array('d')
        self.w = []
        self.r = r
        self.s = s
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



def perceptron_is_valid(perceptron, data_learn):
    valid = []
    for case, datum in data_learn.data:
        y = perceptron.evaluate(datum)
        valid.append((y[case] == 1) and (sum(y) == 1))
    return all(valid)


def learn_cycle(perceptron, data_learn):
    for out_number, (case, datum) in product(range(perceptron.s), data_learn.data):
        if out_number == case:
            perceptron.learn(out_number, datum, 1)
        else:
            perceptron.learn(out_number, datum, 0)

def learn_perceptron(perceptron, data_learn, max_iteration=None):
    iteration = 0
    while not perceptron_is_valid(perceptron, data_learn):
        iteration = iteration + 1
        learn_cycle(perceptron, data_learn)
        if max_iteration is not None:
            if iteration > max_teration:
                break            

def learn_perceptron_with_iter(perceptron, data_learn, max_iteration):
    for iteration in range(max_iteration):
        learn_cycle(perceptron, data_learn)


def learn(perceptron, learn_function, max_iteration, learn_directory):
    data_learn = DataLearn()
    for file_name in os.listdir(learn_directory):
        with open(os.path.join(learn_directory, file_name)) as file:
            data_learn.read(file)
    learn_function(perceptron, data_learn, max_iteration)

if __name__ == '__main__':
    perceptron = Perceptron(8*8, 7)
    learn(perceptron, learn_perceptron, None, sys.argv[1])
    with open(argv[2], 'wb') as file:
        pickle.dump(perceptron, file)
    

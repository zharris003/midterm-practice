import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 

def main(): 
    # 1.1
    def next_x(a,c,m,prev_x):
        next_num = (a * prev_x + c) % m
        return next_num
    
    #1.2
    def random_sequence(a,c,m,x0,n):
        nums = [x0]
        for i in range(n-1):
            next_num = next_x(a,c,m,nums[-1])
            nums.append(next_num)
        return nums

    a,c,m,x0,n = 106,1283,6075,42,10
    assert(random_sequence(a,c,m,x0,n) == [42, 5735, 1693, 4566, 5354, 3832, 450, 383, 5431, 5919])

    #1.3
    class RandomIntGenerator:
        def __init__(self, num_max, num_min = 0, a = 1664525, c = 1013904223 , m = 2**32, x0 = 42):
            self.num_max = num_max
            self.num_min = num_min
            self.a = a
            self.c = c
            self.m = m
            self.x = x0

        def next(self):
            self.x =  next_x(self.a,self.c,self.m,self.x)
            return self.num_min + self.x % (self.num_max+1-self.num_min)
            

        def random_sequence(self, n):
            result = [self.num_min + self.x%(self.num_max+1-self.num_min)]
            for i in range(n-1):
                result.append(self.next())
                assert(self.num_min <= result[-1] <= self.num_max)
            return result

    num_min=1
    num_max=6
    seq_len = 10000
    gen = RandomIntGenerator(num_max, num_min)
    seq = gen.random_sequence(seq_len)
    min(seq), max(seq), len(seq)

    #1.4
    data = gen.random_sequence(10000)
    
    bins=np.arange(num_min-0.5,num_max+1.5)

    fig, ax = plt.subplots()
    ax.hist(seq, bins)
    ax.savefig("histplot.png")


if __name__ == "__main__":
    main()



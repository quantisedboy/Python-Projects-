import numpy as np
from matplotlib import pyplot as plt 
import random

class Random:
    def __init__(self, count):
        self.n=count
    
    def one_dimensional_random_walk(self):
        x=0    #The starting point for the Random Walker
        for i in range(self.n):
            random_number=random.random()
            if(random_number>=0.5):
                x+=1
            else:
                x-=1
        print('The final position of the Random Walker: {}'.format(x))

a=Random(100)
a.one_dimensional_random_walk()
"""
2.1.1
"""
import numpy as np
from matplotlib import pyplot as plt 
import random

class Random:
    """
    A class to represent a Random Walker in 1D and 2D
    ...

    Attributes
    ----------
    count : int 
        The number of steps the Random Walker will take

    x : int
        The starting x-cordinate position 
        default value = 0

    y : int 
        The starting y-cordinate position
        default value = 0

    Methods 
    -------
    one_dimensional_random_walk():
        prints 1D Random walk final distance for given "count" value
    
    """
    def __init__(self, count, x=0, y=0):
        """
        Constructs necessary info for a Random class object

        Parameter
        ---------
        count : int 
            The number of steps the Random Walker will take
            stored : self.n

        x : int
            The starting x-cordinate position 
            default value = 0
            stored : self.x

        y : int 
            The starting y-cordinate position
            default value = 0
            stored : self.y

        """
        self.n=count
        self.x=x
        self.y=y
    
    def one_dimensional_random_walk(self):
        """
        Computes and Prints 1D Random Walk final Location for given nnumber of steps
        and given initial x value.

        Displays the final position w.r.t the initial position in a 1D line.
        Axis turned on.

        Parameters
        ----------
        none

        Returns
        -------
        none
        """
        x=self.x    #The starting point for the Random Walker
        for i in range(self.n):
            random_number=random.random()
            if(random_number>=0.5):
                x+=1
            else:
                x-=1
        print('The final position of the Random Walker: {}'.format(x))
        plt.figure()
        a=[self.x,x]
        plt.hlines(y=1, xmin=-20, xmax=20)
        plt.eventplot(a, colors='r')
        plt.axis('on')
        plt.show()

    def two_dimensional_random_walk(self):
        """
        Computes and prints Random Walk in 2D for given number of steps and 
        given initial values

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        x=self.x
        y=self.y
        for i in range(self.n):
            random_number=random.randint(1,4)
            if(random_number==1):
                y+=1
            elif(random_number==2):
                x+=1
            elif(random_number==3):
                y-=1
            else:
                x-=1
        print('The Final Position of Random Walker x:{pos1} , y:{pos2}'.format(pos1=x, pos2=y))
                

walker=Random(1000)
walker.two_dimensional_random_walk()
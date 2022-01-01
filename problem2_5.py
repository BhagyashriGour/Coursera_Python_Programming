import random

def problem2_5():
    """ Simulates rolling a die 10 times."""
    random.seed(171)
    for i in range(10):
      a= random.randint(1,6)
      print(a)
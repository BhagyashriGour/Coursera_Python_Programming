import random 

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    a=[]
    for i in range(10):
      a.append(random.random())
    
    for j in range(len(a)):
      a[j] = (a[j] * 5) +30
    print(a)
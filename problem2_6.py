def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)
    for i in range(100):
      a= random.randint(1,6)
      b= random.randint(1,6)
      print(a+b)
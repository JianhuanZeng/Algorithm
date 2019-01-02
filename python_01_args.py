########################################################
#*args 
def find_bear(n, *args):
  # number of bear: n
  # the amount of needed food of each bear:*args
  return n
  
#**kwargs
def find_bear(n, **kwargs):
  # number of bear: n
  # the amount of total energy and needed food of each bear: **kwargs
  return n
  
# order: some_func(func_args, *args, **kwargs)  
########################################################
# ! python -m pdb test.py

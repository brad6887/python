import operator
import functools
LHW = '1 2 3'
LHW_list = LHW.split()
LHW_list = [int(i) for i in LHW_list]
pumpkin = functools.reduce(operator.mul, LHW_list)



print(pumpkin)
print(LHW_list)
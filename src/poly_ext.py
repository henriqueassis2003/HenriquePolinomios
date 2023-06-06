def ext_evaluate(polynom, x):
  sum_of_x = 0
  for degree in polynom:
      sum_of_x += polynom[degree] * (x ** degree)
  return sum_of_x
      

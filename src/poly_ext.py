def ext_evaluate(polynom, x):
  sum_of_x = 0
  for degree in polynom:
      sum_of_x += polynom[degree] * (x ** degree)
  return sum_of_x
def ext_sucessive_appx(polinomial_dict, min_interval, max_interval):
        diference = 1
        if self.evaluate(polinomial_dict, min_interval) <= evaluate(polinomial_dict, max_interval):
            if evaluate(polinomial_dict, min_interval) == 0:
                return min_interval
            
            while diference >= 1e-15:
                if evaluate(polinomial_dict, (min_interval+max_interval)/2) > 0:
                    max_interval=(min_interval+max_interval)/2
                if evaluate(polinomial_dict, (min_interval + max_interval) / 2) < 0:
                    min_interval = (min_interval + max_interval) / 2
                diference = abs(evaluate(polinomial_dict, (min_interval + max_interval) / 2))
                if evaluate(polinomial_dict, (min_interval + max_interval) / 2) == 0:
                    return  (min_interval + max_interval) / 2
            return  (min_interval + max_interval) / 2
        if evaluate(polinomial_dict, min_interval) > evaluate(polinomial_dict, max_interval):
            if evaluate(polinomial_dict, max_interval) == 0:
                return min_interval
              
            while diference >= 1e-15:
                if evaluate(polinomial_dict, (min_interval+max_interval)/2) > 0:
                    min_interval=(min_interval+max_interval)/2
                if evaluate(polinomial_dict, (min_interval + max_interval) / 2) < 0:
                    max_interval = (min_interval + max_interval) / 2
                diference=abs(evaluate(polinomial_dict, (min_interval + max_interval) / 2))
                if evaluate(polinomial_dict, (min_interval + max_interval) / 2) == 0:
                    return  (min_interval + max_interval) / 2
            return (min_interval + max_interval) / 2


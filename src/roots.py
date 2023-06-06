def ext_evaluate(polynom, x):
  sum_of_x = 0
  for degree in polynom:
      sum_of_x += polynom[degree] * (x ** degree)
  return sum_of_x

def symDerivate(polinomial_dict):
    return {(i - 1) : (polinomial_dict[i] * i) for i in polinomial_dict}

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

    def newtonRaphson(polinomial_dict, min_interval, max_interval):
        if abs(max_interval - min_interval) < 2:
            xn = (max_interval + min_interval) / 2
            for i in range(1, 20):
                xn -= (evaluate(polinomial_dict, xn)) / (evaluate(symDerivate(), xn))
            return xn
        else:
            for j in range(abs(int(max_interval - min_interval)) // 2 + 1):
                xn = min_interval + j * (abs(max_interval - min_interval) // 2 + 1)
                for i in range(1, 100):
                    xn -= (evaluate(polinomial_dict, xn)) / (evaluate(symDerivate(), xn))
                if evaluate(polinomial_dict, xn) < 1e-5:
                    return xn
        return False

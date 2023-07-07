def ext_evaluate(polynomial, x):
    sum_of_x = 0
    for degree in polynomial:
        sum_of_x += polynomial[degree] * (x ** degree)
    return sum_of_x

def ext_symDerivate(polynomial_dict):
    return {(i - 1): (polynomial_dict[i] * i) for i in polynomial_dict}

def ext_successiveAppx(self, min_interval, max_interval,tolerance=1e-12) :
        itter=0
        while abs(ext_evaluate(self.polynomial_dict, (min_interval + max_interval) / 2)) >= tolerance:
            if ext_evaluate(self.polynomial_dict, min_interval) * ext_evaluate(self.polynomial_dict,(min_interval + max_interval) / 2) < 0:
                max_interval = (min_interval + max_interval) / 2
            else:
                min_interval = (min_interval + max_interval) / 2
            if itter>120:
               return False
            itter+=1
        return (min_interval + max_interval) / 2

def ext_newtonRaphson(polynomial_dict, root,cycles=100):
    derivate_dict=ext_symDerivate(polynomial_dict)
    for i in range(cycles):
        root-=ext_evaluate(polynomial_dict,root)/ext_evaluate(derivate_dict,root)
    return root

class polinomioHenrique:
    def __init__(self, polinomial_list):
        self.polinomial_dict = {}
        for i in polinomial_list:
            inverse_list = (i[1], i[0])
            if inverse_list[1] in self.polinomial_dict:
                self.polinomial_dict[inverse_list[0]] += inverse_list[1]
            else:
                self.polinomial_dict[inverse_list[0]] = inverse_list[1]
        print(self.polinomial_dict)

    def sumModules(self, modules_list):
        for j in modules_list:
            inverse_list = (j[1], j[0])
            if inverse_list[1] in self.polinomial_dict:
                self.polinomial_dict[inverse_list[0]] += inverse_list[1]
            else:
                self.polinomial_dict[inverse_list[0]] = inverse_list[1]

    def symIntegral(self):
        integral_dict_out = {(i + 1) : (self.polinomial_dict[i] / (i + 1)) for i in self.polinomial_dict}
        return integral_dict_out

    def symDerivate(self):
        derivate_dict_out = {(i - 1) : (self.polinomial_dict[i] * i) for i in self.polinomial_dict}
        return derivate_dict_out

    @staticmethod
    def evaluate(polynom, x):
        somatorio = 0
        for j in polynom:
            somatorio += polynom[j] * (x ** j)
        return somatorio

    def newtonRaphson(self, min_interval, max_interval):
        if abs(max_interval - min_interval) < 2:
            xn = (max_interval + min_interval) / 2
            for i in range(1, 20):
                xn -= (self.evaluate(self.polinomial_dict, xn)) / (self.evaluate(self.symDerivate(), xn))
            return xn
        else:
            for j in range(abs(int(max_interval - min_interval)) // 2 + 1):
                xn = min_interval + j * (abs(max_interval - min_interval) // 2 + 1)
                for i in range(1, 100):
                    xn -= (self.evaluate(self.polinomial_dict, xn)) / (self.evaluate(self.symDerivate(), xn))
                if self.evaluate(self.polinomial_dict, xn) < 1e-5:
                    return xn
        return False

    def sucessiveAproximation(self, min_interval, max_interval):
        if self.evaluate(self.polinomial_dict, min_interval) <= self.evaluate(self.polinomial_dict, max_interval):
            if self.evaluate(self.polinomial_dict, min_interval) == 0:
                return min_interval
            diference = 1
            while diference >= 1e-15:
                if self.evaluate(self.polinomial_dict, (min_interval+max_interval)/2) > 0:
                    max_interval=(min_interval+max_interval)/2
                if self.evaluate(self.polinomial_dict, (min_interval + max_interval) / 2) < 0:
                    min_interval = (min_interval + max_interval) / 2
                diference = abs(self.evaluate(self.polinomial_dict, (min_interval + max_interval) / 2))
                if self.evaluate(self.polinomial_dict, (min_interval + max_interval) / 2) == 0:
                    return  (min_interval + max_interval) / 2
            return  (min_interval + max_interval) / 2
        if self.evaluate(self.polinomial_dict, min_interval) > self.evaluate(self.polinomial_dict, max_interval):
            if self.evaluate(self.polinomial_dict, max_interval) == 0:
                return min_interval

            diference = 1
            while diference >= 1e-15:
                print("caiu no loop")
                if self.evaluate(self.polinomial_dict, (min_interval+max_interval)/2) > 0:
                    min_interval=(min_interval+max_interval)/2
                if self.evaluate(self.polinomial_dict, (min_interval + max_interval) / 2) < 0:
                    max_interval = (min_interval + max_interval) / 2
                diference=abs(self.evaluate(self.polinomial_dict, (min_interval + max_interval) / 2))
                if self.evaluate(self.polinomial_dict, (min_interval + max_interval) / 2) == 0:
                    return  (min_interval + max_interval) / 2
            return (min_interval + max_interval) / 2




polinomio = polinomioHenrique([(-1,1),(1,)])
print(polinomio.newtonRaphson(-10,10))
print(polinomio.sucessiveAproximation(-10,10))
print("d")

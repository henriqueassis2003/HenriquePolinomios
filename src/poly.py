import roots
import graphics as gfx
class polynomHenrique:
    def __init__(self, polynomial_dict):
        self.polynomial_dict = polynomial_dict

    def sum_polynom(self, modules_dict):
        for j in modules_dict:
            if j in self.polynomial_dict:
                self.polynomial_dict[j] += modules_dict[j]
            else:
                self.polynomial_dict[j] = modules_dict[j]

    def erase_degree(self,degree):
        del self.polynomial_dict[degree]

    def sym_Integral(self,inplace=False):
        integral_dict_out = {(i + 1) : (self.polynomial_dict[i] / (i + 1)) for i in self.polynomial_dict}
        if inplace:
            self.polynomial_dict= integral_dict_out
        else:
            return polynomHenrique(integral_dict_out)

    def sym_Derivative(self,inplace=False):
        derivate_dict_out = {(i - 1) : (self.polynomial_dict[i] * i) for i in self.polynomial_dict}
        if -1 in derivate_dict_out:
            del derivate_dict_out[-1]
        if inplace:
            self.polynomial_dict= derivate_dict_out
        else:
            return polynomHenrique(derivate_dict_out)

    def evaluate(self, x):
        sum_of_x = 0
        for degree in self.polynomial_dict:
            sum_of_x += self.polynomial_dict[degree] * (x ** degree)
        return sum_of_x

    def newton_Raphson(self, root,cycles=100):
        return roots.ext_newtonRaphson(self.polynomial_dict, root, cycles)

    def successive_Approximation(self, min_interval, max_interval,tolerance=1e-3):
        return roots.ext_successiveAppx(self, min_interval, max_interval, tolerance)

    def to_dict(self):
        return self.polynomial_dict

    def start_plot(self,xmin=-10,xmax=10,step=1e-3):
        self.gfxvar=gfx.PolyPlot(xmin,xmax,step)

    def insert_graph(self,label,polynom_obj):
        dict=polynom_obj.polynomial_dict
        self.gfxvar.send_plot(label,dict)

    def plot_remove(self,label):
        self.gfxvar.plot_erase( label)

    def execute_plot(self,legends=False,title="poly-Henrique"):
        self.gfxvar.plot_exec(legends,title)

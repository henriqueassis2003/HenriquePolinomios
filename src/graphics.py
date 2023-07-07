import matplotlib.pyplot as plt

def ext_evaluate(polynomial, x):
    sum_of_x = 0
    for degree in polynomial:
        sum_of_x += polynomial[degree] * (x ** degree)
    return sum_of_x

class PolyPlot:
    def __init__(self,xmin=-10,xmax=10,step=1e-3):
        self.xmin,self.xmax=xmin,xmax
        self.step,self.plot_dict=step,{}
        auxmin,self.x_axys=xmin,[]
        while auxmin<xmax:
            self.x_axys.append(auxmin)
            auxmin+=step
        self.x_axys=self.x_axys

    def send_plot(self,name,poly_dict_r):
        temp_ylist=[ext_evaluate(poly_dict_r,i) for i in self.x_axys]
        self.plot_dict[name]=plt.plot(self.x_axys, temp_ylist)

    def plot_erase(self,name):
        aux=self.plot_dict[name][0]
        aux.remove()
        del self.plot_dict[name]

    def plot_exec(self,legends=False,title="poly-Henrique"):
        plt.title(title)
        if legends:
            list_label = []
            for j in self.plot_dict:
                list_label.append(j)
            plt.legend(list_label)
        plt.show()

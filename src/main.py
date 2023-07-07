import poly
#importing the polynom library

#creating and calling the polynom
poly_example=poly.polynomHenrique({7:3,2:11,1:20,0:2})

#returning to a dictionary
print(poly_example.to_dict())

#erasing a degree
poly_example.erase_degree(7)
print(poly_example.to_dict())

#sum new Module/part
poly_example.sum_polynom({2:-3,1:-5,0:12,4:5})
print(poly_example.to_dict())

#symbolic integrate
poly_example2=poly_example.sym_Integral()
print(poly_example2.to_dict())

#symbolic derivative
poly_example3=poly_example2.sym_Derivative()
print(poly_example3.to_dict())

#evaluate a function
print(poly_example.evaluate(2))

#newton raphson method
poly_example=poly.polynomHenrique({5:1,3:1,1:1,0:7})
print(poly_example.newton_Raphson(-1))

#sucessive aproximation method
print(poly_example.successive_Approximation(-2,-1,10**-5))

#starting plot
poly_example.start_plot(-5,5,1e-5)

#adding 3 graphs
poly_example.insert_graph("f",poly_example)
poly_example.insert_graph("f'",poly_example2)
poly_example.insert_graph("int f'",poly_example3)

#removing a graph
poly_example.plot_remove("f")

#plotting in the screhe graphic
poly_example.execute_plot(True,"Example-graphic")

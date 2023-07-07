# HenriquePolinomios

<h1>Objectives</h1>

The goal of this library is to provide easy and efficient polynomial management.

<h1>Limitations</h1>

Issues may arise when:

- Trying to manage high-degree polynomials, such as 120 or higher (especially in methods)


<h1>Requirements</h1>

To execute the library, the following is needed:

- A Python compiler or Venv running Python version 3.1.4 (or newer).

- Installation of the matplotlib library.
This can be done in the Python terminal with the following command:

```console
pip install matplotlib
```

<h1> Syntax and user command</h1>

<h3>Importing polynom library</h3>

after install the polynom library

To import the polynom library after installing it, you can use various methods. One way to do it is:

```python
import poly
```
Make sure you have successfully installed the polynom library before attempting to import it



To start using the library, 
the first step is to define a variable and instantiate the Polynom class using a function-like syntax.
This can be done with the following code:

```python
poly.polynomHenrique(dictionary)
```

When dictionary is a dictionary that represents a polynomial,
where the keys represent the degrees and the values represent the corresponding multipliers for each degree

example, $$3x^7+11x^2+20x+2$$

can be represented as:

```python
poly_example=poly.polynomHenrique({7:3,2:11,1:20,0:2})
```

<h3>returning to a dictionary </h3>

To convert a polynomial class to a dictionary, you can use the following command:

```
variable.to_dict()
```

example:
```python
print(poly_example.to_dict())
```
the output will be like this:


```
{7: 3, 2: 11, 1: 20, 0: 2}
```

<h3>deleting terms from the polynomial.</h3>
To erase a part of the polynomial, you can use the following command:

```python
variable.erase_degree(degree)
```

 ```degree```  "It is the key/degree that will be deleted.
 
example, in:

$$3x^7+11x^2+20x+2$$

will be deleted:
$$3x^7$$
using the following command:
```python
poly_example.erase_degree(7)
print(poly_example.to_dict())
```

the output will be like this:

```
{2: 11, 1: 20, 0: 2}
```

 :warning: **This command will modify the polynomial directly** (in-place) and won't return any information. Please be careful.


<h3>sum terms from the polynomial</h3>


To sum a new part to the polynomial, you can use the following command:

```python
variable.sum_polynom(dictionary)
```

example:

add:
$$-3x^2+15+5x^4$$
in: 
$$11x^2+20x+2$$

using the following command:

```python
poly_example.sum_polynom({2:-3,1:-5,0:12,4:5})
print(poly_example.to_dict())
```

the output should be:

```
{2: 8, 1: 15, 0: 14, 4: 5}
```

 :warning: **This command will modify the polynomial directly** (in-place) and won't return any information. Please be careful.

<h3>Obtain the symbolic integral</h3>

To obtain the symbolic integral of the polynomial,
you can create a new variable and assign the integral expression to it, following command:


```python
variable2=variable.sym_Integral(inplace)
```

or 

```python
variable.sym_Integral(True)
```

```inplace``` is an optional parameter(```False``` by default)
if set to ```True```  it will directly modify the primitive polynomial by overwriting it.
if set to ```False```  it will return a new instance of the polynomial-class

example:

$$\int 5x^4+8x^2+15x+14 dx$$

using: 

```python
poly_example2=poly_example.sym_Integral()
print(poly_example2.to_dict())
```

<h3>Obtain the symbolic derivative</h3>


To obtain the symbolic derivative of the polynomial,
you can create a new variable and assign the derivative expression to it, following command:

```python
variable2=variable.sym_Derivative(inplace)
```

or 

```python
variable.sym_Derivative(True)
```

```inplace``` is an optional parameter (```False``` by default)
if set to   ```True```  it will directly modify the primitive polynomial by overwriting it.
if set to ```False``` it will return a new instance of the polynomial-class

example:

$$\frac{d}{dx}(x^5+\frac{5x^3}{3}+\frac{15x^2}{2}+14x)$$


Can be done using the following command:

```python
poly_example3=poly_example2.sym_Derivative()
print(poly_example3.to_dict())
```

the output will be like this:
```
{2: 8.0, 1: 15.0, 0: 14.0, 4: 5.0}
```

<h3>Evaluate a function </h3>

To evaluate a function at a point, is used 

```python
variable.evaluate(x)
```



```x``` is the point on the horizontal axis

Example:

```python
print(poly_example.evaluate(2))
```

the output will be like this:

```
156
```

<h3>root  finding I</h3>

The first method of root finding is the Newton-Raphson method.

the command is:

```python
variable.newton_Raphson(root,cycles)
```

```root``` An initial guess for the roo

```cycles```  The number of iterations for the Newton-Raphson method
is an optional parameter, with a default value of 100 iterations.

example:

$$x^5-x^3+x+7=0;x_0=-1$$


can be done using the following command:

```python
poly_example=poly.polynomHenrique({5:1,3:1,1:1,0:7})
print(poly_example.newton_Raphson(-1))
```

the output will be like this:

```
-1.289546366784894
```



:warning:  **if derivative of polynom at the poin is zero, the method will fail, with an exception** 


:warning:  **if the number of iteraction/cycle is low this meth return a wrong root value** make sure that cycle number is sufficient 

<h3>root  finding II</h3>

the second method is sucessive approximation(bisection)
breaking the interval in two part in each iteraction

the command is 

```
variable.successive_Approximation( min_interval, max_interval,tolerance)
```

when

```min_interval``` is the lower value in analisys

```max_interval``` is the maximum value in analisys

```tolerance``` the errorof the root(deffine thestop point of the method)
an optional parameter, and default value is 0.001(1e-3)


example

$$x^5-x^3+x+7=0;-2\leq  x\leq -1; \epsilon =10^{-5}$$

can be done with

```
poly_example.successive_Approximation(-2,-1,10**-5)
```

aznd will  return

```
-1.289546012878418
```

:warning:  **the root finding wil, fail, if the root is out of interval, or dont exist**

:warning:  **the method may fail, if exist two roots or more, in interval**

<h3>graphics starting</h3>

to start the graphic the comand is 

```
variable.start_plot(xmin,xmax,step)
```
where
```xmin``` is minimum value in graphical analisys.
an optional parameter the default value is -10

```xmax``` is maximum value in graphical analisys.
an optional parameter the default value is +10

```step``` is ´the step between analisys value in  axys
an optional parameter the default value is 0.001(1e-3)

example

```
poly_example.start_plot(-5,5,1e-5)
```

:warning:  **after be setted up, this values of minimum, maximum, step can´t be editted** is needed to create a new variable and new graphical

<h3>adding function to graphics</h3>

to add new function to graphics the command is 

```
variable.insert_graph(label,polynom)
```

where

````label``` is a flag/name to identify  the function(also used to setup the legend/subtitle)

```polynom``` is the function polynom form expressed in class of polynom

example

insert 3 function to graphics

can be done with

```
poly_example.insert_graph("f",poly_example)
poly_example.insert_graph("f'",poly_example2)
poly_example.insert_graph("int f'",poly_example3)
```

<h3>removing gunction before plot</h3>

to remove a function the command is

```
variable.plot_remove(label)
```

where

```label``` is a flag/name to identify  the function

example

remove the first function

can be done with:

```
poly_example.plot_remove("f")

```


<h3>Plotting in the screen the graphic</h3>

to plot in the screen the graphic the command is 

```
variable.execute_plot(legends,title)
```

```legends``` an optional parameter, setted ````False``` by default.
if ````True``` will show the legends/subtitle in the sreen

```title```  an optional parameter, setted "poly-Henrique" by default.
this parameter is the name/title that appear in p of the graphic(title of graphic)

example

plot in the screen the graphic showing the legends and  with title "Example-graphic"

can be done with:

```
poly_example.execute_plot(True,"Example-graphic")
```

and finally wilurn/show 

![Captura de Tela (48)](https://github.com/henriqueassis2003/HenriquePolinomios/assets/128740531/4220c763-9216-4fe2-8977-6b72d363b313)

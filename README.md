# HenriquePolinomios

<h1>Objectives</h1>

The goals of ts libbrary is provide easy and good polynom management

<h1>Limitations</h1>

Issues can appear when:

- Try to manage high degree polynom like 120 or higher (Especially in methods)


<h1>Requeriments</h1>

to execute the library is needed:

- A python compiler or Venv runninthon version 3.1.4 (or Newer)

- Install the matplotb library

  can be done in python terminal with:

```console
pip install matplotlib
```

<h1> Syntax and user command</h1>

<h3>Importing polynom library</h3>

after install the polynom library

the next step is import the polynom library, can be done by several ways
one way is:

```python
import poly
```


to start thuse of the library the step is, 
deffine a variable and call the polynom class with a function like syntax,
can be done with:

```
poly.polynomHenrique(dictionary)
```

when ```dictionary``` is a dictionary that represent the polynom. 
The key represent the degree and the value represent the multiplier for each key/degree

example, $$3x^7+11x^2+20x+2$$

can be represented in

```python
poly_example=poly.polynomHenrique({7:3,2:11,1:20,0:2})
```

<h3>returning for dictionary </h3>

for return thepolynom-class to dictionary, the command is

```
variable.to_dict()
```

example:
```python
print(poly_example.to_dict())
```
the output like this:


```
{7: 3, 2: 11, 1: 20, 0: 2}
```

<h3>Erasing parts of the polynom</h3>
to erase a part of the polynom, the command is:

```
variable.erase_degree(degree)
```

when ```degree```  is the degree/key that will be deleted

example, in
$$3x^7+11x^2+20x+2$$
will be deleted the
$$3x^7$$
using the 
```python
poly_example.erase_degree(7)
print(poly_example.to_dict())
```

the output will be:

```
{2: 11, 1: 20, 0: 2}
```

 :warning:  **This command will modify directly the polynom**(inplace), and don't return any information, be careful


<h3>sum the parts for the polynom</h3>

to sum a new part
the command is:

```
variable.sum_polynom(dictionary)
```

example:

add 
$$-3x^2+15+5x^4$$
in the 
$$11x^2+20x+2$$

using the command

```
poly_example.sum_polynom({2:-3,1:-5,0:12,4:5})
print(poly_example.to_dict())
```

the output must be:

```
{2: 8, 1: 15, 0: 14, 4: 5}
```

:warning:  **This command will modify directly the polynom**(inplace), and don't return any information, be careful

<h3>Getting symbolic integral</h3>

to get the new integral can be used creating a new variable like that

```
variable2=variable.sym_Integral(inplace)
```

or 

```
variable.sym_Integral(True)
```

```inplace``` is a optional parameter, (```False``` by default)
if ```True``` will modify directly the primitive polynom(overwrite)
if ```False``` will return a class-polynom 

example:

$$\int 5x^4+8x^2+15x+14 dx$$

using 

```
poly_example2=poly_example.sym_Integral()
print(poly_example2.to_dict())
```

<h3>Getting symbolic derivative</h3>

to get the simbolic derivative

can be used creating a new variable like that

```
variable2=variable.sym_Derivative(inplace)
```

or 

```
variable.sym_Derivative(True)
```

```inplace``` is a optional parameter, (```False``` by default)
if ```True``` will modify directly the primitive polynom(overwrite)
if ```False``` will return a class-polynom 

example

$$\frac{d}{dx}(x^5+\frac{5x^3}{3}+\frac{15x^2}{2}+14x)$$


can be done with:
```
poly_example3=poly_example2.sym_Derivative()
print(poly_example3.to_dict())
```

the output is like that:
```
{2: 8.0, 1: 15.0, 0: 14.0, 4: 5.0}
```

<h3>Evaluate a function </h3>

to evaluate the function at point, is used 

```
variable.evaluate(x)
```

where

```x``` is the point of horizontal axys

Example:

```
print(poly_example.evaluate(2))
```

and this return

```
156
```

<h3>root  finding I</h3>

the frst method of root finding is newton-Raphson method

the command is

```
variable.newton_Raphson(root,cycles)
```

```root``` is a initial guess value for root of the polynom

```cycles```  is the number of iterations of newton method
Is an optional parameter, and default value is 100 iterations

example

$$x^5-x^3+x+7=0;x_0=-1$$


cn be done with

```
poly_example=poly.polynomHenrique({5:1,3:1,1:1,0:7})
print(poly_example.newton_Raphson(-1))
```
and return 

```
-1.289546366784894
```

:warning:  **if derivative of polynom at the poin is zero, the method will fail, with an exception** 


:warning:  **if the number of iteraction/cycle is low this meth return a wrong root value** make sure that cycle number is sufficient 


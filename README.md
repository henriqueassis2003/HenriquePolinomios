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

```
pip install matplotlib
```

<h1> Syntax and user command</h1>

<h3>Importing polynom library</h3>

after install the polynom library

the next step is import the polynom library, can be done by several ways
one way is:

```
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

```
poly_example=poly.polynomHenrique({7:3,2:11,1:20,0:2})
```

<h3>returning for dictionary </h3>

for return thepolynom-class to dictionary, the command is

```
variable.to_dict()
```

example:
```
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


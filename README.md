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

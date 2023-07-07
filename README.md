# HenriquePolinomios

<h1>Objectives</h1>

The goal of this library is to provide easy and efficient polynomial management.

<h1>Limitations</h1>

Issues may arise when:

- Trying to manage high-degree polynomials, such as 120 or higher (especially in numeric methods)


<h1>Requirements</h1>

To execute the library, the following is needed:

- A Python compiler or Venv running Python version 3.1.4 (or newer).

- Installation of the matplotlib library.
This can be done in the Python terminal with the following command:

```console
pip install matplotlib
```

<h1> Syntax and user command</h1>

<h3>Importing  polynomial library</h3>

After install the  polynomial library

To import the  polynomial library after installing it, you can use various methods. One way to do it is:

```python
import poly
```
Make sure you have successfully installed the  polynomial library before attempting to import it



To start using the library. 
The first step is to define a variable and instantiate the  polynomial class using a function-like syntax.
This can be done with the following code:

```python
poly.polynomHenrique(dictionary)
```

```dictionary``` Is a dictionary that represents a polynomial,
Where the keys represent the degrees and the values represent the corresponding multipliers for each degree

Example: $$3x^7+11x^2+20x+2$$

Can be represented as:

```python
poly_example=poly.polynomHenrique({7:3,2:11,1:20,0:2})
```

<h3>Returning to a dictionary </h3>

To convert a polynomial class to a dictionary, you can use the following command:

```python
variable.to_dict()
```

Example:
```python
print(poly_example.to_dict())
```
the output will be like this:


```
{7: 3, 2: 11, 1: 20, 0: 2}
```

<h3>Deleting terms from the polynomial.</h3>
To erase a part of the polynomial, you can use the following command:

```python
variable.erase_degree(degree)
```

 ```degree```  "It is the key/degree that will be deleted.
 
Example, in:

$$3x^7+11x^2+20x+2$$

will be deleted:
$$3x^7$$
Using the following command:
```python
poly_example.erase_degree(7)
print(poly_example.to_dict())
```

The output will be like this:

```
{2: 11, 1: 20, 0: 2}
```

 :warning: **This command will modify the polynomial directly** (in-place) and won't return any information. Please be careful.


<h3>Sum terms from the polynomial</h3>


To sum a new part to the polynomial, you can use the following command:

```python
variable.sum_polynom(dictionary)
```

Example:

Add:
$$-3x^2+15+5x^4$$
In: 
$$11x^2+20x+2$$

Using the following command:

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
You can create a new variable and assign the integral expression to it, following command:


```python
variable2=variable.sym_Integral(inplace)
```

Or 

```python
variable.sym_Integral(True)
```

```inplace``` is an optional parameter(```False``` by default)
If set to ```True```  it will directly modify the primitive polynomial by overwriting it.
If set to ```False```  it will return a new instance of the polynomial-class

Example:

$$\int 5x^4+8x^2+15x+14 dx$$

Using: 

```python
poly_example2=poly_example.sym_Integral()
print(poly_example2.to_dict())
```

<h3>Obtain the symbolic derivative</h3>


To obtain the symbolic derivative of the polynomial,
You can create a new variable and assign the derivative expression to it, following command:

```python
variable2=variable.sym_Derivative(inplace)
```

Or 

```python
variable.sym_Derivative(True)
```

```inplace``` is an optional parameter (```False``` by default)
If set to   ```True```  it will directly modify the primitive polynomial by overwriting it.
If set to ```False``` it will return a new instance of the polynomial-class

Example:

$$\frac{d}{dx}(x^5+\frac{5x^3}{3}+\frac{15x^2}{2}+14x)$$


Can be done using the following command:

```python
poly_example3=poly_example2.sym_Derivative()
print(poly_example3.to_dict())
```

The output will be like this:
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

The output will be like this:

```
156
```

<h3>Root  finding I</h3>

The first method of root finding is the Newton-Raphson method.

The command is:

```python
variable.newton_Raphson(root,cycles)
```

```root``` An initial guess for the roo

```cycles```  The number of iterations for the Newton-Raphson method
Is an optional parameter, with a default value of 100 iterations.

Example:

$$x^5-x^3+x+7=0;x_0=-1$$


Can be done using the following command:

```python
poly_example=poly.polynomHenrique({5:1,3:1,1:1,0:7})
print(poly_example.newton_Raphson(-1))
```

The output will be like this:

```
-1.289546366784894
```



:warning: **If the derivative of the polynomial at the point is zero, the method will fail, resulting in an exception.**

:warning: **If the number of iterations/cycles is low, this method may return an incorrect root value.** Make sure the cycle number is sufficient.

<h3>Root  finding II</h3>


The second method is successive approximation (bisection), which involves dividing the interval into two parts in each iteration.

The command is:

```python
variable.successive_Approximation( min_interval, max_interval,tolerance)
```



```min_interval``` The lower value is the starting point of the analysis.

```max_interval``` The maximum value in the analysis.

```tolerance```  is the error of the root, which defines the stopping point of the method.
It is an optional parameter, and the default value is 0.001 (1e-3)


Example:

$$x^5-x^3+x+7=0;-2\leq  x\leq -1; \epsilon =10^{-5}$$

Can be done using the following command:

```python
poly_example.successive_Approximation(-2,-1,10**-5)
```

The output will be like this:

```
-1.289546012878418
```


:warning: **The root finding will fail if the root is outside the interval or does not exist**

:warning: **The method may fail if there are two or more roots within the interval**

<h3>Starting the graphics</h3>

To start the graphic, the command is:

```python
variable.start_plot(xmin,xmax,step)
```


```xmin``` is the minimum value in graphical analysis.
It is an optional parameter, and the default value is -10

```xmax```  is the maximum value in graphical analysis.
It is an optional parameter, and the default value is +10

```step``` is the step between analysis values on the axis.
It is an optional parameter, and the default value is 0.001 (1e-3).

example:

```python
poly_example.start_plot(-5,5,1e-5)
```

:warning: **After being set up, the values of minimum, maximum, and step cannot be edited.**
You would need to create a new variable and a new graphical analysis with the updated values

<h3>adding function to graphics</h3>

To add a new function to the graphics, the command is: 

```python
variable.insert_graph(label, polynomial)
```



```label``` is a flag or name used to identify the function.
It is also used to set up the legend or subtitle for the function

``` polynomial```  represents the polynomial function expressed in polynomial class form

Example:

Insert 3 function to graphics

Can be done using the following command:

```python
poly_example.insert_graph("f",poly_example)
poly_example.insert_graph("f'",poly_example2)
poly_example.insert_graph("int f'",poly_example3)
```

<h3>Removing gunction before plot</h3>


To remove a function before plotting, the command is

```python
variable.plot_remove(label)
```



```label``` is a flag/name to identify  the function

Example:

Remove the first function.

Can be done using the following command:



```python
poly_example.plot_remove("f")

```


<h3>Plotting in the screen the graphic</h3>


To plot the graphic on the screen, the command is

```python
variable.execute_plot(legends,title)
```

```legends``` is an optional parameter, set to ```False``` by default.
If set to ````True``` it will display the legends/subtitle on the screen.

```title```   is an optional parameter, set to "poly-Henrique" by default.
This parameter represents the name or title that appears at the top of the graphic.

Example:

To plot the graphic on the screen showing the legends and with the title "Example-graphic",
You can use the following command:

```python
poly_example.execute_plot(True,"Example-graphic")
```

And finally, the plot will be returned and shown on the screen.

![Captura de Tela (48)](https://github.com/henriqueassis2003/HenriquePolinomios/assets/128740531/4b1e77cb-04cd-49bc-96ad-ddb0be3bf5ac)


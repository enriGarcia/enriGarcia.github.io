---
layout: page
title: Uso de Sympy para la asignatura de cálculo
description: Tutorial de uso de Sympy
---
> Este tutorial es para usuarios que tengan instalado el módulo de Sympy. Si aún no lo ha instalado de click aquí.

# Índice
- [Funciones](#funciones)
- [Límites](#límites)
- [Derivadas](#derivadas)


# Funciones
[Volver al Índice](#índice)

En la primera tarea del curso de cálculo diferencial se nos pide que demostremos el resultado de algunas funciones usando el sistema de cómputo algebraico Sympy.

### Ejemplo 1.

Dado \\( f(x) = x^{3}-10x^{2}+31x-30 \\) demuestre que:

$$\begin{aligned}
f(0)=-30
\end{aligned}$$

El siguiente script de Python nos ayuda a calcular el resultado:

```python
from sympy import *
x = symbols("x")
f = x**3 - 10*x**2 + 31*x -30
print("f(0)=", f.subs(x, 0))
```

Produce el siguiente resultado:
```bash
f(0)= -30
```

Algunos otros ejemplos:

$$\begin{aligned}
f(-1)=-6f(6)
\end{aligned}$$

```python
from sympy import *
x = symbols("x")
f = x**3 - 10*x**2 + 31*x -30
print("f(-1)=", f.subs(x, -1))
print("-6f(6)=", -6*f.subs(x, 6))
```

Resultado:

```bash
f(-1)= -72
-6f(6)= -72
```

$$\begin{aligned}
f(yz)=y^{3}z^{3}-10y^{2}z^{2}+31yz-30
\end{aligned}$$

```python
from sympy import *
x, y, z = symbols("x y z")
f = x**3 - 10*x**2 + 31*x -30
print("f(yz)=", f.subs(x, y*z))
```

Resultado:

```bash
f(yz)= y**3*z**3 - 10*y**2*z**2 + 31*y*z - 30
```

$$\begin{aligned}
f(x-2)=x^{3}-16x^{2}+83x-140
\end{aligned}$$

Algunas veces hay que usar el método `expand()` para expandir las expresiones matemáticas.

```python
from sympy import *
x = symbols("x")
f = x**3 - 10*x**2 + 31*x -30
print("f(x-2)=", expand(f.subs(x, x-2)))
```

Resultado:

```bash
f(x-2)= x**3 - 16*x**2 + 83*x - 140
```

### Ejemplo 2.

Dado \\( f(x)=x^{3}-3x+2 \\) obtener:

$$\begin{aligned}
f\left(-\frac{1}{2}\right)
\end{aligned}$$

De manera opuesta a los números decimales, para el manejo de fracciones se utiliza la clase `Rational`, como se muestra en el siguiente script:

```python
from sympy import *
x = symbols("x")
f = x**3 - 3*x + 2
print("f(-1/2)=", f.subs(x, Rational(-1,2)))
```

Resultado:

```bash
f(-1/2)= 27/8
```

### Ejemplo 3.

Si \\( f(x)=x^{3}-10x^{2}+31x-30 \\) y \\( \phi(x)=x^{4}-55x^{2}-210x-216 \\) demuestre que:

$$\begin{aligned}
f(0)+\phi(0)+246=0
\end{aligned}$$

```python
from sympy import *
x = symbols("x")
f = x**3 - 10*x**2 + 31*x - 30
phi = x**4 - 55*x**2 - 210*x - 216
print(f.subs(x, 0) + phi.subs(x, 0) + 246)
```

Resultado:

```bash
0
```

# Límites
[Volver al Índice](#índice)

En la segunda tarea del curso de cálculo diferencial se nos pide que demostremos el resultado de algunos límites usando el sistema de cómputo algebraico Sympy.

### Ejemplo 4.

Demostrar cada una de las siguientes igualdades:

$$\begin{aligned}
\lim_{x\to\infty} \frac{5-2x^{2}}{3x+5x^{2}} = -\frac{2}{5}
\end{aligned}$$

El siguiente script de Python nos ayuda a calcular el resultado:

```python
from sympy import *
x = symbols("x")
f = (5 - 2*x**2)/(3*x+5*x**2)
lim = limit(f, x, oo)
print("El límite de la función que tiende a oo es {}".format(lim))
```

Produce el siguiente resultado:
```bash
El límite de la función que tiende a oo es -2/5
```

### Ejemplo 5.

$$\begin{aligned}
\lim_{x\to\infty} \frac{6x^{3}-5x^{2}+3}{2x^{3}+4x-7} = 3
\end{aligned}$$

El siguiente script de Python nos ayuda a calcular el resultado:

```python
from sympy import * 
x = symbols("x") 
f = (6*x**3 - 5*x**2 + 3)/(2*x**3 + 4*x - 7) 
lim = limit(f, x, oo) 
print("El límite de la función que tiende a oo es {}".format(lim)) 
```

Produce el siguiente resultado:
```bash
El límite de la función que tiende a oo es 3
```
### Ejemplo 6.

$$\begin{aligned}
\lim_{k\to 0} \frac{\left(2z+3k\right)^{3}-4k^{2}z}{2z\left(2z-k\right)^{2}} = 1
\end{aligned}$$

El siguiente script de Python nos ayuda a calcular el resultado:

```python
from sympy import *
z, k = symbols("z, k")
f = ((2*z + 3*k)**3 - 4*z*k**2)/(2*z*(2*z - k)**2)
lim = limit(f, k, 0)
print("El límite de la función que tiende a 0 es {}".format(lim))
```

Produce el siguiente resultado:
```bash
El límite de la función que tiende a 0 es 1
```

# Derivadas
[Volver al Índice](#índice)

En la tercera tarea del curso de cálculo diferencial se nos pide que demostremos el resultado de algunos límites usando el sistema de cómputo algebraico Sympy.

### Ejemplo 7.

Hallar la derivada de las siguientes funciones:

$$\begin{aligned}
y=2-3x
\end{aligned}$$

El siguiente script de Python nos ayuda a calcular el resultado:

```python
from sympy import *
x, y = symbols('x y')
init_printing(use_unicode=True)
print(diff(2-3*x, x))
```

Produce el siguiente resultado:
```bash
-3
```

### Ejemplo 8.

$$\begin{aligned}
u=4v^{2}+2v^{3}
\end{aligned}$$

El siguiente script de Python nos ayuda a calcular el resultado:

```python
from sympy import *
u, v = symbols('u v')
init_printing(use_unicode=True)
print(diff(4*v**2 + 2*v**3, v))
```

Produce el siguiente resultado:
```bash
6*v**2 + 8*v
```

### Ejemplo 9.

$$\begin{aligned}
y=\frac{x^{2}}{4-x^{2}}
\end{aligned}$$

La mayoria de las veces no es visualmente agradable observar el resultado de las ecuaciones en la Terminal, por lo que es mejor en estos casos usar un Jupyter Notebook, para este ejemplo [descarguelo aquí]({{ BASE_PATH}}/pages/stuff/03_derivadas.ipynb).

<!-- Note: this is how to write a comment in HTML. Everything in here won't show up on your webpage.-->

<!--
To increase the size of the title, use fewer # in front of the paper title.
To decrease the size of the title, use more #. 
To remove the italics, remove the * before and after the description
To remove the underline from the title, remove the <u> tags (<u> and </u>)
-->

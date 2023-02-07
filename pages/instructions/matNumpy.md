---
layout: page
title: Uso de Numpy
description: Tutorial de uso de Numpy
---
> Este tutorial es para usuarios que tengan instalado el módulo de Numpy. Si aún no lo ha instalado de click aquí.

# Índice
- [1. Funciones](#1.-funciones)


# 1. Funciones
[Volver al Índice](#índice)

En la primera tarea del curso de Matemáticas para Ingeniería 1 se nos pide que demostremos el resultado de algunas funciones usando el sistema de cómputo científico Numpy.

### Ejemplo 1.

Dado:

$$\begin{aligned}
A=\begin{bmatrix}
-1 & 2 & 0 \\
4 & 5 & 3 
\end{bmatrix}
B=\begin{bmatrix}
7 & 1 & -3\\
2 & 0 & 6 
\end{bmatrix}
\end{aligned}$$

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

<!-- Note: this is how to write a comment in HTML. Everything in here won't show up on your webpage.-->

<!--
To increase the size of the title, use fewer # in front of the paper title.
To decrease the size of the title, use more #. 
To remove the italics, remove the * before and after the description
To remove the underline from the title, remove the <u> tags (<u> and </u>)
-->

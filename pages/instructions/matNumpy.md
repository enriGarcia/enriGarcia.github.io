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
E=\begin{bmatrix}
 0& 1\\
 1& 0\\
 0& 3\\
\end{bmatrix}
\end{aligned}$$

Encuentre:

$$\begin{aligned}
A+B
\end{aligned}$$

$$\begin{aligned}
5B-AE
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

<!-- Note: this is how to write a comment in HTML. Everything in here won't show up on your webpage.-->

<!--
To increase the size of the title, use fewer # in front of the paper title.
To decrease the size of the title, use more #. 
To remove the italics, remove the * before and after the description
To remove the underline from the title, remove the <u> tags (<u> and </u>)
-->

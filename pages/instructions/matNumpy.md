---
layout: page
title: Uso de Numpy
description: Tutorial de uso de Numpy
---
> Este tutorial es para usuarios que tengan instalado el módulo de Numpy. Si aún no lo ha instalado de click aquí.

# Índice
- [1. Funciones](#1.-funciones)


# 1. Operaciones matriciales básicas
[Volver al Índice](#índice)

En la primera tarea del curso de Matemáticas para Ingeniería 1 se nos pide que demostremos el resultado de algunas operaciones matriciales usando el sistema de cómputo científico Numpy.

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
C=\begin{bmatrix}
-3 & 2\\
1 & 7
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
5AE
\end{aligned}$$

$$\begin{aligned}
C^{2}
\end{aligned}$$

El siguiente script de Python nos ayuda a calcular el resultado:

```python
import numpy as np

A = np.array([[-1, 2, 0], [4, 5, 3]])
B = np.array([[7, 1, -3], [2, 0, 6]])
C = np.array([[-3, 3], [1, 7]])
E = np.array([[0, 1], [1, 0], [0, 3]])

print("A+B=")
print(A+B)
print("5*A*E=")
print(5*np.matmul(A, E))
print("C**2=")
print(np.power(C, 2))
```

Produce el siguiente resultado:
```bash
A+B=
[[ 6  3 -3]
 [ 6  5  9]]
5*A*E=
[[10 -5]
 [25 65]]
C**2=
[[ 9  9]
 [ 1 49]]
```

### Ejemplo 2.

Dado:

$$\begin{aligned}
F=\begin{bmatrix}
5 & 19 & 3 & -1 \\
2 & -4 & -3&  2 \\
-10 & 0 & 7 & -8
\end{bmatrix}
\end{aligned}$$

Encuentre:

$$\begin{aligned}
A^{T}
\end{aligned}$$

El siguiente script de Python nos ayuda a calcular el resultado:

```python
import numpy as np

F = np.array([[5, 19, 3, -1], [2, -4, -3, 2], [-10, 0, 7, -8]])

print("Transpuesta de F:")
print(np.transpose(F))
```

Produce el siguiente resultado:
```bash
Transpuesta de F:
[[  5   2 -10]
 [ 19  -4   0]
 [  3  -3   7]
 [ -1   2  -8]]
```

<!-- Note: this is how to write a comment in HTML. Everything in here won't show up on your webpage.-->

<!--
To increase the size of the title, use fewer # in front of the paper title.
To decrease the size of the title, use more #. 
To remove the italics, remove the * before and after the description
To remove the underline from the title, remove the <u> tags (<u> and </u>)
-->

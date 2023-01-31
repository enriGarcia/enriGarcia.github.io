---
layout: page
title: Uso de Sympy para las materias de Cálculo Diferencial e Integral 
description: Tutorial de uso de Sympy
---
> Este tutorial es para usuarios de Windows.

# Índice
- [1. Funciones](#1.-funciones)


# 1. Funciones
[Volver al Índice](#índice)

Dado \\( f(x) = x^{3}-10x^{2}+31x-30 \\) demuestre que:

$$\begin{aligned}
f(0)=-30
\end{aligned}$$

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





<!-- Note: this is how to write a comment in HTML. Everything in here won't show up on your webpage.-->

<!--
To increase the size of the title, use fewer # in front of the paper title.
To decrease the size of the title, use more #. 
To remove the italics, remove the * before and after the description
To remove the underline from the title, remove the <u> tags (<u> and </u>)
-->

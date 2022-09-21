---
date: 2022-09-09 第一次习题课
title: 2022秋高等代数习题课
---

**习题1.2 第3题**
已知两个变量$x,y$之间有某种函数关系$y=f(x)$，并且有如下对应值

   x   1   2   3    4
  --- --- --- ---- ----
   y   2   7   16   29

问：$y$是否可能是$x$的二次函数？如果可能，试求出满足要求的二次函数。

**解**：假设$y$是$x$的二次函数，即存在实数$a,b,c$使得
$$y = a + bx + cx^2$$ 我们有

     x     1   2   3    4
  ------- --- --- ---- ----
   $x^2$   1   4   9    16
     y     2   7   16   29

上式需要满足
$$\begin{pmatrix} 2 \\ 7 \\ 16 \\ 29 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 4 \\ 1 & 3 & 9 \\ 1 & 4 & 16 \end{pmatrix} \begin{pmatrix} a \\ b \\ c \end{pmatrix}$$
高斯消元法化简 $$\begin{gathered}
\begin{pmatrix}[ccc|c] 1 & 1 & 1 & 2 \\ 1 & 2 & 4 & 7 \\ 1 & 3 & 9 & 16 \\ 1 & 4 & 16 & 29 \end{pmatrix}
\longrightarrow \begin{pmatrix}[ccc|c] 1 & 1 & 1 & 2 \\ 0 & 1 & 3 & 5 \\ 0 & 2 & 8 & 14 \\ 0 & 3 & 15 & 27 \end{pmatrix}
\longrightarrow \begin{pmatrix}[ccc|c] 1 & 1 & 1 & 2 \\ 0 & 1 & 3 & 5 \\ 0 & 1 & 4 & 7 \\ 0 & 1 & 5 & 9 \end{pmatrix} \\
\longrightarrow \begin{pmatrix}[ccc|c] 1 & 1 & 1 & 2 \\ 0 & 1 & 3 & 5 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 1 & 2 \end{pmatrix}
\longrightarrow \begin{pmatrix}[ccc|c] 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 1 & 2 \end{pmatrix}
\longrightarrow \begin{pmatrix}[ccc|c] 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 1 & 2 \end{pmatrix}\end{gathered}$$
得
$$\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} a \\ b \\ c \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 2 \\ 2 \end{pmatrix}$$
得$(a,b,c) = (1,-1,2)$, 即$y = 1 - x + 2x^2$。

这题也可以用拉格朗日插值多项式来做。一般来说，过$n+1$个点$(x_0, y_0), \ldots, (x_n, y_n)$的$n$次插值多项式为
$$L(x) = \sum\limits_{i=0}^n y_i \prod\limits_{j \neq i}  \dfrac{x-x_j}{x_i-x_j}.$$
一般来说这是一个$n$次多项式，它也有可能退化为更低次的多项式。在这题中，我们有4个点，会得到次数$\leqslant 3$次的多项式。大家可以具体去算一算，最后答案还是$y = 1 - x + 2x^2$.
我们可以用[程序](https://gitee.com/wenh06/buaa-advanced-algebra-2021/blob/master/notebooks/class-1.ipynb)验证这个结果：

::: center
``` {.python language="Python"}
import numpy as np
import sympy as sp

def LagrangePolynomial(xs, ys):
    X = sp.symbols("x")
    assert len(xs) == len(ys)
    y = 0
    for k in range(len(xs)):
        t = 1
        for j in range(len(xs)):
            if j != k:
                t = t * ( (X - xs[j]) / (xs[k] - xs[j]) )
        y += t * ys[k]
    return sp.simplify(y)

xs = np.array([1, 2, 3, 4])
ys = np.array([2, 7, 16, 29])

LagrangePolynomial(xs, ys)
```
:::

**习题1.2 第4题** 在实数范围内解线性方程组 $$\begin{cases}
x + 3y + 2z = 4 \\
2x + 5y -3z = -1 \\
4x + 11y + z = 7
\end{cases}$$

这个方程组的解集在3维空间中的图像$\Pi$是什么？

将这个方程组的常数项全部变成0，得到的方程组的解集在3维空间中的图像$\Pi_0$是什么？$\Pi_0$与$\Pi$有什么关系？

**解**：该线性方程组的增广系数矩阵为 $$\begin{pmatrix}[ccc|c]
  1 & 3 & 2 & 4\\
  2 & 5 & -3 & -1 \\
  4 & 11 & 1 & 7
\end{pmatrix}$$ 通过高斯消元法（具体过程类似上一题，这里略去）化为阶梯形
$$\begin{pmatrix}[ccc|c]
  1 & 0 & -19 & -23\\
  0 & 1 & 7 & 9
\end{pmatrix}$$ 所以解集为$(x,y,z) = (19t-23,-7t+9,t)$,
$t\in\mathbb{R}$. 它在3维空间中的图像$\Pi$是一条直线。

将这个方程组的常数项全部变成0，得到的方程组的解集在3维空间中的图像$\Pi_0$一条过原点的直线。$\Pi_0$与$\Pi$之间可以通过平移相互得到，即$\Pi = \Pi_0 + \begin{pmatrix} -23 \\ 9 \\ 0 \end{pmatrix}$，$\begin{pmatrix} -23 \\ 9 \\ 0 \end{pmatrix}$可以换为原非齐次线性方程组的任意一个特解。

**习题1.3 第2题** 讨论当$\lambda$取什么值时下面的方程组有解
$$\begin{cases}
\lambda x_1 + x_2 + x_3 = 1 \\
x_1 + \lambda x_2 + x_3 = \lambda \\
x_1 + x_2 + \lambda x_3 = \lambda^2 \\
\end{cases}$$
当方程组有解时求出解来，并讨论$\lambda$取什么值时方程组有唯一解，什么时候有无穷多组解。

**解**：对增广系数矩阵做行变换 $$\begin{aligned}
& \begin{pmatrix}[ccc|c]
  \lambda & 1 & 1 & 1\\
  1 & \lambda & 1 & \lambda \\
  1 & 1 & \lambda & \lambda^2
\end{pmatrix}
\to
\begin{pmatrix}[ccc|c]
  1 & 1 & \lambda & \lambda^2 \\
  1 & \lambda & 1 & \lambda \\
  \lambda & 1 & 1 & 1
\end{pmatrix} \\
\to &
\begin{pmatrix}[ccc|c]
  1 & 1 & \lambda & \lambda^2 \\
  0 & \lambda-1 & -(\lambda-1) & -\lambda(\lambda-1) \\
  0 & -(\lambda-1) & -(\lambda-1)(\lambda+1) & -(\lambda-1)(\lambda^2+\lambda+1)
\end{pmatrix} \\
\to &
\begin{pmatrix}[ccc|c]
  1 & 1 & \lambda & \lambda^2 \\
  0 & \lambda-1 & -(\lambda-1) & -\lambda(\lambda-1) \\
  0 & 0 & (\lambda-1)(\lambda+2) & (\lambda-1)(\lambda+1)^2
\end{pmatrix}\end{aligned}$$ 所以

-   当$\lambda = 1$时，增广系数矩阵化为$\begin{pmatrix}[ccc|c] 1 & 1 & 1 & 1 \end{pmatrix}$，原线性方程组有无穷多组解
    $$\begin{pmatrix}
      1 - t_1 - t_2 \\ t_1 \\ t_2
    \end{pmatrix}, \quad t_1, t_2 \in \mathbb{R}.$$

-   当$\lambda = -2$时，增广系数矩阵化为
    $$\begin{pmatrix}[ccc|c] 1 & 1 & -2 & 4 \\ 0 & -3 & 3 & -6 \\ 0 & 0 & 0 & -3 \end{pmatrix}$$
    此时原线性方程组无解。

-   其余情况，增广系数矩阵可进一步约化 $$\begin{aligned}
    & \to
    \begin{pmatrix}[ccc|c]
      1 & 1 & \lambda & \lambda^2 \\
      0 & 1 & -1 & -\lambda \\
      0 & 0 & 1 & \frac{(\lambda+1)^2}{\lambda+2}
    \end{pmatrix} \to
    \begin{pmatrix}[ccc|c]
      1 & 0 & 0 & -\frac{\lambda+1}{\lambda+2} \\
      0 & 1 & 0 & \frac{1}{\lambda+2} \\
      0 & 0 & 1 & \frac{(\lambda+1)^2}{\lambda+2}
    \end{pmatrix}\end{aligned}$$ 此时原线性方程组有唯一解
    $$\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} -\frac{\lambda+1}{\lambda+2} \\ \frac{1}{\lambda+2} \\ \frac{(\lambda+1)^2}{\lambda+2} \end{pmatrix}$$

可以用[程序](https://gitee.com/wenh06/buaa-advanced-algebra-2021/blob/master/notebooks/class-1.ipynb)验证答案（在$\mathbb{Q}(\lambda)$中的解，适合一般情况，不适合$\lambda = 1,-2$这样的退化的情况）：

::: center
``` {.python language="Python"}
import sympy as sp
from sympy.solvers.solveset import linsolve
x, y, z, u = sp.symbols("x,y,z,u")
linsolve(
    [u*x + y + z - 1, x + u*y + z - u, x + y + u*z - u**2],
    (x, y, z)
)
```
:::

**习题1.1 第2题** (1).
求证：如果复数集合的子集$P$包含至少一个非零数，并且对加、减、乘、除（除数不为$0$）封闭，则$P$包含$0,1$，从而是数域。

(2). 求证：所有的数域都包含有理数域。

(3). 求证：集合$F = \{ a+b\sqrt{2} \ |\ a,b\in\mathbb{Q} \}$
是数域。（其中$\mathbb{Q}$是有理数域。）

(4). 试求包含$\sqrt[3]{2}$ 的最小的数域。

**解**：(1). 设$P$包含非零数$a$，则$0 = a-a \in P$,
$1 = a/a \in P$，所以$P$是数域。

(2).
任意一个数域$F$都包含$0,1$，且对加、减、乘、除封闭，故$F$包含整数$\mathbb{Z}$（包含$0,1$且对加、减封闭），进而包含有理数域$\mathbb{Q}$（对乘、除封闭）。有理数域$\mathbb{Q}$与有限域$\mathbb{F}_p$，$p$为素数，为最小的域，即不真包含更小的域，称为素域。

\(3\) 集合$F = \{ a+b\sqrt{2} \ |\ a,b\in\mathbb{Q} \}$包含$0,1$
（分别令$(a,b) = (0,0)$与$(a,b) = (1,0)$）。设$a_1, b_1, a_2, b_2 \in \mathbb{Q}$，下面验证

-   加、减法封闭：
    $$(a_1+b_1\sqrt{2}) \pm (a_2+b_2\sqrt{2}) = (a_1 \pm a_2) + (b_1 \pm b_2)\sqrt{2}$$

-   乘法封闭：
    $$(a_1+b_1\sqrt{2}) \cdot (a_2+b_2\sqrt{2}) = (a_1a_2+2b_1b_2) + (a_1b_2 + a_2b_1)\sqrt{2}$$

-   除法封闭（$a_2, b_2$不同时为零）：
    $$(a_1+b_1\sqrt{2}) / (a_2+b_2\sqrt{2}) = \dfrac{a_1a_2-2b_1b_2}{a_2^2-2b_2^2} + \dfrac{a_2b_1-a_1b_2}{a_2^2-2b_2^2}\sqrt{2}$$

(4). 包含$\sqrt[3]{2}$的最小的数域为
$$\mathbb{Q}(\sqrt[3]{2}) = \{ a + b\sqrt[3]{2} + c\sqrt[3]{4} \ |\ a,b,c\in\mathbb{Q} \}$$

很容易看到任何包含$\sqrt[3]{2}$的数域都必须包含$\sqrt[3]{2}, \sqrt[3]{4}$，从而包含$\mathbb{Q}(\sqrt[3]{2})$，那么只要证明$\mathbb{Q}(\sqrt[3]{2})$是一个数域。

解法一：直接验证$\mathbb{Q}(\sqrt[3]{2})$是对加、减、乘、除封闭。其中对加、减、乘封闭好验证。对于除法封闭，只要验证$1/(a + b\sqrt[3]{2} + c\sqrt[3]{4}) \in \mathbb{Q}(\sqrt[3]{2})$，$a,b,c$不全为零，即可。不妨设$a,b,c$都不为零（其余情况更简单）。这种情况下，又不妨设$c=1$，记$\theta = \sqrt[3]{2}$，要证明
$$1/(a + b\theta + \theta^2) \in \mathbb{Q}(\theta)$$ 利用带余除法，有
$$\theta^3-2 = (\theta^2 + b\theta + a) (\theta-b) + ((b^2-a)\theta + ab-2)$$
若$b^2-a=0$，则$ab-2\neq 0$，此时有
$$1/(\theta^2 + b\theta + a) = (\theta-b)/(2-ab).$$ 若$b^2-a\neq 0$，则
$$\begin{gathered}
(\theta^2 + b\theta + a) \\
= ((b^2-a)\theta + ab-2) \left(\frac{1}{b^2-a}\theta + \frac{b^3 - 2ab + 2}{(b^2-a)^2} \right) + a - (ab-2)\frac{b^3 - 2ab + 2}{(b^2-a)^2}\end{gathered}$$
将上式回代，有 $$\begin{gathered}
(\theta^3-2) \left(\frac{1}{b^2-a}\theta + \frac{b^3 - 2ab + 2}{(b^2-a)^2} \right) \\
= (\theta^2 + b\theta + a) \left[ (\theta-b) \left(\frac{1}{b^2-a}\theta + \frac{b^3 - 2ab + 2}{(b^2-a)^2} \right) + 1 \right] - \gamma\end{gathered}$$
其中$\gamma = a - (ab-2)\frac{b^3 - 2ab + 2}{(b^2-a)^2}$，只要验证$\gamma\neq 0$，即有
$$1/(\theta^2 + b\theta + a) = \left[ (\theta-b) \left(\frac{1}{b^2-a}\theta + \frac{b^3 - 2ab + 2}{(b^2-a)^2} \right) + 1 \right] / \gamma$$

解法二：

设$m(x) = x^3 - 2$，这是$\sqrt[3]{2}$的所谓的（首一的,
monic）极小多项式[^1](minimal polynomial over
$\mathbb{Q}$)。令$F = \mathbb{Q}[x] / (m(x))$为$\mathbb{Q}$系数多项式全体的等价类组成的集合，其中的等价关系为
$$f_1(x) \sim f_2(x) \quad \Longleftrightarrow \quad \exists g(x) \ s.t.\ f_1(x)-f_2(x) = g(x)m(x)$$
作为一个$\mathbb{Q}$线性空间，$F$的一组基可以取作$1, \overline{x}, \overline{x}^2$。这是因为对于任意一个$f(x) \in \mathbb{Q}[x]$，都存在$g(x), r(x)$，$\deg r(x) < \deg m(x)$，使得
$$f(x) = g(x)m(x) + r(x)$$ 于是
$$F = \{ a + b\overline{x} + c\overline{x}^2 \ |\ a,b,c\in\mathbb{Q} \}$$
定义
$$\varphi : F \to \mathbb{Q}(\sqrt[3]{2}), \overline{x} \mapsto \sqrt[3]{2}$$
可以验证

-   $F$关于加、减、乘、除封闭。加、减、乘封闭很容易验证。任取$f(x) \in \mathbb{Q}[x] \setminus m(x)\cdot\mathbb{Q}[x]$，即$\overline{f} \neq 0 \in F$，那么$f(x)$与$m(x)$互素，即他们的最大公因子为$1$，记作$(f(x), m(x)) = 1$。于是（通过辗转相除法）存在$g_1(x), g_2(x) \in \mathbb{Q}[x]$，使得$g_1(x)f(x) + g_2(x)m(x) = 1$，于是$\overline{f}$在$F$中的逆元即为$\overline{g}_1$。

-   $\varphi$是一个一一对应（且保运算，即是一个域同构）。

[^1]: 使得满足$f(\sqrt[3]{2})=0$的$\mathbb{Q}$系数多项式中次数最低的，如果要求是首一的，即最高次项系数为1，则这样的多项式是唯一的。
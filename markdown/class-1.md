---
date: 2021-09-17 第一次习题课
title: 2021秋高等代数习题课
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
高斯消元法化简得
$$\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} a \\ b \\ c \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 2 \\ 2 \end{pmatrix}$$
得$(a,b,c) = (1,-1,2)$, 即$y = 1 - x + 2x^2$。

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
\end{pmatrix}$$ 通过高斯消元法化为阶梯形 $$\begin{pmatrix}[ccc|c]
  1 & 0 & -19 & -23\\
  0 & 1 & 7 & 9
\end{pmatrix}$$ 所以解集为$(x,y,z) = (19t-23,-7t+9,t)$,
$t\in\mathbb{R}$.
它在3维空间中的图像$\Pi$是一条直线。将这个方程组的常数项全部变成0，得到的方程组的解集在3维空间中的图像$\Pi_0$一条过原点的直线。$\Pi_0$与$\Pi$之间可以通过平移相互得到，即$\Pi = \Pi_0 + \begin{pmatrix} -23 \\ 9 \\ 0 \end{pmatrix}$，$\begin{pmatrix} -23 \\ 9 \\ 0 \end{pmatrix}$可以换为原非齐次线性方程组的任意一个特解。

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

可以用程序验证答案：

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

**习题四** 设齐次线性方程组(I), (II)的系数矩阵分别为
$$A = \begin{pmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{s1} & \cdots & a_{sn} \end{pmatrix}, \quad B = \begin{pmatrix} b_{11} & \cdots & b_{1n} \\ \vdots & \ddots & \vdots \\ b_{\ell 1} & \cdots & b_{\ell n} \end{pmatrix}$$
若$A$与$B$的行等价，判断(I)与(II)是否等价，并证明你的结论。

**解**：若$A$与$B$的行等价，那么矩阵$P_{\ell\times s}$，使得$P_{\ell\times s}A = B$，同时存在矩阵$Q_{s\times \ell}$，使得$Q_{s\times \ell}B = A$。设$x$满足$Ax = 0$，那么
$Bx = P_{\ell\times s}Ax = P_{\ell\times s}\cdot 0 = 0$。反过来，若$x$满足$Bx = 0$，那么
$Ax = Q_{s\times \ell}Bx = Q_{s\times \ell}\cdot 0 = 0$。所以齐次线性方程组(I),
(II)同解，即是等价的。

将$A$记作$\begin{pmatrix} a_1 \\ \vdots \\ a_s \end{pmatrix}$，将$B$记作$\begin{pmatrix} b_1 \\ \vdots \\ b_{\ell} \end{pmatrix}$，这里的$a_i, b_j$为$n$维行向量。$A$与$B$的行等价即为$A$与$B$的行空间相同，即
$$C(A) = \operatorname{span}\{a_1, \cdots, a_s\} = \operatorname{span}\{b_1, \cdots, b_{\ell}\} = C(B)$$
所以相应的零空间，即解空间相同
$$N(A) = C(A)^{\perp} = C(B)^{\perp} = N(B)$$

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

很容易看到任何包含$\sqrt[3]{2}$的数域都必须包含$\sqrt[3]{2}, \sqrt[3]{4}$，从而包含$\mathbb{Q}(\sqrt[3]{2})$，那么只要证明$\mathbb{Q}(\sqrt[3]{2})$是一个数域。设$m(x) = x^3 - 2$，这是$\sqrt[3]{2}$的所谓的（首一的,
monic）极小多项式[^1](minimal polynomial over
$\mathbb{Q}$)。令$F = \mathbb{Q}[x] / (m(x))$为$\mathbb{Q}$系数多项式全体的等价类组成的集合，其中的等价关系为
$$f_1(x) \sim f_2(x) \quad \Longleftrightarrow \quad \exists g(x) \ s.t.\ f_1(x)-f_2(x) = g(x)m(x)$$
作为一个$\mathbb{Q}$线性空间，$F$的一组基可以取作$1, \overline{x}, \overline{x}^2$。这是因为对于任意一个$f(x) \in \mathbb{Q}[x]$，都存在$g(x), r(x)$，$\deg r(x) < \deg m(x)$，使得
$$f(x) = g(x)m(x) + r(x)$$ 于是
$$F = \{ a + b\overline{x} + c\overline{x}^2 \ |\ a,b,c\in\mathbb{Q} \}$$
定义
$$\varphi : F \to \mathbb{Q}(\sqrt[3]{2}), \overline{x} \mapsto \sqrt[3]{2}$$
可以验证

-   $F$关于加、减、乘、除封闭。加、减、乘封闭很容易验证。任取$f(x)\\in \mathbb{Q}[x] \setminus m(x)\cdot\mathbb{Q}[x]$，即$\overline{f} \neq 0 \in F$，那么$f(x)$与$m(x)$互素，即他们的最大公因子为$1$，记作$(f(x), m(x)) = 1$。于是（通过辗转相除法）存在$g_1(x), g_2(x) \in \mathbb{Q}[x]$，使得$g_1(x)f(x) + g_2(x)m(x) = 1$，于是$\overline{f}$在$F$中的逆元即为$\overline{g}_1$。

-   $\varphi$是一个一一对应（且保运算，即是一个域同构）。

[^1]: 使得满足$f(\sqrt[3]{2})=0$的$\mathbb{Q}$系数多项式中次数最低的，如果要求是首一的，即最高次项系数为1，则这样的多项式是唯一的。

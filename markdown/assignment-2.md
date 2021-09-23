---
date: 第二次作业
title: 2021秋高等代数课后习题
---

**习题2.1 第1题**

向量组$\mathbf{\alpha}_1, \cdots, \mathbf{\alpha}_m$是否线性相关等价于线性方程组$\lambda_1\mathbf{\alpha}_1 + \cdots + \lambda\mathbf{\alpha}_m = 0$是否有非零解。

所以(1)线性无关，(2)线性相关。

注意，可以用`numpy`的函数`numpy.linalg.matrix_rank`得到的齐次线性方程组系数矩阵的秩与未知元个数进行比较得出结论。

**习题2.1 第2题**
类似第1题的方法进行判断，(1)，(2)中的向量组都是线性相关的。

**习题2.1 第3题**
3维空间中的一般的平面可以表达为$t_1\alpha_1 + t_2\alpha_2 + \beta$,
$t_1,t_2\in\mathbb{R}$，其中$\alpha_1,\alpha_2$为非零向量。如果$\alpha_1,\alpha_2$中一个为零向量，则退化为直线；如果两个都为零向量，则退化为点。3维空间中$m$个点（$m\geqslant 4$，小于4个没有讨论意义）$a_1,\cdots,a_m$判断是否共面（或者退化为共线，乃至一个点），只要判断$b_1 = a_2-a_1, \cdots, b_{m-1}=a_m-a_1$能否表达为$t_1\alpha_1 + t_2\alpha_2$。即判断齐次线性方程组
$$\lambda_1 b_1 + \cdots + \lambda_{m-1} b_{m-1} = 0$$
的解的情况。于是，（1）共面，（2）不共面。

**习题2.1 第7题** 考虑
$$\lambda_1 (\alpha_1+\alpha_2) + \lambda_2 (\alpha_2+\alpha_3) + \cdots + \lambda_n (\alpha_n+\alpha_1) = 0$$
$\lambda_1, \cdots, \lambda_n\in\mathbb{R}$, 变形为
$$(\alpha_1, \cdots, \alpha_n)
\begin{pmatrix}
1 & 0 & \cdots & \cdots & 0 & 1 \\
1 & 1 & 0 & & & 0 \\
0 & 1 & 1 & \ddots & & \vdots \\
\vdots & \ddots & \ddots & \ddots & \ddots & \vdots \\
\vdots & & \ddots & \ddots & \ddots & 0 \\
0 & \cdots & \cdots & 0 & 1 & 1
\end{pmatrix}
\begin{pmatrix}
\lambda_1 \\ \vdots \\ \lambda_n
\end{pmatrix} = 0$$
对系数矩阵进行从上往下进行上一行乘以-1加到下一行的操作，有
$$A := \begin{pmatrix}
1 & 0 & \cdots & \cdots & 0 & 1 \\
1 & 1 & 0 & & & 0 \\
0 & 1 & 1 & \ddots & & \vdots \\
\vdots & \ddots & \ddots & \ddots & \ddots & \vdots \\
\vdots & & \ddots & \ddots & \ddots & 0 \\
0 & \cdots & \cdots & 0 & 1 & 1
\end{pmatrix}
\to
\begin{pmatrix}
1 & 0 & \cdots & \cdots & 0 & 1 \\
0 & 1 & 0 & & & -1 \\
0 & 0 & 1 & \ddots & & 1 \\
\vdots & \ddots & \ddots & \ddots & \ddots & \vdots \\
\vdots & & \ddots & 0 & 1 & (-1)^{n-2} \\
0 & \cdots & \cdots & 0 & 0 & 1 + (-1)^{n-1}
\end{pmatrix}$$
当$n$为偶数时，此时化简后的系数矩阵最后一行全为零，故$A\begin{pmatrix}
\lambda_1 \\ \vdots \\ \lambda_n
\end{pmatrix} = 0$有非零解，此时$\alpha_1+\alpha_2, \alpha_2+\alpha_3, \alpha_n+\alpha_1$一定线性相关。

当$n$为奇数时，化简后的系数矩阵满秩，此时$\alpha_1+\alpha_2, \alpha_2+\alpha_3, \cdots, \alpha_n+\alpha_1$线性相关当且仅当$\alpha_1, \alpha_2, \cdots, \alpha_n$线性相关。

**习题2.1 第8题** 类似第7题，将问题写为 $$(\alpha_1, \cdots, \alpha_n)
\begin{pmatrix}
1 & 0 & \cdots & \cdots & 0 & -\lambda \\
-\lambda & 1 & 0 & & & 0 \\
0 & -\lambda & 1 & \ddots & & \vdots \\
\vdots & \ddots & \ddots & \ddots & \ddots & \vdots \\
\vdots & & \ddots & \ddots & \ddots & 0 \\
0 & \cdots & \cdots & 0 & -\lambda & 1
\end{pmatrix}
\begin{pmatrix}
z_1 \\ \vdots \\ z_n
\end{pmatrix} = 0$$
$z_1, \cdots, z_n \in \mathbb{C}$.对系数矩阵进行从上往下进行上一行乘以$\lambda$加到下一行的操作，有
$$A := \begin{pmatrix}
1 & 0 & \cdots & \cdots & 0 & -\lambda \\
-\lambda & 1 & 0 & & & 0 \\
0 & -\lambda & 1 & \ddots & & \vdots \\
\vdots & \ddots & \ddots & \ddots & \ddots & \vdots \\
\vdots & & \ddots & \ddots & \ddots & 0 \\
0 & \cdots & \cdots & 0 & -\lambda & 1
\end{pmatrix}
\to
\begin{pmatrix}
1 & 0 & \cdots & \cdots & 0 & -\lambda \\
0 & 1 & 0 & & & -\lambda^2 \\
0 & 0 & 1 & \ddots & & 1 \\
\vdots & \ddots & \ddots & \ddots & \ddots & \vdots \\
\vdots & & \ddots & 0 & 1 & -\lambda\cdot\lambda^{n-2} \\
0 & \cdots & \cdots & 0 & 0 & 1-\lambda\cdot\lambda^{n-1}
\end{pmatrix}$$
若$\alpha_1,\cdots,\alpha_n$线性无关，则只需要$1-\lambda^{n} \neq 0$，即$\lambda$不取$n$次单位根$e^{2k\pi i/n}$，即可使$\alpha_1-\lambda\alpha_2,\cdots,\alpha_n-\lambda\alpha_1$线性无关。

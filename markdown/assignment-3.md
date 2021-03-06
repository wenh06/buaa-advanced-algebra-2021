**习题2.2**

一般来说，将向量$\alpha_1,\cdots,\alpha_n$排成向量，组成矩阵$A$。求向量组$\{\alpha_1,\cdots,\alpha_n\}$的线性关系，即求齐次线性方程组
$$0 = Ax = (\alpha_1,\cdots,\alpha_n) \begin{pmatrix} x_{1} \\ \vdots \\ x_{n} \end{pmatrix}$$
的性质。事实上，如果$\{\alpha_{i_1},\cdots,\alpha_{i_m}\}$线性无关，那么
$$(\alpha_{i_1},\cdots,\alpha_{i_m}) \begin{pmatrix} x_{i_1} \\ \vdots \\ x_{i_m} \end{pmatrix} = 0$$
只有零解。于是，只要将$A$通过高斯消元法化为阶梯阵$B = (\beta_1,\cdots,\beta_n)$，将每行第一个非零元（可以设为1，被称作主元，pivot）对应的列（被称作主列，pivot
columns）拿到一起，设其下标为$i_1,\cdots,i_m$，那么$\{\alpha_{i_1},\cdots,\alpha_{i_m}\}$就是一个极大线性无关组。这是因为，此时
$$(\beta_{i_1},\cdots,\beta_{i_m}) = \begin{pmatrix} 1 & & \makebox(0,0){\text{\huge $\ast$}} \\ & \ddots & \\ \makebox(0,0){\text{\huge\bf 0}} & & 1 \\ & & \\ & \makebox(0,0){\text{\huge\bf 0}} & \\ & & \end{pmatrix}$$
要注意的是改变$\alpha_1,\cdots,\alpha_n$排列次序组成矩阵$A$，可能得到不同的极大线性无关组。

矩阵化为阶梯形可以利用如下的[程序](https://github.com/wenh06/buaa-advanced-algebra-2021/blob/master/notebooks/assignment-3.ipynb)进行

<div class="center">

``` python
import sympy as sp

mat = sp.Matrix(
    [[1,-1,2,4],[0,3,1,2],[3,0,7,14],[1,-1,2,0],[2,1,5,6]]
).T
echelon, pivots = mat.rref()
```

</div>

以上得到的“echelon”即为阶梯形，“pivots”为主列的下标（下标从0开始）。

第(1)问，全部四个向量$\alpha_1,\alpha_2,\alpha_3,\alpha_4$组成极大线性无关组。第(2)问的一个线性无关组为$\alpha_1,\alpha_2,\alpha_4$.

**习题2.2 第2题**

将$\alpha_1,\cdots,\alpha_5$排成向量，组成矩阵$A$（可以顺序不同，但$\alpha_1,\alpha_2$排在前2位），并化为阶梯型
$$A = \begin{pmatrix} 0 & 1 & 3 & 4 & 6 \\ 1 & 2 & 4 & 3 & 5 \\ 2 & 3 & 5 & 2 & 4 \\ 3 & 4 & 6 & 1 & 3 \end{pmatrix} \to
\begin{pmatrix} 1 & 0 & -2 & -5 & -7 \\ 0 & 1 & 3 & 4 & 6 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{pmatrix}$$
于是$\alpha_1,\alpha_2$线性无关，且式原向量组的一个极大线性无关组，不能再扩充了。

**习题2.2 第3题**

通过高斯消元法将矩阵化为阶梯形，主列对应的原矩阵的列即为一个极大线性无关组，列的数目即为秩。矩阵的转置的主列对应原矩阵的行即为一个极大线性无关组。于是
$$\begin{aligned}
\begin{pmatrix}2 & -1 & -1\\-1 & 2 & -1\\-1 & -1 & 2\end{pmatrix} & \to \begin{pmatrix}1 & 0 & -1\\0 & 1 & -1\\0 & 0 & 0\end{pmatrix} \\
\begin{pmatrix}2 & -1 & -1\\-1 & 2 & -1\\-1 & -1 & 2\end{pmatrix}^T & \to \begin{pmatrix}1 & 0 & -1\\0 & 1 & -1\\0 & 0 & 0\end{pmatrix} \\
\begin{pmatrix}1 & 1 & 1 & 1 & 1\\1 & 2 & 3 & 4 & 5\\5 & 4 & 3 & 1 & 2\end{pmatrix} & \to \begin{pmatrix}1 & 0 & -1 & 0 & -5\\0 & 1 & 2 & 0 & 7\\0 & 0 & 0 & 1 & -1\end{pmatrix} \\
\begin{pmatrix}1 & 1 & 1 & 1 & 1\\1 & 2 & 3 & 4 & 5\\5 & 4 & 3 & 1 & 2\end{pmatrix}^T & \to \begin{pmatrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & 1\\0 & 0 & 0\\0 & 0 & 0\end{pmatrix}\end{aligned}$$
(1)的秩为2，前两列（行）构成极大线性无关组。(2)的秩为3，全部3行构成极大线性无关组，第1,2,4列构成极大线性无关组。

**习题2.2 第6题**

(1).
如果某$r$个线性无关向量不构成极大线性无关组，那么这$r$个向量还可以进一步添加向量得到极大线性无关组，这样得到的极大线性无关组中向量个数大于$r$，与秩为$r$矛盾。

(2). 在第7题中证明。

**习题2.2 第7题**

设向量组(I)为$\alpha_1,\cdots,\alpha_n$，向量组(II)为$\beta_1,\cdots,\beta_m$。设向量组(II)的一个极大线性无关组为$R = \{\beta_{i_1},\cdots,\beta_{i_r}\}$，那么向量组(II)可以由这个极大线性无关组$R$线性表出，从而向量组(I)可以由$R$线性表出。任取向量组(I)的一个极大线性无关组$S = \{\alpha_{j_1},\cdots,\alpha_{j_s}\}$，那么有
$$(\alpha_{j_1},\cdots,\alpha_{j_s}) = (\beta_{i_1},\cdots,\beta_{i_r})A_{r\times s}$$
$A_{r\times s}$为某个$r\times s$的矩阵。假设$s > r$，那么齐次线性方程组
$$A_{r\times s} \begin{pmatrix}
x_1 \\ \vdots \\ x_s
\end{pmatrix} = 0$$
必然有非零解。 那么
$$(\alpha_{j_1},\cdots,\alpha_{j_s})\begin{pmatrix}
x_1 \\ \vdots \\ x_s
\end{pmatrix} = (\beta_{i_1},\cdots,\beta_{i_r})A_{r\times s}\begin{pmatrix}
x_1 \\ \vdots \\ x_s
\end{pmatrix} = 0$$
有非零解，从而$\{\alpha_{j_1},\cdots,\alpha_{j_s}\}$线性相关，这与它是极大线性无关组矛盾。

其实，可以直接利用不等式
$$\begin{aligned}
\operatorname{rank}(\alpha_{j_1},\cdots,\alpha_{j_s}) & \leqslant \min \{ \operatorname{rank}(\beta_{i_1},\cdots,\beta_{i_r}), \operatorname{rank}(A_{r\times s}) \} \\
& \leqslant \min \{ r, \min \{ r,s \} \} = \min \{ r,s \} \\
& \leqslant r\end{aligned}$$

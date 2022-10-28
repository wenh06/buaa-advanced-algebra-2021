---
date: 2022-10-21 第四次习题课
title: 2022秋高等代数习题课
---

**第一题**. 计算下列行列式。

\(1\)
$D = \begin{vmatrix} 2 & 1 & -1 & 3 \\ 1 & 4 & 1 & 2 \\ -1 & 2 & 1 & 1 \\ 1 & 0 & 2 & 1 \end{vmatrix}$;
(2)
$D_n = \begin{vmatrix} 1 + a_1 & a_2 & a_3 & \cdots & a_n \\ a_1 & 1 + a_2 & a_3 & \cdots & a_n \\ a_1 & a_2 & 1 + a_3 & \cdots & a_n \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_1 & a_2 & a_3 & \cdots & 1 + a_n \end{vmatrix}$

**解**： (1) $$\begin{aligned}
D & = \begin{vmatrix} 2 & 1 & -1 & 3 \\ 1 & 4 & 1 & 2 \\ -1 & 2 & 1 & 1 \\ 1 & 0 & 2 & 1 \end{vmatrix} = \begin{vmatrix} 0 & 1 & -5 & 1 \\ 0 & 4 & -1 & 1 \\ 0 & 2 & 3 & 2 \\ 1 & 0 & 2 & 1 \end{vmatrix} = (-1)^{4+1} \begin{vmatrix} 1 & -5 & 1 \\ 4 & -1 & 1 \\ 2 & 3 & 2 \end{vmatrix} \\
& = - (-1)^{1+1} \begin{vmatrix} 1 & -5 & 1 \\ 0 & 19 & -3 \\ 0 & 13 & 0 \end{vmatrix} = - \begin{vmatrix} 19 & -3 \\ 13 & 0 \end{vmatrix} = -39\end{aligned}$$

\(2\)
利用行列式的多线性性进行求解。令$e_1 = (1, 0, \ldots, 0)^T, \ldots, e_n = (0, \ldots, 0, 1)^T,$
$\gamma = (1, \ldots, 1)^T = e_1 + \cdots + e_n.$ 那么 $$\begin{aligned}
D_n & = \det( e_1 + a_1 \gamma, \ldots, e_n + a_n \gamma) \\
& = \det( e_1, \ldots, e_n) + \det( a_1 \gamma, e_2, \ldots, e_n) + \cdots + \det( e_1, \ldots, e_{n-1}, a_n \gamma) + 0 + \cdots + 0 \\
& = 1 + a_1 \det( \gamma, e_2, \ldots, e_n) + \cdots + a_n \det( e_1, \ldots, e_{n-1}, \gamma) \\
& = 1 + a_1 \det( e_1 + \cdots + e_n, e_2, \ldots, e_n) + \cdots + a_n \det( e_1, \ldots, e_{n-1}, e_1 + \cdots + e_n) \\
& = 1 + a_1 \det( e_1, e_2, \ldots, e_n) + \cdots + a_n \det( e_1, \ldots, e_{n-1}, e_n) \\
& = 1 + a_1 + \cdots + a_n\end{aligned}$$
这题也可以利用加边的方式进行求解。

**第二题**.
求下列线性方程组的一个特解$\gamma_0$以及导出组的一个基础解系，并用它们表出线性方程组的全部解。
$$\begin{cases}
x_1 - x_2 - 3 x_3 + x_4 + 3 x_5 = 1 \\
x_1 - x_2 - x_3 + x_4 + x_5 = 1 \\
x_1 + x_2 + x_3 - x_4 - x_5 = 1
\end{cases}$$

**解**： 化为增广矩阵的形式进行化简 $$\begin{aligned}
\arraycolsep=4pt
\left( \begin{array}{ccccc|c} 1 & -1 & -3 & 1 & 3 & 1 \\ 1 & -1 & -1 & 1 & 1 & 1 \\ 1 & 1 & 1 & -1 & -1 & 1 \end{array} \right) & \rightarrow
\arraycolsep=4pt
\left( \begin{array}{ccccc|c} 1 & -1 & -3 & 1 & 3 & 1 \\ 0 & 0 & 2 & 0 & -2 & 0 \\ 0 & 2 & 4 & -2 & -4 & 0 \end{array} \right) \rightarrow
\arraycolsep=4pt
\left( \begin{array}{ccccc|c} 1 & -1 & 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 & -1 & 0 \\ 0 & 2 & 0 & -2 & 0 & 0 \end{array} \right) \\
& \rightarrow
\arraycolsep=4pt
\left( \begin{array}{ccccc|c} 1 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 & -1 & 0 \\ 0 & 1 & 0 & -1 & 0 & 0 \end{array} \right) \rightarrow
\arraycolsep=4pt
\left( \begin{array}{ccccc|c} 1 & 0 & 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & 0 & -1 & 0 \end{array} \right)\end{aligned}$$
解得通解为
$$\begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix} + \tau_1 \begin{pmatrix} 0 \\ 1 \\ 0 \\ 1 \\ 0 \end{pmatrix} + \tau_2 \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 1 \end{pmatrix}, \quad \tau_1, \tau_2 \in \mathbb{R}.$$

**第三题**.
设$\mathbb{F}$上$n$维线性空间$V$的一组基为$\alpha_1, \alpha_2, \ldots, \alpha_n,$
令
$$\beta_k = \alpha_1 + \alpha_2 + \cdots + \alpha_k, \quad k = 1, 2, \ldots, n.$$

-   证明$\beta_1, \beta_2, \ldots, \beta_n$是$V$的一组基；

-   对于$\alpha = \alpha_1 + 2 \alpha_2 + \cdots + n \alpha_n,$
    求出$\alpha$在基$\beta_1, \beta_2, \ldots, \beta_n$下的坐标。

**解**： (1) 我们有
$$(\beta_1, \beta_2, \ldots, \beta_n) = (\alpha_1, \alpha_2, \ldots, \alpha_n) \underbrace{ \begin{pmatrix} 1 & 1 & 1 & \cdots & 1 \\ 0 & 1 & 1 & \cdots & 1 \\ 0 & 0 & 1 & \cdots & 1 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & \cdots & 0 & 1 \end{pmatrix} }_{\text{记作} A}$$
到这里我们可以直接说由于$A$是一个可逆（满秩）方阵，所以$\beta_1, \beta_2, \ldots, \beta_n.$
如果还不清楚的话，我们就假设$\beta_1, \beta_2, \ldots, \beta_n$线性相关，即存在不全为0的数$\lambda_1, \ldots, \lambda_n,$
使得$\lambda_1 \beta_1 + \cdots + \lambda_n \beta_n = 0,$ 即有
$$0 = (\beta_1, \beta_2, \ldots, \beta_n) \underbrace{ \begin{pmatrix} \lambda_1 \\ \vdots \\ \lambda_n \end{pmatrix} }_{\text{记作} \lambda} = (\alpha_1, \alpha_2, \ldots, \alpha_n) A \lambda.$$
由于$\alpha_1, \alpha_2, \ldots, \alpha_n$是基，线性无关，所以要使上式成立，必须有$A\lambda = 0.$
但是方阵$A$满秩，所以$A\lambda = 0$只能有零解，矛盾。

另一种解法：容易看出有$\alpha_1 = \beta_1, \alpha_k = \beta_k - \beta_{k-1}, k = 2, \ldots, n.$
即$\alpha_1, \ldots, \alpha_n$能由$\beta_1, \ldots, \beta_n$线性表出。故$\beta_1, \ldots, \beta_n$的秩大于等于$\alpha_1, \ldots, \alpha_n$的秩。由于$\alpha_1, \ldots, \alpha_n$是基，故秩只能相等，从而知$\beta_1, \ldots, \beta_n$也是一组基。这种解法相当于把矩阵$A$的逆求出来了。

\(2\)
沿用上一小题记号，我们设$\alpha$在基$\beta_1, \beta_2, \ldots, \beta_n$下的坐标为$\lambda = (\lambda_1, \ldots, \lambda_n)^T,$
那么 $$\begin{aligned}
\alpha & = \alpha_1 + 2 \alpha_2 + \cdots + n \alpha_n = (\alpha_1, \alpha_2, \ldots, \alpha_n) \begin{pmatrix} 1 \\ 2 \\ \vdots \\ n \end{pmatrix} \\
& = (\beta_1, \beta_2, \ldots, \beta_n) \lambda = (\alpha_1, \alpha_2, \ldots, \alpha_n) A \lambda\end{aligned}$$
解线性方程组$A \lambda = \begin{pmatrix} 1 \\ 2 \\ \vdots \\ n \end{pmatrix}$：
$$\left( \begin{array}{ccccc|c}1 & 1 & 1 & \cdots & 1 & 1 \\ 0 & 1 & 1 & \cdots & 1 & 2 \\ 0 & 0 & 1 & \cdots & 1 & 3 \\ \vdots & \vdots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 0 & 1 & n \end{array} \right) \rightarrow \left( \begin{array}{ccccc|c}1 & 0 & 0 & \cdots & 0 & -1 \\ 0 & 1 & 1 & \cdots & 1 & 2 \\ 0 & 0 & 1 & \cdots & 1 & 3 \\ \vdots & \vdots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 0 & 1 & n \end{array} \right) \rightarrow \cdots \rightarrow \left( \begin{array}{ccccc|c}1 & 1 & 0 & \cdots & 0 & -1 \\ 0 & 1 & 0 & \cdots & 0 & -1 \\ 0 & 0 & 1 & \cdots & 0 & -1 \\ \vdots & \vdots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 0 & 1 & n \end{array} \right)$$
解得$\alpha$在基$\beta_1, \beta_2, \ldots, \beta_n$下的坐标为$\lambda = (-1, \ldots, -1, n)^T.$

或者我们利用$\alpha_1 = \beta_1, \alpha_k = \beta_k - \beta_{k-1}, k = 2, \ldots, n,$
代入$\alpha = \alpha_1 + 2 \alpha_2 + \cdots + n \alpha_n$也可以得到相同的结论。

**第四题**. 判断下述结论是否正确，并说明理由。

-   设向量组$I = \{ \alpha_1, \alpha_2, \ldots, \alpha_m \}$的秩为$r.$
    若去掉$I$中任意一个向量$\alpha_i (1 \leqslant i \leqslant m)$都有向量组$I \setminus \{ \alpha_i \}$的秩为$r-1,$
    则有$r = m$;

-   若$W$是$V$的子空间，且$\alpha_1 + W, \ldots, \alpha_r + W$是商空间$V / W$的一组基，则$\alpha_1, \ldots, \alpha_r$在$V$中是线性无关的。

**解**： (1) 正确。

用反证法，假设$r < m,$
那么取向量组$I$的一个极大线性无关组$I' = \{ \alpha_{i_1}, \alpha_{i_2}, \ldots, \alpha_{i_r} \},$
那么取$I$中不属于$I'$的任意一个向量$\alpha$,
都有$I \setminus \{ \alpha \}$包含$I',$ 从而秩为$r,$ 矛盾。

\(2\) 正确。

用反证法，假设$\alpha_1, \ldots, \alpha_r$在$V$中线性相关，那么存在不全为0的数$\lambda_1, \ldots, \lambda_r,$
使得$\lambda_1 \alpha_1 + \cdots + \lambda_r \alpha_r = 0 \in W.$ 那么
$$\lambda_1 (\alpha_1 + W) + \cdots + \lambda_r (\alpha_r + W) = 0 + W.$$
从这里我们可以看到，$\alpha_1, \ldots, \alpha_r$的选取需要比它们线性无关更强的条件，即进一步要求
$$\operatorname{span}\{ \alpha_1, \ldots, \alpha_r \} \cap W = \{0\}.$$

**第五题**. 设$V = \mathbb{F}^n, n \geqslant 2,$
定义$\mathbb{F}^n$的子集$W_1, W_2$如下： $$\begin{gathered}
W_1 = \{ (x_1, \ldots, x_n) \in \mathbb{F}^n \ |\ x_1 + \cdots + x_n = 0 \}, \\
W_2 = \{ (y_1, \ldots, y_n) \in \mathbb{F}^n \ |\ y_1 - \cdots - y_n = 0 \}. \\\end{gathered}$$

-   证明$W_1, W_2$都是$V$的子空间，并且$V = W_1 + W_2$.

-   求$\dim (W_1 \cap W_2)$和$W_1 \cap W_2$的一组基。

**解**： (1)
这题可以根据定义去验证，也可以通过$W_1, W_2$是两个齐次线性方程（组）的解空间来说明他们是$V$的子空间。关于维数关系，我们有
$$\dim (W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2) = (n - 1) + (n - 1) - \dim(W_1 \cap W_2).$$
$W_1 \cap W_2$是线性方程组 $$\begin{cases}
x_1 + \cdots + x_n = 0 \\
x_1 - \cdots - x_n = 0
\end{cases}$$ 的解空间，维数为$n-2,$
从而有$\dim (W_1 + W_2) = 2n - 2 - \dim(W_1 \cap W_2) = 2n - 2 - (n - 2) = n,$
即有$V = W_1 + W_2$.

另一种方法是，可以很容易写出$W_1$的一组基$(1, -1, 0, \ldots, 0)^T,$
$(1, 0, -1, 0, \ldots, 0)^T,$ $\ldots,$ $(1, 0, \ldots, 0, -1)^T,$
以及$W_2$的一组基$(1, 1, 0, \ldots, 0)^T,$ $(1, 0, 1, 0, \ldots, 0)^T,$
$\ldots,$ $(1, 0, \ldots, 0, 1)^T.$
把这两组基合并在一起组成$W_1 + W_2$中的一个向量组，容易看出这个向量组的秩为$n,$
从而知$V = W_1 + W_2.$

\(2\) 进一步解上述线性方程组有解
$$x = \begin{pmatrix} 0 \\ \tau_1 \\ \vdots \\ \tau_{n-2} \\ -(\tau_1 + \cdots + \tau_{n-2}) \end{pmatrix}, ~~ \tau_1, \ldots, \tau_{n-2} \in \mathbb{R}.$$
即知$\dim (W_1 + W_2) = n - 2,$ 一组基可以取为
$$\left\{ \begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \\ 0 \\ -1 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ \vdots \\ 0 \\ -1 \end{pmatrix}, \cdots, \begin{pmatrix} 0 \\ \vdots \\ 0 \\ 1 \\ -1 \end{pmatrix} \right\}.$$

**第六题**.
设$\alpha_1, \alpha_2, \ldots, \alpha_r$和$\beta_1, \beta_2, \ldots, \beta_r$分别是$n$维线性空间$V_1$和$V_2$的两组线性无关的向量组，

-   构造一个$V_1$到$V_2$的同态映射$f$满足
    $$f(\alpha_i) = \beta_i, i = 1, \ldots, r, \text{ 并且 } \dim(\ker(f)) = n-r,$$

-   满足上述条件的同态映射是否唯一？并证明你的结论。

**解**： (1)
将线性空间$V_1$的线性无关组$\alpha_1, \alpha_2, \ldots, \alpha_r$扩充为一组基$\alpha_1, \alpha_2, \ldots, \alpha_r, \alpha_{r+1}, \cdots, \alpha_n.$
定义$f: V_1 \rightarrow V_2$（在$V_1$的基$\alpha_1, \ldots, \alpha_n$上作用）为
$$f(\alpha_i) = \begin{cases}
\beta_i, & i = 1, \ldots, r, \\
0, & i = r+1, \ldots, n.
\end{cases}$$
由于$\beta_1, \beta_2, \ldots, \beta_r$线性无关，所以$\ker(f) = \operatorname{span}\{ \alpha_{r+1}, \cdots, \alpha_n \},$
即有$\dim(\ker(f)) = n-r.$

\(2\)
不唯一。事实上，只要我们让$f(\alpha_i) \in \operatorname{span} \{ \beta_1, \beta_2, \ldots, \beta_r \}, i = r+1, \ldots, n,$
即可。例如 $$f(\alpha_i) = \begin{cases}
\beta_i, & i = 1, \ldots, r, \\
\beta_1, & i = r+1, \ldots, n.
\end{cases}$$
此时，$\operatorname{Im}(f) = \operatorname{span} \{ \beta_1, \beta_2, \ldots, \beta_r \},$
即有$\dim(\operatorname{Im}(f)) = r,$ 那么根据维数公式有
$$\dim(\ker(f)) = \dim V_1 - \dim(\operatorname{Im}(f)) = n - r.$$
或者，你也可以通过$f$的定义算得
$$\ker f = \operatorname{span} \{ \alpha_1 - \alpha_i \ |\ i = r + 1, \ldots, n \},$$
再得到上述空间的维数为$n - r.$

同时，根据维数公式可知，条件$f(\alpha_i) \in \operatorname{span} \{ \beta_1, \beta_2, \ldots, \beta_r \}, i = r+1, \ldots, n,$是满足题设条件的同态映射$f$必须要满足的条件。

注：线性空间之间的同态映射（这里就是线性映射）完全由它在定义域（$V_1$）上每个元素的取值唯一决定，如果两个$V_1$到$V_2$的线性映射在$V_1$中的每个向量上的取值都一样，那么它们就是相等的，是同一个线性映射。当$V_1$取定了一组基$\alpha_1, \ldots, \alpha_n$之后，$V_1$中的每个元素$\alpha$都可以唯一表示为$\alpha_1, \ldots, \alpha_n$的线性组合
$$\alpha = \lambda_1(\alpha) \alpha_1 + \cdots + \lambda_n(\alpha) \alpha_n,$$
这里的$\lambda_i(\alpha)$指的是一些由$\alpha$（唯一）决定的数。作为线性映射，$f$就必须满足
$$f(\alpha) = \lambda_1(\alpha) f(\alpha_1) + \cdots + \lambda_n(\alpha) f(\alpha_n).$$
于是，只要在基$\alpha_1, \ldots, \alpha_n$上的取值（值是$V_2$中的向量）确定了，那么在$V_1$中每个向量上的取值就确定了，这个线性映射就唯一确定了。
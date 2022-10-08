---
date: 2022-09-23 第二次习题课
title: 2022秋高等代数习题课
---

**第一题**.
设$\alpha_1, \ldots, \alpha_n$线性无关。令$\beta_j = a_{j1}\alpha_1 + \cdots + a_{jn}\alpha_n,$
$j = 1, \ldots, n.$
令$\gamma_j = \begin{pmatrix} a_{j1} \\ \vdots \\ a_{jn} \end{pmatrix},$
$j = 1, \ldots, n.$ 证明$\beta_1, \ldots, \beta_n$线性无关
$\Longleftrightarrow$ $\gamma_1, \ldots, \gamma_n$ 线性无关。

**证明**：$\Longrightarrow$: 假设$\gamma_1, \ldots, \gamma_n$
线性相关，那么存在不全为0的数$\lambda_1, \ldots, \lambda_n$使得
$$\lambda_1 \gamma_1 + \cdots + \lambda_n \gamma_n = 0.$$ 那么有
$$\begin{aligned}
& ~~ \lambda_1 \beta_1 + \cdots + \lambda_n \beta_n \\
= & ~~ \lambda_1 (a_{11}\alpha_1 + \cdots + a_{1n}\alpha_n) + \cdots + \lambda_n (a_{n1}\alpha_1 + \cdots + a_{nn}\alpha_n) \\
= & ~~ (\lambda_1 a_{11} + \cdots + \lambda_n a_{n1}) \alpha_1 + \cdots + (\lambda_1 a_{1n} + \cdots + \lambda_n a_{nn}) \alpha_n \\
= & ~~ (\alpha_1, \cdots, \alpha_n) \begin{pmatrix} \lambda_1 a_{11} + \cdots + \lambda_n a_{n1} \\ \vdots \\ \lambda_1 a_{1n} + \cdots + \lambda_n a_{nn} \end{pmatrix} \\
= & ~~ (\alpha_1, \cdots, \alpha_n) \left( \begin{pmatrix} \lambda_1 a_{11} \\ \vdots \\ \lambda_1 a_{1n} \end{pmatrix} + \cdots + \begin{pmatrix} \lambda_n a_{n1} \\ \vdots \\ \lambda_n a_{nn} \end{pmatrix} \right) \\
= & ~~ (\alpha_1, \cdots, \alpha_n) (\lambda_1 \gamma_1 + \cdots + \lambda_n \gamma_n) \\
= & ~~ 0.\end{aligned}$$
这与$\beta_1, \ldots, \beta_n$线性无关的条件矛盾。

$\Longleftarrow$: 假设$\beta_1, \ldots, \beta_n$
线性相关，那么存在不全为0的数$\lambda_1, \ldots, \lambda_n$使得
$$\lambda_1 \beta_1 + \cdots + \lambda_n \beta_n = 0.$$ 上式左边有
$$\lambda_1 \beta_1 + \cdots + \lambda_n \beta_n = (\lambda_1 a_{11} + \cdots + \lambda_n a_{n1}) \alpha_1 + \cdots + (\lambda_1 a_{1n} + \cdots + \lambda_n a_{nn}) \alpha_n$$
由于$\alpha_1, \ldots, \alpha_n$线性无关，所以有 $$\begin{cases}
\lambda_1 a_{11} + \cdots + \lambda_n a_{n1} = 0\\
\hspace{3em} \vdots \\
\lambda_1 a_{1n} + \cdots + \lambda_n a_{nn} = 0
\end{cases}$$ 排成列向量的形式，即有
$$0 = \begin{pmatrix} 0 \\ \vdots \\ 0 \end{pmatrix} = \begin{pmatrix} \lambda_1 a_{11} + \cdots + \lambda_n a_{n1} \\ \vdots \\ \lambda_1 a_{1n} + \cdots + \lambda_n a_{nn} \end{pmatrix} = \lambda_1 \begin{pmatrix} a_{11} \\ \vdots \\ a_{1n} \end{pmatrix} + \cdots + \lambda_n \begin{pmatrix} a_{n1} \\ \vdots \\ a_{nn} \end{pmatrix} = \lambda_1 \gamma_1 + \cdots + \lambda_n \gamma_n.$$
这与$\gamma_1, \ldots, \gamma_n$ 线性无关矛盾。

**习题2.2 第6题**. 设向量组$\alpha_1, \ldots, \alpha_n$的秩是$r.$ 求证：

(1).
$\alpha_1, \ldots, \alpha_n$中任意$r$个线性无关向量都是极大线性无关组。

(2).
设$\alpha_1, \ldots, \alpha_n$能被其中某$r$个向量$\beta_1, \ldots, \beta_r$线性表出，则$\beta_1, \ldots, \beta_r$线性无关。

**证明**： (1).
任取$\alpha_1, \ldots, \alpha_n$中$r$个线性无关向量$\alpha_{i_1}, \ldots, \alpha_{i_r}$,
假设它不是极大线性无关组，那么存在$j, 1\leqslant j \leqslant n, j\not\in \{i_1, \ldots, i_r \},$
使得$\alpha_{i_1}, \ldots, \alpha_{i_r}, \alpha_j$线性无关。这与$\alpha_1, \ldots, \alpha_n$的秩为$r$是矛盾的。

(2).
假设$\beta_1, \ldots, \beta_r$线性相关，那么存在不全为0的数$\lambda_1, \ldots, \lambda_r$使得$\lambda_1\beta_1 + \cdots + \lambda_r\beta_r = 0.$
任取$\alpha_1, \ldots, \alpha_n$的一个极大线性无关组$\alpha_{i_1}, \ldots, \alpha_{i_r}$.
由于$\alpha_1, \ldots, \alpha_n$能被$\beta_1, \ldots, \beta_r$线性表出，所以存在系数$a_{11}, \ldots, a_{rr},$
使得 $$\begin{cases}
\alpha_{i_1} = a_{11}\beta_1 + \cdots + a_{r1}\beta_r \\
\hspace{3em} \vdots \\
\alpha_{i_r} = a_{1r}\beta_1 + \cdots + a_{rr}\beta_r,
\end{cases}$$
写成矩阵形式$(\alpha_{i_1}, \ldots, \alpha_{i_r}) = (\beta_1, \ldots, \beta_r) A$,
其中$A = (a_{ij})_{1\leqslant i,j \leqslant r}.$
不妨设方阵$A$是满秩的，否则齐次线性方程组$Ax = 0$有非零解，此时任取其中一个非零解$x = (x_1, \ldots, x_r),$
即有
$$x_1\alpha_{i_1} + \cdots + x_r\alpha_{i_r} = (\beta_1, \ldots, \beta_r) Ax = 0,$$
这与$\alpha_{i_1}, \ldots, \alpha_{i_r}$是线性无关组是矛盾的。

令$t_1, \ldots, t_r$为未知数，考虑 $$\begin{aligned}
t_1 \alpha_{i_1} + \cdots + t_r \alpha_{i_r} & = t_1 (a_{11}\beta_1 + \cdots + a_{r1}\beta_r) + \cdots + t_r (a_{1r}\beta_1 + \cdots + a_{rr}\beta_r) \\
& = (t_1 a_{11} + \cdots + t_r a_{1r}) \beta_1 + \cdots + (t_1 a_{r1} + \cdots + t_r a_{rr}) \beta_r \\
& = (\beta_1, \ldots, \beta_r) A \begin{pmatrix} t_1 \\ \vdots \\ t_r \end{pmatrix}\end{aligned}$$
由于$A$是满秩方阵，那么非齐次线性方程组$A \begin{pmatrix} t_1 \\ \vdots \\ t_r \end{pmatrix} = \begin{pmatrix} \lambda_1 \\ \vdots \\ \lambda_r \end{pmatrix}$有唯一解，记为$(x_1, \ldots, x_r).$
由于$\lambda_1, \ldots, \lambda_r$不全为0，所以$x_1, \ldots, x_r$不全为0.
那么有
$$x_1 \alpha_{i_1} + \cdots + x_r \alpha_{i_r} = (\beta_1, \ldots, \beta_r) A \begin{pmatrix} x_1 \\ \vdots \\ x_r \end{pmatrix} = (\beta_1, \ldots, \beta_r) \begin{pmatrix} \lambda_1 \\ \vdots \\ \lambda_r \end{pmatrix} = \lambda_1\beta_1 + \cdots + \lambda_r\beta_r = 0$$
这还是与$\alpha_{i_1}, \ldots, \alpha_{i_r}$是线性无关组矛盾。故假设不成立，$\beta_1, \ldots, \beta_r$必定是线性无关的。

**习题2.2 第7题**.
证明：若向量组(I)可以由向量组(II)线性表出，则(I)的秩不超过(II)的秩。

**解**： 这其实已经在上一题（习题2.2
第6题第(2)问）中证明了，因为在证明过程中，我们并没有假设$\beta_1, \cdots, \beta_r$是取自$\alpha_1, \ldots, \alpha_n$中的。事实上，假设向量组(I)秩为$r$，可以由秩为$s$的向量组(II)线性表出，且$r > s$,
那么取向量组(II)的一个极大线性无关组，再从向量组(II)可重复地随机添加$r-s$个向量，构成一个数量为$r$的向量组，那么这个向量组可以线性表出向量组(I)可以由这个向量组线性表出。根据上一题结论，这个向量组秩为$r$，矛盾。

**第四题**.
设$A$是$\mathbb{R}$上$n$阶方阵。若$\lvert a_{ii} \rvert > \sum\limits_{j\neq i} \lvert a_{ij} \rvert,$
$i = 1, \ldots, n,$ 求矩阵$A$的秩$r(A)$.

**解**：
假设$A$不满秩，那么$A = (\alpha_1, \cdots, \alpha_n)$列不满秩，其中$\alpha_1, \ldots, \alpha_n$是$A$的列。那么存在不全为0的实数$\lambda_1, \ldots, \lambda_n$，
使得
$$0 = \lambda_1 \alpha_1 + \cdots + \lambda_n \alpha_n = \begin{pmatrix} \lambda_1 a_{11} + \cdots + \lambda_n a_{1n} \\ \vdots \\ \lambda_1 a_{n1} + \cdots + \lambda_n a_{nn} \end{pmatrix}.$$
令$i_0 = \operatorname{argmax} \{ \lvert \lambda_i \rvert \ |\ i = 1, \ldots, n \}$为满足$\lambda_i$中绝对值最大者的下标（如果有不止一个则任取一个即可）。考察上式右边第$i_0$位的元素
$$\lambda_{1} a_{i_01} + \cdots + \lambda_{i_0} a_{i_0i_0} + \cdots \lambda_n a_{i_0n} = 0.$$
那么会有 $$\begin{aligned}
& ~~ \lvert \lambda_{1} a_{i_01} + \cdots + \lambda_{i_0-1} a_{i_0,i_0-1} + \lambda_{i_0+1} a_{i_0,i_0+1} + \cdots + \lambda_n a_{i_0n} \rvert \\
= & ~~ \lvert \lambda_{i_0} a_{i_0i_0} \rvert = \lvert \lambda_{i_0} \rvert \cdot \lvert a_{i_0i_0} \rvert ~~ {\color{red} >} ~~ \lvert \lambda_{i_0} \rvert \sum\limits_{j\neq i_0} \lvert a_{i_0j} \rvert \\
\geqslant & ~~ \lvert \lambda_{1} a_{i_01} \rvert + \cdots + \lvert \lambda_{i_0-1} a_{i_0,i_0-1} \rvert + \lvert \lambda_{i_0+1} a_{i_0,i_0+1} \rvert + \cdots + \lvert \lambda_n a_{i_0n} \rvert.\end{aligned}$$
上述不等式是不可能成立的。所以假设不成立，级$A$是满秩的，$r(A) = n.$

满足题设条件的方阵被称为（强）对角优势矩阵（diagonally dominant
matrix）。这样的矩阵都是非奇异的。如果学了方阵特征值的知识，此题还可以利用如下结论证明：

> 设$A$是复数域$\mathbb{C}$上$n$阶方阵，对$i = 1, \ldots, n$, 令
> $$\begin{aligned}
> R_{i} & = \sum_{j\neq {i}}\lvert a_{ij} \rvert, \\
> D(a_{ii}, R_{i}) & = \left\{ x \in \mathbb{C} \ |\ \lvert x - a_{ii} \rvert \leqslant R_{i} \right\}.\end{aligned}$$
> 那么$A$的每个特征值都落在某个$D(a_{ii}, R_{i})$中。

**习题2.3 第6题**.
设$S, T$是向量组。求证：$S$与$T$等价$\Longleftrightarrow$
$\operatorname{rank} S = \operatorname{rank} (S\cup T) = \operatorname{rank} T.$

**证明**： $\Longrightarrow$:
若$S$与$T$等价，则他们可以相互线性表出，那么根据上一题（习题2.2
第7题），有$\operatorname{rank} S \leqslant \operatorname{rank} T$,
以及$\operatorname{rank} T \leqslant \operatorname{rank} S$.
所以必须有$\operatorname{rank} S = \operatorname{rank} T.$
对于向量组$S\cup T,$ 它里面的每一个向量，要么属于$S$, 要么属于$T$,
都可以用$S$的向量线性表出。反之，$S$中每一个向量显然可以用向量组$S\cup T$的向量线性表出。所以向量组$S$与$S\cup T$线性等价，从而有$\operatorname{rank} S = \operatorname{rank} (S\cup T).$

$\Longleftarrow$: 令向量组$S\cup T$的秩为$r$.
任取$S$的一个极大线性无关组，记为$\alpha_1, \ldots, \alpha_r$.
那么它们也是向量组$S\cup T$中的$r$个线性无关的的向量，根据习题2.2
第6题第(1)小题的结论，$\alpha_1, \ldots, \alpha_r$是向量组$S\cup T$的一个极大线性无关组，从而可以线性表出其中每一个向量。$T$作为$S\cup T$的一个子集，其中每一个向量也能被$\alpha_1, \ldots, \alpha_r$线性表出。所以$T$能被$S$线性表出。

同样地可以证明$S$能被$T$线性表出。二者可以相互线性表出，所以它们是线性等价的。

**习题2.3 第7题**. 求证：两个齐次线性方程组(I),
(II)同解的充分必要条件是他们互为线性组合。

**证明**： 考虑齐次线性方程组$A_1X = 0$与$A_2X = 0,$
其中$A_1, A_2$分别是$m_1\times n$与$m_2\times n$的矩阵。将$A_1, A_2$的行向量组分别记作$S_1, S_2$,
那么线性方程组$\begin{pmatrix}A_1 \\ A_2\end{pmatrix} X = 0$的行向量组即为$S_1 \cup S_2$.
对于齐次线性方程组，我们知道
$$\left( \begin{pmatrix}A_1 \\ A_2\end{pmatrix} X = 0 \text{ 的解空间 } \right) = \left( A_1 X = 0 \text{ 的解空间 } \right) \cap \left( A_2X = 0 \text{ 的解空间 } \right)$$
那么 $$\begin{aligned}
& ~~ A_1X = 0 \text{ 与 } A_2X = 0 \text{ 同解 } \\
\Longleftrightarrow & ~~ A_1X = 0, A_2X = 0, \begin{pmatrix}A_1 \\ A_2\end{pmatrix} X = 0 \text{ 同解 } \\
\Longleftrightarrow & ~~ \operatorname{rank} S_1 = \operatorname{rank} (S_1 \cup S_2) = \operatorname{rank} S_2 \\
\Longleftrightarrow & ~~ S_1, S_2 \text{ 线性等价 }\end{aligned}$$
最后一个等价是根据习题2.3 第6题。倒数第二个等价的解释如下：

$\begin{pmatrix}A_1 \\ A_2\end{pmatrix} X = 0$的解空间是$A_1X = 0$(或$A_2X = 0$)的子空间，其维数分别为$n - \operatorname{rank} (S_1\cup S_2)$以及$n - \operatorname{rank} S_1$(或者$n - \operatorname{rank} S_2$)。一个线性空间与它的一个子空间相等，当且仅当他们维数是相等的，即
$$n - \operatorname{rank} (S_1\cup S_2) = n - \operatorname{rank} S_1 ~~ (\text{或} ~~ n - \operatorname{rank} S_2),$$
即
$$\operatorname{rank} (S_1\cup S_2) = \operatorname{rank} S_1 ~~ (\text{或} ~~ \operatorname{rank} S_2).$$
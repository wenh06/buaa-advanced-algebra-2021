---
date: 2022-10-7 第三次习题课
title: 2022秋高等代数习题课
---

非空集合$A$到$B$的映射$f: A \to B$指的是某种规则，使得对于$A$中的元素$x$,
有$B$中的唯一的一个元素与之对应，记作$f(x)\in B$.
对于映射，我们要掌握的概念主要由

-   单射：$B$中元素的原像至多有一个，即
    $$f(x_1) = f(x_2) \Longrightarrow x_1 = x_2.$$

-   满射：$B$中每个元素都至少有一个原像，即
    $$\forall y\in B, \exists x\in A, \text{ 使得 } f(x) = y.$$

-   双射（一一映射）：同时是单射与满射的映射，即集合$A, B$在规则$f$下有一一对应：
    $$\forall y\in B, \exists! x\in A, \text{ 使得 } f(x) = y.$$

线性空间在集合之上加了一些结构（加法，数乘），因此在大部分时候，我们考察的线性空间之间的映射的范围要缩小一些，即这个映射不仅仅是集合之间的映射，还要求它保持线性空间的结构。我们把满足保持线性空间结构的映射就称之为线性空间之间的同态映射（homomorphism），意思就是保持（homo
$\to$ same）形态（morph $\to$
shape）的映射，也称作线性映射。书上的线性映射的条件可以合并为一个
$$f(\lambda_1 x_1 + \lambda_2 x_2) = \lambda_1 f(x_1) + \lambda_2 f(x_2).$$

关于线性映射$f: A \to B$的核（kernel），像（image）等概念和性质，可以用下面的交换图表总结（只要了解，不要求掌握）：

$$\begin{tikzcd}[row sep = huge]
& & {\color{cyan} K'} \arrow[d, "i'"', cyan] \arrow[ld, dashed, "\exists ! j_1"', cyan] \arrow[rd, "f\circ i' = 0"', near start, cyan] & {\color{brown} C'} \\
0 \arrow[r] & {\color{red} K} \arrow[r, "i", "{\color{red} \ker (f)}"'] & A \arrow[r, "f"] \arrow[d, "\bar{p}"'] \arrow[ur, "p'\circ f = 0"', near end, brown] & B \arrow[r, "p", "{\color{red} \operatorname{coker} (f)}"'] \arrow[u, "p'"', brown] & {\color{red} C} \arrow[r] \arrow[lu, dashed, "\exists ! j_2"', brown] & 0 \\
& & {\color{red} \operatorname{coker} (i) =: \operatorname{coim} (f)} \arrow[r, dashed, "\exists ! \bar{f}"'] \arrow[d] & {\color{red} \operatorname{im} (f) := \ker (p)} \arrow[u, "\bar{i}"'] \\[-5ex]
& & 0 & 0 \arrow[u]
\end{tikzcd}$$

**第一题**.
设$V_1, V_2$是$\mathbb{F}$上线性空间，$f$是$V_1$到$V_2$的一个同构映射，证明$f^{-1}$是$V_2$到$V_1$的同构映射。

**证明**：
首先，由于$f$是$V_1$到$V_2$的一个同构映射，那么它是一个一一映射，故$f^{-1}$也是一一映射。接下来，我们只要证明$f^{-1}$是一个线性空间之间的同态映射即可。任取$\beta_1, \beta_2 \in V_2,$
设$\alpha_1, \alpha_2 \in V_1$分别为$\beta_1, \beta_2$在$f$下的（唯一的）原像。那么任取两个数$\lambda_1, \lambda_2,$
由于$f$是线性空间的同态映射，所以有
$$f(\lambda_1 \alpha_1 + \lambda_2 \alpha_2) = \lambda_1 f(\alpha_1) + \lambda_2 f(\alpha_2) = \lambda_1 \beta_1 + \lambda_2 \beta_2.$$
由于$f$是一一映射，所以$\lambda_1 \beta_1 + \lambda_2 \beta_2$的在$f$下的原像即是$\lambda_1 \alpha_1 + \lambda_2 \alpha_2.$
那么
$$f^{-1}(\lambda_1 \beta_1 + \lambda_2 \beta_2) = \lambda_1 \alpha_1 + \lambda_2 \alpha_2 = \lambda_1 f^{-1}(\beta_1) + \lambda_2 f^{-1}(\beta_2).$$

**习题2.8 第3题**. 求多项式$f(x)$使$f(1) = 1, f(2) = 2, f(3) = 4.$
这样的多项式$f(x)$是否可能是整系数多项式？

**解**： 一般给定$n$个点$(x_1,y_1), \dots, (x_n,y_n)$，
其中$x_1, \cdots, x_n$互不相同，则有拉格朗日插值多项式
$$\begin{gathered}
L(x) = \sum_{i=1}^{n}y_{i}\ell_{i}(x) \\
\text{其中， } \ell_{i}(x) = \prod_{\begin{smallmatrix}1\leq \leq k \\ j\neq i\end{smallmatrix}}{\frac {x-x_{j}}{x_{i}-x_{j}}}={\frac {(x-x_{0})}{(x_{i}-x_{0})}}\cdots {\frac {(x-x_{i-1})}{(x_{i}-x_{i-1})}}{\frac {(x-x_{i+1})}{(x_{i}-x_{i+1})}}\cdots {\frac {(x-x_{n})}{(x_{i}-x_{n})}},\end{gathered}$$
满足$L(x_i) = y_i, i=1, \dots ,n$。本题对应的拉格朗日插值多项式为$f(x) = L(x) = \dfrac{1}{2}x^2 - \dfrac{1}{2}x + 1$.
这是之前习题课讲过的知识。当然也存在更高次多项式满足题目条件，例如$(x-1)^n(x-2)^m(x-3)^k + L(x)$.

假设存在整系数的多项式$f(x)$满足题设条件，那么考察$g(x) = f(x) - L(x).$
由于$1, 2, 3$是$g(x)$的根，于是存在多项式$h(x)$使得
$$g(x) = f(x) - L(x) = (x-1)(x-2)(x-3) h(x)$$ 于是在$\mathbb{R}[X]$中有
$$f(x) \equiv L(x) \mod (x-1)(x-2)(x-3)$$
由于$f(X)$在$\mathbb{R}[x]$中利用辗转相除法除以$(x-1)(x-2)(x-3)$所得的商多项式与余多项式都是整系数的，所以上式不可能成立。

**第三题**. 已知$\mathbb{F}$上线性空间$V$的有限个真子空间之并不等于$V.$
若$\dim(V) = n,$
$V_1, \ldots, V_s$是$V$的$s$个真子空间。证明$\displaystyle V \setminus \bigcup_{i=1}^s V_i$中包含$V$的一组基。

**证明**： 由于$\displaystyle \bigcup_{i=1}^s V_i \subsetneq V$,
所以可以从$V \setminus \bigcup_{i=1}^s V_i \neq \emptyset$中取到至少一个（非零）向量，记作$\alpha_1.$
令$W_1 = \operatorname{span}_{\mathbb{F}}\{\alpha_1\},$
那么$W_1$是$V$的真子空间。于是，我们可以从$V \setminus \left( W_1 \cup \left( \bigcup_{i=1}^s V_i \right) \right) \neq \emptyset$中取到（非零）向量$\alpha_2,$
并令$W_2 = \operatorname{span}_{\mathbb{F}}\{\alpha_1, \alpha_2\}$.
由于$\alpha_2 \not\in W_1$, 所以$\dim W_2 = 2$.

依此方法，我们可以取到$\alpha_1, \alpha_2, \ldots, \alpha_{n-1}$,
以及相应的$W_i = \operatorname{span}_{\mathbb{F}}\{\alpha_1, \ldots, \alpha_i\}, \dim (W_i) = i, i=1, \ldots, n-1$.
最后考察$V \setminus \left( W_{n-1} \cup \left( \bigcup_{i=1}^s V_i \right) \right) \neq \emptyset,$
从这个集合中取（非零）向量$\alpha_n$.
这样我们就得到了$V$的一组基$\alpha_1, \ldots, \alpha_n.$

**第四题**. 给定$n$元排列$(j_1j_2\cdots j_n),$
若$\tau(j_1j_2\cdots j_n) = r,$
求$n$元排列$(j_n\cdots j_2j_1)$的逆序数$\tau(j_n\cdots j_2j_1)$.

**解**：
一个$n$元排列的序关系总共有$n(n-1)/2$对。排列$(j_1j_2\cdots j_n)$中的顺序关系是排列$(j_n\cdots j_2j_1)$中的逆序关系；排列$(j_1j_2\cdots j_n)$中的逆序关系是排列$(j_n\cdots j_2j_1)$中的顺序关系。因此
$$\tau(j_n\cdots j_2j_1) = n(n-1)/2 - \tau(j_1j_2\cdots j_n) = n(n-1)/2 - r.$$

**习题2.1 第7题**. (1).
若$\alpha_1, \ldots, \alpha_n$线性无关，问$\alpha_1 + \alpha_2, \alpha_2 + \alpha_3, \ldots, \alpha_{n-1} + \alpha_n, \alpha_n + \alpha_1$是否一定线性无关？为什么？

(2).
若$\alpha_1, \ldots, \alpha_n$线性相关，问$\alpha_1 + \alpha_2, \alpha_2 + \alpha_3, \ldots, \alpha_{n-1} + \alpha_n, \alpha_n + \alpha_1$是否一定线性相关？为什么？

**解**： 考虑
$$\lambda_1 (\alpha_1+\alpha_2) + \lambda_2 (\alpha_2+\alpha_3) + \cdots + \lambda_n (\alpha_n+\alpha_1) = 0$$
$\lambda_1, \cdots, \lambda_n\in\mathbb{R}$, 变形为
$$(\alpha_1, \cdots, \alpha_n)
\underbrace{\begin{pmatrix}
1 & 0 & \cdots & \cdots & 0 & 1 \\
1 & 1 & 0 & & & 0 \\
0 & 1 & 1 & \ddots & & \vdots \\
\vdots & \ddots & \ddots & \ddots & \ddots & \vdots \\
\vdots & & \ddots & \ddots & \ddots & 0 \\
0 & \cdots & \cdots & 0 & 1 & 1
\end{pmatrix}
\begin{pmatrix}
\lambda_1 \\ \vdots \\ \lambda_n
\end{pmatrix}
}_{\text{记为} A \lambda}= 0$$
我们考虑齐次线性方程组$A\lambda = 0$的解的情况。对系数矩阵$A$进行从上往下进行上一行乘以-1加到下一行的操作，有
$$A = \begin{pmatrix}
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

**习题2.1 第8题**.
设复数域上的向量$\alpha_1, \ldots, \alpha_n$线性无关。$\lambda$取什么复数值的时候，向量$\alpha_1 - \lambda \alpha_2, \alpha_2 - \lambda \alpha_3, \ldots, \alpha_{n-1} - \lambda \alpha_n, \alpha_n - \lambda \alpha_1$线性无关？

**解**： 类似上一题习题2.1 第7题，将问题写为
$$(\alpha_1, \cdots, \alpha_n)
\underbrace{\begin{pmatrix}
1 & 0 & \cdots & \cdots & 0 & -\lambda \\
-\lambda & 1 & 0 & & & 0 \\
0 & -\lambda & 1 & \ddots & & \vdots \\
\vdots & \ddots & \ddots & \ddots & \ddots & \vdots \\
\vdots & & \ddots & \ddots & \ddots & 0 \\
0 & \cdots & \cdots & 0 & -\lambda & 1
\end{pmatrix}
\begin{pmatrix}
z_1 \\ \vdots \\ z_n
\end{pmatrix}
}_{\text{记为} Az}= 0$$
$z_1, \cdots, z_n \in \mathbb{C}$.对系数矩阵$A$进行从上往下进行上一行乘以$\lambda$加到下一行的操作，有
$$A = \begin{pmatrix}
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
若$\alpha_1,\cdots,\alpha_n$线性无关，则只需要$1-\lambda^{n} \neq 0$，即$\lambda$不取$n$次单位根$e^{2k\pi i/n},$
$k = 0, \ldots, n-1,$
即可使$\alpha_1-\lambda\alpha_2,\cdots,\alpha_n-\lambda\alpha_1$线性无关。

**习题2.5 第4题**.
设向量组$S = \{ \alpha_1, \ldots, \alpha_s \}$线性无关，并且可以由向量组$T = \{ \beta_1, \ldots, \beta_t \}$线性表出。求证：

\(1\) 向量组$T$与向量组$S \cup T$等价。

\(2\)
将$S$扩充为$S \cup T$的一个极大线性无关组$T_1 = \{ \alpha_1, \ldots, \alpha_s, \beta_{i_1}, \ldots, \beta_{i_k} \},$
则$T_1$与$T$线性等价，且$s+k \leqslant t.$

\(3\) (Steinitz替换定理)
可以用向量$\alpha_1, \ldots, \alpha_s$替换向量$\beta_1, \ldots, \beta_t$中某$s$个向量$\beta_{i_1}, \ldots, \beta_{i_s},$
使得得到的向量组$\{ \alpha_1, \ldots, \alpha_s, \beta_{i_{s+1}}, \ldots, \beta_{i_t} \}$与$\{ \beta_1, \ldots, \beta_t \}$等价。

**证明**： (1) 首先，向量组$S\cup T$显然能线性表出它的子集$T$.
另一方面，由于向量组$T$能线性表出向量组$S,$
所以向量组$T = T\cup T$能线性表出向量组$S\cup T.$
于是向量组$T$与向量组$S \cup T$能够相互线性表出，从而是线性等价的。

\(2\) **注意！这里$T_1$不是$T$的子集！**

由线性等价的传递性，我们只要证明向量组$T_1$与向量组$S \cup T$线性等价即可。由于$T_1$是$S \cup T$的子集，我们只要证明$S \cup T$能被$T_1$线性表出即可。更进一步，只要证明任取向量$\gamma \in (S \cup T) \setminus T_1,$
有$\gamma$能被$T_1$中的向量线性表出即可。假设不然，则存在不全为0的数$\lambda_0, \lambda_1, \ldots, \lambda_{s+k},$
使得
$$0 = \lambda_0 \gamma + \lambda_1 \alpha_1 + \cdots + \lambda_s \alpha_s + \lambda_{s+1} \beta_{i_1} + \cdots + \lambda_{s+k} \beta_{i_k}$$
$\lambda_0$不能为0，否则会与$T_1$是线性无关组矛盾，于是
$$\gamma = -\dfrac{\lambda_1}{\lambda_0} \alpha_1 - \cdots - -\dfrac{\lambda_s}{\lambda_0} \alpha_s - \dfrac{\lambda_{s+1}}{\lambda_0} \beta_{i_1} - \cdots - \dfrac{\lambda_{s+k}}{\lambda_0} \beta_{i_k}$$
于是我们就证明了$T_1$, $S \cup T$, $T$是线性等价的，那么它们的秩就都相等
$$s+k = \operatorname{rank}(T_1) = \operatorname{rank}(T) \leqslant \# T = t.$$

\(3\)
我们利用第(2)问中的结论，将$S$扩充为$S \cup T$的一个极大线性无关组$T_1$,
设其元素个数为$s+k.$
我们从$T$中不在$T_1$中的向量（总共有$t - k \geqslant s$个）随意挑出$s$个，那么剩下的向量与$S$并在一起得到的向量组，记作$T_2,$就满足
$$T_1 \subseteq T_2 \subseteq S \cup T.$$
因为$T_1$是$S \cup T$的极大线性无关组，所以$T_1, T_2, S \cup T$三者线性等价，从而与$T$线性等价。

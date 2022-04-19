# 2022.4.1 课外作业

**第一题**.
设$\mathscr{A}$是$n$维向量空间$V$的一个线性变换。对于$V$的一组基$\alpha_1, \alpha_2, \ldots, \alpha_n$和$\alpha = x_1\alpha_1 + \cdot + x_n\alpha_n$,
有 $$\mathscr{A}\alpha = x_n\alpha_1 + \cdot + x_1\alpha_n,$$
判断$\mathscr{A}$是否可对角化，并证明你的结论。

**解**:
设$\lambda$为$\mathscr{A}$的一个特征值，$\sum\limits_{i=1}^n x_i \alpha_i \neq 0$为对应的特征向量，即$x_1,\ldots,x_n$不全为0，且有
$$\lambda(\sum\limits_{i=1}^n x_i \alpha_i) = \mathscr{A}(\sum\limits_{i=1}^n x_i \alpha_i) = \sum\limits_{i=1}^n x_{n+1-i} \alpha_i.$$
于是有 $$\begin{cases}
\lambda x_i = x_{n+1-i} \\
\lambda x_{n+1-i} = x_i \\
\lambda \neq 0,
\end{cases}$$ 解得$\lambda = \pm 1$.

于是，当$n$为偶数时，$\mathscr{A}$对应于特征值$\lambda = 1$有$\dfrac{n}{2}$个特征向量$\alpha_i + \alpha_{n+1-i}, ~ i = 1, \ldots, \dfrac{n}{2},$
$\mathscr{A}$对应于特征值$\lambda = -1$有$\dfrac{n}{2}$个特征向量$\alpha_i - \alpha_{n+1-i}, ~ i = 1, \ldots, \dfrac{n}{2}.$
所以此时$\mathscr{A}$可以对角化。

当$n$是奇数的时候，$\mathscr{A}$对应于特征值$\lambda = 1$有$\dfrac{n+1}{2}$个特征向量$\alpha_i + \alpha_{n+1-i}, ~ i = 1, \ldots, \dfrac{n-1}{2},$
以及$\alpha_{(n+1)/2}$。$\mathscr{A}$对应于特征值$\lambda = -1$有$\dfrac{n-1}{2}$个特征向量$\alpha_i - \alpha_{n+1-i}, ~ i = 1, \ldots, \dfrac{n-1}{2}.$
所以此时$\mathscr{A}$也可以对角化。

解法二：$\mathscr{A}$在这组基$\alpha_1, \alpha_2, \ldots, \alpha_n$下的矩阵表示为$A = \begin{pmatrix} & & 1 \\ & \reflectbox{$\ddots$} & \\ 1 & & \end{pmatrix}$,
那么
$$\lambda I - A = \begin{pmatrix} \lambda & & & & & -1 \\ & \ddots & & & \reflectbox{$\ddots$} & \\ & & \lambda & -1 & & \\ & & -1 & \lambda & & \\ & \reflectbox{$\ddots$} & & & \ddots & \\ -1 & & & & & \lambda \end{pmatrix}, \quad \text{$n$为偶数,}$$
或者
$$\lambda I - A = \begin{pmatrix} \lambda & & & & & & -1 \\ & \ddots & & & & \reflectbox{$\ddots$} & \\ & & \lambda & & -1 & & \\ & & & {\color{red} \lambda - 1} & & & \\ & & -1 & & \lambda & & \\ & \reflectbox{$\ddots$} & & & & \ddots & \\ -1 & & & & & & \lambda \end{pmatrix}, \quad \text{$n$为奇数.}$$
可以算得 $$\det (\lambda I - A) = \begin{cases}
(\lambda+1)^{\frac{n}{2}}(\lambda-1)^{\frac{n}{2}}, & \text{$n$为偶数,} \\
(\lambda+1)^{\frac{n-1}{2}}(\lambda-1)^{\frac{n+1}{2}}, & \text{$n$为偶数,}
\end{cases}$$ 解得特征值为$\pm 1$.
通过解对应的特征方程得到和前一种解法一样的特征向量。

解法三：容易看出$\mathscr{A}^2$是恒等映射，即$\mathscr{A}^2 = \mathscr{I}$,
所以$\mathscr{A}$的一个零化多项式为$f(\lambda) = \lambda^2 - 1$,
它没有重根，所以$\mathscr{A}$的极小多项式也没有重根，所以$\mathscr{A}$可以对角化。

**第二题**.
记$J_n(0) = \begin{pmatrix} 0 & 1 & & \\ & 0 & \ddots & \\ & & \ddots & 1 \\ & & & 0 \end{pmatrix}_{n\times n}$.
若$A$是$n$阶幂零矩阵，且幂零指数为$n$.
证明$A$与$J_n(0)$相似，并求出$A$的最小多项式和特征多项式。

**解**: 由于$A^{n-1} \neq 0$, 所以存在$\alpha \in \mathbb{F}^n$,
$\alpha \neq 0$, 使得$A^{n-1} \alpha \neq 0$.
考虑向量组$A^{n-1} \alpha, \ldots, A\alpha, \alpha$,
假若它们线性相关，则存在一组不全为$0$的数$\lambda_0, \ldots, \lambda_{n-1}$使得$\lambda_0 \alpha + \cdots + \lambda_{n-1} A^{n-1} \alpha = 0$.
那么
$$0 = A^{n-1}(\lambda_0 \alpha + \cdots + \lambda_{n-1} A^{n-1} \alpha) = \lambda_0 A^{n-1} \alpha + \lambda_1 A^{n} \alpha + \cdots + \lambda_{n-1} A^{2n-2} \alpha = \lambda_0 A^{n-1} \alpha,$$
从而必须有$\lambda_0 = 0$.
依次可推出$\lambda_1 = \cdots = \lambda_{n-1} = 0$.
于是假设不成立，向量组$A^{n-1} \alpha, \ldots, A\alpha, \alpha$线性无关，构成了$\mathbb{F}^n$的一组基。$A$在这组基下的矩阵表示即为$J_n(0)$.
$A$的极小多项式与特征多项式都是$f(\lambda) = \lambda^n$.

**第三题**.
若$A$相似于$J_1 = \begin{pmatrix} J_{m_1}(0) & & \\ & \ddots & \\ & & J_{m_s}(0) \end{pmatrix}$和$J_2 = \begin{pmatrix} J_{n_1}(0) & & \\ & \ddots & \\ & & J_{n_t}(0) \end{pmatrix}$,
证明$s=t$,
并且适当调整顺序后可使得$J_{n_1}(0), \ldots, J_{n_s}(0)$与$J_{m_1}(0), \ldots, J_{m_s}(0)$相等（即$\{ m_1, \ldots, m_s \} = \{ n_1, \ldots, n_s \}$）。

**证明**: 由于$s = \dim (\ker (0 I - J_1))$,
$t = \dim (\ker (0 I - J_2))$
为特征值$0$对应的特征空间的维数，而$J_1, J_2$都相似于$A$, 所以
$$s = t = \dim(\ker (0 I - A)) = \dim(\ker A).$$

由于$A, J_1, J_2$相似，所以$\forall k \in \mathbb{N}$, 有
$$\operatorname{rank} A^k = \operatorname{rank} J_1^k = \operatorname{rank} J_2^k.$$
对于$r$阶Jordan块$J_r(0)$,
有$\operatorname{rank} J_r(0)^k = \max \{ 0, r-k \}$, 进而有
$$\operatorname{rank} J_1^k = \sum_{i=1}^s \max \{ 0, m_i-k \}, \quad \operatorname{rank} J_1^k = \sum_{i=1}^s \max \{ 0, n_i-k \}.$$
他们的二阶差分分别为（$k\geqslant 1$） $$\begin{aligned}
D_1(k) & := \operatorname{rank} J_1^{k+1} + \operatorname{rank} J_1^{k-1} - 2 \operatorname{rank} J_1^{k} = \# \{ i \ |\ 1 \leqslant i \leqslant s, ~ m_i = k \} \\
D_2(k) & := \operatorname{rank} J_2^{k+1} + \operatorname{rank} J_2^{k-1} - 2 \operatorname{rank} J_2^{k} = \# \{ i \ |\ 1 \leqslant i \leqslant s, ~ n_i = k \}\end{aligned}$$
于是对于任意$k\geqslant 1$都有
$$\# \{ i \ |\ 1 \leqslant i \leqslant s, ~ m_i = k \} = D_1(k) = D_2(k) = \# \{ i \ |\ 1 \leqslant i \leqslant s, ~ n_i = k \}$$
所以存在$s$阶对称群中的一个元素$\sigma$,
使得$\sigma(m_1, \cdots, m_s) = (n_1, \cdots, n_s)$,
即在不计一个置换作用的意义下，$A$的Jordan标准形是唯一的。

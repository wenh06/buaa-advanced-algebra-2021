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
$$s = t = \dim(\ker (0 I - A)) = \dim(\ker A)$$

令$J_1, J_2$对应的空间的（循环）分解分别为$V_1\oplus V_2 \oplus \cdots \oplus V_s$与$W_1\oplus W_2 \oplus \cdots \oplus W_s$.
那么对于$V_1$, 有直和分解
$$V_1 = V_1 \cap \mathbb{F}^n = V_1 \cap (W_1\oplus W_2 \oplus \cdots \oplus W_s) = (V_1 \cap W_1) \oplus \cdots \oplus (V_1 \cap W_s)$$
如果上式右边有至少2个空间$V_1 \oplus W_i, V_1 \oplus W_j, i\neq j$,
是非平凡的，那么$J_{m_1}(0), m_1\geqslant 2$,
就可以准对角化，但这是不可能的。于是存在$i_1 \in \{1, \ldots, s\}$,
使得$V_1 = W_{i_1}$. 同理可知，对于$V_2, \ldots, V_s$,
都分别存在$i_2, \ldots, i_s$,
使得$V_2 = W_{i_2}, \ldots, V_s = W_{i_s}$,
而且这些$i_1, i_2, \ldots, i_s$显然都是互异的，即$\{i_1, \ldots, i_s\} = \{1, 2, \ldots, s\}$。因此
$$m_j = \dim V_j = \dim W_{i_j} = n_{i_j}, \quad j = 1, 2, \ldots, s,$$
从而适当调换顺序之后有 $$(m_1, \ldots, m_s) = (n_1, \ldots, n_s)$$
或者更准确来说，是
$$(m_1, \ldots, m_s) = \begin{pmatrix} 1 2 \cdots s \\ i_1 i_2 \cdots i_s \end{pmatrix} (n_1, \ldots, n_s).$$

注：关于$J_{r}(0), r \geqslant 2$不能准对角化的证明：

假设$J_{r}(0)$可以准对角化为$\begin{pmatrix} M_1 & \\ & M_2 \end{pmatrix}$,
那么$M_1, M_2$都只有特征值$0$.
于是$M_1, M_2$可以通过循环分解，分解为对角线元素都是$0$的上三角矩阵，即
$$\begin{aligned}
J_{r}(0) & = \begin{pmatrix} Q_1 & \\ & Q_2 \end{pmatrix} \begin{pmatrix} M_1 & \\ & M_2 \end{pmatrix} \begin{pmatrix} Q_1^{-1} & \\ & Q_2^{-1} \end{pmatrix} \\
& = \begin{pmatrix} Q_1 & \\ & Q_2 \end{pmatrix} \begin{pmatrix} P_1^{-1} & \\ & P_2^{-1} \end{pmatrix} \begin{pmatrix} P_1M_1P_1^{-1} & \\ & P_2M_2P_2^{-1} \end{pmatrix} \begin{pmatrix} P_1 & \\ & P_2 \end{pmatrix} \begin{pmatrix} Q_1^{-1} & \\ & Q_2^{-1} \end{pmatrix} \\
& = \begin{pmatrix} Q_1 & \\ & Q_2 \end{pmatrix} \begin{pmatrix} P_1^{-1} & \\ & P_2^{-1} \end{pmatrix} \begin{pmatrix} \begin{pmatrix} 0 & & \ast \\ & \ddots & \\ & & 0 \end{pmatrix} & \\ & \begin{pmatrix} 0 & & \ast \\ & \ddots & \\ & & 0 \end{pmatrix} \end{pmatrix} \begin{pmatrix} P_1 & \\ & P_2 \end{pmatrix} \begin{pmatrix} Q_1^{-1} & \\ & Q_2^{-1} \end{pmatrix}\end{aligned}$$
比较两边的秩可知上式不可能成立。
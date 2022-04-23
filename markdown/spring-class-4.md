**第一题**. 对于$\mathscr{A} \in \mathcal{L}(\mathbb{F}^3),$
若$\mathscr{A}$在基$\alpha_1 = \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}$,
$\alpha_2 = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}$,
$\alpha_3 = \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix}$下的矩阵为$A = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ -1 & 2 & 1 \end{pmatrix}$,
证明：

(1). $\mathscr{A}$是可逆线性变换；

(2).
求$\mathscr{A}$在基$\varepsilon_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$,
$\varepsilon_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$,
$\varepsilon_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$下的矩阵。

**证明**. (1).
要证明$\mathscr{A}$是可逆线性变换，只要证$\det A \neq 0$即可：
$$\det A = \begin{vmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ -1 & 2 & 1 \end{vmatrix} = \begin{vmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ -2 & 2 & 0 \end{vmatrix} = \begin{vmatrix} 0 & 0 & 1 \\ 1 & 1 & 0 \\ -2 & 2 & 0 \end{vmatrix} = (-1)^4 \begin{vmatrix} 1 & 1 \\ -2 & 2 \end{vmatrix} = 4 \neq 0.$$

(2).
由已知条件，$\mathscr{A}(\alpha_1,\alpha_2,\alpha_3) = (\alpha_1,\alpha_2,\alpha_3) A$.
令$(\alpha_1,\alpha_2,\alpha_3)$到$(\varepsilon_1,\varepsilon_2,\varepsilon_3)$的过渡矩阵为$P$,
即$(\varepsilon_1,\varepsilon_2,\varepsilon_3) = (\alpha_1,\alpha_2,\alpha_3) P$,
那么
$$\mathscr{A}(\varepsilon_1,\varepsilon_2,\varepsilon_3) = \mathscr{A}(\alpha_1,\alpha_2,\alpha_3) P = (\alpha_1,\alpha_2,\alpha_3) AP = (\varepsilon_1,\varepsilon_2,\varepsilon_3) P^{-1}AP.$$
容易看出$P^{-1} = \begin{pmatrix} -1 & 1 & 1 \\ 1 & -1 & 1 \\ 1 & 1 & -1 \end{pmatrix}$,
利用$P = (P^{-1})^{-1} = \dfrac{1}{\det P^{-1}} (P^{-1})^{\ast}$解得$P = \dfrac{1}{4} \begin{pmatrix} 0 & 2 & 2 \\ 2 & 0 & 2 \\ 2 & 2 & 0 \end{pmatrix}$,
所以$\mathscr{A}$在基$\varepsilon_1$, $\varepsilon_2$,
$\varepsilon_3$下的矩阵为
$$P^{-1}AP = \dfrac{1}{2} \begin{pmatrix} -1 & 1 & 1 \\ 1 & -1 & 1 \\ 1 & 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ -1 & 2 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix} = \dfrac{1}{2} \begin{pmatrix} 3 & -1 & 2 \\ 3 & 1 & 0 \\ -1 & 3 & 2 \end{pmatrix}$$

**第二题**.
在向量空间$V = \mathbb{F}[x]$中定义线性变换$\mathscr{A, B}$如下：
$$\mathscr{A}(f(x)) = f'(x), ~ \mathscr{B}(f(x)) = xf(x), \quad \forall f(x) \in V.$$
对于$W = \mathbb{F}_n[x] = \{ a_nx^n + \cdots + a_1x + a_0 \ |\ a_i\in\mathbb{F},~ 0 \leqslant i \leqslant n \}$

(1). 证明$W$是$\mathscr{BA}$的不变子空间；

(2).
求$\operatorname{Im}((\mathscr{BA})^n)$和$\ker((\mathscr{BA})^n)$的维数与一组基。

**解**：这是课本上的原题。

(1). 任取$f(x) \in V$,
有$\mathscr{BA}(f(x)) = \mathscr{B}(\mathscr{A}(f(x))) = \mathscr{B}(f'(x)) = xf'(x)$.
令$f(x) = a_nx^n + \cdots + a_1x + a_0 \in W$,
那么$\mathscr{BA}(f(x)) = na_nx^n + \cdots + a_1x \in W$.
所以$W$是$\mathscr{BA}$的不变子空间。

(2).
我们首先将$\mathscr{BA}$视作$W$上的线性变换。由$\mathscr{BA}(a_nx^n + \cdots + a_1x + a_0) = na_nx^n + \cdots + a_1x$容易看出$(\mathscr{BA})^n(a_nx^n + \cdots + a_1x + a_0) = n^na_nx^n + \cdots + a_1x$.

所以当$\operatorname{char}(\mathbb{F}) = 0$时，任取$g(x) = b_nx^n + \cdots + b_1x$,
总有$(\mathscr{BA})^n\left(\dfrac{b_n}{n^n} x^n + \cdots + b_1x\right) = g(x).$
于是
$$\operatorname{Im}((\mathscr{BA})^n) = \{ a_nx^n + \cdots + a_1x \ |\ a_i\in\mathbb{F},~ 1\leqslant i \leqslant n \}$$
其维数为$n$, 基可取为$\{x^n, \ldots, x\}$.
$\ker((\mathscr{BA})^n)$维数为$1$，可取常值函数（多项式）$f(x) = 1$为其一组基。

当$\operatorname{char}(\mathbb{F}) = p$, $p$为某个素数时，有
$$(\mathscr{BA})^n(a_nx^n + \cdots + a_1x + a_0) = \sum_{\substack{1\leqslant k \leqslant n \\ p\nmid k}} k^n a_k x^k$$
此时有
$$\operatorname{Im}((\mathscr{BA})^n) = \left\{ \sum_{\substack{1\leqslant k \leqslant n \\ p\nmid k}} a_k x^k \ \middle|\ a_k\in\mathbb{F},~ 1\leqslant k \leqslant n, ~ p\nmid k \right\}$$
它的一组基可取为$\{ x^k \ |\ 1 \leqslant k \leqslant n, q\nmid k \}$,
维数等于$n - \left\lfloor \dfrac{n}{p} \right\rfloor$.
$\ker((\mathscr{BA})^n)$维数等于$\# (\{ 0 \} \cup \{ k \ |\ 1\leqslant k \leqslant n, ~ p\nmid k \}) = 1 + \left\lfloor \dfrac{n}{p} \right\rfloor.$
它的一组基可以取为$1, x^p, \ldots, x^{mp}$,
其中$m = \left\lfloor \dfrac{n}{p} \right\rfloor.$

若将$\mathscr{BA}$视作$V$上的线性变换，则以上关于核空间的论断不变。$\operatorname{char}(\mathbb{F}) = 0$时，象空间基为$\{x^m \ |\ m\in\mathbb{N}_+ \}$,
是一个无穷维线性空间。$\operatorname{char}(\mathbb{F}) = p$时象空间基为$\{ x^m \ |\ m\in\mathbb{N}_+, ~ p \nmid m \}$,
也是一个无穷维线性空间。

**第三题**. 在$V = M_n(\mathbb{F})$中定义变换$\sigma: X \mapsto AX$,
$\forall X\in V$,
其中$A = \begin{pmatrix} \lambda_1 & & \ast \\ & \ddots & \\ 0 & & \lambda_n \end{pmatrix}$,
$\lambda_1,\ldots,\lambda_n$两两不同。

(1). 证明$\sigma$是$V$上的线性变换；

(2). 判断$\sigma$能否对角化，并证明你的结论。

**解**：(1). 任取$a_1, a_2 \in \mathbb{F}$, $X_1, X_2 \in V$, 有
$$\sigma(a_1X_1 + a_2X_2) = A(a_1X_1 + a_2X_2) = a_1AX_1 + a_2AX_2 = a_1 \sigma(X_1) + a_2 \sigma(X_2).$$
所以$\sigma$是$V$上的线性变换。

\(2\)
由于$\lambda_1,\ldots,\lambda_n$两两不同，所以$A$可以对角化，即存在可逆方阵$P$,
使得$PAP^{-1} = \operatorname{diag}(\lambda_1, \ldots, \lambda_n) = \Lambda$.

设$\lambda$是$\sigma$的一个特征值，对应特征向量为$X$,
即$\sigma(X) = \lambda X$, 那么$P^{-1} \Lambda PX = \lambda X$,
等价于$\Lambda PX = \lambda PX$. 记$PX = (a_{ij})$, 那么有
$$\begin{pmatrix}
\lambda_1 a_{11} & \lambda_1 a_{12} & \cdots & \lambda_1 a_{1n} \\
\lambda_2 a_{21} & \lambda_2 a_{22} & \cdots & \lambda_2 a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
\lambda_n a_{n1} & \lambda_n a_{n2} & \cdots & \lambda_1 a_{nn} \\
\end{pmatrix}
= (\lambda a_{ij})$$
上式$\lambda = \lambda_i$的解有$E_{i1}, \ldots, E_{in}$,
$i = 1, \ldots, n$, 其中$E_{ij}$为第$(i,j)$位元素值为$1$,
其余位置值为$0$的$n$阶方阵。从而知$\sigma(X) = \lambda X$能解得$n$个特征值$\lambda_1, \ldots, \lambda_n$,
其中每个$\lambda_i$对应的特征向量有$n$个，为$P^{-1}E_{i1}, \ldots, P^{-1}E_{in}$,
$i = 1, \ldots, n$. 所以$\sigma$可以对角化。

**第四题**.
设$V$是$\mathbb{C}$上$n$维向量空间，$\mathscr{A}\in\mathcal{L}(V),$
且$\varphi_{\mathscr{A}}(\lambda) = (\lambda - \lambda_0)^m g(\lambda),$
$g(\lambda_0) \neq 0$.
用$W_{\lambda_0}$表示$V$的属于$\lambda_0$的根子空间，证明
$$W_{\lambda_0} = \{ g(\mathscr{A})\alpha \ |\ \alpha \in V \}.$$

**证明**：习题课讲过类似的题目。任取$\alpha \in V$,
有$(\mathscr{A} - \lambda_0)^m g(\mathscr{A}) (\alpha) = \varphi_{\mathscr{A}}(\mathscr{A}) (\alpha) = 0$,
所以$W \supseteq \{ g(\mathscr{A})\alpha \ |\ \alpha \in V \}.$
下证$W \subseteq \{ g(\mathscr{A})\alpha \ |\ \alpha \in V \}.$

任取$\beta \in W_{\lambda_0}$,
那么存在非负整数$k$使得$(\mathscr{A} - \lambda_0)^k \beta = 0$.
我们希望找到某个$\alpha \in V$, 使得$g(\mathscr{A}) \alpha = \beta$.

由于多项式$(\lambda - \lambda_0)^m$,
$g(\lambda)$互素，所以存在多项式$u(\lambda), v(\lambda) \in \mathbb{F}[\lambda]$,
使得$u(\lambda)(\lambda-\lambda_0)^m + v(\lambda)g(\lambda) = 1.$ 那么
$$\beta = (u(\mathscr{A})(\mathscr{A}-\lambda_0)^m + v(\mathscr{A})g(\mathscr{A})) \beta = u(\mathscr{A})(\mathscr{A}-\lambda_0)^m \beta + g(\mathscr{A}) (v(\mathscr{A}) \beta)$$
下面我们证明$u(\mathscr{A})(\mathscr{A}-\lambda_0)^m \beta = 0$.
假设$k$是使得$(\mathscr{A} - \lambda_0)^k \beta = 0$成立的最小的非负整数。如果$k \leqslant m$,
则证明完毕。若$k > m$, 那么
$$(\mathscr{A}-\lambda_0)^{k-m} \beta = u(\mathscr{A})(\mathscr{A}-\lambda_0)^k \beta + g(\mathscr{A}) (\mathscr{A}-\lambda_0)^{k-m} (v(\mathscr{A}) \beta) = g(\mathscr{A}) (\mathscr{A}-\lambda_0)^{k-m} (v(\mathscr{A}) \beta)$$
若$k \geqslant 2m$,
则上式右边等于$\varphi_{\mathscr{A}}(\mathscr{A}) (\mathscr{A}-\lambda_0)^{k-2m} (v(\mathscr{A}) \beta) = 0.$
此时$k - m$也满足$(\mathscr{A} - \lambda_0)^{k-m} \beta = 0$,
与$k$的极小性矛盾。若$k < 2m$,
那么上式左右两边同时用$(\mathscr{A}-\lambda_0)^{2m-k}$作用, 有
$$(\mathscr{A}-\lambda_0)^m \beta = \varphi_{\mathscr{A}}(\mathscr{A}) (v(\mathscr{A}) \beta) = 0.$$
这也与$k > m$以及$k$的极小性的假设矛盾。所以必然有$k \leqslant m$.
于是，我们证明了$\beta = g(\mathscr{A}) (v(\mathscr{A}) \beta)$, 从而有
$$W_{\lambda_0} = \{ g(\mathscr{A})\alpha \ |\ \alpha \in V \}.$$

**第五题**.
设$A$是数域$\mathbb{F}$上$n$阶幂零矩阵，且$A$的最小多项式$d(\lambda) = \lambda^m, m\leqslant n$.
证明 $$r(A) \leqslant \dfrac{(m-1)n}{m}.$$

**证明**.
将$A$视作$\mathbb{F}$的代数闭包$\overline{\mathbb{F}}$上的矩阵，秩不改变。由于$A$是$n$阶幂零矩阵，所以$A$的Jordan标准形可以写为$\operatorname{diag}(J_{r_1}(0), \ldots, J_{r_s}(0))$.
由于$A$的最小多项式$d(\lambda) = \lambda^m$,
所以$\forall 1 \leqslant i \leqslant s$, 有$r_i \leqslant m$. 于是我们有
$$\begin{cases}
\operatorname{rank}(A) = \sum\limits_{i=1}^s \operatorname{rank} J_{r_i}(0) = \sum\limits_{i=1}^s r_i - 1, \\
\sum\limits_{i=1}^s r_i = n, \\
r_i \leqslant m, ~ \forall 1 \leqslant i \leqslant s.
\end{cases}$$
于是$\operatorname{rank} A = n - s \leqslant n - \dfrac{n}{m} = \dfrac{(m-1)n}{m}$.

我们以下说明，可以不用将$A$视作$\overline{\mathbb{F}}$上的矩阵，也有$A$相似于Jordan形$\operatorname{diag}(J_{r_1}(0), \ldots, J_{r_s}(0))$的结论。我们考虑$A$的有理标准形（或循环标准形）$\operatorname{diag}(C_{r_1}, \ldots, C_{r_s})$,
这些$C_{r_i}$是$A$的不变因子组$\lambda^{r_i}$的友阵。多项式$\lambda^{r_i}$的友阵是$\begin{pmatrix} 0 & & & 0 \\ 1 & \ddots & & \vdots \\ & \ddots & \ddots & \vdots \\ & & 1 & 0 \end{pmatrix}$,
这是一个Jordan块（或其转置）$J_{r_i}(0).$
因此$A$相似于Jordan形$\operatorname{diag}(J_{r_1}(0), \ldots, J_{r_s}(0))$.

**第六题**.
设$\mathscr{A}$是$n$维向量空间$V$的一个线性变换。对于$V$的一组基$\alpha_1, \alpha_2, \ldots, \alpha_n$和$\alpha = x_1\alpha_1 + \cdots + x_n\alpha_n$,
有 $$\mathscr{A}\alpha = x_n\alpha_1 + \cdots + x_1\alpha_n,$$
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

**第七题**.
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

**第八题**.
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

**第一题**.
设$A,B$为$n$阶实方阵，求证：若$A,B$在复数域$\mathbb{C}$上相似，则他们在实数域$\mathbb{R}$上相似。

**证明**.
：若$A,B$在复数域$\mathbb{C}$上相似，那么存在可逆的复矩阵$P = P_1 + i P_2 \in M_n(\mathbb{C})$
使得$P^{-1}BP = A$.
其中$P_1, P_2 \in M_n(\mathbb{R})$是实矩阵，但不一定可逆。由$P^{-1}BP = A$有$BP = PA$,
从而有$P_1A + i P_2A = BP_1 + i BP_2$, 所以有
$$P_1A = BP_1, \quad P_2A = BP_2$$
考虑实系数多项式$f(\lambda) = \det (P_1 + \lambda P_2)$.
由于$f(i) = \det (P_1 + i P_2) = \det P \neq 0$,
所以$f(\lambda)$是非平凡的实系数多项式，从而存在$\lambda_0 \in \mathbb{R}$,
使得$f(\lambda_0) \neq 0$.
令$P' = P_1 + \lambda_0 P_2 \in M_n(\mathbb{R})$,
那么$\det P' = f(\lambda_0) \neq 0$, $P'$是可逆的实矩阵，而且有
$$P'A = P_1A + \lambda_0 P_2A = BP_2 + \lambda_0 BP_2 = BP'$$
从而有$P'^{-1}BP' = A$, 即$A,B$在实数域$\mathbb{R}$上也是相似的。

**第二题**. 设$A \in M_n (\mathbb{F})$, 并且$A^2 = I$.
证明$A$相似于矩阵$B = \begin{pmatrix} I_r & \\ & -I_s \end{pmatrix}$,
其中$r+s=n$.

**证明**：由于$A^2 = I$,
所以$f(\lambda) = \lambda^2 - 1 = (\lambda + 1) (\lambda - 1)$是$A$的一个零化多项式。若$A$的极小多项式是$\lambda + 1$,
那么$A = -I_n$; 若$A$的极小多项式是$\lambda - 1$, 那么$A = I_n$.
若$A$的极小多项式是$\lambda^2 - 1$,
那么依据定理6.7.2可知，由于$A$的极小多项式无重根，所以可对角化，其对角元就是它的特征值$\pm 1$.
假设特征值$1, -1$的重数分别为$r,s$, 那么$r+s = n$,
$A$相似于$\begin{pmatrix} I_r & \\ & -I_s \end{pmatrix}$.

另一种证法：将$A$视作$\mathbb{F}^n$上的线性变换，考察特征子空间$V_1, V_{-1}$,
设$\dim V_1 = s, \dim V_2 = r$.
由于$V_1 + V_{-1}$是直和，只要证明$\dim V_1 + \dim V_{-1} = n$，那么存在$V_1$的一组基$\alpha_1, \ldots, \alpha_s$,
$V_{-1}$的一组基$\beta_1, \ldots, \beta_r$,
他们构成$V$的一组基$\alpha_1, \ldots, \alpha_s, \beta_1, \ldots, \beta_r$,
在这组基下$A$的矩阵表示为$\begin{pmatrix} I_r & \\ & -I_s \end{pmatrix}$.
或者等价地，令$P = (\alpha_1, \ldots, \alpha_s, \beta_1, \ldots, \beta_r)$,
有$P^{-1}AP = \begin{pmatrix} I_r & \\ & -I_s \end{pmatrix}$.
考虑如下两个$\mathbb{F}^n$上的线性变换
$$\sigma_1: v \mapsto (A-I)v, \quad \sigma_{-1}: v \mapsto (A+I)v.$$
那么 $\sigma_1\sigma_{-1}(v) = 0$,
于是$V_1 = \ker (\sigma_1) \supset \operatorname{Im} (\sigma_{-1})$,
从而有
$$s = \dim V_1 = \dim \ker (\sigma_1) \geqslant \dim \operatorname{Im} (\sigma_{-1}) = n - \dim \ker (\sigma_{-1}) = n - \dim V_{-1} = n - r,$$
于是有$n \geqslant \dim V_1 + \dim V_{-1} = s + r \geqslant n$.

**第三题**. 若$A \in M_n (\mathbb{C})$满足$A^n = I$,
证明$A$的特征值是$n$次单位根。

**证明**：令$f(\lambda)$为$A$的极小多项式，令$g(\lambda) = \lambda^n - 1$,
那么$g(\lambda)$为$A$的零化多项式，$f(\lambda) | g(\lambda)$.
由于$A$的特征值都是$f(\lambda)$的根，所以他们也都是$g(\lambda) = \lambda^n - 1$的根，从而是$n$次单位根。

**第四题**. 设$A, B \in M_n(\mathbb{F})$, $AB=BA$,
若$A,B$均相似于对角矩阵，证明存在可逆矩阵$P$使得$P^{-1}AP$与$P^{-1}BP$同时为对角形。

**证明**：令$V = \mathbb{F}^n$,
并将$A,B$视作$V \to V$的线性映射。由于$A$可对角化，即存在可逆的$P_A \in M_n(\mathbb{F})$，使得
$$P_A^{-1}AP_A = \operatorname{diag} (\underbrace{\lambda_1,\cdots,\lambda_1}_{r_1}, \cdots, \underbrace{\lambda_m,\cdots,\lambda_m}_{r_m}).$$
其中$\lambda_1, \ldots, \lambda_m$为其互不相等的特征值，（代数，也是几何重数）重数分别为$r_1,\ldots,r_m$.
令$V_{\lambda_i} = \ker (\lambda_i I_n - A)$为$\lambda_i$对应的特征空间。由于$V_{\lambda_1} + \cdots + V_{\lambda_m}$是直和，而且他们维数之和等于$\dim V = n$，所以
$$V = \bigoplus_{i=1}^m V_{\lambda_i}.$$

任取$v \in V_{\lambda_i}$, 有
$$A(Bv) = ABv = BAv = B(Av) = B(\lambda_i v) = \lambda_i Bv$$
所以有$Bv \in V_{\lambda_i}$, 即$BV_{\lambda_i} \subset V_{\lambda_i}$,
$V_{\lambda_i}$是$B$的不变子空间。
考虑$B|_{V_{\lambda_i}}: V_{\lambda_i} \to V_{\lambda_i}$.
若$B|_{V_{\lambda_i}}$可对角化，那么存在$V_{\lambda_i}$的一组基$v_{i1},\ldots,v_{ir_i} \in V_{\lambda_i}$使得
$$B v_{i1} = B|_{V_{\lambda_i}} v_{i1} = \mu_{i1} v_{i1}, \quad \ldots, \quad  B v_{ir_i} = B|_{V_{\lambda_i}} v_{ir_i} = \mu_{ir_i} v_{ir_i}$$
同时又有$A v_{i1} = \lambda_i v_{i1}, \ldots, A v_{i1} = \lambda_i v_{i1}$.
于是在$V$的这组基$v_{11}, \ldots, v_{1r_1}, \ldots, v_{m1}, \ldots, v_{mr_m}$下，$A,B$的矩阵表示分别为$\operatorname{diag} (\underbrace{\lambda_1,\cdots,\lambda_1}_{r_1}, \cdots, \underbrace{\lambda_m,\cdots,\lambda_m}_{r_m})$,
$\operatorname{diag} (\mu_{11}, \ldots, \mu_{1r_1}, \ldots, \mu_{m1}, \ldots, \mu_{mr_m})$.
亦即令$P = (v_{11}, \ldots, v_{1r_1}, \ldots, v_{m1}, \ldots, v_{mr_m})$,
有
$$\begin{aligned}
P^{-1}AP & = \operatorname{diag} (\underbrace{\lambda_1,\cdots,\lambda_1}_{r_1}, \cdots, \underbrace{\lambda_m,\cdots,\lambda_m}_{r_m}) \\
P^{-1}BP & = \operatorname{diag} (\mu_{11}, \ldots, \mu_{1r_1}, \ldots, \mu_{m1}, \ldots, \mu_{mr_m})\end{aligned}$$

下证$B|_{V_{\lambda_i}}$可对角化。令$B$的极小多项式为$f(\lambda)$,
那么$f(B)$是$V$上的零变换，从而也是$V_{\lambda_i}$上的零变换，所以$f(\lambda)$是$B|_{V_{\lambda_i}}$的零化多项式。由于$B$可对角化，所以$f(\lambda)$无重根，$B|_{V_{\lambda_i}}$的极小多项式整除$f(\lambda)$,
所以也无重根，故可对角化。

注意，此题可以稍微加强为如下结论：设$A, B \in M_n(\mathbb{F})$,
若$A,B$均相似于对角矩阵，那么$AB=BA$当且仅当$A,B$可同时对角化。

此外，还可以扩展为如下的结论：设$M_n(\mathbb{F})$中有一族矩阵，它们两两可相互交换而且均可对角化，那么这些矩阵可以同时对角化。

**第五题**. 设$V = M_n (\mathbb{F})$, $A,B \in M_n (\mathbb{F})$,
且满足$AB=BA$以及$A,B$均相似于对角矩阵。在$V$中定义线性变换$\sigma: X \mapsto AX - XB, \forall X \in V$.
判断$\sigma$是否可对角化并证明你的结论。

**解**.
由上一题第四题知$A,B$可同时对角化，即存在可逆矩阵$P$使得$P^{-1}AP$与$P^{-1}BP$同时为对角阵$D_A = \operatorname{diag}(a_1, \ldots, a_n), D_B = \operatorname{diag}(b_1, \ldots, b_n)$.
考虑如下两个$V$上的线性变换
$$\begin{aligned}
\theta: & V \to V, X \mapsto PXP^{-1},\\
\mu: & V \to V, X \mapsto D_A X - X D_B.\end{aligned}$$
若$X$为$\mu$的特征向量（假设有），即$\mu(X) = \lambda X$,
$\lambda \in \mathbb{F}$, 那么
$$\begin{aligned}
\sigma(\theta(X)) & = A PXP^{-1} - PXP^{-1} B = PP^{-1}APXP^{-1} - PXP^{-1}BPP^{-1} \\
& = P(D_AX - XD_B)P^{-1} = P(\mu(X))P^{-1} = P (\lambda X) P^{-1} = \lambda PXP^{-1} \\
& = \lambda \theta(X).\end{aligned}$$
那么，$\theta(X)$是$\sigma$的特征向量，对应的特征值是$\lambda$.
任取$X = (x_{ij}) \in M_n (\mathbb{F})$, 那么
$$\begin{aligned}
D_AX - XD_B & = \operatorname{diag}(a_1, \ldots, a_n) X - X \operatorname{diag}(b_1, \ldots, b_n) \\
& = \begin{pmatrix} a_1x_{11} & \cdots & a_1x_{1n} \\ \vdots & & \vdots \\ a_nx_{n1} & \cdots & a_nx_{nn} \end{pmatrix} - \begin{pmatrix} b_1x_{11} & \cdots & b_nx_{1n} \\ \vdots & & \vdots \\ b_1x_{n1} & \cdots & b_nx_{nn} \end{pmatrix} \\
& = \begin{pmatrix} (a_1-b_1)x_{11} & \cdots & (a_1-b_n)x_{1n} \\ \vdots & & \vdots \\ (a_n-b_1)x_{n1} & \cdots & (a_n-b_n)x_{nn} \end{pmatrix}\end{aligned}$$
所以取$E_{ij} \in M_n (\mathbb{F})$, 为第$(i,j)$位元素为$1$,
其余位置元素为$0$的矩阵，即有
$$D_AE_{ij} - E_{ij}D_B = (a_i-b_j)E_{ij}$$
$\{ E_{11}, \ldots, E_{1n}, \ldots, E_{nn}\}$构成了$M_n (\mathbb{F})$的一组基。由于$P$可逆，所以
$$\{ PE_{11}P^{-1}, \ldots, PE_{1n}P^{-1}, \ldots, PE_{nn}P^{-1} \}$$
也构成了$M_n (\mathbb{F})$的一组基。在这组基下，$\sigma$相似于对角矩阵
$$\operatorname{diag}(a_1-b_1, \ldots, a_1-b_n, \ldots, a_n-b_n).$$

**第六题**. 求证复线性空间的任何两个可交换的线性变换必有公共的特征向量。

**证明**.
任取一个$n$维的复线性空间$V$，设$\sigma, \mu$为$V$上可交换的两个线性变换，满足$\sigma\mu - \mu\sigma = 0$.
任取$\mu$的一个特征值$\lambda \in \mathbb{C}$,
以及对应的一个特征向量$v$.
因为$V$是复线性空间，这样的$\lambda, v$总是存在的。

考察$\mu' = \mu - \lambda$. 若$\mu' = 0$,
那么$V$中任何非零向量都是$\mu$对应于特征值$\lambda$的特征向量，要证明的结论自动成立。以下假设$\mu'$非零映射，令$V' = \ker\mu'$为$\lambda$对应的$\mu$的特征子空间。那么$v\in V'$,
从而知道$1 \leqslant \dim V' < n$. 而且我们有
$$\sigma\mu' = \sigma(\mu-\lambda) = \sigma\mu - \lambda\sigma = 
\mu\sigma - \lambda\sigma = (\mu-\lambda)\sigma = \mu'\sigma.$$
于是，任取$w\in V'$, 有
$$\mu'(\sigma(w)) = \sigma(\mu'(w)) = \sigma(0) = 0,$$
也就是说$\sigma(w) \in V'$.
所以$V'$是$\sigma$的不变子空间。于是$\sigma|_{V'}$是非平凡复线性空间$V'$上的线性变换，至少有一个特征向量$\lambda'$,
以及对应的特征向量$v'\in V'$. $v'$即为$\sigma, \mu$的公共特征向量。

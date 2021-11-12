**第1题**.
讨论参数$\lambda$决定$n\times n$的矩阵$A(\lambda) = \begin{pmatrix} 1 & \cdots & 1 & \lambda \\ 1 & \cdots & \lambda & 1 \\ \vdots & \reflectbox{$\ddots$} & \vdots & \vdots \\ \lambda & \cdots & 1 & 1 \end{pmatrix}$的秩

**解：**首先计算$A(\lambda)$的行列式，有 $$\begin{aligned}
    \det A(\lambda) & = \begin{vmatrix} 1 & \cdots & 1 & \lambda \\ 1 & \cdots & \lambda & 1 \\ \vdots & \reflectbox{$\ddots$} & \vdots & \vdots \\ \lambda & \cdots & 1 & 1 \end{vmatrix} = \begin{vmatrix} 1 & \cdots & 1 & \lambda \\ 0 & \cdots & \lambda-1 & 1-\lambda \\ \vdots & \reflectbox{$\ddots$} & \vdots & \vdots \\ \lambda-1 & \cdots & 0 & 1-\lambda \end{vmatrix} \\
    & = \begin{vmatrix} 1 & \cdots & 1 & \lambda + (n-1) \\ 0 & \cdots & \lambda-1 & 0 \\ \vdots & \reflectbox{$\ddots$} & & \vdots \\ \lambda-1 & \cdots & \cdots & 0 \end{vmatrix} \\
    & = (-1)^{\frac{n(n-1)}{2}} (\lambda+(n-1))(\lambda-1)^{n-1}\end{aligned}$$
所以当$\lambda \neq 1, 1-n$时，矩阵$A(\lambda)$行列式不为$0$，从而满秩，秩为$n$.
当$n = 1$时，矩阵$A(\lambda)$所有元素值都为$1$，这样的矩阵秩为$1$.
当$n = 1-n$时，矩阵$A(\lambda)$在之前求行列式化简到最后一步对应的矩阵为
$$\begin{pmatrix} 1 & \cdots & 1 & 0 \\ 0 & \cdots & -n & 0 \\ \vdots & \reflectbox{$\ddots$} & & \vdots \\ -n & \cdots & \cdots & 0 \end{pmatrix}$$
很容易看出这个矩阵的秩为$n-1$. 另一种做法是把矩阵$A(\lambda)$化为阶梯形
$$\begin{aligned}
    A(1-n) & = \begin{pmatrix} 1 & \cdots & 1 & 1-n \\ 1 & \cdots & 1-n & 1 \\ \vdots & \reflectbox{$\ddots$} & \vdots & \vdots \\ 1-n & \cdots & 1 & 1 \end{pmatrix} \to \begin{pmatrix} 1 & \cdots & 1 & 1-n \\ 0 & \cdots & -n & n \\ \vdots & \reflectbox{$\ddots$} & \vdots & \vdots \\ -n & \cdots & 0 & n \end{pmatrix} \\
    & \to \begin{pmatrix} 1 & \cdots & 1 & 1-n \\ 0 & \cdots & 1 & -1 \\ \vdots & \reflectbox{$\ddots$} & \vdots & \vdots \\ 1 & \cdots & 0 & -1 \end{pmatrix} \to \begin{pmatrix} 0 & \cdots & 0 & 0 \\ 0 & \cdots & 1 & -1 \\ \vdots & \reflectbox{$\ddots$} & \vdots & \vdots \\ 1 & \cdots & 0 & -1 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & \cdots & 0 & -1 \\ 0 & 1 & \cdots & 0 & -1 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \cdots & 1 & -1 \\ 0 & 0 & \cdots & 0 & 0 \end{pmatrix}\end{aligned}$$

**第2题**.
设$V$是复数域$\mathbb{C}$上的$n$维线性空间，$\alpha_1,\ldots,\alpha_n$是一组基。证明$V$也是实数域$\mathbb{R}$上的$2n$维线性空间，并求出它的一组基。更一般地，设$V$是数域$\mathbb{F}$上的$n$维线性空间，$\mathbb{F}$是子域$\mathbb{F}_0$的$m$维线性空间，问$V$是域$\mathbb{F}_0$上多少维线性空间，如何确定它的一组基？

**解：**由于$V$是复数域$\mathbb{C}$上的线性空间，其本身有加法，满足有零元，结合律，交换律（即$V$是一个交换群）。任取$\lambda \in \mathbb{R} \subseteq \mathbb{C}$,
$v\in V$，定义数乘$\lambda v$为$V$作为复数域$\mathbb{C}$上线性空间时的数乘，相关的性质同样满足。所以$V$也是实数域$\mathbb{R}$上的维线性空间，记作$V_{\mathbb{R}}$。下面证明
$$\alpha_1,i\alpha_1,\ldots,\alpha_n,i\alpha_n$$
是$V_{\mathbb{R}}$的一组基。由于$\alpha_1,\cdots,\alpha_n$是$V$作为复数域$\mathbb{C}$上线性空间的一组基，任取$v\in V_{\mathbb{R}}$，存在$\lambda_{11} + i\lambda_{12}, \ldots, \lambda_{n1} + i\lambda_{n2} \in \mathbb{C}$使得
$$v = (\lambda_{11} + i\lambda_{12})\alpha_1 + \cdots + (\lambda_{n1} + i\lambda_{n2})\alpha_n = \lambda_{11}\alpha_1 + \lambda_{12}(i\alpha_1) + \cdots + \lambda_{n1}\alpha_n + \lambda_{n2}(i\alpha_n)$$
所以$\alpha_1,i\alpha_1,\ldots,\alpha_n,i\alpha_n$可以线性表出$V_{\mathbb{R}}$中所有向量。上式同时也可看出$\alpha_1,i\alpha_1,\ldots,\alpha_n,i\alpha_n$在$\mathbb{R}$上线性无关（取$v=0$）。所以它是$V_{\mathbb{R}}$的一组基，从而知$V$是实数域$\mathbb{R}$上的$2n$维线性空间。

若$V$是数域$\mathbb{F}$上的$n$维线性空间，$\mathbb{F}$是子域$\mathbb{F}_0$的$m$维线性空间，那么$V$是域$\mathbb{F}_0$上的$mn$维线性空间。设$\mathbb{F}$作为$\mathbb{F}_0$上线性空间的一组基为$\mu_1, \ldots, \mu_m$,
那么$V$作为域$\mathbb{F}_0$上的线性空间的一组基可以取为
$$\left\{ \mu_i\alpha_j \ \middle|\ 1 \leqslant i \leqslant m, 1 \leqslant j \leqslant n \right\}.$$
利用同样的方法可以证明以上这组向量在可以在$\mathbb{F}_0$上线性表出$V$中所有向量，并且在$\mathbb{F}_0$上线性无关。

**第3题**. 设$V = \mathbb{F}^n$,
$W = \left\{ \begin{pmatrix} a_1 \\ \vdots \\ a_n \end{pmatrix} \ \middle|\ a_1+a_2=a_2-a_3=0 \right\}$.
求商空间$V / W$的维数与一组基。

**解：**$W$为齐次线性方程组$\begin{cases} a_1+a_2= 0 \\ a_2-a_3=0 \end{cases}$的解空间，所以$\dim W = n-2$，根据维数公式有
$$\dim V/W = \dim V - \dim W = n - (n-2) = 2$$
令$v_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}, v_2 = \begin{pmatrix} 0 \\ 1 \\ -1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$,
那么$W^{\perp} = \operatorname{span}\{v_1, v_2\}$,
所以商空间$V / W$的一组基可以取为$\overline{v}_1 = v_1 + W$,
$\overline{v}_2 = v_2 + W$.

**第4题**. 设$\mathbb{R}^2$中三条不同直线的方程为 $$\begin{aligned}
    \ell_1: & \quad ax+by+c=0 \\
    \ell_2: & \quad cx+ay+b=0 \\
    \ell_3: & \quad bx+cy+a=0 \\\end{aligned}$$
证明$\ell_1,\ell_2,\ell_3$交于一点 $\Longleftrightarrow$ $a+b+c=0$.

**证明：**求三条直线方程交点的方程组可写为
$$A\begin{pmatrix} x \\ y \\ 1 \end{pmatrix} = 0, \quad \text{ 其中 } A = \begin{pmatrix} a & b & c \\ c & a & b \\ b & c & a \end{pmatrix}.$$
$\ell_1,\ell_2,\ell_3$交于一点当且仅当$A\begin{pmatrix} x \\ y \\ 1 \end{pmatrix} = 0$有唯一解，这又等价于$A\begin{pmatrix} x \\ y \\ z \end{pmatrix} = 0$解空间维数为$1$，即$A$的秩为2，且在$z$轴上的投影非平凡。对$A$做行、列的初等变换有
$$\begin{aligned}
A & = \begin{pmatrix} a & b & c \\ c & a & b \\ b & c & a \end{pmatrix} \to \begin{pmatrix} a & b & c \\ c & a & b \\ a+b+c & a+b+c & a+b+c \end{pmatrix}\end{aligned}$$

若$a+b+c\neq 0$，则有进一步变换 $$\begin{aligned}
A & = \begin{pmatrix} a & b & c \\ c & a & b \\ b & c & a \end{pmatrix} \to \begin{pmatrix} a & b & c \\ c & a & b \\ a+b+c & a+b+c & a+b+c \end{pmatrix} \\
& \to \begin{pmatrix} a & b & c \\ c & a & b \\ 1 & 1 & 1 \end{pmatrix} \to \begin{pmatrix} a-c & b-c & 0 \\ c-b & a-b & 0 \\ 0 & 0 & 1 \end{pmatrix}\end{aligned}$$
由于$\det\begin{pmatrix} a-c & b-c \\ c-b & a-b \end{pmatrix} = a^2+b^2+c^2-ab-bc-ac = \frac12\left( (a-b)^2 + (b-c)^2 + (c-a)^2 \right)$.
于是若有$a=b=c$，此时$\operatorname{rank}(A) = 1$，其余情况下$\operatorname{rank}(A) = 3$,
都不满足$\operatorname{rank}(A) = 2$.

若$a+b+c=0$，则进一步变换为 $$\begin{aligned}
A & = \begin{pmatrix} a & b & c \\ c & a & b \\ b & c & a \end{pmatrix} \to \begin{pmatrix} a & b & c \\ c & a & b \\ a+b+c & a+b+c & a+b+c \end{pmatrix} = \begin{pmatrix} a & b & c \\ c & a & b \\ 0 & 0 & 0 \end{pmatrix}\\
& \to \begin{pmatrix} a & b & a+b+c \\ c & a & a+b+c \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} a & b & 0 \\ c & a & 0 \\ 0 & 0 & 0 \end{pmatrix}\end{aligned}$$
考虑到$\det\begin{pmatrix} a & b \\ c & a \end{pmatrix} = \frac12\left( a^2-bc\right)$，此式等于$0$当且仅当$a=b=c=0$，但此时$\ell_1,\ell_2,\ell_3$就不是直线方程了。所以在$a+b+c=0$的情况下，总有$\operatorname{rank}(A) = 2$。于是
$$\ell_1,\ell_2,\ell_3 \text{ 交于一点 } \Longleftrightarrow \ a+b+c=0$$

**第5题** 求循环矩阵（Circulant Matrix）$A$的行列式，
$$A = \begin{pmatrix} a_0 & a_1 & a_2 & \cdots & a_{n-1} \\ a_{n-1} & a_0 & a_1 & \cdots & a_{n-2} \\ \vdots & \vdots & \vdots & & \vdots \\ a_1 & a_2 & a_3 & \cdots & a_0 \end{pmatrix}, \quad a_0,\ldots,a_{n-1} \in \mathbb{C}$$

**解：**设$u$为任一$n$次单位根，令$\mu = \begin{pmatrix} 1 \\ u \\ \vdots \\ u^{n-1} \end{pmatrix}$,
那么有
$$A\mu = \begin{pmatrix} a_0 + a_1u + \cdots + a_{n-1}u^{n-1} \\ a_{n-1} + a_0u + \cdots + a_{n-2}u^{n-1} \\ \vdots \\ a_1 + a_2u + \cdots + a_0u^{n-1} \end{pmatrix} = \begin{pmatrix} f(u) \\ uf(u) \\ \vdots \\ u^{n-1}f(u) \end{pmatrix} = f(u)\mu,$$
其中$f(u) = a_0 + a_1u + \cdots + a_{n-1}u^{n-1}$.
现令$u = \exp(2\pi i/n)$为$n$次本原单位根，$\omega_j = \begin{pmatrix} 1 \\ u^j \\ \vdots \\ u^{(n-1)j} \end{pmatrix}$,
$j=0,\ldots,n-1$, 那么有$A\omega_j = f(u^j)\omega_j$.
又令$W = (\omega_0, \cdots, \omega_{n-1})$, 有
$$AW = (A\omega_0, \cdots, A\omega_{n-1}) = (f(u^0)\omega_0, \cdots, f(u^{n-1})\omega_{n-1}).$$
于是有
$$\det A \cdot \det W = \det(AW) = \det(f(u^0)\omega_0, \cdots, f(u^{n-1})\omega_{n-1}) = \prod_{j=0}^{n-1}f(u^j) \det W$$
因为$u$为$n$次本原单位根，$u^0, \ldots, u^{n-1}$互不相同，$\det W \neq 0$,
上式两边同时消去$\det W$有 $$\begin{aligned}
& \det A = \prod_{j=0}^{n-1}f(u^j), \\
& \text{其中}\  u = \exp(2\pi i/n), \ f(u) = a_0 + a_1u + \cdots + a_{n-1}u^{n-1}.\end{aligned}$$
以上情况比较特殊，实际上我们直接观察出来了$A$的所有特征向量与特征值，于是有
$$AW = W\operatorname{diag}(f(u^0), \ldots, f(u^{n-1})),$$
从而有$\det A = \det(\operatorname{diag}(f(u^0), \ldots, f(u^{n-1})))$.

**习题3.5 第1题**. (2).
记$D_n = \begin{vmatrix} 1+x_1 & 1+x_1^2 & \cdots & 1+x_1^n \\ 1+x_2 & 1+x_2^2 & \cdots & 1+x_2^n \\ \vdots & \vdots & & \vdots \\ 1+x_n & 1+x_n^2 & \cdots & 1+x_n^n \end{vmatrix}$,
令$\alpha_i = \begin{pmatrix} x_1^i \\ \vdots \\ x_n^i \end{pmatrix}$,
$e = \begin{pmatrix} 1 \\ \vdots \\ 1 \end{pmatrix}$, 那么
$$\begin{aligned}
D_n & = \det (e+\alpha_1, e+\alpha_2, \cdots, e+\alpha_n) \\
& = \det(\alpha_1, \cdots, \alpha_n) + \det(e, \alpha_2, \cdots, \alpha_n) + \cdots + \det(\alpha_1, \cdots, \alpha_{n-1}, e) \\
& = \det(\alpha_1, \cdots, \alpha_n) + \det(e, \alpha_2, \cdots, \alpha_n) + \cdots + (-1)^{n-1}\det(e, \alpha_1, \cdots, \alpha_{n-1}) \\
& = 2\det(\alpha_1, \cdots, \alpha_n) - \left\{(-1)^2\det(\alpha_1, \cdots, \alpha_n) + \cdots + (-1)^{n+2} \det(e, \alpha_1, \cdots, \alpha_{n-1})\right\} \\
& = 2\det(\alpha_1, \cdots, \alpha_n) - \det\begin{pmatrix} 1 & 1 & \cdots & 1 \\ e & \alpha_1 & \cdots & \alpha_n \end{pmatrix} \\
& = 2x_1\cdots x_n \prod_{1\leqslant i<j \leqslant n} (x_j-x_i) - \prod_{0\leqslant i<j \leqslant n} (x_j-x_i) \quad (\text{其中$x_0=1$}) \\
& = \left( 2\prod_{k=1}^n x_k - \prod_{k=1}^n(x_k-1) \right) \prod_{1\leqslant i<j \leqslant n} (x_j-x_i)\end{aligned}$$

**习题3.5 第2题**.
记$D = \begin{vmatrix} 0 & a_1+a_2 & \cdots & a_1+a_n \\ a_2+a_1 & 0 & \cdots & a_2+a_n \\ \vdots & \vdots & \ddots & \vdots \\ a_n+a_2 & a_n+a_2 & \cdots & 0 \end{vmatrix}$,
令$\alpha_1 = \begin{pmatrix} -a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}$,
$\ldots$,
$\alpha_n = \begin{pmatrix} a_1 \\ \vdots \\ a_{n-1} \\ -a_n \end{pmatrix}$,
$e = \begin{pmatrix} 1 \\ \vdots \\ 1 \end{pmatrix}$, 那么类似上一题有
$$\begin{aligned}
D_n & = \det(\alpha_1 + a_1e, \cdots, \alpha_n + a_ne) \\
& = 2\det(\alpha_1, \cdots, \alpha_n) - \det\begin{pmatrix} 1 & a_1 & \cdots & a_n \\ e & \alpha_1 & \cdots & \alpha_n \end{pmatrix}\end{aligned}$$
这两个都是比较好计算的行列式。

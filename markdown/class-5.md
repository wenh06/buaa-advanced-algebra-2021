---
date: 2022-11-4 第五次习题课
title: 2022秋高等代数习题课
---

**第一题** (习题4.2第6题第（2）小题).
已知$A$是$n$阶方阵且满足条件$A^3 = I.$ 计算
$$\begin{pmatrix} \dfrac{1}{2} A & - \dfrac{\sqrt{3}}{2} A \\ \dfrac{\sqrt{3}}{2} A & \dfrac{1}{2} A \end{pmatrix}^{2000}.$$

**解**： 令$\theta = \dfrac{\pi}{3},$ 那么
$$\begin{pmatrix} \dfrac{1}{2} A & - \dfrac{\sqrt{3}}{2} A \\ \dfrac{\sqrt{3}}{2} A & \dfrac{1}{2} A \end{pmatrix} = \begin{pmatrix} A & \\ & A \end{pmatrix} \underbrace{\begin{pmatrix} \cos\theta I_n & - \sin\theta I_n \\ \sin\theta I_n & \cos\theta I_n \end{pmatrix}}_M,$$
并且矩阵$\begin{pmatrix} A & \\ & A \end{pmatrix}$和$M$是可交换的。于是
$$\begin{aligned}
\begin{pmatrix} \dfrac{1}{2} A & - \dfrac{\sqrt{3}}{2} A \\ \dfrac{\sqrt{3}}{2} A & \dfrac{1}{2} A \end{pmatrix}^{2000} & = \begin{pmatrix} A & \\ & A \end{pmatrix}^{2000} M^{2000} = \begin{pmatrix} A^{2000} & \\ & A^{2000} \end{pmatrix} \begin{pmatrix} \cos 2000\theta I_n & - \sin 2000\theta I_n \\ \sin 2000\theta I_n & \cos 2000\theta I_n \end{pmatrix} \\
& = \begin{pmatrix} A^2 & \\ & A^2 \end{pmatrix} \begin{pmatrix} \cos 2\theta I_n & - \sin 2\theta I_n \\ \sin 2\theta I_n & \cos 2\theta I_n \end{pmatrix} = \begin{pmatrix} A^2 & \\ & A^2 \end{pmatrix} \begin{pmatrix} - \dfrac{1}{2} I_n & - \dfrac{\sqrt{3}}{2} I_n \\ \dfrac{\sqrt{3}}{2} I_n & - \dfrac{1}{2} I_n \end{pmatrix} \\
& = \begin{pmatrix} - \dfrac{1}{2} A^2 & - \dfrac{\sqrt{3}}{2} A^2 \\ \dfrac{\sqrt{3}}{2} A^2 & - \dfrac{1}{2} A^2 \end{pmatrix}.\end{aligned}$$

**第二题** (习题4.3第8题). 设$A^*$表示$n$阶方阵$A$的伴随方阵。证明：

-   $(\lambda A)^* = \lambda^{n-1}A^*$ 对任意数$\lambda$成立；

-   $(AB)^* = B^*A^*$对任意同阶方阵$A,B$成立；

-   当$n > 2$时，$(A^*)^* = (\det A)^{n-2}A$;
    当$n = 2$时，$(A^*)^* = A$.

**证明：** (1).
由于$(\lambda A)^*$第$(j,i)$位元素为$\lambda A$第$(i,j)$个代数余子式$(\lambda A)_{(i,j)}$。由于任意$n-1$阶方阵$B$都有$\det(\lambda B) = \lambda^{n-1}\det B$,
所以$(\lambda A)_{(i,j)} = \lambda^{n-1} A_{(i,j)}$,
进而有$(\lambda A)^* = \lambda^{n-1}A^*$.

(2). 令$B^*A^* = (c_{ij})$, 那么 $$\begin{aligned}
c_{ij} & = \sum\limits_{k=1}^n B_{ki} A_{jk} \\
& = \sum\limits_{k=1}^n (-1)^{k+j}\det A\begin{pmatrix} 1,\cdots,j-1,j+1,\cdots,n \\ 1,\cdots,k-1,k+1,\cdots,n \end{pmatrix} \cdot (-1)^{k+i} \det B\begin{pmatrix} 1,\cdots,k-1,k+1,\cdots,n \\ 1,\cdots,i-1,i+1,\cdots,n \end{pmatrix} \\
& = (-1)^{i+j} \sum\limits_{k=1}^n \det\widehat{A}_j\begin{pmatrix} 1,\cdots,n-1 \\ 1,\cdots,k-1,k+1,\cdots,n \end{pmatrix} \cdot \det \widetilde{B}_i\begin{pmatrix} 1,\cdots,k-1,k+1,\cdots,n \\ 1,\cdots,n-1 \end{pmatrix} \\
& = (-1)^{i+j} \det(\widehat{A}_j \widetilde{B}_i),\end{aligned}$$
其中$B_{ki}, A_{jk}$分别为$B$在第$(k,i)$位的代数余子式与$A$在第$(j,k)$位的代数余子式，$\widehat{A}_j$为方阵$A$删掉第$j$行得到的$(n-1)\times n$的矩阵，$\widetilde{B}_i$为方阵$B$删掉第$i$列得到的$n\times (n-1)$的矩阵。后面这个等号是根据Binet-Cauchy公式（课本定理4.5.3(3)）得到的。

另一方面，方阵$(AB)^*$的第$(i,j)$位元素，记为$d_{ij}$，为方阵$AB$的第$(j,i)$位代数余子式$(AB)_{ji}$,
其值为$(-1)^{i+j}$乘以方阵$AB$删掉第$j$行第$i$列得到的$n-1$阶方阵的行列式，此$n-1$阶方阵就等于$\widehat{A}_j \widetilde{B}_i$,
即我们会有
$$d_{ij} = (AB)_{ji} = (-1)^{i+j} \det(\widehat{A}_j \widetilde{B}_i).$$

于是，对于所有的$1\leqslant i,j \leqslant n$,
都有$c_{ij} = d_{ij}$，所以相应的矩阵是同一矩阵，即$(AB)^* = B^*A^*$.

另一种解法：当$A,B$都是可逆阵的时候，有
$$(AB)^* = \det(AB) \cdot (AB)^{-1} = (\det B \cdot B^{-1}) \cdot (\det A \cdot A^{-1}) = B^*A^*.$$
若$A$不可逆，则考虑$A(\lambda) = \lambda I + A$;
若$B$不可逆，$B(\lambda) = \lambda I + B$. 由于$\det A(\lambda)$,
$\det B(\lambda)$都是$\lambda$的多项式，至多有有限多个根，在$0$的一个小的去心领域$\mathring{U}(0,\delta)$内，$A(\lambda), B(\lambda)$总是可逆的，从而有
$$(A(\lambda)B(\lambda))^* = B(\lambda)^*A(\lambda)^*$$
对上式取极限$\lim\limits_{\mathring{U}(0,\delta) \ni x\to 0}$即有$(AB)^* = B^*A^*$.
这里可以取极限，是因为以上的每一个（伴随）矩阵的元素，都是$\lambda$的多项式，关于$\lambda$都是连续的。

(3).
由于$A^*$的每个元素都是$A$的某个$n-1$阶代数余子式，所以若$r(A)\leqslant n-2$,
那么$A^* = 0$. 又由于$AA^* = \det A I_n$,
所以当$r(A) = n$时，$r(A^*) = n$.
当$r(A) = n-1$时，由于$r(A^*) + r(A) - n \leqslant r(AA^*)$,
所以$r(A^*) \leqslant 1$,
同时$A$至少有一个非零子式，即$A^*$至少有一个非零元，所以$r(A^*) \geqslant 1$,
从而必须有$r(A^*) = 1$. 于是，我们证明了
$$r(A^*) = \begin{cases} n, & \text{ 若 } r(A) = n \\ 1, & \text{ 若 } r(A) = n-1 \\ 0, & \text{ 其余情况} \end{cases}$$
所以当$n > 2$时，当$r(A) = n$时，
$$(A^*)^* = \det A^* \cdot (A^*)^{-1} = (\det A)^{n-1} (\det A \cdot A^{-1})^{-1} = (\det A)^{n-2} A.$$
当$r(A) < n$，有$r(A^*) \leqslant 1 < n-1$
(注意，这里用到了$n > 2$的条件), 进而有$r((A^*)^*) = 0$,
也满足$(A^*)^* = (\det A)^{n-2}A$.
唯一需要额外讨论的是$n=2, r(A) = 1$的情形，但这种情况下能直接通过伴随矩阵的定义得出$n = 2$时，$(A^*)^* = A$的结论。

**第三题** (习题4.3第9题).
设方阵$A = (a_{ij})_{n\times n} \in \mathbb{F}^{n\times n}$的行列式$|A| \neq 0$,
$\beta\in\mathbb{F}^{n\times 1}$,
则线性方程组$AX=\beta$有唯一解$X = A^{-1}\beta$.
利用$A^{-1}$的表达式$A^{-1} = \frac{1}{|A|}A^*$证明Cramer法则。

**证明：**线性方程组$AX=\beta$的解$X = A^{-1}\beta = \frac{1}{|A|}A^*\beta$.
记$X = (x_1, \cdots, x_n)^T, A^* = (c_{ij}), \beta = (b_1, \cdots, b_n)^T$,
其中$c_{ij} = A_{ji}$为方阵$A$的第$(j,i)$位代数余子式。那么有
$$x_i = \frac{c_{i1}b_1 + \cdots + c_{in}b_n}{|A|} = \frac{A_{1i}b_1 + \cdots + A_{ni}b_n}{|A|}$$
上式右边分子正好是将矩阵$A$的第$i$列替换为$\beta$,
再按第$i$列展开计算得到的替换后方阵的行列式，此即为Cramer法则。

**第四题**.
设$A$是$m\times n$矩阵，$B$是$n\times s$矩阵。令$C = \begin{pmatrix} 0 & A \\ B & I_n \end{pmatrix}, D = \begin{pmatrix} AB & 0 \\ 0 & I_n \end{pmatrix},$
证明

-   $r(C) = r(D);$

-   $r(C) \geqslant r(A) + r(B);$

-   $r(AB) \geqslant r(A) + r(B) - n.$

**证明**： (1) 由于有
$$\begin{pmatrix} I & -A \\ 0 & I \end{pmatrix} \underbrace{\begin{pmatrix} 0 & A \\ B & I \end{pmatrix}}_{C} \begin{pmatrix} -I & 0 \\ B & I \end{pmatrix} = \begin{pmatrix} AB & 0 \\ 0 & I \end{pmatrix} = D,$$
而且$\begin{pmatrix} I & -A \\ 0 & I \end{pmatrix}, \begin{pmatrix} -I & 0 \\ B & I \end{pmatrix}$都是可逆矩阵，所以$r(C) = r(D).$

\(2\)
设$P_A A Q_A = \begin{pmatrix} I_{r(A)} & 0 \\ 0 & 0 \end{pmatrix}, P_B B Q_B = \begin{pmatrix} I_{r(B)} & 0 \\ 0 & 0 \end{pmatrix}$,
其中$P_A, Q_A, P_B, Q_B$分别是$m$阶，$n$阶，$n$阶，$s$阶可逆方阵。那么
$$\begin{pmatrix} P_A & 0 \\ 0 & P_B \end{pmatrix} \underbrace{\begin{pmatrix} 0 & A \\ B & I \end{pmatrix}}_{C} \begin{pmatrix} Q_B & 0 \\ 0 & Q_A \end{pmatrix} = \begin{pmatrix} 0 & P_A A Q_A \\ P_B B Q_B & P_B Q_A \end{pmatrix} = \begin{pmatrix} {\Large \text{0}} & & I_{r(A)} & 0 \\ & & 0 & 0 \\ I_{r(B)} & 0 & E_{11} & E_{12} \\ 0 & 0 & E_{21} & E_{22} \end{pmatrix},$$
其中$P_B Q_A$被划分为分块矩阵$\begin{pmatrix} E_{11} & E_{12} \\ E_{21} & E_{22} \end{pmatrix}.$
于是$r(C) \geqslant r(A) + r(B),$
并且只要$E_{22}$不是零矩阵，上述不等号就成立。

一般来说，$r(C) = r \begin{pmatrix} 0 & A \\ B & I_n \end{pmatrix} = r(A) + n$
（或者$r(B) + n$）是不成立的。反例：
$$A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}, ~~ \text{ 此时 } C = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \end{pmatrix}.$$
此时$r(C) = 2 \neq 1 + 2 = r(A) + 2.$

\(3\) 由前面2个小问知有不等式
$$r(A) + r(B) \leqslant r(C) = r(D) = r \begin{pmatrix} AB & 0 \\ 0 & I_n \end{pmatrix} = r(AB) + n,$$
所以$r(AB) \geqslant r(A) + r(B) - n.$

**第五题**. (Sherman--Morrison formula)
设$A$是$n$阶可逆实方阵，$u, v$是两个$n$维实的列向量。证明$n$阶实方阵$A + uv^T$可逆当且仅当实数$1 + v^TA^{-1}u \neq 0,$
并且此时有
$$\left(A + uv^T \right)^{-1} = A^{-1} - \dfrac{ A^{-1}uv^TA^{-1}}{1 + v^TA^{-1}u}.$$

**证明**：
考虑分块矩阵$\begin{pmatrix} A & u \\ -v^T & 1 \end{pmatrix}$的对角化。一方面以$A$为中心，用第一行、第一列去"乘以倍数"加到第二行、第二列，有
$$\begin{pmatrix} I & 0 \\ v^TA^{-1} & 1 \end{pmatrix} \begin{pmatrix} A & u \\ -v^T & 1 \end{pmatrix} \begin{pmatrix} I & -A^{-1}u \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} A & 0 \\ 0 & 1 + v^TA^{-1}u \end{pmatrix},$$
另一方面$1$为中心，用第二行、第二列去"乘以倍数"加到第一行、第一列，有
$$\begin{pmatrix} I & -u \\ 0 & 1 \end{pmatrix} \begin{pmatrix} A & u \\ -v^T & 1 \end{pmatrix} \begin{pmatrix} I & 0 \\ v^T & 1 \end{pmatrix} = \begin{pmatrix} A + uv^T & 0 \\ 0 & 1 \end{pmatrix}$$
于是我们有等价关系： $$\begin{aligned}
A + uv^T \text{ 可逆 } & \Longleftrightarrow \begin{pmatrix} A + uv^T & 0 \\ 0 & 1 \end{pmatrix} \text{ 可逆 } \Longleftrightarrow \begin{pmatrix} A & u \\ -v^T & 1 \end{pmatrix} \text{ 可逆 } \Longleftrightarrow \begin{pmatrix} A & 0 \\ 0 & 1 + v^TA^{-1}u \end{pmatrix} \text{ 可逆 } \\
& \Longleftrightarrow 1 + v^TA^{-1}u \neq 0.\end{aligned}$$ 此时，
$$\begin{aligned}
\begin{pmatrix} (A + uv^T)^{-1} & 0 \\ 0 & 1 \end{pmatrix} & = \begin{pmatrix} A + uv^T & 0 \\ 0 & 1 \end{pmatrix}^{-1} = \begin{pmatrix} I & 0 \\ v^T & 1 \end{pmatrix}^{-1} \begin{pmatrix} A & u \\ -v^T & 1 \end{pmatrix}^{-1} \begin{pmatrix} I & -u \\ 0 & 1 \end{pmatrix}^{-1} \\
& = \begin{pmatrix} I & 0 \\ v^T & 1 \end{pmatrix}^{-1} \begin{pmatrix} I & -A^{-1}u \\ 0 & 1 \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & 1 + v^TA^{-1}u \end{pmatrix}^{-1} \begin{pmatrix} I & 0 \\ v^TA^{-1} & 1 \end{pmatrix} \begin{pmatrix} I & -u \\ 0 & 1 \end{pmatrix}^{-1} \\
& = \begin{pmatrix} I & 0 \\ -v^T & 1 \end{pmatrix} \begin{pmatrix} I & -A^{-1}u \\ 0 & 1 \end{pmatrix} \begin{pmatrix} A^{-1} & 0 \\ 0 & \dfrac{1}{1 + v^TA^{-1}u} \end{pmatrix} \begin{pmatrix} I & 0 \\ v^TA^{-1} & 1 \end{pmatrix} \begin{pmatrix} I & u \\ 0 & 1 \end{pmatrix} \\
& = \begin{pmatrix} I & -A^{-1}u \\ -v^T & 1 + v^TA^{-1}u \end{pmatrix} \begin{pmatrix} A^{-1} & 0 \\ 0 & \dfrac{1}{1 + v^TA^{-1}u} \end{pmatrix} \begin{pmatrix} I & u \\ v^TA^{-1} & 1 + v^TA^{-1}u \end{pmatrix} \\
& = \begin{pmatrix} A^{-1} & \dfrac{-A^{-1}u}{1 + v^TA^{-1}u} \\ -v^T A^{-1} & \dfrac{1}{1 + v^TA^{-1}u} \end{pmatrix} \begin{pmatrix} I & u \\ v^TA^{-1} & 1 + v^TA^{-1}u \end{pmatrix} \\
& = \begin{pmatrix} A^{-1} - \dfrac{ A^{-1}uv^TA^{-1}}{1 + v^TA^{-1}u} & 0 \\ 0 & 1 \end{pmatrix}\end{aligned}$$
所以$(A + uv^T)^{-1} = A^{-1} - \dfrac{ A^{-1}uv^TA^{-1}}{1 + v^TA^{-1}u}.$
注意，最后算得的这个矩阵非对角元一定是$0,$
如果不是，说明你哪一步算错了，需要检查改正。

扩展练习：设$A$为$n$阶可逆实方阵，$U$为$n\times m$的实方阵，$C$为$m$阶可逆实方阵，$V$为$m\times n$的实方阵。证明$n$阶方阵$A + UCV$可逆当且仅当$m$阶方阵$C^{-1} + VA^{-1}U$可逆，以及如下的Woodbury
matrix identity
$$\left( A + UCV \right)^{-1} = A^{-1} - A^{-1} U \left( C^{-1} + VA^{-1}U \right)^{-1} V A^{-1}.$$

**第六题** 求循环矩阵（Circulant Matrix）$A$的行列式，
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

这次期中考试第一个计算行列式就差不多是一个循环矩阵的行列式，如果把中间两行调换一下的话。不过它只是一个4阶的行列式，不太需要用到这里的结论。用这个结论反而会把问题复杂化。

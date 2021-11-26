**习题4.3 第8题**. 设$A^*$表示$n$阶方阵$A$的伴随矩阵。证明：

(1). $(\lambda A)^* = \lambda^{n-1}A^*$ 对任意数$\lambda$成立；

(2). $(AB)^* = B^*A^*$对任意同阶方阵$A,B$成立；

(3). 当$n > 2$时，$(A^*)^* = (\det A)^{n-2}A$;
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
当$r(A) < n$，有$r(A*) \leqslant 1 < n-1$, 进而有$r((A^*)^*) = 0$,
也满足$(A^*)^* = (\det A)^{n-2}A$.
唯一需要额外讨论的是$n=2, r(A) = 1$的情形，但这种情况下能直接通过伴随矩阵的定义得出$n = 2$时，$(A^*)^* = A$的结论。

**习题4.3 第9题**.
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

**习题4.4 第5题**.
已知$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
求2阶初等方阵$P,Q$使$PAQ$具有形式$\begin{pmatrix} a & 0 \\ 0 & d_1 \end{pmatrix}$.

**解：**这题需要添加条件$a\neq 0$，否则$A = \begin{pmatrix} 0 & b \\ c & d \end{pmatrix}$,
$b,c\neq 0$时不可能能化成$\begin{pmatrix} 0 & 0 \\ 0 & d_1 \end{pmatrix}$的形式。

$$\begin{pmatrix} 1 & 0 \\ -\frac{c}{a} & 1 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & -\frac{b}{a} \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} a & 0 \\ 0 & d - \frac{bc}{a} \end{pmatrix}$$
所以可以取$P = \begin{pmatrix} 1 & 0 \\ -\frac{c}{a} & 1 \end{pmatrix}, Q = \begin{pmatrix} 1 & -\frac{b}{a} \\ 0 & 1 \end{pmatrix}$,
$d_1 = d - \frac{bc}{a}$.

**习题4.4 第6题**.
设$A,B,C,D\in\mathbb{F}^{n\times n}$且$A$可逆。求$2n$阶可逆方阵$P,Q$使$P\begin{pmatrix} A & B \\ C & D \end{pmatrix}Q$具有形式$\begin{pmatrix} A & 0 \\ 0 & D_1 \end{pmatrix}$,
其中$D_1$是某个$n$阶方阵。

**解：** 这题可以依照习题4.4 第6题类似地做，只是需要注意矩阵相乘的顺序。
$$\begin{pmatrix} I & 0 \\ -CA^{-1} & I \end{pmatrix} \begin{pmatrix} A & B \\ C & D \end{pmatrix} \begin{pmatrix} I & -A^{-1}B \\ 0 & I \end{pmatrix} = \begin{pmatrix} A & 0 \\ 0 & D - CA^{-1}B \end{pmatrix}$$
$D_1 = D - CA^{-1}B$.

**第5题**. 设$A$是秩为1的$n$阶方阵，若存在正整数$k$，使得$A^k = 0$,
证明$A^2 = 0$.

**证明：**由于$A$秩为1，所以至少存在某一行元素不全为0，记这一行为$\alpha = (a_1, \cdots, a_n)$。由于$A$秩为1，$\{\alpha\}$即为$A$的行的极大线性无关组，能表出其他所有行。也就是说$A$的所有行都能表示为$\lambda_1\alpha, \ldots, \lambda_n\alpha$，于是有$A = \lambda \alpha$，其中$\lambda = \begin{pmatrix}
\lambda_1 \\ \vdots \\ \lambda_n \end{pmatrix}$. 那么对于$k\geqslant 2$,
$$A^k = (\lambda\alpha)^k = \lambda (\alpha\lambda)^{k-1} \alpha = \left( \sum_{i=1}^n \lambda_i a_i \right)^{k-1} \lambda \alpha = \left( \sum_{i=1}^n \lambda_i a_i \right)^{k-1} A$$
于是若$A^k = 0$, 那么$\sum\limits_{i=1}^n \lambda_i a_i = 0$, 所以
$$A^2 = \left( \sum_{i=1}^n \lambda_i a_i \right) A = 0.$$

**第6题**. 设$A$是$m\times n$矩阵，$B$是$n\times s$矩阵。证明
$$r(\begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix}) \leqslant r(\begin{pmatrix} A & 0 \\ I_n & B \end{pmatrix}) = r(\begin{pmatrix} AB & 0 \\ 0 & I_n \end{pmatrix})$$

**证明：** 由于有
$$\begin{pmatrix} I & -A \\ 0 & I \end{pmatrix} \begin{pmatrix} A & 0 \\ I & B \end{pmatrix} \begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix} \begin{pmatrix} I & 0 \\ B & I \end{pmatrix} = \begin{pmatrix} AB & 0 \\ 0 & I \end{pmatrix},$$
而且$\begin{pmatrix} I & -A \\ 0 & I \end{pmatrix}, \begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}, \begin{pmatrix} I & 0 \\ B & I \end{pmatrix}$都是满秩方阵，所以$r(\begin{pmatrix} A & 0 \\ I_n & B \end{pmatrix}) = r(\begin{pmatrix} AB & 0 \\ 0 & I_n \end{pmatrix})$。

设可逆矩阵$P_1,Q_1,P_2,Q_2$使得$P_1AQ_1 = \begin{pmatrix} I_{r_1} & 0 \\ 0 & 0 \end{pmatrix}$,
$P_2BQ_2 = \begin{pmatrix} I_{r_2} & 0 \\ 0 & 0 \end{pmatrix}$, 那么
$$\begin{aligned}
\begin{pmatrix} P_1 & 0 \\ 0 & P_2 \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} \begin{pmatrix} Q_1 & 0 \\ 0 & Q_2 \end{pmatrix} & = \begin{pmatrix} I_{r_1} & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & I_{r_2} & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix} \\
\begin{pmatrix} P_1 & 0 \\ 0 & P_2 \end{pmatrix} \begin{pmatrix} A & 0 \\ I & B \end{pmatrix} \begin{pmatrix} Q_1 & 0 \\ 0 & Q_2 \end{pmatrix} & = \begin{pmatrix} I_{r_1} & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ C_{11} & C_{12} & I_{r_2} & 0 \\ C_{21} & C_{22} & 0 & 0 \end{pmatrix}\end{aligned}$$
其中$P_2Q_1 = \begin{pmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{pmatrix}$.
于是上式中第一行的方阵的秩小于等于第二行的方阵的秩，同时又由于$\begin{pmatrix} P_1 & 0 \\ 0 & P_2 \end{pmatrix}$,
$\begin{pmatrix} Q_1 & 0 \\ 0 & Q_2 \end{pmatrix}$都是可逆（满秩）的，所以有$r(\begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix}) \leqslant r(\begin{pmatrix} A & 0 \\ I_n & B \end{pmatrix})$.

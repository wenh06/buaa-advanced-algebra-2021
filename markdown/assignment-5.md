**习题2.5 第3题**

设整数$k\geqslant 2$，数域$\mathbb{F}$上的线性空间$V$中的向量$\alpha_1,\cdots, \alpha_k$线性相关。证明：存在不全为0的数$\lambda_1,\cdots,\lambda_k\in \mathbb{F}$，使得对任何$\alpha_{k+1}$，向量组$\{\alpha_1+\lambda_1\alpha_{k+1}, \cdots, \alpha_k+\lambda_k\alpha_{k+1}\}$线性相关。

**证明：**由于$\alpha_1,\cdots, \alpha_k$线性无关，所以存在不全为0的数$x_1,\cdots,x_k$使得$x_1\alpha_1+\cdots+x_k\alpha_k = 0$。考虑
$$(\alpha_1+\lambda_1\alpha_{k+1}, \cdots, \alpha_k+\lambda_k\alpha_{k+1}) \begin{pmatrix} x_1 \\ \vdots \\ x_k \end{pmatrix} = 0$$
变形为
$$(\alpha_1, \cdots, \alpha_k, \alpha_{k+1}) \begin{pmatrix} x_1 \\ \vdots \\ x_k \\ x_1\lambda_1+\cdots+x_k\lambda_k \end{pmatrix} = 0$$
所以只要存在不全为0的$\lambda_1,\cdots,\lambda_k$使得$x_1\lambda_1+\cdots+x_k\lambda_k=0$即可。因为$k\geqslant 2$，$(x_1,\cdots,x_k)$在$\mathbb{F}^k$中的正交补总是非平凡的，所以这样的$\lambda_1,\cdots,\lambda_k$总是存在的。

**习题2.5 第6题**

设向量组$\alpha_1,\cdots,\alpha_s$的秩为$r$，在其中任取$m$个向量$\alpha_{i_1},\cdots,\alpha_{i_m}$组成向量组$S$。求证$S$的秩$\geqslant r+m-s$。

**证明：**设$S$的秩为$t$，那么$S$中存在一个元素个数为$t$的极大线性无关组。那么从这个线性无关的向量组出发，通过往其中添加不在$S$中的向量，可以得到整个向量组的一个极大线性无关组。假设添加了$k$个向量，那么有$t+k=r$且$k\leqslant s-m$，从而有
$$t = r - k \geqslant r - (s-m) = r+m-s$$

**习题2.5 第7题**

证明：在所有次数不大于$n$的实系数多项式构成的$n+1$维实线性空间中，$1, (x-c), (x-c)^2, \cdots, (x-c)^n$构成一组基。并求$f(x) = a_0 + a_1x + \cdots + a_nx^n$在这组基下的坐标。

**证明：**只要证明$1, (x-c), (x-c)^2, \cdots, (x-c)^n$线性无关即可。假设存在不全为0的实数$\lambda_0,\cdots,\lambda_n$使得
$$f_0(x) = \lambda_0 + \lambda_1(x-c) + \cdots + \lambda_n(x-c)^n = 0$$
那么$f_0(x)$的$n$阶导函数$f_0^{(n)}(x) = n!\lambda_n = 0$，从而有$\lambda_n = 0$。逐步反推可以导出$\lambda_{n-1} = \cdots = \lambda_0 = 0$，矛盾。

设$f(x) = a_0 + a_1x + \cdots + a_nx^n = \lambda_0 + \lambda_1(x-c) + \cdots + \lambda_n(x-c)^n$，那么$f_0^{(n)}(x) = n! a_n = n! \lambda_n$，故$\lambda_n = a_n$。将所得的$\lambda_n,\cdots,\lambda_{n-k}$回代，并考察$f_0^{(n-k-1)}(0)$，有
$$f_0^{(n-k-1)}(0) = (n-k-1)!a_{n-k-1} = (n-k-1)!\lambda_{n-k-1} + \dfrac{(n-k)!}{1!} (0-c)\lambda_{n-k} + \cdots + \dfrac{n!}{(k+1)!} (0-c)^{k+1}\lambda_{n}$$
得$a_{n-k-1} = \lambda_{n-k-1} + C_{n-k}^1(-c)\lambda_{n-k} + \cdots + C_{n}^{k+1}(-c)^{k+1}\lambda_{n}$
所以有 $$\begin{pmatrix} a_n \\ \vdots \\ a_0 \end{pmatrix}
= \begin{pmatrix} 1 & & & & \\ C_{n}^1(-c) & 1 & & & \\ C_{n}^2(-c)^2 & C_{n-1}^1(-c) & 1 & & \\ \vdots & \vdots & \vdots & \ddots & \\ C_{n}^n(-c)^n & C_{n-1}^{n-1}(-c)^{n-1} & C_{n-2}^{n-2}(-c)^{n-2} & \cdots & 1 \end{pmatrix}
\begin{pmatrix} \lambda_n \\ \vdots \\ \lambda_0 \end{pmatrix}
= A \begin{pmatrix} \lambda_n \\ \vdots \\ \lambda_0 \end{pmatrix}$$
故$f(x) = a_0 + a_1x + \cdots + a_nx^n$在这组基下的坐标为
$$\begin{pmatrix} \lambda_n \\ \vdots \\ \lambda_0 \end{pmatrix} = A^{-1} \begin{pmatrix} a_n \\ \vdots \\ a_0 \end{pmatrix}.$$

若考察$f_0^{(n-k-1)}(c)$，则有
$$f_0^{(n-k-1)}(c) = (n-k-1)!\lambda_{n-k-1} = (n-k-1)!a_{n-k-1} + \dfrac{(n-k)!}{1!} c a_{n-k} + \cdots + \dfrac{n!}{(k+1)!} c^{k+1} a_{n}$$
得$\lambda_{n-k-1} = a_{n-k-1} + C_{n-k}^1c a_{n-k} + \cdots + C_{n}^{k+1}c^{k+1} a_{n}$
所以有 $$\begin{pmatrix} \lambda_n \\ \vdots \\ \lambda_0 \end{pmatrix}
= \begin{pmatrix} 1 & & & & \\ C_{n}^1c & 1 & & & \\ C_{n}^2c^2 & C_{n-1}^1c & 1 & & \\ \vdots & \vdots & \vdots & \ddots & \\ C_{n}^nc^n & C_{n-1}^{n-1}c^{n-1} & C_{n-2}^{n-2}c^{n-2} & \cdots & 1 \end{pmatrix}
\begin{pmatrix} a_n \\ \vdots \\ a_0 \end{pmatrix}$$

**习题2.5 第10题**

将数域$\mathbb{F}$上的$n$维（$n\geqslant 2$）数组空间$\mathbb{F}^n$中的每个向量$\alpha = (a_1,a_2,\cdots,a_n)$看作一个具有$n$项的数列。如下集合$W$是否组成$\mathbb{F}^n$的一个线性子空间？如果是，求出它的维数及一组基。

-   $\mathbb{F}^n$中所有等比数列组成的集合。

-   $\mathbb{F}^n$中所有等差数列组成的集合。

**解：**(1). 不构成线性子空间。$(0,\cdots,0)\not\in W$不构成等比数列。

(2).
构成线性子空间。$(0,\cdots,0)\in W$构成等差数列。令$(a_1,a_2,\cdots,a_n), (b_1,b_2,\cdots,b_n)\in W$为两个等差数列，差分别为$d_1, d_2$，那么任取$\lambda_1, \lambda_2 \in \mathbb{R}$，有$\lambda_1(a_1,a_2,\cdots,a_n) + \lambda_2(b_1,b_2,\cdots,b_n)$是差为$d_1\lambda_1 + d_2\lambda_2$的等差数列。所以$\mathbb{F}^n$中所有等差数列组成的集合$W$构成线性子空间。$W$的元素都可以表示为
$$(a,a+d,\cdots,a+(n-1)d) = a(1,\cdots,1) + d(0,1,\cdots,n-1), \quad a,d\in\mathbb{R}$$
所以$W$维数为2，一组基可以取为$(1,\cdots,1), (0,1,\cdots,n-1)$.

另一解法：$W$由以下有$n-2$个方程的齐次线性方程组定义（$n\geqslant 3$时）
$$\begin{cases}
a_3-a_2 = a_2-a_1 \\
a_4-a_3 = a_3-a_2 \\
\cdots\cdots \\
a_n-a_{n-1} = a_{n-1}-a_{n-2}
\end{cases}$$ 系数矩阵秩为$n-2$，从而$W$维数为$n-(n-2)=2$.

**习题2.6 第1题**

设复数域上线性空间$V$中的向量$\alpha_1,\cdots,\alpha_n$线性无关。对复数$\lambda$的不同值，求向量组$\{ \alpha_1+\lambda\alpha_2, \cdots, \alpha_{n-1}+\lambda\alpha_n, \alpha_n+\lambda\alpha_1 \}$的秩。

**解：**
$$(\alpha_1+\lambda\alpha_2, \cdots, \alpha_{n-1}+\lambda\alpha_n, \alpha_n+\lambda\alpha_1) = (\alpha_1,\cdots,\alpha_n) \begin{pmatrix}
1 & & & & \lambda \\ \lambda & 1 & & & \\ & \lambda & \ddots & & \\ & & \ddots & \ddots & \\ & & & \lambda & 1
\end{pmatrix} = (\alpha_1,\cdots,\alpha_n)A$$
$\{ \alpha_1+\lambda\alpha_2, \cdots, \alpha_{n-1}+\lambda\alpha_n, \alpha_n+\lambda\alpha_1 \}$的秩即为矩阵$A$的秩。那么$A$的阶梯形为
$$\begin{pmatrix}
1 & & & & \lambda \\ & 1 & & & \lambda\cdot(-\lambda) \\ & & \ddots & & \\ & & & \ddots & \lambda\cdot(-\lambda)^{n-2} \\ & & & & 1 + \lambda\cdot(-\lambda)^{n-1}
\end{pmatrix}$$ 所以$\lambda = -\zeta_{n}^k$,
$k=0,1,\cdots, n-1$时，$A$的秩为$n-1$，其中$\zeta_{n} = e^{\frac{2\pi}{n}}$为$n$次单位根；其余情况，$A$的秩为$n$。

**习题2.6 第3题**

设$V$是由复数组成的无穷数列$\{a_n\} = \{ a_1,a_2,\cdots,a_n,\cdots \}$的全体组成的集合，定义$V$中任意两个数列的加法$\{a_n\} + \{b_n\} = \{a_n+b_n\}$及任意数列与任意复数的乘法$\lambda\{a_n\} = \{\lambda a_n\}$之后称为复数域$\mathbb{C}$上线性空间。

-   求证：$V$中满足条件$a_n = a_{n-1}+a_{n-2} (\forall n \geqslant 3)$的全体数列$\{a_n\}$组成$V$的子空间$W$。$W$的维数是多少？

-   对任意$(a_1,a_2)\in\mathbb{C}^2$，定义$\sigma(a_1,a_2) = \{ a_1,a_2,\cdots,a_n,\cdots \} \in W$。求证：$\sigma$是$\mathbb{C}^2$到$W$的同构映射。

-   求证：$W$中存在一组由等比数列组成的基$M$

-   设数列$\{F_n\}$满足条件$F_1 = F_2 = 1$且$F_n = F_{n-1} + F_{n-2}$。求$\{F_n\}$在基$M$下的坐标，并由此求出$\{F_n\}$的通项公式。

**解：**(1)
首先${0,\cdots,0,\cdots}\in W$起到零元的作用。任取$\{a_n\} , \{b_n\} \in W$以及$\lambda_1,\lambda_2\in\mathbb{C}$。有
$$\lambda_1 a_n + \lambda_2 b_n = \lambda_1 (a_{n-1}+a_{n-2}) + \lambda_2 (b_{n-1}+b_{n-2}) = (\lambda_1 a_{n-1} + \lambda_2 b_{n-1}) + (\lambda_1 a_{n-2} + \lambda_2 b_{n-2})$$
故$\lambda_1\{a_n\} + \lambda_2\{b_n\} \in W$.
所以$W$是$V$的线性子空间。由于$W$中向量的自由变量只有前两项$a_1,a_2$，故其维数为2。

\(2\) 首先，检查$\sigma$是线性映射： $$\begin{aligned}
\sigma(\lambda_1(a_1,a_2)+\lambda_2(b_1,b_2)) & = \{\lambda_1a_1+\lambda_2b_1, \lambda_1a_2+\lambda_2b_2,\cdots\} \\
& = \{\lambda_1a_1, \lambda_1a_2,\cdots\} + \{\lambda_2b_1, \lambda_2b_2,\cdots\} \\
& = \lambda_1\sigma(a_1,a_2) + \lambda_2\sigma(b_1,b_2)\end{aligned}$$
其次，检查$\ker\sigma = \{(0,0)\}$：设$\sigma(a_1,a_2) = \{0,0,\cdots\}$，那么$\{a_1,a_2,\cdots\} = \{0,0,\cdots\}$，从而有$\ker\sigma = \{(0,0)\}$。再由两个线性空间维数相同，即可得出$\sigma$是线性同构的结论。

\(3\)
假设有等比数列$\{a,aq,\cdots,aq^n,\cdots\}\in W$，那么有$aq^{n+2} = aq^{n+1} + aq^{n}$。解得$q = \dfrac{1\pm\sqrt{5}}{2}$。由此可知
$$\left\{1, \dfrac{1+\sqrt{5}}{2}, \cdots, \left(\dfrac{1+\sqrt{5}}{2}\right)^n, \cdots, \right\}, \left\{1, \dfrac{1-\sqrt{5}}{2}, \cdots, \left(\dfrac{1-\sqrt{5}}{2}\right)^n, \cdots, \right\} \in W$$
而且他们线性无关，故构成了$W$的一组基。

\(4\)
令$(1,1) = \lambda_1 \left(1, \dfrac{1+\sqrt{5}}{2}\right) + \lambda_2 \left(1, \dfrac{1-\sqrt{5}}{2}\right)$，解得
$$\lambda_1 = \frac{\sqrt{5}}{10} + \frac{1}{2}, \quad \lambda_2 = \frac{1}{2} - \frac{\sqrt{5}}{10}$$
所以$\{F_n\}$在这组基下坐标为$\begin{pmatrix}\frac{\sqrt{5}}{10} + \frac{1}{2}\\\frac{1}{2} - \frac{\sqrt{5}}{10}\end{pmatrix}$，通项公式为
$$F_n = \left( \frac{\sqrt{5}}{10} + \frac{1}{2} \right) \left( \dfrac{1+\sqrt{5}}{2} \right)^{n-1} + \left( \frac{1}{2} - \frac{\sqrt{5}}{10} \right) \left( \dfrac{1-\sqrt{5}}{2} \right)^{n-1}.$$

**习题2.6 第4题**

设$\mathbb{R}^+$是所有正实数组成的集合。对任意$a,b\in\mathbb{R}^+$定义$a\oplus b = ab$（实数$a,b$按通常乘法的乘积），对任意$a\in\mathbb{R}^+$和$\lambda\in\mathbb{R}$定义$\lambda\circ a = a^{\lambda}$。求证：

-   $\mathbb{R}^+$按上述定义的加法$a\oplus b$和数乘$\lambda\circ a$成为实数域$\mathbb{R}$上的线性空间。

-   实数集合$\mathbb{R}$按通常方式定义加法和乘法看成$\mathbb{R}$上的线性空间，求证：通常的这个线性空间$\mathbb{R}$与按上述方式定义的线性空间$\mathbb{R}^+$同构。并给出这两个空间之间的全部同构映射。

**证明：**首先，很容易验证$\mathbb{R}^+$关于加法$a\oplus b$封闭，$1$为加法零元，$a\in\mathbb{R}^+$的加法逆元为$\frac{1}{a}\in\mathbb{R}^+$。任取$a,b\in\mathbb{R}^+$,
$\lambda_1,\lambda_2\in\mathbb{R}$, 有 $$\begin{aligned}
& 1\circ a = a^1 = a \\
& \lambda_1 \circ (a\oplus b) = \lambda_1 \circ ab = (ab)^{\lambda_1} = a^{\lambda_1} b^{\lambda_1} = (\lambda_1\circ a) \oplus (\lambda_1\circ b) \\
& (\lambda_1 + \lambda_2) \circ a = a^{\lambda_1 + \lambda_2} = a^{\lambda_1} a^{\lambda_2} = (\lambda_1 \circ a) \oplus (\lambda_2 \circ a) \\
& (\lambda_1\lambda_2)\circ a = a^{\lambda_1\lambda_2} = (a^{\lambda_2})^{\lambda_1} = \lambda_1 \circ (\lambda_2 \circ a)\end{aligned}$$

\(2\) 任取$a\in\mathbb{R}^{+}$, $a \neq 1$,
定义$\sigma_a: \mathbb{R} \to \mathbb{R}^{+}, x \mapsto a^x$, 那么有
$$\begin{aligned}
\sigma_a(\lambda_1x_1 + \lambda_2x_2) = a^{\lambda_1x_1 + \lambda_2x_2} = (a^{x_1})^{\lambda_1} (a^{x_2})^{\lambda_2} = \lambda_1\circ \sigma_a(x_1) \oplus \lambda_2\circ \sigma_a(x_2)\end{aligned}$$
所以$\sigma_a$是线性映射。任取$b\in\mathbb{R}^{+}$,
有$\sigma_a(\log_a b) = b$，所以$\sigma_a$是满射。令$\sigma_a(x) = a^x = 1$，那么有$x = 0$，从而知$\sigma_a$是单射。所以$\sigma_a$是线性空间的同构映射。

\(2\) 任取同构映射$\sigma: \mathbb{R} \to \mathbb{R}^{+}$,
令$a = \sigma(1)$，有$a\neq 1$，否则$\sigma$不是单射。那么任取$x\in\mathbb{R}$，有
$$\sigma(x) = \sigma(x\cdot 1) = x \circ \sigma(1) = x \circ a = a^{x} = \sigma_a(x)$$
所以$\sigma_a, a\in\mathbb{R}^{+} \setminus {1}$即是$\mathbb{R} \to \mathbb{R}^{+}$的所有线性同构映射。

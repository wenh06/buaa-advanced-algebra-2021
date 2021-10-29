**习题3.2 第4题**. 计算$n$阶行列式

(1).
$\begin{vmatrix} a_1-b_1 & a_1-b_2 & \cdots & a_1-b_n \\ a_2-b_1 & a_2-b_2 & \cdots & a_2-b_n \\ \vdots & \vdots & & \vdots \\ a_n-b_1 & a_n-b_2 & \cdots & a_n-b_n \end{vmatrix}$;
$\quad$ (3).
$\begin{vmatrix} 1 & 3 & 3 & \cdots & 3 \\ 3 & 2 & 3 & \cdots & 3 \\ \vdots & \vdots & \vdots & & \vdots \\ 3 & 3 & \cdots & n-1 & 3 \\ 3 & 3 & \cdots & 3 & n \end{vmatrix}$

**解：**(1).
令原行列式为$D_n$，$\alpha = \begin{pmatrix} a_1 \\ \vdots \\ a_n \end{pmatrix}$,
$\beta = \begin{pmatrix} 1 \\ \vdots \\ 1 \end{pmatrix}$, 那么有
$$\begin{aligned}
D_n & = \det (\alpha-b_1\beta, \alpha-b_2\beta, \cdots, \alpha-b_n\beta) \\
& = \det (\alpha-b_1\beta, (b_1-b_2)\beta, \cdots, (b_1-b_n)\beta)\end{aligned}$$
于是，因为后$n-1$列秩至多为1，若$n \geqslant 3$，那么$D_n = 0$；若$n \leqslant 2$，那么
$$D_n = (b_1-b_2) \det (\alpha-b_1\beta, \beta) = (b_1-b_2)((a_1-b_1)-(a_2-b_1)) = (b_1-b_2)(a_1-a_2).$$

(3). 令原行列式为$D_n$，$e_i, i=1,\cdots,n,$
为$\mathbb{F}^n$的自然基，$\beta = \begin{pmatrix} 1 \\ \vdots \\ 1 \end{pmatrix}$,
那么有 $$\begin{aligned}
D_n & = \det (-2e_1+3\beta, -e_2+3\beta, 3\beta, e_4+3\beta, \cdots, (n-3)e_n+3\beta) \\
& = \det (-2e_1, -e_2, 3\beta, e_4, \cdots, (n-3)e_n)\end{aligned}$$
于是当$n \geqslant 3$时，$D_n = 6 \cdot (n-3)!$，$D_2 = -4$, $D_1 = 1$.

**习题3.3 第1题**. 计算$n$阶行列式

(2).
$\begin{vmatrix} x & a & a & \cdots & a \\ -a & x & a & \cdots & a \\ -a & -a & x & \cdots & a \\ \vdots & \vdots & \vdots & & \vdots \\ -a & -a & -a & \cdots & x \end{vmatrix}$;
$\quad$ (4).
$\begin{vmatrix} x & 0 & \cdots & 0 & a_n \\ -1 & x & \cdots & 0 & a_{n-1} \\ 0 & -1 & \ddots & \vdots & \vdots \\ \vdots & \vdots & \ddots & x & a_2 \\ 0 & 0 & \cdots & -1 & x+a_1 \end{vmatrix}$

**解：**(2). 令原行列式为$D_n$，那么有（$n\geqslant 2$时）
$$\begin{aligned}
D_n & = \begin{vmatrix} x-a & a & a & \cdots & a \\ 0 & x & a & \cdots & a \\ 0 & -a & x & \cdots & a \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & -a & -a & \cdots & x \end{vmatrix} + \begin{vmatrix} a & a & a & \cdots & a \\ -a & x & a & \cdots & a \\ -a & -a & x & \cdots & a \\ \vdots & \vdots & \vdots & & \vdots \\ -a & -a & -a & \cdots & x \end{vmatrix} \\
& = (x-a)D_{n-1} + \begin{vmatrix} a & 0 & 0 & \cdots & 0 \\ -a & x+a & 2a & \cdots & 2a \\ -a & 0 & x+a & \cdots & 2a \\ \vdots & \vdots & \vdots & & \vdots \\ -a & 0 & 0 & \cdots & x+a \end{vmatrix} \\
& = (x-a)D_{n-1} + a (x+a)^{n-1} \\
& = (x-a)^2D_{n-2} + a(x-a)(x+a)^{n-2} + a(x+a)^{n-1} \\
& \cdots \\
& = (x-a)^{n-1} D_1 + a\sum\limits_{i=0}^{n-2} (x-a)^i(x+a)^{n-i-1} \\
& = (x-a)^{n-1} x + a\dfrac{(x+a)^{n-1}\left(1 - \left(\dfrac{x-a}{x+a}\right)^{n-1} \right)}{1 - \dfrac{x-a}{x+a}}, \quad a \neq 0 \\
& = (x-a)^{n-1} x + \dfrac{(x+a)^n-(x+a)(x-a)^{n-1}}{2}, \quad a \neq 0 \\
& = \dfrac{(x+a)^n+(x-a)^n}{2}, \quad a \neq 0\end{aligned}$$
容易验证，当$n = 1$以及当$a = 0$时的特殊情况也符合这个通项公式，所以
$$D_n = \dfrac{(x+a)^n+(x-a)^n}{2}.$$

(4). 令原行列式为$D_n$，从第$n$行开始，逐行乘以$x$加到上一行，有
$$\begin{aligned}
D_n & = \begin{vmatrix} 0 & 0 & \cdots & 0 & x^n+a_1x^{n-1}+\cdots+a_n \\ -1 & 0 & \cdots & 0 & x^{n-1}+a_1x^{n-2}+\cdots+a_{n-1} \\ 0 & -1 & \ddots & \vdots & \vdots \\ \vdots & \vdots & \ddots & 0 & x^2+a_1x+a_2 \\ 0 & 0 & \cdots & -1 & x+a_1 \end{vmatrix} \\
& = (-1)^{1+n}(x^n+a_1x^{n-1}+\cdots+a_n) \begin{vmatrix} -1 & 0 & \cdots & 0 \\ 0 & -1 & \ddots & \vdots \\ \vdots & \vdots & \ddots & 0 \\ 0 & 0 & \cdots & -1 \end{vmatrix} \\
& = (-1)^{1+n}(x^n+a_1x^{n-1}+\cdots+a_n) (-1)^{n-1} \\
& = x^n+a_1x^{n-1}+\cdots+a_n\end{aligned}$$

令$f(x) = x^n+a_1x^{n-1}+\cdots+a_n$，$C(f) = \begin{pmatrix} 0 & 0 & \cdots & 0 & -a_n \\ 1 & 0 & \cdots & 0 & -a_{n-1} \\ 0 & 1 & \ddots & \vdots & \vdots \\ \vdots & \vdots & \ddots & 0 & -a_2 \\ 0 & 0 & \cdots & 1 & -a_1 \end{pmatrix}$，那么$D_n = \det (x - C(f))$。方阵$C(f)$被称作多项式$f(x)$的友阵（Companion
Matrix）。

**补充题**.
设$f_k(x)$是数域$\mathbb{F}$上的$k$次多项式，其首项系数为$a_k \neq 0$,
$k = 0,1,\cdots,n-1$。又设$b_1,b_2,\cdots,b_n\in\mathbb{F}$.
计算下列行列式 $$D = \begin{vmatrix}
f_0(b_1) & f_0(b_2) & \cdots & f_0(b_n) \\
f_1(b_1) & f_1(b_2) & \cdots & f_1(b_n) \\
\vdots & \vdots & & \vdots \\
f_{n-1}(b_1) & f_{n-1}(b_2) & \cdots & f_{n-1}(b_n) \\
\end{vmatrix}$$

**解：**令$f_k(x) = \sum\limits_{i=1}^n c_{ik} x^{i-1}$,
$c_{ik} = 0$当$i \geqslant k+1$, $c_{kk} = a_k$. 令
$$\beta_i = (b_1^{i}, b_2^{i}, \cdots, b_n^{i}), \quad i = 0,\cdots,n-1,$$
那么有 $$\begin{aligned}
D & = \begin{vmatrix}
a_0\beta_0 \\ c_{10}\beta_0 + a_1\beta_1 \\ c_{20}\beta_0 + c_{21}\beta_1 + a_2\beta_2 \\ \vdots \\ c_{n0}\beta_0 + c_{n1}\beta_1 + \cdots + a_{n-1}\beta_{n-1}
\end{vmatrix}
= \begin{vmatrix}
a_0\beta_0 \\ a_1\beta_1 \\ a_2\beta_2 \\ \vdots \\ a_{n-1}\beta_{n-1}
\end{vmatrix} \\
& = \left( \prod_{k=0}^{n-1} a_k \right) \cdot \begin{vmatrix} 1 & 1 & \cdots & 1 \\ b_1 & b_2 & \cdots & b_n \\ \vdots & \vdots & & \vdots \\ b_1^{n-1} & b_2^{n-1} & \cdots & b_n^{n-1} \end{vmatrix} \\
& = \prod_{k=0}^{n-1} a_k \prod_{1\leqslant i < j \leqslant n} (b_j-b_i)\end{aligned}$$

**习题3.2 第1题**. 计算行列式

(1).
$\begin{vmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 2 & 3 & 4 \\ 1 & 3 & 5 & 9 \end{vmatrix}$;
$\quad$ (3).
$\begin{vmatrix} x & y & x+y \\ y & x+y & x \\ x+y & x & y \end{vmatrix}$;

(5).
$\begin{vmatrix} a & b & c & d \\ a & a+b & a+b+c & a+b+c+d \\ a & 2a+b & 3a+2b+c & 4a+3b+2c+d \\ a & 3a+b & 6a+3b+c & 10a+6b+3c+d \end{vmatrix}$

**解：**(1).
$\begin{vmatrix} 1 & 1 & 1 & 1 \\ 1 & -1 & 1 & -1 \\ 1 & 2 & 3 & 4 \\ 1 & 3 & 5 & 9 \end{vmatrix} = \begin{vmatrix} 1 & 0 & 0 & 0 \\ 1 & -2 & 0 & -2 \\ 1 & 1 & 2 & 3 \\ 1 & 2 & 4 & 8 \end{vmatrix} = -4 \begin{vmatrix} 1 & 0 & 1 \\ 1 & 2 & 3 \\ 1 & 2 & 4 \end{vmatrix} = -4 \begin{vmatrix} 1 & 0 & 1 \\ 0 & 2 & 2 \\ 0 & 2 & 3 \end{vmatrix} = -8$

(3).
$\begin{vmatrix} x & y & x+y \\ y & x+y & x \\ x+y & x & y \end{vmatrix} = \begin{vmatrix} x & y & 2(x+y) \\ y & x+y & 2(x+y) \\ x+y & x & 2(x+y) \end{vmatrix} = 2(x+y)\begin{vmatrix} 0 & 0 & 1 \\ y-x & x & 1 \\ y & x-y & 1 \end{vmatrix} = 2(x+y)(-(x-y)^2-xy) = -2(x^3+y^3)$

类似的方阵经过行（或列）的调换后可以形成所谓的循环矩阵（Circulant
matrix）。关于循环矩阵的行列式，有一般的结论。

(5). $$\begin{aligned}
& \begin{vmatrix} a & b & c & d \\ a & a+b & a+b+c & a+b+c+d \\ a & 2a+b & 3a+2b+c & 4a+3b+2c+d \\ a & 3a+b & 6a+3b+c & 10a+6b+3c+d \end{vmatrix} = \begin{vmatrix} a & b & c & d \\ 0 & a & a+b & a+b+c \\ 0 & 2a & 3a+2b & 4a+3b+2c \\ 0 & 3a & 6a+3b & 10a+6b+3c \end{vmatrix} \\
= & a \begin{vmatrix} a & a+b & a+b+c \\ 2a & 3a+2b & 4a+3b+2c \\ 3a & 6a+3b & 10a+6b+3c \end{vmatrix} = a \begin{vmatrix} a & a+b & a+b+c \\ 0 & a & 2a+b \\ 0 & 3a & 7a+3b \end{vmatrix} \\
= & a^2 \begin{vmatrix} a & 2a+b \\ 3a & 7a+3b \end{vmatrix} = a^4\end{aligned}$$

**习题3.2 第3题**. 证明

(1).
$\begin{vmatrix} b+c & c+a & a+b \\ q+r & r+p & p+q \\ y+z & z+x & x+y \end{vmatrix} = 2 \begin{vmatrix} a & b & c \\ p & q & r \\ x & y & z \end{vmatrix}$;
$\quad$ (2).
$\begin{vmatrix} 1 & a & a^2-bc \\ 1 & b & b^2-ac \\ 1 & c & c^2-ab \end{vmatrix} = 0$.

**证明：**(1). $$\begin{aligned}
\begin{vmatrix} b+c & c+a & a+b \\ q+r & r+p & p+q \\ y+z & z+x & x+y \end{vmatrix} & = \begin{vmatrix} b & c+a & a+b \\ q & r+p & p+q \\ y & z+x & x+y \end{vmatrix} + \begin{vmatrix} c & c+a & a+b \\ r & r+p & p+q \\ z & z+x & x+y \end{vmatrix} \\
& = \begin{vmatrix} b & c+a & a \\ q & r+p & p \\ y & z+x & x \end{vmatrix} + \begin{vmatrix} c & a & a+b \\ r & p & p+q \\ z & x & x+y \end{vmatrix} \\
& = \begin{vmatrix} b & c & a \\ q & r & p \\ y & z & x \end{vmatrix} + \begin{vmatrix} c & a & b \\ r & p & q \\ z & x & y \end{vmatrix} \\
& = 2 \begin{vmatrix} a & b & c \\ p & q & r \\ x & y & z \end{vmatrix}\end{aligned}$$

(2). $$\begin{aligned}
\begin{vmatrix} 1 & a & a^2-bc \\ 1 & b & b^2-ac \\ 1 & c & c^2-ab \end{vmatrix} & = \begin{vmatrix} 1 & a & a^2-bc \\ 0 & b-a & b^2-ac-a^2+bc \\ 0 & c-a & c^2-ab-a^2+bc \end{vmatrix} = \begin{vmatrix} b-a & (b-a)(a+b+c) \\ c-a & (c-a)(a+b+c) \end{vmatrix} = 0\end{aligned}$$

**习题3.2 第4题**. 计算$n$阶行列式

(2). $D_n = \begin{vmatrix}
a_1 & b_2 & \cdots & b_n \\ c_2 & a_2 & & \\ \vdots & & \ddots & \\ c_n & & & a_n
\end{vmatrix}$

按最后一行展开有 $$\begin{aligned}
D_n & = a_nD_{n-1} + b_nc_na_2\cdots a_{n-1} = a_n(a_{n-1}D_{n-2} + b_{n-1}c_{n-1}a_2\cdots a_{n-2}) + b_nc_na_2\cdots a_{n-1} \\
& = a_na_{n-1}D_{n-2} + b_nc_na_2\cdots a_{n-1} + b_{n-1}c_{n-1}a_2\cdots a_{n-2}a_n \\
& \cdots \\
& = \left( \prod_{i=2}^n a_i \right) D_1 + \sum_{i=2}^n \left( b_ic_i \prod_{2 \leqslant j \leqslant n, j \neq i} a_j \right) \\
& = \prod_{i=1}^n a_i + \sum_{i=2}^n \left( b_ic_i \prod_{2 \leqslant j \leqslant n, j \neq i} a_j \right)\end{aligned}$$

(4). $D_n = \begin{vmatrix}
x & a_1 & a_2 & \cdots & a_{n-1} \\ a_1 & x & a_2 & \cdots & a_{n-1} \\ a_1 & a_2 & x & \cdots & a_{n-1} \\ \vdots & \vdots & \vdots & & \vdots \\ a_1 & a_2 & \cdots & a_{n-1} & x
\end{vmatrix}$

有 $$\begin{aligned}
D_n & = \begin{vmatrix}
x & a_1 & a_2 & \cdots & a_{n-1} \\ a_1 & x & a_2 & \cdots & a_{n-1} \\ a_1 & a_2 & x & \cdots & a_{n-1} \\ \vdots & \vdots & \vdots & & \vdots \\ a_1 & a_2 & \cdots & a_{n-1} & a_{n-1}
\end{vmatrix} + \begin{vmatrix}
x & a_1 & a_2 & \cdots & 0 \\ a_1 & x & a_2 & \cdots & 0 \\ a_1 & a_2 & x & \cdots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ a_1 & a_2 & \cdots & a_{n-1} & x-a_{n-1} \end{vmatrix} \\
& = a_{n-1} \begin{vmatrix}
x-a_1 & a_1-a_2 & a_2-a_3 & \cdots & 0 \\ 0 & x-a_2 & a_2-a_3 & \cdots & 0 \\ 0 & 0 & x-a_3 & \cdots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ a_1 & a_2 & \cdots & a_{n-1} & 1
\end{vmatrix} + (x-a_{n-1}) D_{n-1} \\
& = a_{n-1} \prod_{i=1}^{n-1}(x-a_i) + (x-a_{n-1}) D_{n-1} \\
& = (x-a_{n-1}) \left( (x-a_{n-2})D_{n-2} + a_{n-2}\prod_{i=1}^{n-2}(x-a_i) \right) + a_{n-1} \prod_{i=1}^{n-1}(x-a_i) \\
& = (x-a_{n-1})(x-a_{n-2})D_{n-2} + (a_{n-2} + a_{n-1}) \prod_{i=1}^{n-1}(x-a_i) \\
& \cdots \\
& = x \cdot \prod_{i=1}^{n-1}(x-a_i) + \left( \sum_{i=1}^{n-1} a_i \right) \cdot \prod_{i=1}^{n-1}(x-a_i) = \left(x + \sum_{i=1}^{n-1} a_i \right) \cdot \prod_{i=1}^{n-1}(x-a_i)\end{aligned}$$

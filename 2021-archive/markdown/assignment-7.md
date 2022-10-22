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

(5).
$$\begin{aligned}
& \begin{vmatrix} a & b & c & d \\ a & a+b & a+b+c & a+b+c+d \\ a & 2a+b & 3a+2b+c & 4a+3b+2c+d \\ a & 3a+b & 6a+3b+c & 10a+6b+3c+d \end{vmatrix} = \begin{vmatrix} a & b & c & d \\ 0 & a & a+b & a+b+c \\ 0 & 2a & 3a+2b & 4a+3b+2c \\ 0 & 3a & 6a+3b & 10a+6b+3c \end{vmatrix} \\
= & a \begin{vmatrix} a & a+b & a+b+c \\ 2a & 3a+2b & 4a+3b+2c \\ 3a & 6a+3b & 10a+6b+3c \end{vmatrix} = a \begin{vmatrix} a & a+b & a+b+c \\ 0 & a & 2a+b \\ 0 & 3a & 7a+3b \end{vmatrix} \\
= & a^2 \begin{vmatrix} a & 2a+b \\ 3a & 7a+3b \end{vmatrix} = a^4\end{aligned}$$

**习题3.2 第3题**. 证明

(1).
$\begin{vmatrix} b+c & c+a & a+b \\ q+r & r+p & p+q \\ y+z & z+x & x+y \end{vmatrix} = 2 \begin{vmatrix} a & b & c \\ p & q & r \\ x & y & z \end{vmatrix}$;
$\quad$ (2).
$\begin{vmatrix} 1 & a & a^2-bc \\ 1 & b & b^2-ac \\ 1 & c & c^2-ab \end{vmatrix} = 0$.

**证明：**(1).
$$\begin{aligned}
\begin{vmatrix} b+c & c+a & a+b \\ q+r & r+p & p+q \\ y+z & z+x & x+y \end{vmatrix} & = \begin{vmatrix} b & c+a & a+b \\ q & r+p & p+q \\ y & z+x & x+y \end{vmatrix} + \begin{vmatrix} c & c+a & a+b \\ r & r+p & p+q \\ z & z+x & x+y \end{vmatrix} \\
& = \begin{vmatrix} b & c+a & a \\ q & r+p & p \\ y & z+x & x \end{vmatrix} + \begin{vmatrix} c & a & a+b \\ r & p & p+q \\ z & x & x+y \end{vmatrix} \\
& = \begin{vmatrix} b & c & a \\ q & r & p \\ y & z & x \end{vmatrix} + \begin{vmatrix} c & a & b \\ r & p & q \\ z & x & y \end{vmatrix} \\
& = 2 \begin{vmatrix} a & b & c \\ p & q & r \\ x & y & z \end{vmatrix}\end{aligned}$$

(2).
$$\begin{aligned}
\begin{vmatrix} 1 & a & a^2-bc \\ 1 & b & b^2-ac \\ 1 & c & c^2-ab \end{vmatrix} & = \begin{vmatrix} 1 & a & a^2-bc \\ 0 & b-a & b^2-ac-a^2+bc \\ 0 & c-a & c^2-ab-a^2+bc \end{vmatrix} = \begin{vmatrix} b-a & (b-a)(a+b+c) \\ c-a & (c-a)(a+b+c) \end{vmatrix} = 0\end{aligned}$$

**习题3.2 第4题**. 计算$n$阶行列式

(1).
令原行列式为$D_n$，$\alpha = \begin{pmatrix} a_1 \\ \vdots \\ a_n \end{pmatrix}$,
$\beta = \begin{pmatrix} 1 \\ \vdots \\ 1 \end{pmatrix}$, 那么有
$$\begin{aligned}
D_n & = \det (\alpha-b_1\beta, \alpha-b_2\beta, \cdots, \alpha-b_n\beta) \\
& = \det (\alpha-b_1\beta, (b_1-b_2)\beta, \cdots, (b_1-b_n)\beta)\end{aligned}$$
于是，因为后$n-1$列秩至多为1，若$n \geqslant 3$，那么$D_n = 0$；若$n \leqslant 2$，那么
$$D_n = (b_1-b_2) \det (\alpha-b_1\beta, \beta) = (b_1-b_2)((a_1-b_1)-(a_2-b_1)) = (b_1-b_2)(a_1-a_2).$$

(2). $D_n = \begin{vmatrix}
a_1 & b_2 & \cdots & b_n \\ c_2 & a_2 & & \\ \vdots & & \ddots & \\ c_n & & & a_n
\end{vmatrix}$

按最后一行展开有
$$\begin{aligned}
D_n & = a_nD_{n-1} + (-1)^{1+n} (-1)^{1+(n-1)} b_nc_na_2\cdots a_{n-1} = a_n(a_{n-1}D_{n-2} - b_{n-1}c_{n-1}a_2\cdots a_{n-2}) - b_nc_na_2\cdots a_{n-1} \\
& = a_na_{n-1}D_{n-2} - b_nc_na_2\cdots a_{n-1} - b_{n-1}c_{n-1}a_2 \cdots a_{n-2}a_n \\
& \cdots \\
& = \left( \prod_{i=2}^n a_i \right) D_1 - \sum_{i=2}^n \left( b_ic_i \prod_{2 \leqslant j \leqslant n, j \neq i} a_j \right) \\
& = \prod_{i=1}^n a_i - \sum_{i=2}^n \left( b_ic_i \prod_{2 \leqslant j \leqslant n, j \neq i} a_j \right)\end{aligned}$$

(3). 令原行列式为$D_n$，$e_i, i=1,\cdots,n,$
为$\mathbb{F}^n$的自然基，$\beta = \begin{pmatrix} 1 \\ \vdots \\ 1 \end{pmatrix}$,
那么有
$$\begin{aligned}
D_n & = \det (-2e_1+3\beta, -e_2+3\beta, 3\beta, e_4+3\beta, \cdots, (n-3)e_n+3\beta) \\
& = \det (-2e_1, -e_2, 3\beta, e_4, \cdots, (n-3)e_n)\end{aligned}$$
于是当$n \geqslant 3$时，$D_n = 6 \cdot (n-3)!$，$D_2 = -4$, $D_1 = 1$.

(4). $D_n = \begin{vmatrix}
x & a_1 & a_2 & \cdots & a_{n-1} \\ a_1 & x & a_2 & \cdots & a_{n-1} \\ a_1 & a_2 & x & \cdots & a_{n-1} \\ \vdots & \vdots & \vdots & & \vdots \\ a_1 & a_2 & \cdots & a_{n-1} & x
\end{vmatrix}$

有
$$\begin{aligned}
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

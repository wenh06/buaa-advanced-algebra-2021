**习题3.5 第1题**.

(1).
$$\begin{aligned}
D_n & = \begin{vmatrix} 1 & 2 & 3 & \cdots & n \\ x & 1 & 2 & \cdots & n-1 \\ x & x & 1 & \cdots & n-2 \\ \vdots & \vdots & \vdots & & \vdots \\ x & x & x & \cdots & 1 \end{vmatrix} = \begin{vmatrix} 1 & 1 & 1 & \cdots & 1 \\ x & 1-x & 1 & \cdots & 1 \\ \vdots & & \ddots & \ddots & \vdots \\ \vdots & & & \ddots & 1 \\ x & & & & 1-x \end{vmatrix} \\
& = \begin{vmatrix} 1-x & 1 & 1 & \cdots & 1 \\ 0 & 1-x & 1 & \cdots & 1 \\ \vdots & & \ddots & \ddots & \vdots \\ 0 & & & \ddots & 1 \\ x^2 & & & & 1-x \end{vmatrix} = \begin{vmatrix} 1-x & 1 & 0 & \cdots & 0 \\ 0 & 1-x & x & \cdots & 0 \\ \vdots & & \ddots & \ddots & \vdots \\ 0 & & & \ddots & x \\ x^2 & & & & 1-x \end{vmatrix} \\
& = (1-x) \begin{vmatrix} 1-x & x & & \\ & \ddots & \ddots & \\ & & \ddots & x \\ & & & 1-x \end{vmatrix} + (-1)^{n+1}x^2 \begin{vmatrix} 1 & & & \\ 1-x & x & & \\ & \ddots & \ddots & \\ & & 1-x & x \end{vmatrix} \\
& = (1-x)^n + (-1)^{n+1}x^n\end{aligned}$$

(2).
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
令$\alpha_1 = \begin{pmatrix} -a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}$,
$\ldots$,
$\alpha_n = \begin{pmatrix} a_1 \\ \vdots \\ a_{n-1} \\ -a_n \end{pmatrix}$,
$e = \begin{pmatrix} 1 \\ \vdots \\ 1 \end{pmatrix}$, 那么类似第一题有
$$\begin{aligned}
D_n & = \det(\alpha_1 + a_1e, \cdots, \alpha_n + a_ne) \\
& = 2\det(\alpha_1, \cdots, \alpha_n) - \det\begin{pmatrix} 1 & a_1 & \cdots & a_n \\ e & \alpha_1 & \cdots & \alpha_n \end{pmatrix}\end{aligned}$$
这两个都是比较好计算的行列式。

**习题5.1 第4题**.
设$f(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0$是数域$\mathbb{F}$上的多项式，$c\in\mathbb{F}$.
求证：$x-c$除$f(x)$的商$q(x) = b_{n-1}x^{n-1} + \cdots + b_1x + b_0$和余式$r$可以用如下的算法得出
$$\begin{array}{c|cccccccc}
c & & a_n & a_{n-1} & \cdots & a_i & \cdots & a_1 & a_0 \\
& +) & & cb_{n-1} & \cdots & cb_i & \cdots & cb_1 & cb_0 \\ \hline
& & b_{n-1} & b_{n-1} & \cdots & b_{i-1} & \cdots & b_0 & r
\end{array}$$ 其中$b_{n-1} = a_n$,
$b_{i-1} = a_i + cb_i \ (\forall 1 \leqslant i \leqslant n)$,
$r = a_0 + cb_0$.

**证明**：考虑$f(x) = (x-c)g(x) + r$, 即 $$\begin{aligned}
a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0 = & \ (x-c) (b_{n-1}x^{n-1} + \cdots + b_1x + b_0) + r \\
= & \ b_{n-1}x^{n} + \cdots + b_1x^2 + b_0x + r \\
& \ - cb_{n-1}x^{n-1} - \cdots - cb_1x - cb_0\end{aligned}$$
移项之后即有
$$a_nx^n + (a_{n-1}+cb_{n-1})x^{n-1} + \cdots + (a_1+cb_1)x + (a_0 + cb_0) = b_{n-1}x^{n} + \cdots + b_1x^2 + b_0x + r,$$
对应次项的系数相等，从而有$b_{n-1} = a_n, b_{n-2} = a_{n-1}+cb_{n-1}, \ldots, b_0 = a_1+cb_1, r = a_0 + cb_0$.

**习题5.1 第8题**. 给定正整数$k\geqslant 2$,
求非零实系数多项式$f(x)$满足条件$f(x^k) = (f(x))^k$.

**解**：设非零实系数多项式$f(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0$,
$a_n\neq 0$, $n\geqslant 0$, 满足$f(x^k) = (f(x))^k$.
考察最高次项，有$a_n^k = a_n$. 因为$f(x)$是实系数多项式，$k\geqslant 2$,
于是有
$$a_n = \begin{cases}\pm 1 & \text{$k$为奇数}, \\ 1 & \text{$k$为偶数}. \end{cases}$$

假设除$a_n$外还有系数非零，最高次项为$a_mx^m$,
$0 \leqslant m \leqslant n-1$, 那么$f(x) = a_nx^n + a_mx^m + g(x)$,
其中$\deg g < m$. 那么 $$\begin{aligned}
& (f(x))^k = a_n^kx^{kn} + ka_mx^{(k-1)n+m} + h(x) \\
& f(x^k) = a_nx^{kn} + a_mx^{km} + g(x^k)\end{aligned}$$
其中$\deg h < (k-1)n+m$.
因为$0 \leqslant m \leqslant n-1$且$k\geqslant 2$,
所以$(k-1)n+m \neq km$. 所以要使$f(x^k) = (f(x))^k$, 必须有$ka_m = 0$,
即$a_m = 0$. 这与假设矛盾. 所以除最高次项外, $f(x)$没有其他非零项。所以
$$f(x) = \begin{cases}\pm x^n & \text{$k$为奇数}, \\ x^n & \text{$k$为偶数}. \end{cases} \quad n = 0, 1, \ldots$$

**习题5.2 第3题**. 对如下多项式$f(x), g(x)$,
求次数最低的多项式$u(x), v(x)$, 使$u(x)f(x) + v(x)g(x) = 1$.

(1). $f(x) = x^3, g(x) = (x-3)^2$

**解**：辗转相除有 $$\begin{aligned}
x^3 & = (x+6) \cdot (x-3)^2 + 27(x-2) \\
(x-3)^2 & = \frac{x-4}{27} \cdot 27(x-2) + 1\end{aligned}$$ 进行回代，有
$$1 = \left( 1 + \frac{(x-4)(x+6)}{27} \right) \cdot (x-3)^2 + \frac{-x+4}{27} \cdot x^3$$
于是$u(x) = \frac{-x+4}{27}$, $v(x) = \frac{x^2+2x+3}{27}$.

**习题5.2 第4题**.
如果两个整系数三次方程有公共的无理根，那么它们还有另一个公共根。

**证明**：设整系数三次方程$f(x) = 0, g(x) = 0$有公共无理根$\alpha\in\mathbb{R}$.
令$h(x)\in\mathbb{Q}[x]$为$\alpha$在$\mathbb{Q}$上的极小多项式，即满足$h(\alpha) = 0$的首一的有理系数多项式中次数最低的。首先，$\deg h \leqslant \deg f$.
其次，必须有$h(x)|f(x)$,
否则可以在$\mathbb{Q}[x]$上做带余除法$f(x) = h(x)\cdot s(x) + r(x)$,
其中$\deg r < \deg h$,
这与$h(x)$的定义矛盾。基于同样的原因，有$h(x)|g(x)$.

由于$\alpha$是无理数，所以$\deg h \geqslant 2$,
而且$h(x)$没有有理根，否则$h(x) = h'(x)(x-\beta)$, $\beta\in\mathbb{Q}$,
$h'(x)\in\mathbb{Q}[x]$, $\deg h' < \deg h$, $h'(\alpha) = 0$.

综上可知，$f(x)$与$g(x)$除了$\alpha$外，还至少有另一个公共无理根，为$h(x)$的根。

**习题5.2 第8题**. 已知多项式$r_1(x) = x^2+2x+3$, $r_2(x) = 3x-7$.
矩阵$A = \begin{pmatrix} A_1 & 0 \\ 0 & A_2 \end{pmatrix}$,
$B = \begin{pmatrix} B_1 & 0 \\ 0 & B_2 \end{pmatrix}$, 其中
$$A_1 = \begin{pmatrix} 0 & 1 & 0 \\ & 0 & 1 \\ & & 0 \end{pmatrix}, A_2 = \begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}, B_1 = \begin{pmatrix} 3 & 2 & 1 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{pmatrix}, B_2 = \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix}.$$
试验证$r_1(A_1) = B_1$, $r_2(A_2) = B_2$.
并求一个最低次数的多项式$f(x)$使$f(A) = B$.

**解**：容易算得$A_1^2 = \begin{pmatrix} 0 & 0 & 1 \\ & 0 & 0 \\ & & 0 \end{pmatrix}$,
所以
$$r_1(A_1) = A_1^2 + 2A_1 + 3 = \begin{pmatrix} 0 & 0 & 1 \\ & 0 & 0 \\ & & 0 \end{pmatrix} + \begin{pmatrix} 0 & 2 & 0 \\ & 0 & 2 \\ & & 0 \end{pmatrix} + 3 = \begin{pmatrix} 3 & 2 & 1 \\ & 3 & 2 \\ & & 3 \end{pmatrix} = B_1.$$
$r_2(A_2)$可以直接计算
$$r_2(A_2) = 3\begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix} - 7 = \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix} = B_2.$$

易知$f(A) = f(\begin{pmatrix} A_1 & 0 \\ 0 & A_2 \end{pmatrix}) = \begin{pmatrix} f(A_1) & 0 \\ 0 & f(A_2) \end{pmatrix}$.那么要使$f(A) = B$,
只要使$f(A_1) = B_1$,
$f(A_2) = B_2$即可。易知$A_1$的极小多项式为$g_1(x) = x^3$,
$A_2$的极小多项式为$g_2(x) = (x-3)^2$, 所以多项式$f(x)$就是满足
$$f(x) \equiv r_1(x) \mod g_1(x), \quad f(x) \equiv r_2(x) \mod g_2(x)$$
的次数最低的多项式。这一问便化为了习题5.2第7题。

根据习题5.2第3题第(1)问，有$u(x) = \frac{-x+4}{27}$,
$v(x) = \frac{x^2+2x+3}{27}$, 使得$g_1(x)u(x) + g_2(x)v(x) = 1$, 那么
$$\begin{aligned}
f_0(x) & := g_1(x)u(x)r_2(x) + g_2(x)v(x)r_1(x) \\
& = x^3 \cdot \frac{-x+4}{27} \cdot (3x-7) + (x-3)^2 \cdot \frac{x^2+2x+3}{27} \cdot (x^2+2x+3)\end{aligned}$$
即满足
$$f_0(x) \equiv r_1(x) \mod g_1(x), \quad f_0(x) \equiv r_2(x) \mod g_2(x)$$
由于任意两个满足上式的多项式$f(x),f'(x)$,
都必须有$g_1(x)g_2(x) | (f(x)-f'(x))$,
所以次数最低的$f(x)$即为$f_0(x)$除以$g_1(x)g_2(x)$的余式:
$$\begin{aligned}
f(x) & = f_0(x) \mod g_1(x)g_2(x) = (g_1(x)u(x)r_2(x) + g_2(x)v(x)r_1(x)) \mod g_1(x)g_2(x) \\
& = g_1(x) \cdot (u(x)r_2(x) \mod g_2(x)) + g_2(x) \cdot (v(x)r_1(x) \mod g_1(x)) \\
& = \frac{x^3}{27} ( (-x+4) \cdot (3x-7) \mod (x-3)^2) + \frac{(x-3)^2}{27}( (x^2+2x+3) \cdot (x^2+2x+3) \mod x^3) \\
& = \frac{x^3}{27} (x-1) + \frac{(x-3)^2}{27}(10x^2+12x+9) \\
& = \frac{1}{27}(11x^4 - 49x^3 + 27x^2 + 54x + 81)\end{aligned}$$

**第6题**.
设$V = \mathbb{F}[x]$是$\mathbb{F}$上全体一元多项式关于多项式加法和数乘多项式运算构成的$\mathbb{F}$上线性空间，用$V_n = \mathbb{F}_n[x]$表示$V$中全体次数$\leqslant n$的多项式集合，则$V_n$构成$V$的一个子空间，

(1). 证明$1, x-1, \ldots, (x-1)^n$构成$V_n$的一组基

(2). 对于$f(x) = x^n + \cdots + x + 1 \in V_n$,
求$f(x)$在上述基下的坐标。

**解**：这题基本与习题2.7第7题类似。在哪里我们考察的是$x-c$,
$c\in\mathbb{F}$, 是比$x-1$更一般的情况。 以下我们都考察$x-c$的情形。

(1).
只要证明$1, (x-c), (x-c)^2, \cdots, (x-c)^n$线性无关即可。假设存在不全为0的实数$\lambda_0,\cdots,\lambda_n$使得
$$f_0(x) = \lambda_0 + \lambda_1(x-c) + \cdots + \lambda_n(x-c)^n = 0$$
那么$f_0(x)$的$n$阶导函数$f_0^{(n)}(x) = n!\lambda_n = 0$，从而有$\lambda_n = 0$。逐步反推可以导出$\lambda_{n-1} = \cdots = \lambda_0 = 0$，矛盾。

(2).
我们考虑一个更一般的$n$次多项式$f(x) = a_0 + a_1x + \cdots + a_nx^n = \lambda_0 + \lambda_1(x-c) + \cdots + \lambda_n(x-c)^n$，那么$f_0^{(n)}(x) = n! a_n = n! \lambda_n$，故$\lambda_n = a_n$。将所得的$\lambda_n,\cdots,\lambda_{n-k}$回代，并考察$f_0^{(n-k-1)}(c)$，则有
$$f_0^{(n-k-1)}(c) = (n-k-1)!\lambda_{n-k-1} = (n-k-1)!a_{n-k-1} + \dfrac{(n-k)!}{1!} c a_{n-k} + \cdots + \dfrac{n!}{(k+1)!} c^{k+1} a_{n}$$
得$\lambda_{n-k-1} = a_{n-k-1} + C_{n-k}^1c a_{n-k} + \cdots + C_{n}^{k+1}c^{k+1} a_{n}$
所以有 $$\begin{pmatrix} \lambda_n \\ \vdots \\ \lambda_0 \end{pmatrix}
= \begin{pmatrix} 1 & & & & \\ C_{n}^1c & 1 & & & \\ C_{n}^2c^2 & C_{n-1}^1c & 1 & & \\ \vdots & \vdots & \vdots & \ddots & \\ C_{n}^1c^n & C_{n-1}^{n-1}c^{n-1} & C_{n-2}^{n-2}c^{n-2} & \cdots & 1 \end{pmatrix}
\begin{pmatrix} a_n \\ \vdots \\ a_0 \end{pmatrix} = A\begin{pmatrix} a_n \\ \vdots \\ a_0 \end{pmatrix}.$$
故$f(x) = a_0 + a_1x + \cdots + a_nx^n$在这组基下的坐标为
$$\begin{pmatrix} \lambda_n \\ \vdots \\ \lambda_0 \end{pmatrix} = A \begin{pmatrix} a_n \\ \vdots \\ a_0 \end{pmatrix}.$$

若考察$f_0^{(n-k-1)}(0)$，则有
$$f_0^{(n-k-1)}(0) = (n-k-1)!a_{n-k-1} = (n-k-1)!\lambda_{n-k-1} + \dfrac{(n-k)!}{1!} (0-c)\lambda_{n-k} + \cdots + \dfrac{n!}{(k+1)!} (0-c)^{k+1}\lambda_{n}$$
得$a_{n-k-1} = \lambda_{n-k-1} + C_{n-k}^1(-c)\lambda_{n-k} + \cdots + C_{n}^{k+1}(-c)^{k+1}\lambda_{n}$
所以有 $$\begin{pmatrix} a_n \\ \vdots \\ a_0 \end{pmatrix}
= \begin{pmatrix} 1 & & & & \\ C_{n}^1(-c) & 1 & & & \\ C_{n}^2(-c)^2 & C_{n-1}^1(-c) & 1 & & \\ \vdots & \vdots & \vdots & \ddots & \\ C_{n}^1(-c)^n & C_{n-1}^{n-1}(-c)^{n-1} & C_{n-2}^{n-2}(-c)^{n-2} & \cdots & 1 \end{pmatrix}
\begin{pmatrix} \lambda_n \\ \vdots \\ \lambda_0 \end{pmatrix}
= B \begin{pmatrix} \lambda_n \\ \vdots \\ \lambda_0 \end{pmatrix}$$
则$f(x) = a_0 + a_1x + \cdots + a_nx^n$在这组基下的坐标为
$$\begin{pmatrix} \lambda_n \\ \vdots \\ \lambda_0 \end{pmatrix} = B^{-1} \begin{pmatrix} a_n \\ \vdots \\ a_0 \end{pmatrix}.$$

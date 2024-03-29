---
date: 2022-12-2 第七次习题课
title: 2022秋高等代数习题课
---

**第一题** (习题5.4第4题)

-   求以$2 + \sqrt{3}$为根的最低次数的首一的有理系数多项式$g(x).$

-   设$f(x) = x^5 - 4x^4 + 3x^3 - 2x^2 + x - 1,$ 求$f(2 + \sqrt{3}).$

-   用(1)中求出的$g(x)$除$f(x) = x^5 - 4x^4 + 3x^3 - 2x^2 + x - 1$得到商$q(x)$和余式$r(x),$
    将$f(x)$写成$f(x) = q(x) g(x) + r(x)$的形式，再将$x = 2 + \sqrt{3}$代入求$f(2 + \sqrt{3}).$
    是否比(2)中更简便？

-   设$h(x)$是任一有理系数多项式，$2 + \sqrt{3}$是$h(x)$的根，求证：$g(x)$整除$h(x),$
    并且$2 - \sqrt{3}$也是$h(x)$的根。

**解**： (1) 记$a = 2 + \sqrt{3},$ 容易看到$(a - 2)^2 = 3,$ 所以多项式
$$(x - 2)^2 - 3 = x^2 - 4x + 1$$ 的一个根为$a.$
此多项式为2次的首一的有理系数多项式。由于$2 + \sqrt{3}$不是有理数，所以$g(x)$次数必须大于$1.$（大家应该在数学分析课上证明过类似$\sqrt{3}$不是有理数这种结论）因此
$$g(x) = x^2 - 4x + 1$$
即为以$2 + \sqrt{3}$为根的最低次数的首一的有理系数多项式。假设$h(x)$是另一个以$2 + \sqrt{3}$为根的2次的首一的有理系数多项式。那么$\deg (g - h) < 2,$
且$(g - h)(2 + \sqrt{3}) = g(2 + \sqrt{3}) - h(2 + \sqrt{3}) = 0,$
那么必须有$h = g,$
否则$g - h$就是一个以$2 + \sqrt{3}$为根的次数低于2的多项式，与$2 + \sqrt{3}$不是有理数矛盾。

\(2\) 由于$a = 2 + \sqrt{3}$满足$g(a) = 0,$ 即$a^2 - 4a + 1 = 0,$ 即
$$a^2 = 4a - 1.$$
根据上式，可以以一种递归的方式把$a^n$化为$a$的1次多项式，$n\geqslant 2:$
$$\begin{aligned}
a^3 & = a \cdot a^2 = a(4a - 1) = 4a^2 - a = 4(4a - 1) - a = 15a - 4 \\
a^4 & = a \cdot a^3 = a(15a - 4) = 15(4a - 1) - 4a = 56a - 15 \\
a^5 & = a \cdot a^4 = a(56a - 15) = 56(4a - 1) - 15a = 209a - 56\end{aligned}$$
因此有 $$\begin{aligned}
f(a) & = a^5 - 4a^4 + 3a^3 - 2a^2 + a - 1 \\
& = (209a - 56) - 4(56a - 15) + 3(15a - 4) - 2(4a - 1) + a - 1 \\
& = 23a - 7 = 23(2 + \sqrt{3}) - 7 \\
& = 39 + 23\sqrt{3}\end{aligned}$$

\(3\) 我们用多项式的带余除法： $$\begin{aligned}
r_1(x) & = f(x) - {\color{red} x^3} \cdot g(x) = - 4x^4 + 3x^3 - 2x^2 + x - 1 - x^3 (- 4x + 1) \\
& = - 4x^4 + 3x^3 - 2x^2 + x - 1 + 4x^4 - x^3 \\
& = 2x^3 - 2x^2 + x - 1 \\
r_2(x) & = r_1(x) - {\color{red} 2x} \cdot g(x) = - 2x^2 + x - 1 - 2x (- 4x + 1) \\
& = - 2x^2 + x - 1 + 8x^2 - 2x \\
& = 6x^2 - x - 1 \\
r_3(x) & = r_2(x) - {\color{red} 6} \cdot g(x) = - x - 1 - 6 (- 4x + 1) = 23 x - 7\end{aligned}$$
因为$\deg r_3 = 1 < 2 = \deg g,$
带余除法结束。可以看到和(2)中计算结果一致。或者我们写成更加熟悉的形式：

::: center
:::

\(4\)
若$2 + \sqrt{3}$是$h(x)$的根，那么根据$g(x)$的选取知道$\deg h \geqslant \deg g.$
于是令$h(x) = g(x) q(x) + r(x),$ $\deg r < \deg g.$ 若$r(x) \neq 0,$
那么$2 + \sqrt{3}$也是$r(x)$的根，这与$2 + \sqrt{3}$不是有理数矛盾。于是必须有$r(x) = 0,$
即知$g(x)$整除$h(x).$
由于$2 - \sqrt{3}$是$g(x)$的根，从而也是$h(x)$的根。

这里$2 - \sqrt{3}$是$2 + \sqrt{3}$的共轭元（在involution
$\sigma: \mathbb{Q}(\sqrt{3}) / \mathbb{Q} \to \mathbb{Q}(\sqrt{3}) / \mathbb{Q}, ~ \sqrt{3} \mapsto -\sqrt{3}$下），从而也是$g(x)$的根。类似的结论大家会在日后要学习的抽象代数、代数数论等后续课程中学习更多。

**第二题** (习题5.4第6题) 求多项式$x^3 + px + q$有重根的条件。

Hint: 这题考察了 "5.4.2 重因式与重根" 的知识。

**解**： 令$f(x) = x^3 + px + q.$ 由定理5.4.3知，
$$f(x) \text{ 有重根 } \Longleftrightarrow \left( f(x), f'(x) \right) = r(x) \neq 1.$$
容易算得$f'(x) = 3x^2 + p.$ 利用辗转相除法（同时假设$p\neq 0$），
$$\begin{aligned}
r_1(x) & = f(x) - {\color{red} \dfrac{1}{3}x} \cdot f'(x) = x^3 + px + q - \left( x^3 + \dfrac{p}{3}x \right) = \dfrac{2}{3}px + q \\
r_2(x) & = f'(x) - {\color{red} \left( \dfrac{9}{2p}x - \dfrac{27q}{4p^2} \right)} \cdot r_1(x) \\
& = 3x^2 + p - \left( 3x^2 + \dfrac{9q}{2p}x - \dfrac{9q}{2p}x - \dfrac{27q^2}{4p^2} \right) = p + \dfrac{27q^2}{4p^2}\end{aligned}$$
于是必须有$0 = r_2(x) = p + \dfrac{27q^2}{4p^2},$ 即$4p^3 + 27q^2 = 0.$
以上辗转相除过程中的$\dfrac{1}{3}x, \dfrac{9}{2p}x - \dfrac{27q}{4p^2}$都是多项式的带余除法得到的商。

若$p = 0,$ 那么显然只要$q$不等于0,
$f(x)$就没有重根。所以，此时$f(x)$有重根$\Rightarrow q = 0.$
这个关系也能用$4p^3 + 27q^2 = 0$表达。

更一般地，我们可以通过多项式的判别式（discriminant）来判断它是否有重根。一个多项式有重根当且仅当它的判别式为0.
例如我们在中学已经学习过了，对一个二次多项式$f(x) = ax^2 + bx + c,$
$a \neq 0,$
它在实数域内的根的情况完全由它的判别式$\Delta = b^2 - 4ac$决定：

-   $\Delta > 0 \Rightarrow$ $f(x)$在$\mathbb{R}$内有两个不同的实根；

-   $\Delta = 0 \Rightarrow$ $f(x)$在$\mathbb{R}$内有一个实根；

-   $\Delta < 0 \Rightarrow$
    $f(x)$在$\mathbb{R}$内无实根，但在$\mathbb{C}$内有两个共轭（不同）的虚根。

设$n$次多项式
$$f(x) = a_{n}x^{n} + a_{n-1}x^{n-1} + \cdots + a_{0}, ~ a_n \neq 0,$$
系数属于某个域$\mathbb{F},$ 那么它的判别式定义为
$$\operatorname{Disc}_x(f) = a_n^{2n-2} \prod_{1 \leqslant i < j \leqslant n} (\lambda_i - \lambda_j)^2 \in \mathbb{F}.$$
这里的$\lambda_1, \ldots, \lambda_n$为$f(x)$在代数闭域$\bar{\mathbb{F}}$内的根。

多项式$f$的判别式可以利用多项式$f$与它的微商$f'$的结式（resultant）进行计算。一般地，设
$$g(x) = b_{m}x^{m} + b_{m-1}x^{m-1} + \cdots + b_{0}, ~ b_m \neq 0,$$
是另一个系数在域$\mathbb{F}$内的$m$次多项式，那么$f, g$的结式被定义为
$$\operatorname{Res} (f, g) = a_n^n b_m^m \prod_{ \substack{(\lambda, \mu) \in \bar{\mathbb{F}}^2 \\ f(\lambda) = 0, g(\mu) = 0}} (\lambda - \mu) \in \mathbb{F}$$
可以看出判别式与结式的关系为
$$\operatorname{Disc}_{x}(f) = \frac{(-1)^{n(n-1)/2}}{a_{n}} \operatorname{Res}_{x}(f, f')$$
可以很容易地列举结式的部分性质：

-   $\operatorname{Res} (f, g) = (-1)^{mn} \operatorname{Res} (g, f)$

-   $\operatorname{Res} (f_1f_2, g) = \operatorname{Res} (f_1, g) \cdot \operatorname{Res} (f_2, g)$

-   设$r(x) = f(x) - q(x) \cdot g(x)$,
    那么$\operatorname{Res} (r, g) = b_m^{\deg r - n}\operatorname{Res} (f, g)$

结式可用如下的（Sylvester matrix的）行列式进行计算
$$\operatorname{Res} (f, g) = \begin{vmatrix} a_{n} & 0 & \cdots & 0 & b_{m} & 0 & \cdots & 0 \\ a_{n-1} & a_{n} & \cdots & 0 & b_{m-1} & b_{m} & \cdots & 0 \\ a_{n-2} & a_{n-1} & \ddots & 0 & b_{m-2} & b_{m-1} & \ddots & 0 \\ \vdots & \vdots & \ddots & a_{n} & \vdots & \vdots & \ddots & b_{m} \\ a_{0} & a_{1} & \cdots & \vdots & b_{0} & b_{1} & \cdots & \vdots \\ 0 & a_{0} & \ddots & \vdots & 0 & b_{0} & \ddots & \vdots \\ \vdots & \vdots & \ddots & a_{1} & \vdots & \vdots & \ddots & b_{1} \\ 0 & 0 & \cdots & a_{0} & 0 & 0 & \cdots & b_{0}\end{vmatrix}_{(m+n) \times (m+n)}$$

可以算得三次多项式$f(x) = x^3 + px + q$的判别式为
$$\operatorname{Disc}_x(f) = -4p^3 - 27q^2.$$

Python软件包sympy提供了计算多项式判别式的功能，例子如下

::: center
``` {.python language="Python"}
>>> import sympy as sp
>>> x, p, q = sp.symbols("x, p, q")
>>> f = sp.Poly(x**3 + p * x + q, x)
>>> f.discriminant()
```
:::

更多例子可见[Jupyter
Notebook](https://gitee.com/wenh06/buaa-advanced-algebra-2021/blob/master/notebooks/class-7.ipynb).

**第三题** (习题5.4第8题(2))
$n_1, n_2, n_3, n_4, n_5$是任意正整数，证明：
$$(x^4 + x^3 + x^2 + x + 1) | (x^{5n_1} + x^{5n_2+1} + x^{5n_3+2} + x^{5n_4+3} + x^{5n_5+4})$$

Hint: 这题考察了同余的一些性质：

-   $a \equiv b \mod{m}, c \equiv d \mod{m} \Rightarrow a-c \equiv b-d \mod{m}.$

-   $a \equiv b \mod{m}, c \equiv d \mod{m} \Rightarrow ac \equiv bd \mod{m},$
    特别地，$a^k \equiv b^k \mod{m}.$

**解**：
考察$x^{5n+k} = (x^5)^n \cdot x^k$除以$x^4 + x^3 + x^2 + x + 1$的余式，其中$n$为任意正整数，$0 \leq k < 5.$
由同余的形式知道，我们只要计算$x^5$除以$x^4 + x^3 + x^2 + x + 1$的余式即可。由于
$$x^5 = (x-1) \cdot (x^4 + x^3 + x^2 + x + 1) + 1,$$ 所以有
$$x^5 \equiv 1 \mod{x^4 + x^3 + x^2 + x + 1},$$ 进而有
$$x^{5n+k} \equiv 1^n \cdot x^k = x^k \mod{x^4 + x^3 + x^2 + x + 1}.$$
所以 $$\begin{gathered}
x^{5n_1} + x^{5n_2+1} + x^{5n_3+2} + x^{5n_4+3} + x^{5n_5+4} \\
\equiv 1 + x + x^2 + x^3 + x^4 \equiv 0 \mod{x^4 + x^3 + x^2 + x + 1},\end{gathered}$$
即$(x^4 + x^3 + x^2 + x + 1) | (x^{5n_1} + x^{5n_2+1} + x^{5n_3+2} + x^{5n_4+3} + x^{5n_5+4}).$

**第四题** 设$f(x) = a_n x^n + \cdots + a_1 x + a_0 \in \mathbb{C}[x],$
$a_n \neq 0,$ 且$f(x)$的$n$个根为$\alpha_1, \ldots, \alpha_n.$ 求

-   以$c\alpha_1, \ldots, c\alpha_n$为根的一个$n$次多项式，$c \neq 0.$

-   以$1/\alpha_1, \ldots, 1/\alpha_n$为根的一个$n$次多项式，$\alpha_i \neq 0.$

**解**： (1) 依题，我们有
$$f(x) = a_n x^n + \cdots + a_1 x + a_0 = a_n \prod\limits_{i=1}^n (x - \alpha_i),$$
从而有
$$\dfrac{a_{n-k}}{a_n} = (-1)^k e_k(\alpha_1, \ldots, \alpha_n) = (-1)^k \sum\limits_{1 \leqslant j_{1} < j_{2} < \cdots < j_{k} \leqslant n} \alpha_{j_{1}} \dotsm \alpha_{j_{k}},$$
这里的$e_k = e_k(\alpha_1, \ldots, \alpha_n),$
$0\leqslant k \leqslant n,$
是$\alpha_1, \ldots, \alpha_n$的初等对称多项式，同时约定$e_0 = 1.$

若$g(x)$以$c\alpha_1, \ldots, c\alpha_n$为根，那么 $$\begin{aligned}
g(x) & = t \prod\limits_{i=1}^n (x - c\alpha_i) = t \sum\limits_{k=0}^n x^{n-k} (-c)^k e_k \\
& = t \sum\limits_{k=0}^n x^{n-k} (-c)^k (-1)^k \dfrac{a_{n-k}}{a_n} = \dfrac{t}{a_n} \sum\limits_{k=0}^n x^{n-k} c^k a_{n-k} \\
& = \dfrac{t}{a_n} \sum\limits_{k=0}^n c^{n-k} a_k x^k\end{aligned}$$
取$t = a_n,$
则$g(x) = \sum\limits_{k=0}^n c^{n-k} a_k x^k$以$c\alpha_1, \ldots, c\alpha_n$为根。

\(2\) 考虑有理式
$$\tilde{f}(x) = f \left( \dfrac{1}{x} \right) = a_n \dfrac{1}{x^n} + \cdots + a_1 \dfrac{1}{x} + a_0 = \dfrac{\sum\limits_{k=0}^n a_k x^{n-k}}{x^n} = \dfrac{g(x)}{h(x)}.$$
其中$g(x) = \sum\limits_{k=0}^n a_k x^{n-k}, h(x) = x^n$为多项式。那么任取$\alpha_k,$
令$x = 1/\alpha_k,$ 有 $$\tilde{f}(x) = f(1/x) = f(\alpha_k) = 0,$$
同时$h(x) = h(1/\alpha_k) = 1/\alpha_k^n \neq 0,$
所以必须有$g(1/\alpha_k) = 0.$
于是$g(x) = \sum\limits_{k=0}^n a_k x^{n-k}$就是一个以$1/\alpha_1, \ldots, 1/\alpha_n$为根的$n$次多项式。

**第五题**
给出实系数$4$次多项式在$\mathbb{R}$上所有不同类型的标准分解式。

**解**： $4$次实系数多项式在复数域$\mathbb{C}$上的根的所有可能的情况如下

-   有4个实根$a_1, a_2, a_3, a_4;$

-   有2个实根$a_1, a_2,$ 以及1对复共轭的虚根$a \pm bi;$

-   有2对复共轭的虚根$a_1 \pm b_1i, a_2 \pm b_2i.$

于是，对应第一种情况的分解式为 $$f(x) = t(x-a_1)(x-a_2)(x-a_3)(x-a_4);$$
对应第二种情况的分解式为 $$\begin{aligned}
f(x) & = t(x-a_1)(x-a_2)(x-(a + bi))(x-(a - bi)) \\
& = t(x-a_1)(x-a_2)(x^2-2ax+a^2+b^2);\end{aligned}$$
对应第二种情况的分解式为 $$\begin{aligned}
f(x) & = t(x-(a_1 + b_1i))(x-(a_1 - b_1i))(x-(a_2 + b_2i))(x-(a_2 - b_2i)) \\
& = t(x^2-2a_1x+a_1^2+b_1^2)(x^2-2a_2x+a_2^2+b_2^2).\end{aligned}$$
以上的$a, b, a_1, a_2, a_3, a_4, b_1, b_2, t \in \mathbb{R},$
$t \neq 0.$

**第六题 (习题5.1 第8题)** 给定正整数$k\geqslant 2$,
求非零实系数多项式$f(x)$满足条件$f(x^k) = (f(x))^k$.

**解**：设非零实系数多项式$f(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0$,
$a_n\neq 0$, $n\geqslant 0$, 满足$f(x^k) = (f(x))^k$.
考察最高次项，有$a_n^k = a_n$. 因为$f(x)$是实系数多项式，$k\geqslant 2$,
$a^{k-1} = 1$的实根至多是$\pm 1.$ 于是有
$$a_n = \begin{cases}\pm 1 & \text{$k$为奇数}, \\ 1 & \text{$k$为偶数}. \end{cases}$$

假设除$a_n$外还有系数非零，最高次项为$a_mx^m$,
$0 \leqslant m \leqslant n-1$, 那么$f(x) = a_nx^n + a_mx^m + g(x)$,
其中$\deg g < m$. 那么 $$\begin{aligned}
& (f(x))^k = a_n^kx^{kn} + ka_n^{k-1}a_mx^{(k-1)n+m} + h(x) \\
& f(x^k) = a_nx^{kn} + a_mx^{km} + g(x^k)\end{aligned}$$
其中$\deg h < (k-1)n+m$.
因为$0 \leqslant m \leqslant n-1$且$k\geqslant 2$,
所以$(k-1)n+m \neq km$. 所以要使$f(x^k) = (f(x))^k$, 必须有$ka_m = 0$,
即$a_m = 0$. 这与假设矛盾. 所以除最高次项外, $f(x)$没有其他非零项。所以
$$f(x) = \begin{cases}\pm x^n & \text{$k$为奇数}, \\ x^n & \text{$k$为偶数}. \end{cases} \quad n = 0, 1, \ldots$$

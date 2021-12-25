**习题5.4 第10题**.
求证方程$x^3 - x^2 - \frac{1}{2}x - \frac{1}{6} = 0$的根不可能全为实数。

**证明**：对于一个一般的$n$次多项式$f(x) = a_{n}x^{n}+a_{n-1}x^{n-1}+\cdots +a_{1}x+a_{0}$,
其判别式（discriminant）被定义为
$$\Delta = a_n^{2n-2} \prod_{i< j} (r_i - r_j)^2$$
其中$r_1,\ldots, r_n$为$f(x)$在其分裂域（或者某个代数闭域）上的$n$个根。对于3次实多项式$f(x) = ax^3+bx^2+cx_1+d$来说，如果它有3个实根，那么显然它的判别式是一个非负实数；如果他有复根$\beta$,
那么$\beta$的复共轭$\bar{\beta}$也是它的复根。设它的另一个实根为$\alpha$，那么它的判别式为
$$\Delta = a^4 (\alpha-\beta)^2(\alpha-\bar{\beta})^2(\beta-\bar{\beta})^2 = a^4 (\alpha^2-\alpha(\beta+\bar{\beta})+\beta\bar{\beta})^2 (\beta-\bar{\beta})^2$$
因为$\alpha^2-\alpha(\beta+\bar{\beta})+\beta\bar{\beta}$是实数，$\beta-\bar{\beta}$是纯虚数，所以判别式在这种情况下必然是一个负实数。

关于多项式判别式的计算，有如下结果
$$\Delta = \frac{(-1)^{n(n-1)/2}}{a_n} R(f,f')$$
其中$R(f,f')$为$f$与其导函数$f'$的结式。对于一般的三次方程，其判别式为
$$\Delta = b^{2}c^{2}-4ac^{3}-4b^{3}d-27a^{2}d^{2}+18abcd$$
对于本题的$x^3 - x^2 - \frac{1}{2}x - \frac{1}{6}$, 其判别式为
$$(-1)^2(-\frac{1}{2})^2 - 4(-\frac{1}{2})^3 - 4(-1)^3(-\frac{1}{6}) - 27(-\frac{1}{6})^2 + 18(-1)(-\frac{1}{2})(-\frac{1}{6}) = -\frac{13}{6} < 0$$
或者做变量替换$x\to x+\frac{1}{3}$得到$x^{3} - \frac{5}{6}x - \frac{11}{27}$，这个多项式的判别式的计算更简单
$$\Delta = -4(-\frac{5}{6})^3 - 27 (\frac{11}{27})^2 = -\frac{13}{6} < 0.$$
所以它有一个实根，两个共轭的复根。

**习题5.4 第11题**.
分别在复数域、实数域上将下列多项式分解为不可约多项式的乘积：(4)
$x^{2n} + x^n + 1$.

**解**.
多项式方程$y^2 + y + 1 = 0$的复根为$y = e^{2\pi i/3}, e^{4\pi i/3}$,
那么多项式$x^{2n} + x^n + 1$在复数域上的根为
$$e^{2\pi i/3n} \cdot e^{2k\pi i/n},\ e^{4\pi i/3n} \cdot e^{2k\pi i/n}, \quad 0 \leqslant k \leqslant n-1,$$
所以在复数域上有
$$x^{2n} + x^n + 1 = \prod_{k=0}^{n-1} \left(x - e^{\frac{\theta_1 i}{n} + \frac{2k\pi i}{n}}\right) \left(x - e^{\frac{\theta_2 i}{n} + \frac{2k\pi i}{n}}\right), \quad \theta_1 = \frac{2\pi}{3}, \theta_2 = \frac{4\pi}{3}.$$
要求该多项式在实数域上的分解，只要将其复数域上的分解式中共轭的一次式拿到一起，得到实系数的二次式即可。对于任意$0\leqslant k \leqslant n-1$,
取$k' = n-k-1$, 即有$0\leqslant k' \leqslant n-1$,
且$(\frac{\theta_1 i}{n} + \frac{2k\pi i}{n}) + (\frac{\theta_2 i}{n} + \frac{2k'\pi i}{n}) = 2\pi i,$
即$e^{\frac{\theta_1 i}{n} + \frac{2k\pi i}{n}}$与$e^{\frac{\theta_2 i}{n} + \frac{2k'\pi i}{n}}$互为复共轭，即有
$$\begin{cases}
e^{\frac{\theta_1 i}{n} + \frac{2k\pi i}{n}} + e^{\frac{\theta_2 i}{n} + \frac{2k'\pi i}{n}} = 2 \cos \left( \frac{\theta_1}{n} + \frac{2k\pi}{n} \right) = 2 \cos \left( \frac{2\pi}{3n} + \frac{2k\pi}{n} \right) \\
e^{\frac{\theta_1 i}{n} + \frac{2k\pi i}{n}} \cdot e^{\frac{\theta_2 i}{n} + \frac{2k'\pi i}{n}} = 1
\end{cases}$$ 所以$x^{2n} + x^n + 1$在实数域上的分解为
$$x^{2n} + x^n + 1 = \prod_{k=0}^{n-1} \left( x^2 - 2 \cos \left( \frac{2\pi}{3n} + \frac{2k\pi}{n} \right) + 1 \right)$$

**第三题**. 设正整数$m,n$满足$(m,n)=1$,
用$\Omega_m, \Omega_n$分别表示$x^m-1$与$x^n-1$在$\mathbb{C}$内的全部根的集合。证明$\Omega_m \cap \Omega_n = \{1\}$.

**证明**：正整数$m,n$满足$(m,n)=1$, 则存在整数$a,b\in\mathbb{Z}$,
使得$am+bn=1$. 任取$\alpha\in \Omega_m \cap \Omega_n$, 有
$$\alpha^m = \alpha^n = 1,$$ 那么$\alpha^{am} = \alpha^{bn} = 1,$ 进而有
$$\alpha = \alpha^{am+bn} = \alpha^{am} \cdot \alpha^{bn} = 1 \cdot 1 = 1$$

另一种证明方法：$\Omega_m = \{ e^{\frac{2k\pi i}{m}} \ |\ 0\leqslant k \leqslant m-1 \}$,
$\Omega_n = \{ e^{\frac{2k\pi i}{n}} \ |\ 0\leqslant k \leqslant n-1 \}$,
那么只要证明任取$0 < k < m$, $0 < k' < n$,
有$e^{\frac{2k\pi i}{m}} \neq e^{\frac{2k'\pi i}{n}}$即可。在这种情况下，只要证明$\frac{k}{m} \neq \frac{k'}{n}$即可。用反证法，假设$kn=k'm$,
由于$(m,n)=1$, 所以必须有 $$m|k, n|k'$$ 同时成立，但这是不可能的。

**习题5.5 第2题**.
整系数多项式$f(x)$能否同时满足$f(10)=10, f(20)=20, f(30)=40$?

**解.** 如果是有理系数的话，则肯定有这样的多项式，Lagrange插值多项式
$$\begin{aligned}
L(x) & = 10\frac{(x-20)(x-30)}{(10-20)(10-30)} + 20\frac{(x-10)(x-30)}{(20-10)(20-30)} + 40\frac{(x-10)(x-20)}{(30-10)(30-20)} \\
& = \frac{x^2}{20} - \frac{x}{2} + 10\end{aligned}$$
即是满足$L(10)=10, L(20)=20, L(30)=40$的有理系数多项式。假设存在题设的整系数多项式$f(x)$,
考虑$g(x) = f(x) - L(x)$, $g(x) \neq 0$. 那么
$$(x-10)(x-20)(x-30) \ |\ g(x)$$ 也就是说存在（整系数）多项式$h(x)$,
使得$f(x) = (x-10)(x-20)(x-30)h(x) + L(x)$.
那么$L(x)$是$f(x)$除以$(x-10)(x-20)(x-30)$的余项。但这是不可能的，因为整系数多项式除以首一的整系数多项式的余项也应该是整系数的。所以这样的整系数多项式$f(x)$不存在。

另一种证法：假设$f(x) = a_nx^n + \cdots + a_1x + a_0$满足题设条件。任取$\alpha,\beta\in\mathbb{Z}$,
有 $$\begin{aligned}
f(\alpha) - f(\beta) & = a_n(\alpha^n-\beta^n) + \cdots + a_1(\alpha-\beta) \\
& = a_n(\alpha-\beta)(\alpha^{n-1}+\alpha^{n-2}\beta+\cdots+\alpha\beta^{n-2}+\beta^{n-1}) + \cdots + a_1(\alpha-\beta),\end{aligned}$$
所以$(\alpha-\beta) \ |\ (f(\alpha) - f(\beta))$, 但题目中有
$$(30-10) \nmid (f(30)-f(10)).$$

**习题5.5 第8题**. 设$a,b,n$都是非零整数，$n\geqslant 2$,
且$ab\ |\ (a+b)^n$. 求证$b|a^{n-1}$.

**证明.** 由于
$$ab\ |\ a^n + C_n^1a^{n-1}b + C_n^2a^{n-2}b^2 + \cdots + C_n^{n-1}ab^{n-1} + b^n$$
且右边前$n$项都被$a$整除，所以第$n+1$项$b^n$也被$a$整除，即存在整数$h$使得$b^n = ah$.
故有 $$b\ |\ a^{n-1} + C_n^1a^{n-2}b + \cdots + C_n^{n-1}b^{n-1} + h,$$
从此式能推出$b\ |\ a^{n-1} + h$. 也就是说，我们有 $$\begin{cases}
b\ |\ a^{n-1} + h \\
b^n = ah
\end{cases}$$ 设$b$的素因子分解为有限乘积$b = \pm \prod p_i^{k_i}$,
$p_i$为素数，$k_i>0$.
那么上面第一式告诉我们，要么$p_i^{k_i}$同时整除$a^{n-1}$与$h$，要么都不整除$a^{n-1}$与$h$.
上面第二式告诉我们，都不整除$a^{n-1}$与$h$的$p_i^{k_i}$是不存在的，否则左边$p_i$的次数大于等于$2k_i$,
右边$p_i$的次数小于$2k_i$。于是$b$同时整除除$a^{n-1}$与$h$.

以上，我们排除的是$a^{n-1}$与$h$各含有$b$的部分素因子的情况。

另一种证法：考虑与$\frac{a^{n-1}}{b}$对称的$\frac{b^{n-1}}{a}$,
并构造有理系数多项式
$$f(x) = \left(x-\frac{a^{n-1}}{b}\right) \left(x-\frac{b^{n-1}}{a}\right) = x^2 + \frac{a^n+b^n}{ab} x + a^{n-2}b^{n-2}$$
由于
$$ab\ |\ a^n + C_n^1a^{n-1}b + C_n^2a^{n-2}b^2 + \cdots + C_n^{n-1}ab^{n-1} + b^n,$$
故$ab\ |\ a^n + b^n,$
所以$f(x)$是整系数多项式。由有理根定理知道$f(x)$的有理根的既约分数形式的分母整除$f(x)$的最高次项系数1，故$f(x)$的有理根实际上都是整根，即$\frac{a^{n-1}}{b}$与$\frac{b^{n-1}}{a}$都是整数。

**习题2.3 第1题**

令$\beta = x_1\alpha_1 + x_2\alpha_2 + x_3\alpha_3$，那么有
$$\begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix} = \beta^T = (\alpha_1^T, \alpha_2^T, \alpha_3^T) \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} 3 & 6 & 1 \\ 1 & 3 & 3 \\ 0 & 2 & 5 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}$$
解得$(x_1,x_2,x_3) = (-76,41,-16)$.

**习题2.3 第2题**

都写成列向量的形式。令$e_1,e_2,e_3,e_4$为$\mathbb{R}^4$的自然基。那么向量组$\alpha_1,\alpha_2,e_1,e_2,e_3,e_4$秩为4，将相应矩阵（前两列之间，后四列之间可以调换顺序）化为阶梯形，其主列对应原矩阵的列即为由$\alpha_1,\alpha_2$扩充得到的为$\mathbb{R}^4$的一组基。

**习题2.3 第3题**

依题有
$$\begin{pmatrix}1 & 0 & 0 & 0\\0 & 1 & 0 & 0\\0 & 0 & 1 & 0\\0 & 0 & 0 & 1\end{pmatrix} = \begin{pmatrix} e_1 \\ e_2 \\ e_3 \\ e_4 \end{pmatrix} = A_{4\times 4} \begin{pmatrix} \alpha_1 \\ \alpha_2 \\ \alpha_3 \\ \alpha_4 \end{pmatrix} = A_{4\times 4} \begin{pmatrix}1 & 1 & 1 & 1\\0 & 1 & -1 & -1\\0 & 0 & 1 & -1\\0 & 0 & 0 & 1\end{pmatrix},$$
那么有
$$A_{4\times 4} = \begin{pmatrix}1 & 0 & 0 & 0\\0 & 1 & 0 & 0\\0 & 0 & 1 & 0\\0 & 0 & 0 & 1\end{pmatrix} \cdot \begin{pmatrix}1 & 1 & 1 & 1\\0 & 1 & -1 & -1\\0 & 0 & 1 & -1\\0 & 0 & 0 & 1\end{pmatrix}^{-1} = \begin{pmatrix}1 & -1 & -2 & -4\\0 & 1 & 1 & 2\\0 & 0 & 1 & 1\\0 & 0 & 0 & 1\end{pmatrix},$$
于是
$$\begin{pmatrix} e_1 \\ e_2 \\ e_3 \\ e_4 \end{pmatrix} = \begin{pmatrix}1 & -1 & -2 & -4\\0 & 1 & 1 & 2\\0 & 0 & 1 & 1\\0 & 0 & 0 & 1\end{pmatrix} \cdot \begin{pmatrix} \alpha_1 \\ \alpha_2 \\ \alpha_3 \\ \alpha_4 \end{pmatrix} = \begin{pmatrix} \alpha_1-\alpha_2-2\alpha_3-4\alpha_4 \\ \alpha_2+\alpha_3+2\alpha_4 \\ \alpha_3+\alpha_4 \\ \alpha_4 \end{pmatrix}.$$

**习题2.3 第4(2)题**

高斯消元法标准解法可解此题。

**习题2.3 第5题**

设齐次线性方程组系数矩阵为$A$，则任取$A$的一行$(a_1,\cdots,a_5)$，它必须满足三个方程
$$(a_1,\cdots,a_5) \cdot X_i^T = 0, \quad i=1,2,3$$
或者等价地，
$$\begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} = \begin{pmatrix} X_1 \\ X_2 \\ X_3 \end{pmatrix} \cdot \begin{pmatrix} a_1 \\ \vdots \\ a_5 \end{pmatrix} = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & -1 & 1 & -1 & 1 \\ 1 & 2 & 4 & 8 & 16 \end{pmatrix} \cdot \begin{pmatrix} a_1 \\ \vdots \\ a_5 \end{pmatrix}.$$
解得$(a_1,\cdots,a_5) = (6,1,-4,1,0) t_1 + (16,6,-11,0,1) t_2$.从中任取$n$个向量，只要这$n$个向量的秩为$2$，即可组成一个齐次线性方程组，使得$X_1,X_2,X_3$是其基础解系。

**习题2.4 第1题**

(1).
容易计算向量组$X_1,X_2,X_3$秩为3，由于原方程为5元的，且系数矩阵秩为3，所以原方程必然是非齐次的。令$X_1$为特解，那么通解为$X_1+t_1\alpha_1+t_2\alpha_2$,
$t_1,t_2\in\mathbb{R}$.
可知$t_1(X_2)$与知$t_1(X_3)$不同时为0，且$t_2(X_2)$与知$t_2(X_3)$不同时为0，否则向量组$X_1,X_2,X_3$秩小于3。于是相应齐次方程组的基础解系可以取为$X_2-X_1,X_3-X_1$。所以原方程的通解为
$$(1,1,1,1,1) + t_1(0,1,2,3,4) + t_2(0,-1,-4,-3,-4), \quad t_1,t_2\in\mathbb{R}$$

(2,3). 设原方程为$AX = \beta$, $\beta$非零向量。那么
$$\begin{gathered}
A(X_1+X_2+X_3)= AX_1+AX_2+AX_3 = 3\beta \neq \beta \\
A\left(\dfrac{1}{3}(X_1+X_2+X_3)\right)= \dfrac{1}{3}(AX_1+AX_2+AX_3) = \beta\end{gathered}$$
所以$X_1+X_2+X_3$不是解，$\dfrac{1}{3}(X_1+X_2+X_3)$是解。

**习题2.4 第2题**

(1). 当二者都无解时，不需要二者等价。

(2). 设非齐次线性方程组(I),(II)分别为$A_1X=\beta_1, A_2X=\beta_2$.

若他们等价，则可以通过初等行变换
$$\begin{aligned}
\begin{pmatrix} A_1 \\ \mathbf{0} \end{pmatrix} X = \begin{pmatrix} \beta_1 \\ \mathbf{0} \end{pmatrix} & \to \begin{pmatrix} A_1 \\ A_2 \end{pmatrix} X = \begin{pmatrix} \beta_1 \\ \beta_2 \end{pmatrix} \Longrightarrow \text{(II)的解集为(I)的解集的子集} \\
\begin{pmatrix} \mathbf{0} \\ A_2 \end{pmatrix} X = \begin{pmatrix} \mathbf{0} \\ \beta_2 \end{pmatrix} & \to \begin{pmatrix} A_1 \\ A_2 \end{pmatrix} X = \begin{pmatrix} \beta_1 \\ \beta_2 \end{pmatrix} \Longrightarrow \text{(I)的解集为(II)的解集的子集}\end{aligned}$$
所以此时二者同解。

若二者有解且同解，要证明的是矩阵$\begin{pmatrix}[c|c] A_1 & \beta_1 \end{pmatrix}$与矩阵$\begin{pmatrix}[c|c] A_2 & \beta_2 \end{pmatrix}$行等价。这等价于齐次线性方程组$\begin{pmatrix}[c|c] A_1 & \beta_1 \end{pmatrix} Y = 0$与$\begin{pmatrix}[c|c] A_2 & \beta_2 \end{pmatrix} Y = 0$同解。设$Y = \begin{pmatrix} X \\ c \end{pmatrix}$是$\begin{pmatrix}[c|c] A_1 & \beta_1 \end{pmatrix} Y = 0$的解，那么$A_1X + c\beta_1 = 0$.
若$c\neq 0$，那么
$$-c(A_1(-\dfrac{1}{c}X) - \beta_1) = 0 \Longrightarrow c(A_2(-\dfrac{1}{c}X) - \beta_2) = 0 \Longrightarrow \text{$Y = \begin{pmatrix} X \\ c \end{pmatrix}$是$\begin{pmatrix}[c|c] A_2 & \beta_2 \end{pmatrix} Y = 0$的解}$$
若$c = 0$，由于$A_1X = \beta_1$有解，任取一解$X_0$，即$A_1X_0 = \beta_1$，那么有
$$\begin{aligned}
A_1X+(A_1X_0-\beta_1) = 0+0 = 0 & \Longrightarrow A_1(X+X_0)-\beta_1 = 0 \\
& \Longrightarrow A_2(X+X_0)-\beta_2 = 0 \\
& \Longrightarrow A_2X+(A_2X_0-\beta_2) = 0 \\
& \Longrightarrow A_2X = 0 \\
& \Longrightarrow \text{$Y = \begin{pmatrix} X \\ 0 \end{pmatrix}$是$\begin{pmatrix}[c|c] A_2 & \beta_2 \end{pmatrix} Y = 0$的解}\end{aligned}$$

**习题2.4 第3题**

设原方程为$AX = \beta$, $\beta$非零向量，那么
$$A(\lambda_1X_1+\cdots+\lambda_kX_k) = \lambda_1AX_1+\cdots+\lambda_kAX_k = \lambda_1AX_1+\cdots+\lambda_kAX_k = (\lambda_1+\cdots+\lambda_k)\beta$$
由于$\beta$非零向量，故
$$\begin{aligned}
\lambda_1X_1+\cdots+\lambda_kX_k \text{ 是解} & \Longleftrightarrow (\lambda_1+\cdots+\lambda_k)\beta = \beta \\
& \Longleftrightarrow \lambda_1+\cdots+\lambda_k = 1\end{aligned}$$

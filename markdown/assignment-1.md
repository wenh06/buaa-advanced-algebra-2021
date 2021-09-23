---
date: 第一次作业
title: 2021秋高等代数课后习题
---

**习题1.2 第1题**\
(2) 将线性方程组写为增广矩阵的形式
$$\begin{pmatrix}[cccc|c] 0 & 1 & 1 & 1 & 1 \\ 1 & 0 & 1 & 1 & 2 \\ 1 & 1 & 0 & 1 & 3 \\ 1 & 1 & 1 & 0 & 4 \end{pmatrix},$$
进行行变换，得到的答案是$(x_1, x_2, x_3, x_4) = (\frac{7}{3}, \frac{4}{3}, \frac{1}{3}, -\frac{2}{3})$.

\(4\) 将线性方程组写为增广矩阵的形式
$$\begin{pmatrix}[ccccc|c] 1 & 3 & -5 & -5 & 0 & 2 \\ 1 & 2 & 2 & -2 & 1 & -2 \\ 2 & 1 & 3 & -3 & 0 & 2 \\ 1 & -4 & 1 & 1 & -1 & 3 \\ 1 & 0 & 3 & -1 & 1 & 1 \end{pmatrix},$$
进行行变换，得到的答案是$(x_1, x_2, x_3, x_4, x_5) = (-\frac{26}{3}, -\frac{11}{3}, \frac{5}{3}, -6, -\frac{4}{3})$.

**习题1.2 第2题**
三个平面$9x-3y+z=20, x+y+z=0, -x+2y+z=-10$的公共点集即为这三个线性方程组成的线性方程组的解集。
$$\begin{pmatrix}[ccc|c] 9 & -3 & 1 & 20 \\ 1 & 1 & 1 & 0 \\ -1 & 2 & 1 & -10 \end{pmatrix} \to \begin{pmatrix}[ccc|c] 1 & 1 & 1 & 0 \\ 0 & 3 & 2 & -10 \\ 0 & 0 & 0 & -20 \end{pmatrix}$$
无解，故三个平面的公共点集为空集。

**习题1.2 第2题** 已在习题课进行讲解。

**习题1.3 第1题** 增广矩阵为
$$\begin{pmatrix}[ccccc|c] 3 & 2 & a & 1 & -3 & 4 \\ 5 & 4 & 3 & 3 & -1 & 3 \\ 1 & 1 & 3 & 2 & 1 & 1 \\ 0 & 1 & 2 & 2 & 6 & -3 \\ 0 & 0 & 1 & b & 1 & 1 \end{pmatrix}
\to \begin{pmatrix}[ccccc|c] 1 & 0 & 1 & 0 & -5 & 4 \\ 0 & 1 & -2 & 0 & 6 & -5 \\ 0 & 0 & 2 & 1 & 0 & 1 \\ 0 & 0 & 1-2b & 0 & 1 & 1-b \\ 0 & 0 & a-1 & 0 & 0 & 1 \end{pmatrix}$$
所以，当$a=1$时，增广矩阵的秩大于系数矩阵的秩，无解。

当$a\neq 1$时，增广矩阵可进一步化简
$$\begin{pmatrix}[ccccc|c] 1 & 0 & 1 & 0 & -5 & 4 \\ 0 & 1 & -2 & 0 & 6 & -5 \\ 0 & 0 & 2 & 1 & 0 & 1 \\ 0 & 0 & 1-2b & 0 & 1 & 1-b \\ 0 & 0 & a-1 & 0 & 0 & 1 \end{pmatrix}
\to \begin{pmatrix}[ccccc|c] 1 & 0 & 0 & 0 & 0 & \frac{-5ab+9a+15b-15}{a-1} \\ 0 & 1 & 0 & 0 & 0 & \frac{6ab-11a-18b+19}{a-1} \\ 0 & 0 & 1 & 0 & 0 & \frac{1}{a-1} \\ 0 & 0 & 0 & 1 & 0 & \frac{a-3}{a-1} \\ 0 & 0 & 0 & 0 & 1 & \frac{-ab+a+3b-2}{a-1} \end{pmatrix}$$
所以有唯一解
$$\left( \frac{-5ab+9a+15b-15}{a-1}, \frac{6ab-11a-18b+19}{a-1}, \frac{1}{a-1}, \frac{a-3}{a-1}, \frac{-ab+a+3b-2}{a-1} \right)$$

**习题1.3 第3题**\
(1) 增广矩阵为
$$\begin{pmatrix}[ccccc|c] 1 & 1 & 1 & 1 & 1 & 1 \\ 1 & 2 & 3 & 4 & 5 & 6 \\ 1 & 0 & -1 & -2 & -3 & -4 \end{pmatrix}
\to \begin{pmatrix}[ccccc|c] 1 & 0 & -1 & -2 & -3 & -4 \\ 0 & 1 & 2 & 3 & 4 & 5 \end{pmatrix}$$
所以通解为
$$\left( t_1+2t_2+3t_3-4, -2t_1-3t_2-4t_3+5, t_1, t_2, t_3 \right), \quad t_1, t_2, t_3 \in \mathbb{R}$$
或写作
$$t_1\begin{pmatrix} 1 \\ -2 \\ 1 \\ 0 \\ 0 \end{pmatrix} + t_2 \begin{pmatrix} 2 \\ -3 \\ 0 \\ 1 \\ 0 \end{pmatrix} + t_3 \begin{pmatrix} 3 \\ -4 \\ 0 \\ 0 \\ 1 \end{pmatrix} + \begin{pmatrix} -4 \\ 5 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \quad t_1, t_2, t_3 \in \mathbb{R}$$

\(2\) 将(1)中通解的非齐次部分去掉即为相应齐次线性方程组的通解
$$t_1\begin{pmatrix} 1 \\ -2 \\ 1 \\ 0 \\ 0 \end{pmatrix} + t_2 \begin{pmatrix} 2 \\ -3 \\ 0 \\ 1 \\ 0 \end{pmatrix} + t_3 \begin{pmatrix} 3 \\ -4 \\ 0 \\ 0 \\ 1 \end{pmatrix}, \quad t_1, t_2, t_3 \in \mathbb{R}$$

\(3\) 已在(1)中写出。

\(4\)
非齐次线性方程组的通解为相应齐次线性方程组的通解加上该非齐次线性方程组的任意一个特解。

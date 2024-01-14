# LaTeX 数学符号公式

## 1.希腊字母

$$
\alpha, \beta, \gamma, \delta, \epsilon, \zeta
$$

$$
\eta, \theta, \iota, \kappa, \lambda, \mu
$$

$$
\nu, \xi, \omicron, \pi, \rho, \sigma
$$

$$
\tau, \upsilon, \phi, \chi, \psi, \omega
$$

$$
\Alpha, \Beta, \Gamma, \Delta, \Epsilon, \Zeta
$$

$$
\Eta, \Theta, \Iota, \Kappa, \Lambda, \Mu
$$

$$
\Nu, \Xi, \Omicron, \Pi, \Rho, \Sigma
$$

$$
\Tau, \Upsilon, \Phi, \Chi, \Psi, \Omega
$$

$$
\varepsilon, \vartheta, \varpi, \varrho, \varsigma, \varphi
$$

## 2.上标、下标

$$
x^a,
x_a,
x^b_a,
{}_cx_a^b,
{}^cx_a^b,
{}_c^dx_a^b
$$

## 3.根号

$$
\sqrt{x^2+y^2}, \sqrt[n]{x}
$$

## 4.分式

$$
\frac {2xy}{x^2+y^2}
$$

## 5.对数

$$
\ln a, \lg b, \log c, \log_{d}f
$$

## 6.三角函数

$$
\sin a, \cos b, \tan c, \cot d, \sec e, \csc f
$$

## 7.极限

$$
\lim_{x \to \infty} \frac{1}{n}
$$

## 8.微分及导数

$$
dt, \mathrm{d}t, \partial t, \nabla\psi
$$

$$
\frac{dy}{dx},
\frac{\partial^2}{\partial x_1\partial x_2}y
$$

$$
f', f'', f^{(3)}, \dot y, \ddot y, \dddot y
$$

## 9.积分

$$
\int_0^\infty e^{-x} dx ,
\underset{(x,y)\in \triangle}{\iint} e^{x+y} dxdy,
\iint \limits_{(x,y)\in \triangle} e^{x+y} dxdy,
\iiint e^{x+y+z} dxdydz
$$

$$
\oint Pdx+Qdy, \idotsint
$$

## 10.运算符

$$
   +, -, \pm, \mp
$$

$$
\times, \cdot, \div, /, \backslash
$$

## 11.模运算

$$
\mid, \nmid
$$

$$
s_k \equiv 0 \pmod{m}
$$

## 12.集合

$$
\{ \}, \vert , \Vert, \O \empty, \varnothing, \mathbb{R}, \dots
$$

$$
\in, \not\in, \ni, \not\ni
$$

$$
\cap, \cup, \setminus \\
\subset, \supset \\
\subseteq, \supseteq \\
\subsetneqq, \supsetneqq
$$

$$
\bigodot, \bigotimes, \bigoplus
$$

## 13.关系符号

$$
=, \ne \neq, \equiv, \not\equiv, \triangleq
$$

$$
\sim, \simeq, \cong, \ncong
$$

$$
<, \ll, >, \gg, \leq, \geq
$$

## 14.集合符号

$$
\parallel, \nparallel, \perp, \angle, \triangle, {}^\circ
$$

## 15.逻辑符号

$$
\forall, \exists \\
\because, \therefore \\
\neg, \and, \or
$$

## 16.箭头

$$
\Rightarrow, \nRightarrow, \Longrightarrow \\
\Leftarrow, \nLeftarrow, \Longleftarrow \\
\Leftrightarrow, \nLeftrightarrow, \Longleftrightarrow \\
\rightleftharpoons, \leftrightharpoons
$$

## 17.标注

$$
\vec{x}, \bar{x}, \hat{x}, \tilde{x},
\overrightarrow{AB}, \overline{AB}, \underline{AB}, \widehat{AB}, \widetilde{AB}
$$

## 18.求和求积

$$
\sum_{k=1}^N k^2,\prod_{i=1}^N x_i
$$

## 19.二项式系数

$$
\binom{n}{r}={\rm C}^r_n
$$

## 20.矩阵

$$
\begin{matrix}
a & b \\
c & d
\end{matrix}
$$

$$
\begin{vmatrix} m \end{vmatrix},
\begin{Vmatrix} m \end{Vmatrix},
\begin{bmatrix} m \end{bmatrix},
\begin{Bmatrix} m \end{Bmatrix},
\begin{pmatrix} m \end{pmatrix}
$$

$$
\begin{bmatrix}
0      & \cdots & 0      \\
\vdots & \ddots & \vdots \\
0      & \cdots & 0
\end{bmatrix}
$$

## 21.方程组

$$
\begin{cases}
3x + 5y +  z \\
7x - 2y + 4z \\
-6x + 3y + 2z
\end{cases}
$$

## 22.条件表达式

$$
f(n) =
\begin{cases}
n/2,  & \text{if $n$ is even} \\
3n+1, & \text{if $n$ is odd}
\end{cases}
$$

## 23.多行等式

$$
\begin{aligned}
f(x) & = (m+n)^2 \\
     & = m^2+2mn+n^2 \\
\end{aligned}
$$

## 24.数组与表格

$$
\begin{array}{c|lcr}
n & \text{左对齐} & \text{居中对齐} & \text{右对齐} \\
\hline
1 & 0.24 & 1 & 125 \\
2 & -1 & 189 & -8 \\
3 & -20 & 2000 & 1+10i
\end{array}
$$

$$
\left[
    \begin{array}{cc|c}
      1&2&3\\
      4&5&6
    \end{array}
\right]
$$

## 25.自动匹配长度的括号

$$
\left( \frac{a}{b} \right),
\left[ \frac{a}{b} \right],
\left\{ \frac{a}{b} \right\},
\left< \frac{a}{b} \right>,
\left| \frac{a}{b} \right|,
\left\| \frac{a}{b} \right\|,
\left \lfloor \frac{a}{b} \right \rfloor,
\left\{ \frac{a}{b} \right.
$$

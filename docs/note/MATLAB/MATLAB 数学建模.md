# MATLAB 数学建模

## 1.线性规划

```matlab
x=linprog(c,A,b)
x=linprog(c,A,b,Aeq,beq)
x=linprog(c,A,b,Aeq,beq,lb,ub)
[x,fval]=linprog(____)
intlinprog %整数线性规划
```

线性规划模型：

目标函数：$min\,f=c'\times x=c_1x_1+c_2x_2+...+c_nx_n$

   约束条件1：$Ax \le b$
$$
   \begin{aligned}
   a_{11}x_1+a_{12}x_2+&\cdots+a_{1n}x_n \le b_1 \\
   a_{21}x_1+a_{22}x_2+&\cdots+a_{2n}x_n \le b_2 \\
   &\ddots\\
   a_{m1}x_1+a_{m2}x_2+&\cdots+a_{mn}x_n \le b_m \\
   \end{aligned}
$$
   约束条件2：$Aeqx = beq$
$$
   \begin{aligned}
   aeq_{11}x_1+aeq_{12}x_2+&\cdots+aeq_{1n}x_n = beq_1 \\
   aeq_{21}x_1+aeq_{22}x_2+&\cdots+aeq_{2n}x_n = beq_2 \\
   &\ddots\\
   aeq_{m1}x_1+aeq_{m2}x_2+&\cdots+aeq_{mn}x_n = beq_m \\
   \end{aligned}
$$
   约束条件3：$lb \le x \le ub$
$$
   \begin{aligned}
   lb_1 \le & \; x_1 \le ub_1 \\
   &\cdots \\
   lb_n \le & \; x_n \le ub_n \\
   \end{aligned}
$$
   返回值：$x=[x_1,x_2,...,x_n],fval=c'\times x$

import sympy as sp

# 定义变量
x, y = sp.symbols('x y')

print(x,y)
# 定义函数
f = x**2 + 2*y

# 计算函数关于 x 的偏导数
partial_x = sp.diff(f, x)

# 计算函数关于 y 的偏导数
partial_y = sp.diff(f, y)

# 输出结果
print(f"偏导数关于 x 的结果为: {partial_x}")
print(f"偏导数关于 y 的结果为: {partial_y}")

# 计算 x=2 处的偏导数
x_value = 2
partial_x_at_x_equals_2 = partial_x.subs(x, x_value)
partial_y_at_x_equals_2 = partial_y.subs(x, x_value)

# 输出结果
print(f"x=2 处偏导数关于 x 的结果为: {partial_x_at_x_equals_2}")
print(f"x=2 处偏导数关于 y 的结果为: {partial_y_at_x_equals_2}")

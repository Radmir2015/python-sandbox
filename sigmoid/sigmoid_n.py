import itertools
import numpy as np
import pylab as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy.solvers import solve
from matplotlib import cm

beta = 0.1
eps = 0.001
n_error = 100
iters = 10000
n_points_per_grid = 100
x_lim, y_lim = [-10, 10], [-10, 10]

w = np.random.rand(3, 1)
# np.append(np.random.rand(1, 2) * 10 - 5, [1]).reshape(1, 3) also possible
# x_total = np.array([ np.append(np.random.rand(1, 2) * 10 - 5, [[1]], 1) for i in range(iters) ])
x_total = np.array([ np.array([[ np.random.uniform(*x_lim), np.random.uniform(*y_lim), 1 ]]) for i in range(iters) ])

# бинарный ввод
# x = np.array([
#     [1, 1, 0],
#     [1, 0, 1],
#     [0, 0, 0],
#     [0, 0, 1]
# ])

f = lambda u: 1 / (1 + np.exp(-beta * u))

der_f = lambda u: beta * f(u) * (1 - f(u))

dw = lambda x, e, u: np.dot(x.T, e * der_f(u))

# u = lambda w, x, w0: f(np.dot(w, x) + w0)
y = lambda x, w: f(np.dot(x, w))

correct_weights = lambda w, dw, n=1: w + n * dw

def correct_answer(x, solved_func):

    # возвращение статического бинарного ответа
    # return np.array([[1, 1, 0, 0]]).T
    # return np.array([[int(x[0] < x[1]), int(x[0] >= x[1])]])

    # функция y = x
    # return int(x[0, 0] ** 2 < x[0, 1])

    # вычисление введенной функции через библиотеку sympy
    # return int(bool(solved_func.subs('x', x[0, 0]) < x[0, 1]))

    # вычисление введенной через eval
    # print(x)
    return int(eval(str(solved_func).replace('x', str(x[0, 0]))) < x[0, 1])


def get_answer(input_data, w):
    prob = y(np.array([input_data]), w)
    estimation = ''

    if 0.5 - 0.05 < prob < 0.5 + 0.05:
        estimation = 'near 50%'
    elif prob > 0.8:
        estimation = 'near 100%'
    elif prob < 0.2:
        estimation = 'near 0%'
    else:
        estimation = 'ambigious probability'
    
    print('Probability of input data is {}, this is {}.'.format(prob, estimation))


def input_test_value(func):
    print('Equation: f(x, y) = {}. If a point above the graphic it will be 1, if below or on graphic - 0.'.format(func))

    while True:
        x_inp, y_inp = float(input('x = ')), float(input('y = '))

        get_answer(np.array([x_inp, y_inp, 1]), w)


error = []

func = input('Input test function (e.g. f(x, y) = 0): ').replace('= 0', '').replace('=0', '')
solved = solve(func, 'y')[0]

# for i in range(iters):
for x in x_total:
# while True:
#     x = np.array([[ np.random.uniform(*x_lim), np.random.uniform(*y_lim), 1 ]])

    u_i = y(x, w)
    
    e = correct_answer(x, solved) - u_i

    w = correct_weights(w, dw(x, e, u_i))

    error.append(np.average(np.abs(e)) if len(e) > 1 else np.abs(e)[0])

    if len(error) > n_error and np.average(error[-n_error:]) < eps:
        break

print('w =', w)
print('outputs =', u_i)
print('iteration =', len(error))
print('average error =', error[-1])


plt.title('Average Error')

# Отображение всех точек
# plt.plot(range(1, len(error) + 1), error)

# Отображение 100 точек (по-среднему)
plt.plot(range(1, 100 + 1), [np.average(arr) for arr in np.array_split(error, 100)])
# plt.plot(range(1, len(error) // (iters // 100) + 1), [np.average(arr) for arr in np.array_split(error, 100)])
plt.show()

# Зависимость результата сигмоида от входных координат
x_side = np.linspace(x_lim[0], x_lim[1], n_points_per_grid)
y_side = np.linspace(y_lim[0], y_lim[1], n_points_per_grid)

X, Y = np.meshgrid(
        x_side, y_side
    )

# Z = f(np.matmul([X, Y, 1], w))
# Z = f([X, Y, 1] @ w)
# print(Z.shape, Z)


# вычисление через каждой точки графика
# Z = []
# cartesian = np.array([ [[i[0], i[1], 1]] for i in itertools.product(x_side, y_side) ])

# for c in cartesian:
#     Z.append([c[0, 0], c[0, 1], y(c, w)])

# Z = np.array(Z)

# способ отрисовать с помощью reshape
# ax.plot_surface(X, Y, Z[:, 2].reshape(n_points_per_grid, n_points_per_grid))

# отрисовка каждой точки
# for z in np.vsplit(Z, n_points_per_grid):
#     ax.plot3D(z[:, 0], z[:, 1], z[:, 2])


# Z = f(np.dot(cartesian.T, w))
# # Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
# Z = X * w[0] + Y * w[1] + 1 * w[2]
# Z = np.dot(X, w[0]) + np.dot(Y, w[1]) + np.dot(1, w[2])
# Z = np.einsum('ijk,jk->ij', np.array([X, Y, 1]), w)
# Z = f(np.dot(np.array([X, Y, 1]), w))

Z = f(X * w[0] + Y * w[1] + 1 * w[2])

fig = plt.figure(figsize=plt.figaspect(1 / 2.5))
ax1 = fig.add_subplot('121', projection='3d')

ax1.plot_surface(X, Y, Z, cmap=cm.coolwarm)

ax1.set_xlabel('x'), ax1.set_ylabel('y'), ax1.set_zlabel('z')

ax2 = fig.add_subplot('122', projection='3d')
ax2.plot_wireframe(X, Y, Z, rstride=10, cstride=3)

ax2.contour(X, Y, Z, zdir='z', offset=0, cmap=cm.coolwarm)
ax2.contour(X, Y, Z, zdir='x', offset=x_lim[0], cmap=cm.coolwarm)
ax2.contour(X, Y, Z, zdir='y', offset=y_lim[1], cmap=cm.coolwarm)


# ax = Axes3D(fig)
# ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2], color='g')
# ax.scatter3D(x_side, y_side, Z, color='green')
# ax.plot_trisurf(z[:, 0], z[:, 1], z[:, 2])
# ax.contourf(z[:, 0], z[:, 1], z[:, 2])


ax2.set_xlabel('x'), ax2.set_ylabel('y'), ax2.set_zlabel('z')

def on_move(event):
    if event.inaxes == ax1:
        if ax1.button_pressed in ax1._rotate_btn:
            ax2.view_init(elev=ax1.elev, azim=ax1.azim)
        elif ax1.button_pressed in ax1._zoom_btn:
            ax2.set_xlim3d(ax1.get_xlim3d())
            ax2.set_ylim3d(ax1.get_ylim3d())
            ax2.set_zlim3d(ax1.get_zlim3d())
    elif event.inaxes == ax2:
        if ax2.button_pressed in ax2._rotate_btn:
            ax1.view_init(elev=ax2.elev, azim=ax2.azim)
        elif ax2.button_pressed in ax2._zoom_btn:
            ax1.set_xlim3d(ax2.get_xlim3d())
            ax1.set_ylim3d(ax2.get_ylim3d())
            ax1.set_zlim3d(ax2.get_zlim3d())
    else:
        return
    fig.canvas.draw_idle()

c1 = fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()

input_test_value(func.strip())

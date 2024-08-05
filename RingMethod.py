import numpy as np
import matplotlib.pyplot as plt

def plot_problem(problem_num, func1, func2=None, x_range=None, title=""):
    x = np.linspace(x_range[0], x_range[1], 400)
    plt.figure(figsize=(8, 6))
    
    plt.plot(x, func1(x), label='y=' + func1.__name__)
    if func2:
        y2 = np.full_like(x, func2(x))
        plt.plot(x, y2, label='y=' + func2.__name__)
    
    if func2:
        plt.fill_between(x, func1(x), y2, where=(func1(x) >= y2), color='gray', alpha=0.3)
    else:
        plt.fill_between(x, func1(x), 0, color='gray', alpha=0.3)
    
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.legend()
    plt.grid(True)
    plt.show()

def problem_1_func1(x): return 4/x
def problem_1_func2(x): return 0
plot_problem(1, problem_1_func1, problem_1_func2, x_range=(1, 4), title="Problem 1: y=4/x rotated about y-axis")

def problem_2_func1(x): return x**2 + 1
def problem_2_func2(x): return 0
plot_problem(2, problem_2_func1, problem_2_func2, x_range=(0, 2), title="Problem 2: y=x^2+1 rotated about y-axis")

def problem_3_func1(x): return np.sqrt(x)
def problem_3_func2(x): return 0
plot_problem(3, problem_3_func1, problem_3_func2, x_range=(0, 4), title="Problem 3: y=sqrt(x) rotated about x=4")

def problem_4_func1(x): return 4 - x**2
plot_problem(4, problem_4_func1, x_range=(-2, 2), title="Problem 4: y=4-x^2 rotated about x=-2")

def problem_5_func1(x): return 2*x
def problem_5_func2(x): return x**2
plot_problem(5, problem_5_func1, problem_5_func2, x_range=(0, 2), title="Problem 5: y=2x and y=x^2 rotated about y-axis")

def problem_6_func1(x): return (1/4)*x**3 + 2
def problem_6_func2(x): return 2 - x
plot_problem(6, problem_6_func1, problem_6_func2, x_range=(0, 2), title="Problem 6: y=(1/4)x^3+2 and y=2-x rotated about y-axis")

def problem_7_func1(x): return np.cbrt(x)
plot_problem(7, problem_7_func1, x_range=(0, 8), title="Problem 7: y=∛x rotated about x-axis")

def problem_8_func1(x): return -x + 3
plot_problem(8, problem_8_func1, x_range=(0, 3), title="Problem 8: y=-x+3 rotated about y=3")

def problem_9_func1(x): return np.sqrt(x) + 1
def problem_9_func2(x): return x + 1
plot_problem(9, problem_9_func1, problem_9_func2, x_range=(0, 1), title="Problem 9: y=sqrt(x)+1 and y=x+1 rotated about x-axis")

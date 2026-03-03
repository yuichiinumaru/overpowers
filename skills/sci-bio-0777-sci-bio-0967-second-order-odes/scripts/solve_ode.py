import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, t):
    # Example: y'' + y = 0 -> [y', -y]
    dy1 = y[1]
    dy2 = -y[0]
    return [dy1, dy2]

def solve_and_plot():
    y0 = [1, 0] # y(0)=1, y'(0)=0
    t = np.linspace(0, 10, 101)
    sol = odeint(model, y0, t)
    plt.plot(t, sol[:, 0], 'b', label='y(t)')
    plt.plot(t, sol[:, 1], 'g', label="y'(t)")
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.savefig('ode_solution.png')
    print("Solution saved to ode_solution.png")

if __name__ == "__main__":
    solve_and_plot()

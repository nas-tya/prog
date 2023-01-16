import main_cy
from joblib import Parallel, delayed
import math


def integrate(f, a, b, n_iter):
    step = (b - a) / n_iter
    x = a
    s = 0
    while x <= (b - step):
        s += f(x)
        x += step
    return round(s * step, 8)


# backend = 'threading' or 'multiprocessing'
def integrate_async(f, a, b, n_jobs=2, n_iter=1000, backend=None):
    step = (b - a) / n_jobs
    with Parallel(n_jobs=n_jobs, backend=backend) as p:

        fs = (delayed(main_cy.integrate)(f,
                                         a + i * (step + 1),
                                         a + (i + 1) * step,
                                         n_iter=n_iter // n_jobs)
              for i in range(n_jobs))
        return sum(p(fs))


if __name__ == '__main__':
    print(main_cy)
    print(
        integrate_async(math.cos,
                        0,
                        100,
                        n_iter=100,
                        backend='multiprocessing'))

import concurrent.futures as ftres
from functools import partial


def integrate(f, a, b, n_iter):
    """
    timing:
    python -m timeit -n 1000 -u 'msec' -r 100 -s "from main import integrate" "integrate(lambda x: x*x, 1, 2, n_iter=10**3)"

1000 loops, best of 100: 0.639 msec per loop
    """
    step = (b - a) / n_iter
    x = a
    s = 0
    while x <= (b - step):
        s += f(x)
        x += step
    return round(s * step, 8)


def integrate_async(f, a, b, *, n_jobs=2, n_iter=1000000):
    """
    timing:
    python -m timeit -n 1000 -u 'msec' -r 100 -s "from main import integrate_async" "integrate_async(lambda x: x*x, 1, 2, n_jobs=2, n_iter=10**3)"

1000 loops, best of 100: 2.69 msec per loop

    python -m timeit -n 1000 -u 'msec' -r 100 -s "from main import integrate_async" "integrate_async(lambda x: x*x, 1, 2, n_jobs=4, n_iter=10**3)"

1000 loops, best of 100: 3.8 msec per loop

    python -m timeit -n 1000 -u 'msec' -r 100 -s "from main import integrate_async" "integrate_async(lambda x: x*x, 1, 2, n_jobs=6, n_iter=10**3)"

1000 loops, best of 100: 3.98 msec per loop
    """
    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, integrate, f, n_iter=n_iter // n_jobs)
    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    return sum(f.result() for f in ftres.as_completed(fs))


if __name__ == '__main__':
    # tests
    assert round(
        integrate_async(lambda x: 2 * x * x, 1, 2, n_jobs=2, n_iter=100000),
        2) == 4.67
    assert round(
        integrate_async(lambda x: 2 * x, 2, 4, n_jobs=4, n_iter=100000),
        2) == 12.00
    assert round(
        integrate_async(lambda x: 7 * x, 1, 5, n_jobs=6, n_iter=1000000),
        0) == 84

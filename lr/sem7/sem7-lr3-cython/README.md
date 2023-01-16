python -m timeit -n 1000 -u 'msec' -r 100 -s "from main import integrate_async; import math" "integrate_async(math.sin, 0, 1, n_jobs=2, n_iter=10**3,  backend='multiprocessing')"

-> 
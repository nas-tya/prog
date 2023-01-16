def integrate(f, double a, double b, double n_iter):
    cdef double step, x, s
    x = a
    s = 0
    step = (b-a)/n_iter
    while x <= (b - step):
      s += f(x)
      x += step
    return round(s*step, 8)


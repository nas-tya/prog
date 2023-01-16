def integrate(f, a, b, n_iter):
    step = (b-a)/n_iter
    x = a
    s = 0
    while x <= (b- step):
      s += f(x)
      x += step
    return round(s*step, 8)

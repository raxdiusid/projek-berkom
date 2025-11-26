import math
    
def f(x):
    return x**3-2*x-5

def bisect(a, b):
    if f(a) == 0:
        return print(f"root found at x={a}")
    if f(b) == 0:
        return print(f"root found at x={b}")
    if f(a)*f(b) > 0:
        return print("root doesnt exist at that interval or more than one root")
    left = a
    right = b
    r = (a+b)/2
    ro = [r]
    convergence = 10**-5
    i=1
    while True:
        tmp = r
        if f(r)*f(a)<0:
            # cut to the left
            r = (left+r)/2
            right = tmp
        elif f(r)*f(a)>0:
            # cut to the right
            r = (right+r)/2
            left = tmp
        else:
            return print(f"root found x={r}")
        ro.append(r)
        if abs(r-ro[-2]) < convergence:
            break
        print(f"[{i}] x={r} | f({r})={f(r)}")
        i+=1
    return print(f"approximated root x={r}")

bisect(1.5, 5)
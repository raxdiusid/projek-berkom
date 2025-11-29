import math
    
def f(x):
    return x**2 - 4*x + 3

class Bisect:

    def __init__(self, f, interval: list[int], display_process: bool=False) -> None:
        self.f = f
        self.interval = interval
        self.__roots = []
        self.__potential_roots = self._identify_roots(interval[0], interval[1], npartition=100)
        self.display_process = display_process

        for potential_root in self.__potential_roots:
            self.__roots.append(self.bisect(potential_root[0], potential_root[1]))

    def get_roots(self) -> list[int]:
        return self.__roots
    
    def _identify_roots(self, left, right, npartition=100):

        potential_roots_interval = []
        delta = (right-left)/npartition

        previously_identified = False

        for i in range(npartition-1):
            la = left+i*delta
            lb = left+(i+1)*delta
            if self.f(la)*self.f(lb) <= 0 and not previously_identified:
                potential_roots_interval.append([la, lb])
                previously_identified = True
                continue
            previously_identified = False
        return potential_roots_interval

    def bisect(self, a: int, b: int) -> None:

        if f(a) == 0:
            return print(f"root found at x={a}")
        
        if f(b) == 0:
            return print(f"root found at x={b}")
        
        if f(a)*f(b) > 0:
            return print("root doesnt exist at that interval or more than one root")
        
        # The left node of the interval
        left = a

        # The right node of the interval
        right = b

        # The midpoint node of the interval
        mid = (a+b)/2

        # Array of midpoints of the partitioned interval
        partition = [mid]

        # Convergence criteria
        convergence = 10**-5

        i=1
        while True:

            tmp = mid

            if f(mid)*f(a)<0:
                # Cutting the interval to the left
                mid = (left+mid)/2
                right = tmp

            elif f(mid)*f(a)>0:
                # Cutting the interval to the right
                mid = (right+mid)/2
                left = tmp

            else:
                # A condition where f(r)*f(a) == 0 is met, which implies f(r) = 0
                return print(f"root found x={mid}")
            
            partition.append(mid)

            if abs(mid-partition[-2]) < convergence:
                break

            print(f"[{i}] x={mid} | f({mid})={f(mid)}")

            i+=1
        
        self.__roots.append(mid)
        return print(f"approximated root x={mid}")

f1 = Bisect(f, [0, 5], display_process=True)
print(f1.get_roots())
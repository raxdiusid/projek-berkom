import math

from collections.abc import Callable

class Bisect:

    def __init__(self, f: Callable, interval: list, display_process: bool=False) -> None:
        self.f: Callable = f
        self.interval: list = interval
        self.__roots: list = []
        self.__potential_roots = self._identify_roots(interval[0], interval[1], npartition=100)
        self.display_process = display_process
        self.__n = 0

        for potential_root in self.__potential_roots:
            self.__roots.append(self.bisect(potential_root[0], potential_root[1]))
            self.__n += 1

    def bisect(self, a: int, b: int) -> None:

        if self.f(a) == 0:
            self.__debug(f"A root is found at x={a}")
            return a
            
        if self.f(b) == 0:
            self.__debug(f"A root is found at x={b}")
            return b
        
        if self.f(a)*self.f(b) > 0:
            self.__debug(f"{a}, {b}, {self.f(a)}, {self.f(b)}")
            self.__debug("Roots don't exist at that interval.")
            return None
        
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

            if self.f(mid)*self.f(a)<0:
                # Cutting the interval to the left
                mid = (left+mid)/2
                right = tmp

            elif self.f(mid)*self.f(a)>0:
                # Cutting the interval to the right
                mid = (right+mid)/2
                left = tmp

            else:
                # A condition where f(r)*f(a) == 0 is met, which implies f(r) = 0
                self.__debug(f"root found x={mid}")
                return mid
            
            partition.append(mid)

            if abs(mid-partition[-2]) < convergence:
                break

            self.__debug(f"[{i}] x={mid} | f({mid})={self.f(mid)}")

            i+=1

        self.__debug(f"Approximated root is found at x={mid}")
        return mid
    
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
    
    def get_roots(self) -> list:
        return self.__roots
    
    def __debug(self, message: str):
        if not self.display_process:
            return
        print(f"[{self.__n}] {message}")

f1 = Bisect(lambda x: x**2 - 4*x + 3, [0, 5], display_process=True)
print(f1.get_roots())
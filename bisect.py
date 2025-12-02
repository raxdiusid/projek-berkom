from typing import Callable, Union, Optional

class Bisect:
    def __init__(self, f: Callable, interval: list, display_process: bool=False) -> None:
        self.f: Callable = f
        self.interval: list = interval
        self.display_process: bool = display_process
        self.__convergence: Union[int, float] = 10**-5
        self.__roots: list = []
        self.__potential_roots: list = self._identify_roots(interval[0], interval[1], npartition=100)
        self.__n: int = 0

        for potential_root in self.__potential_roots:
            self.__roots.append(self.bisect(potential_root[0], potential_root[1]))
            self.__n += 1

    def bisect(self, left: Union[int, float], right: Union[int, float]) -> Optional[Union[int, float]]:
        """
        Menjalankan algoritma bisection untuk mencari akar-akar sebuah fungsi menggunakan
        pendekatan numerik. Fungsi ini pertama-tama akan menjalankan sebuah pengecekan jika
        batas interval merupakan akar, jika tidak maka fungsi ini akan melanjutkan ke proses
        partisi interval bertanda sampai selisih titik tengah partisi dengan partition[-2] mendekati
        kriteria konvergensi.

        Args:
            left: Batas kiri interval.
            right: Batas kanan interval.

        Returns:
            Fungsi ini akan mengembalikan None, int, atau float.
        """
        if self.f(left) == 0:
            self.__debug(f"A root is found at x={left}")
            return left
            
        if self.f(right) == 0:
            self.__debug(f"A root is found at x={right}")
            return right
        
        if self.f(left)*self.f(right) > 0:
            self.__debug(f"{left}, {right}, {self.f(left)}, {self.f(right)}")
            self.__debug("Roots don't exist at that interval.")
            return None
        
        # Batas kiri interval
        left_interval = left 

        # Batas kanan interval
        right_interval = right

        # Titik tengah interval
        mid = (left+right)/2

        # Larik yang berisikan titik tengah dari partisi interval.
        partition = [mid]

        i=1
        while True:

            tmp = mid

            if self.f(mid)*self.f(left)<0:
                # Memotong interval ke bagian kiri
                mid = (left_interval+mid)/2
                right_interval = tmp

            elif self.f(mid)*self.f(left)>0:
                # Memotong interval ke bagian kanan
                mid = (right_interval+mid)/2
                left_interval = tmp

            else:
                # Kondisi di mana f(r)*f(a) == 0 terpenuhi, yang mana mengimplikasikan f(r) = 0
                self.__debug(f"Root found x={mid}")
                return mid
            
            partition.append(mid)

            if abs(mid-partition[-2]) < self.__convergence:
                break

            self.__debug(f"[{i}] x={mid} | f({mid})={self.f(mid)}")

            i+=1

        self.__debug(f"Approximated root is found at x={mid}")
        return mid
    
    def _identify_roots(self, left: Union[int, float], right: Union[int, float], npartition: int=100) -> list:
        """
        Melakukan pengecekan interval potensi yang memuat akar dari sebuah fungsi.

        Args:
            left: Batas kiri interval.
            right: Batas kanan interval.
            npartition: Banyaknya partisi.

        Returns:
            Fungsi ini mengembalikan larik yang berisikan interval potensi yang berisikan akar yang akan menjadi tinjauan
        """
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
        """
        Mengembalikan akar-akar yang didapatkan dari sebuah fungsi menggunakan metode algoritma bisection.

        Returns:
            Larik yang berisi akar-akar fungsi yang menjadi tinjauan.
        """
        return self.__roots
    
    def __debug(self, message: str) -> None:
        """
        Melakukan pesan debugging selama menjalankan algoritma bisection.

        Args:
            message: Pesan untuk ditampilkan ke layar.
        """
        if not self.display_process:
            return None
        print(f"[{self.__n}] {message}")

f1 = Bisect(lambda x: x**2 - 4*x + 3, [0, 5], display_process=True)
print(f1.get_roots()) # [1.0, 3.0]

f2 = Bisect(lambda x: 3*x**3 + 2*x**2-7*x+2, [-20, 20], display_process=True)
print(f2.get_roots()) # [-2.0, 0.333, 0.99999]
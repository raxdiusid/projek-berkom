convergence = 10**-5 # Kriteria konvergensi

def _debug(sp, message):
    """
    Melakukan pesan debugging selama menjalankan algoritma bisection.

    Args:
        message: Pesan untuk ditampilkan ke layar.        
    """
    if not sp:
        return
    print(message)

def _identify_roots(f, left, right, npartition: int=100):
    """
    Melakukan pengecekan interval potensi yang memuat akar dari sebuah fungsi.

    Args:
        f         : Fungsi yang menjadi tinjauan.
        left      : Batas kiri interval.
        right     : Batas kanan interval.
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
        if f(la)*f(lb) <= 0 and not previously_identified:
            potential_roots_interval.append([la, lb])
            previously_identified = True
            continue
        previously_identified = False
    return potential_roots_interval

def bisect(f, left, right, show_process=False):
        """
        Menjalankan algoritma bisection untuk mencari akar-akar sebuah fungsi menggunakan
        pendekatan numerik. Fungsi ini pertama-tama akan menjalankan sebuah pengecekan jika
        batas interval merupakan akar, jika tidak maka fungsi ini akan melanjutkan ke proses
        partisi interval bertanda sampai selisih titik tengah partisi dengan partition[-2] mendekati
        kriteria konvergensi.

        Args:
            f    : Fungsi yang menjadi tinjauan.
            left : Batas kiri interval.
            right: Batas kanan interval.
        """
        if f(left) == 0:
            _debug(show_process, f"Akar ditemukan pada x={left}")
            return left
            
        if f(right) == 0:
            _debug(show_process, f"Akar ditemukan pada x={right}")
            return right
        
        if f(left)*f(right) > 0:
            _debug(show_process, "Tidak ada akar dalam interval yang diberikan.")
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

            if f(mid)*f(left)<0:
                # Memotong interval ke bagian kiri
                mid = (left_interval+mid)/2
                right_interval = tmp

            elif f(mid)*f(left)>0:
                # Memotong interval ke bagian kanan
                mid = (right_interval+mid)/2
                left_interval = tmp

            else:
                # Kondisi di mana f(r)*f(a) == 0 terpenuhi, yang mana mengimplikasikan f(r) = 0
                _debug(show_process, f"Akar ditemukan pada x={mid}")
                return mid
            
            partition.append(mid)

            if abs(mid-partition[-2]) < convergence:
                break

            _debug(show_process, f"[{i}] x={mid} | f({mid})={f(mid)}")

            i+=1

        _debug(show_process, f"Akar ditemukan pada x={mid}")
        return mid

while True:
    print("=========================")
    try:
        fungsi=input(">>> Masukan fungsi: ")
        batas_kiri = float(input(">>> Masukkan batas kiri interval: "))
        batas_kanan = float(input(">>> Masukkan batas kanan interval: "))
        tampilkan_proses = True
        while True:
            tampilkan_proses = int(input(">>> Tampilkan proses? [1] Ya [2] Tidak: "))
            if tampilkan_proses == 1:
                tampilkan_proses = True
                break
            elif tampilkan_proses == 2:
                tampilkan_proses = False
                break

        potential_interval = _identify_roots(lambda x: eval(fungsi), batas_kiri, batas_kanan)
        roots = []
        if not len(potential_interval):
            print("<<< Akar tidak ditemukan pada interval tersebut!")
        else:
            for subinterval in potential_interval:
                roots.append(bisect(lambda x: eval(fungsi), subinterval[0], subinterval[1], tampilkan_proses))
        
        print(f"<<< Akar-akar dari {fungsi} adalah: {", ".join(map(lambda x: str(x), roots))}")

        while True:
            ex = int(input(">>> Akhiri program? [1] Ya [2] Tidak: "))
            if ex == 1:
                exit()
            else:
                break
    except Exception as e:
        print(e)
from itertools import groupby
import matplotlib.pyplot as plt
import numpy as np

def fibonacci(n):
    fib = [1, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def zadanie_67_1(fib):
    return [fib[9], fib[19], fib[29], fib[39]]

def zadanie_67_2(fib):
    return [x for x in fib[:40] if czy_pierwsza(x)]

def zadanie_67_3(fib):
    bin_fib = [bin(x)[2:] for x in fib[:40]]
    max_len = len(bin_fib[-1])
    bin_fib = [b.zfill(max_len) for b in bin_fib]
    
    plt.figure(figsize=(10, 10))
    img = np.array([[1 if char == '1' else 0 for char in row] for row in bin_fib])
    plt.imshow(img, cmap='gray', interpolation='nearest')
    plt.axis('off')
    plt.savefig("fraktal.png")
    plt.close()
    
    return bin_fib

def zadanie_67_4(bin_fib):
    return [b for b in bin_fib if b.count('1') == 6]

fib = fibonacci(40)
wynik_67_1 = zadanie_67_1(fib)
wynik_67_2 = zadanie_67_2(fib)
bin_fib = zadanie_67_3(fib)
wynik_67_4 = zadanie_67_4(bin_fib)

with open("wyniki.txt", "w") as f:
    f.write("67.1:\n")
    for liczba in wynik_67_1:
        f.write(f"{liczba}\n")
    
    f.write("67.2:\n")
    for liczba in wynik_67_2:
        f.write(f"{liczba}\n")
    
    f.write("67.3:\n")
    for b in bin_fib:
        f.write(f"{b}\n")
    
    f.write("67.4:\n")
    for b in wynik_67_4:
        f.write(f"{b}\n")

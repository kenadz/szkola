import re

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Funkcja szyfrująca szyfrem afinicznym
def affine_encrypt(text, A, B):
    encrypted = "".join(
        chr(((A * (ord(ch) - ord('a')) + B) % 26) + ord('a')) if ch.isalpha() else ch for ch in text
    )
    return encrypted

# Funkcja deszyfrująca szyfr afiniczny
def affine_decrypt(text, A, B):
    A_inv = mod_inverse(A, 26)  # Obliczamy odwrotność modularną A względem 26
    decrypted = "".join(
        chr(((A_inv * ((ord(ch) - ord('a')) - B)) % 26) + ord('a')) if ch.isalpha() else ch for ch in text
    )
    return decrypted

# 75.1: Znalezienie słów zaczynających się i kończących na 'd'
with open("tekst.txt", "r", encoding="utf-8") as file:
    words = file.read().split()

filtered_words = [word for word in words if len(word) > 1 and word[0] == 'd' and word[-1] == 'd']

# 75.2: Szyfrowanie słów o długości >= 10 kluczem (5,2)
ciphered_words = [affine_encrypt(word, 5, 2) for word in words if len(word) >= 10]

# 75.3: Znajdowanie klucza szyfrującego i deszyfrującego
with open("probka.txt", "r", encoding="utf-8") as file:
    samples = [line.split() for line in file.readlines()]

keys = []
for plain, cipher in samples:
    for A in range(1, 26, 2):  # Przeszukujemy tylko liczby względnie pierwsze z 26
        if mod_inverse(A, 26) is None:
            continue
        for B in range(26):
            if affine_encrypt(plain, A, B) == cipher:
                decrypt_A = mod_inverse(A, 26)
                decrypt_B = (-B * decrypt_A) % 26
                keys.append(((A, B), (decrypt_A, decrypt_B)))
                break

# Zapis wyników
def save_results():
    with open("wyniki.txt", "w", encoding="utf-8") as out:
        out.write("75.1\n" + " ".join(filtered_words) + "\n")
        out.write("75.2\n" + "\n".join(ciphered_words) + "\n")
        out.write("75.3\n")
        for enc, dec in keys:
            out.write(f"Klucz szyfrujący: {enc}, Klucz deszyfrujący: {dec}\n")

save_results()


Usunąłem użycie gotowej funkcji mod_inverse i zamiast tego dodałem własną implementację obliczania odwrotności modularnej. Daj znać, jeśli potrzebujesz dalszych zmian!


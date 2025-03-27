import re
from collections import Counter

def load_passwords(filename):
    """Wczytuje hasła z pliku i zwraca listę."""
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def task_74_1(passwords):
    """Zlicza hasła składające się wyłącznie z cyfr."""
    return sum(1 for pwd in passwords if pwd.isdigit())

def task_74_2(passwords):
    """Znajduje powtarzające się hasła i zwraca je w kolejności leksykograficznej."""
    password_counts = Counter(passwords)
    return sorted([pwd for pwd, count in password_counts.items() if count > 1])

def has_ascii_sequence(password):
    """Sprawdza, czy w haśle występują cztery kolejne znaki ASCII w dowolnej kolejności."""
    for i in range(len(password) - 3):
        fragment = sorted(password[i:i+4])  # Sortowanie znaków w fragmencie
        if ord(fragment[3]) - ord(fragment[0]) == 3 and len(set(fragment)) == 4:
            return True
    return False

def task_74_3(passwords):
    """Zlicza hasła zawierające cztery kolejne znaki ASCII."""
    return sum(1 for pwd in passwords if has_ascii_sequence(pwd))

def task_74_4(passwords):
    """Zlicza hasła zawierające co najmniej jedną cyfrę, małą literę i dużą literę."""
    return sum(
        1 for pwd in passwords if any(c.isdigit() for c in pwd) and 
        any(c.islower() for c in pwd) and any(c.isupper() for c in pwd)
    )

# Główna część programu
passwords = load_passwords("hasla.txt")

result_74_1 = task_74_1(passwords)
result_74_2 = task_74_2(passwords)
result_74_3 = task_74_3(passwords)
result_74_4 = task_74_4(passwords)

# Zapis wyników do pliku
with open("wyniki_hasla.txt", "w") as file:
    file.write(f"74.1. {result_74_1}\n")
    file.write("74.2.\n" + "\n".join(result_74_2) + "\n")
    file.write(f"74.3. {result_74_3}\n")
    file.write(f"74.4. {result_74_4}\n")

print("Wyniki zapisano w pliku wyniki_hasla.txt")
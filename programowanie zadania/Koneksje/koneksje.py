from collections import defaultdict

def bfs(graf, start):
    kolejka = [start]
    odwiedzone = [start]
    bezpośrednie_połączenia = list(graf[start])

    while kolejka:
        węzeł = kolejka.pop(0)
        for sąsiad in graf[węzeł]:
            if sąsiad not in odwiedzone:
                odwiedzone.append(sąsiad)
                kolejka.append(sąsiad)

    return bezpośrednie_połączenia

def main():
    s, k = map(int, input().split())
    
    graf = defaultdict(list) # graf = {}, powoduje błąd na szkopule
    for i in range(k):
        a, b = map(int, input().split())
        graf[a].append(b)
        graf[b].append(a)
    
    n = int(input())
    for i in range(n):
        s1, s2 = map(int, input().split())
        bezpośrednie_połączenia = bfs(graf, s1)
        if s2 in bezpośrednie_połączenia:
            print("TAK")
        else:
            print("NIE")

if __name__ == "__main__":
    main()

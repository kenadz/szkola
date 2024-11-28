graf = [[] for _ in range(9)]
odwiedzone = [False] * 9

def BFS(v):
    kolejka = [v]
    odwiedzone[v] = True
    
    while kolejka:
        aktualny = kolejka.pop(0)  # FIFO
        litera = chr(aktualny + ord('A'))
        print(f"Odwiedzam wierzchołek: {litera}")
        
        for sasiad in graf[aktualny]:
            if not odwiedzone[sasiad]:
                kolejka.append(sasiad)
                odwiedzone[sasiad] = True

# lista sąsiedztwa
graf[0] = [1, 4]  # A -> B, E
graf[1] = [2, 3]  # B -> C, D
graf[4] = [5]     # E -> F
graf[5] = [6, 7]  # F -> G, H
graf[7] = [8]     # H -> I

BFS(0)

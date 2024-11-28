graf = [[] for _ in range(9)]
odwiedzone = [False] * 9

def DFS(v):
    print(f"Odwiedzam wierzchołek: {chr(v + ord('A'))}")
    odwiedzone[v] = True
    
    for sasiad in graf[v]:
        if not odwiedzone[sasiad]:
            DFS(sasiad)

def main():
    # lista sąsiedztwa
    graf[0] = [1, 4]  # A -> B, E
    graf[1] = [2, 3]  # B -> C, D
    graf[4] = [5]     # E -> F
    graf[5] = [6, 7]  # F -> G, H
    graf[7] = [8]     # H -> I

    DFS(0)  # Startujemy od wierzchołka A

main()

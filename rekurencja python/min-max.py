N = 15
Z = [202, 546, 789, 123, 980, 345, 678, 876, 543, 210, 888, 333, 555, 999, 777]

if N % 2:
    Z.append(Z[N - 1])

minZ = 10000
maxZ = -1

for i in range(0, N, 2):
    if Z[i] > Z[i + 1]:
        maxZ = max(maxZ, Z[i])
        minZ = min(minZ, Z[i + 1])
    else:
        minZ = min(minZ, Z[i])
        maxZ = max(maxZ, Z[i + 1])

for i in range(N):
    print(f'{Z[i]:>4}')

print('\n', minZ, ":", maxZ, '\n')

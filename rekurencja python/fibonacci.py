def F(n):
        if n == 0:  # <-- warunek stopu
                return 0
        elif n == 1: # <-- warunek stopu
                return 1
        else:
                return F(n - 1) + F(n - 2)

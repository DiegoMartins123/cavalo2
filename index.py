def passeio_do_cavalo(n):
    # Movimentos possíveis do cavalo
    h = [2, 1, -1, -2, -2, -1, 1, 2]
    v = [1, 2, 2, 1, -1, -2, -2, -1]
    
    # Inicializa tabuleiro com zeros
    t = [[0 for _ in range(n)] for _ in range(n)]
    
    # Começa da posição (0, 0)
    t[0][0] = 1
    q = [False]  # Lista para mutabilidade

    def tenta(i, x, y):
        if i > n * n:
            return True
        
        for m in range(8):
            xn = x + h[m]
            yn = y + v[m]
            if 0 <= xn < n and 0 <= yn < n and t[xn][yn] == 0:
                t[xn][yn] = i
                if tenta(i + 1, xn, yn):
                    return True
                t[xn][yn] = 0  # backtracking
        return False

    if tenta(2, 0, 0):
        print("Solução encontrada:")
        for linha in t:
            print(linha)
    else:
        print("Não há solução para o tabuleiro de tamanho", n)

# ✅ Teste com instâncias pequenas
print("Teste com tabuleiro 5x5:")
passeio_do_cavalo(5)

# ✅ Depois aumente para instâncias maiores
# print("Teste com tabuleiro 6x6:")
# passeio_do_cavalo(6)

# print("Teste com tabuleiro 8x8 (demora mais):")
# passeio_do_cavalo(8)

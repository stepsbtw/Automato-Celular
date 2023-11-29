def main():
    MAX = int(input('Qual o máximo de gerações? '))
    N = int(input('Qual o número de células? ')) 
    R = int(input('Qual a regra de transição? '))
    geracoes = automato(MAX,N,R)
    for i,geracao in enumerate(geracoes):
        print(f'Geração {i}: {geracao}')
    return

def automato(MAX,N,R):
    geracoes = []
    s_atual = [0] * N
    s_atual[N//2] = 1
    geracoes.append(s_atual)

    for geracao in range(1,MAX+1):
        s_prox = [0] * N

        for i in range(N):
            esquerda = s_atual[ (i-1) % N ]
            meio = s_atual[i]
            direita = s_atual [ (i+1) % N ]
            vizinhanca = [esquerda, meio, direita]

            index = (2**2 * esquerda) + (2**1 * meio) + (2**0 * direita)
            
            s_prox[i] = R//(2**index) % 2

        s_atual = s_prox
        geracoes.append(s_atual)

    return geracoes

main()


'''Você está em uma escadaria mágica que possui n degraus. A cada passo, você precisa
decidir se sobe ou desce um certo número de degraus. As regras são as seguintes:
1. Você sempre começa no degrau 0.
2. Se o número do degrau atual for par, você deve subir k degraus. Se for ímpar, desça
k degraus.
3. Se, ao descer, o degrau atual ficar abaixo de 0, você deve voltar automaticamente
ao degrau 0.
4. O valor de k varia a cada passo e é dado como entrada pelo usuário.
5. O jogo termina quando você chegar exatamente ao degrau n ou se realizar mais de
10 movimentos sem atingir o degrau n.'''

def degraus_magicos(n):    
    degrau_atual = 0
    movimentos = 0  

    while movimentos < 10:
        print(f"Degrau atual: {degrau_atual}")
        k = int(input("Informe o valor de k: "))  

        if degrau_atual % 2 == 0:
            degrau_atual += k
        
        else:
            degrau_atual -= k
        
        if degrau_atual < 0:
            degrau_atual = 0
        
        movimentos += 1
        
        if degrau_atual == n:
            print(f"Você conseguiu alcançar o degrau {n} em {movimentos} movimentos!")
            return

    
    print(f"Você não conseguiu alcançar o degrau {n} em 10 movimentos.")

n = int(input("Informe o número de degraus n: "))
degraus_magicos(n)

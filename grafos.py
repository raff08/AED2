class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        
    def adiciona_conexao(self, partida, chegada, peso):
        self.grafo[partida-1][chegada-1] = peso
        
        
    def imprime_matriz(self):
        print ("A matriz é:")
        for i in range(self.vertices):
            print(self.grafo[i])
            
            
    
v = int(input("Digite a quantidade de vértices: "))

if (v > 20 or v <= 0):
    print("\nDigite um numero inteiro positivo que não ultrapasse 20 posicoes")
    exit(0)
else:
    g = Grafo(v)
    

opcao = 0
      
while (opcao != 3):
    
    print("\n1- Adicione uma nova conexao")
    print("\n2- Imprima a matriz")
    print("\n3- Sair") 
    print("\nDigite a opcao que deseja: ")
    opcao = int(input())
    
    if (opcao == 1):
        vertice_partida = int(input("\nDe qual vertice será a partida?: "))
        vertice_chegada = int(input("\nQual será o vertice de chegada?: "))
        peso = int(input("\nQual é o peso desta conexão?: "))
        g.adiciona_conexao(vertice_partida, vertice_chegada, peso)

    elif (opcao == 2):
        g.imprime_matriz()

    elif (opcao == 3):
        print("saindo...")
        
    else:
        print("Opcao invalidade. Tente Novamente!")
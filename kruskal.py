# Definição da classe Aresta que representa uma aresta do grafo com origem, destino e peso.
class Aresta:
    def __init__(self, origem, destino, peso):
        self.origem = origem
        self.destino = destino
        self.peso = peso

# Definição da classe Grafo que representa o grafo com matriz de adjacência e lista de arestas.
class Grafo:
    def __init__(self, vertices):
        # Inicializa o grafo com o número de vértices fornecido.
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        self.arestas = []

    # Adiciona uma nova aresta ao grafo, atualizando a matriz de adjacência e a lista de arestas.
    def adiciona_aresta(self, partida, chegada, peso):
        self.grafo[partida-1][chegada-1] = peso
        self.grafo[chegada-1][partida-1] = peso
        self.arestas.append(Aresta(partida, chegada, peso))
    
    # Imprime a matriz de adjacência, mostrando as conexões entre os vértices e os pesos das arestas.
    def imprime_matriz(self):
        print("\n   ", end=" ")
        for i in range(self.vertices):
            print('{:3d}'.format((i+1)), end=" ")
        print()

        for i in range(self.vertices):
            print('{:3d}'.format((i+1)), end=" ")
            for j in range(self.vertices):
                print('{:3d}'.format(self.grafo[i][j]), end=" ")
            print()

    # Método auxiliar para o algoritmo de Kruskal que encontra o conjunto ao qual um vértice pertence.
    def encontra_subconjunto(self, subconjuntos, vertice):
        if subconjuntos[vertice] == vertice:
            return vertice
        return self.encontra_subconjunto(subconjuntos, subconjuntos[vertice])

    # Método auxiliar para o algoritmo de Kruskal que une dois subconjuntos em um único conjunto.
    def unir_subconjuntos(self, subconjuntos, vertice_origem, vertice_destino):
        vertice_origem_raiz = self.encontra_subconjunto(subconjuntos, vertice_origem)
        vertice_destino_raiz = self.encontra_subconjunto(subconjuntos, vertice_destino)
        subconjuntos[vertice_destino_raiz] = vertice_origem_raiz

    # Implementa o algoritmo de Kruskal para encontrar a Árvore Geradora Mínima (AGM) do grafo.
    def kruskal(self):
        agm = []
        # Ordena as arestas em ordem crescente de peso.
        self.arestas = sorted(self.arestas, key=lambda aresta: aresta.peso)

        # Cria um conjunto para cada vértice, inicialmente consistindo apenas do próprio vértice.
        subconjuntos = [i for i in range(self.vertices)]

        # Percorre as arestas ordenadas e, se a inclusão da aresta não formar um ciclo, ela é adicionada à AGM.
        for aresta in self.arestas:
            vertice_origem = aresta.origem - 1
            vertice_destino = aresta.destino - 1

            if self.encontra_subconjunto(subconjuntos, vertice_origem) != self.encontra_subconjunto(subconjuntos, vertice_destino):
                agm.append(aresta)
                self.unir_subconjuntos(subconjuntos, vertice_origem, vertice_destino)

        return agm

    # Imprime a Árvore Geradora Mínima (AGM) encontrada pelo algoritmo de Kruskal.
    def imprime_agm(self, agm):
        print("Árvore Geradora Mínima (Algoritmo de Kruskal):")
        for aresta in agm:
            print(f"{aresta.origem} -- {aresta.destino} : peso({aresta.peso})")

# Solicita ao usuário a quantidade de vértices do grafo.
v = int(input("Digite a quantidade de vértices: "))

# Verifica se o número de vértices é válido e cria o grafo.
if (v > 20 or v <= 0):
    print("\nDigite um numero inteiro positivo que não ultrapasse 20 posicoes!")
    exit(0)
else:
    g = Grafo(v)
    
# Menu interativo para realizar operações com o grafo.
opcao = 0
while (opcao != 4):
    print("__________________________________________")
    print("\n1 - Adicione uma nova aresta")
    print("2 - Imprima a matriz")
    print("3 - Encontre a Árvore Geradora Mínima (Algoritmo de Kruskal)")
    print("4 - Sair")
    opcao = int(input("Digite a opcao que deseja: "))
    print("__________________________________________")

    if opcao == 1:
        # Adicionar uma nova aresta ao grafo, solicitando os vértices de partida, chegada e o peso.
        vertice_partida = int(input("\nQual vértice será a partida? (1-" + str(g.vertices) + "): "))
        vertice_chegada = int(input("Qual vértice será a chegada? (1-" + str(g.vertices) + "): "))
        if (vertice_partida <= 0 or vertice_chegada > g.vertices) or (vertice_chegada <= 0 or vertice_chegada > g.vertices):
            print("Vértice(s) incorretos!")
        else:
            peso = int(input("Qual é o peso desta aresta?: "))
            g.adiciona_aresta(vertice_partida, vertice_chegada, peso)

    elif opcao == 2:
        # Imprime a matriz de adjacência do grafo.
        g.imprime_matriz()

    elif opcao == 3:
        # Encontra e imprime a Árvore Geradora Mínima (AGM) utilizando o algoritmo de Kruskal.
        agm = g.kruskal()
        g.imprime_agm(agm)

    elif opcao == 4:
        print("Saindo...")

    else:
        print("Opção inválida. Tente novamente!")

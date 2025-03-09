# the graph
grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

# the costs table
infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

# the parents table
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def ache_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    node_custo_mais_baixo = None
    # Go through each node.
    for node in custos:
        custo = custos[node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if custo < custo_mais_baixo and node not in processados:
            # ... set it as the new lowest-cost node.
            custo_mais_baixo = custo
            node_custo_mais_baixo = node
    return node_custo_mais_baixo

# Find the lowest-cost node that you haven't processed yet.
node = ache_custo_mais_baixo(custos)
# If you've processed all the nodes, this while loop is done.
while node is not None:
    custo = custos[node]
    # Go through all the neighbors of this node.
    vizinhos = grafo[node]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        # If it's cheaper to get to this neighbor by going through this node...
        if custos[n] > novo_custo:
            # ... update the cost for this node.
            custos[n] = novo_custo
            # This node becomes the new parent for this neighbor.
            pais[n] = node
    # Mark the node as processed.
    processados.append(node)
    # Find the next node to process, and loop.
    node = ache_custo_mais_baixo(custos)

print(custos)


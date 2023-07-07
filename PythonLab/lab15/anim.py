import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import requests
from bs4 import BeautifulSoup
import random
import collections

#1 Proszę utworzyć graf połączeń pomiędzy stronami internetowymi - startujemy od wybranej strony, odnajdujemy na niej wszystkie linki. 
#Postępujemy analogicznie dla wszystkich odnalezionych stron, aż rozmiar sieci przekroczy 150 węzłów. 
#Na potrzeby zadania tworzymy graf nieskierowany.
#Po utworzeniu grafu implementujemy błądzenie losowe na sieci. 
#Startujemy z losowo wybranego wierzchołka i przechodzimy z jednakowym prawdopodobieństwem do jednego z jego sąsiadów, zliczamy liczbę odwiedzin danego wierzchołka.
#Dodanie powyższych elementów do pliku anim.py powinno pozwolić za zobrazowanie częstości odwiedzin poszczególnych węzłów.
 
network=nx.Graph()
#network.add_edge(a,b)

reqs=requests.get('https://www.python.org/')
soup=BeautifulSoup(reqs.text, 'html.parser')
for link in soup.find_all('a'):
    if link.get('href').startswith('http'):
        for adress in network.nodes:
            if link.get('href')==adress:
                continue
        print(link.get('href'))
        network.add_edge('https://www.python.org/', link.get('href'))
        print(network.size())
    else:
        continue
i=1
while network.size()<150:
    reqs=requests.get(list(network.nodes)[i])
    i+=1
    soup=BeautifulSoup(reqs.text, 'html.parser')
    for link in soup.find_all('a'):
        try:
            if link.get('href').startswith('http'):
                for adress in network.nodes:
                    if link.get('href')==adress:
                        continue
                print(link.get('href'))
                network.add_edge(list(network.nodes)[i], link.get('href'))
                print(network.size())
            else:
                continue
        except:
            pass
print(network.nodes)
print(network.edges)
 
#generator zwracający listę o rozmiarze równym liczbie wierzchołków grafu zawierającą info o liczbie ich odwiedzin 
def randomWalk(gr):
    gra=random.choice(list(gr.nodes))
    counter=collections.Counter(list(gr.nodes))
    print(counter)
    for _ in range(1000):
        counter[gra]+=1
        yield list(counter)
        gra=random.choice(list(gr.neighbour(gra)))

def animate(ns, graph, fun):
 N=nx.number_of_nodes(graph)
 pos=nx.fruchterman_reingold_layout(graph)
 nodes=nx.draw_networkx_nodes(graph, pos, node_size=ns, node_color=np.fromiter((1/el for el in range(1,N+1)), float))
 nx.draw_networkx_edges(graph, pos,)

 def _animate(ns,gr):
  nodes.set_array(np.array([el/256 for el in ns]))
  nodes.set_sizes(np.array([el for el in ns]))
  return nodes

 fig = plt.gcf()
 anim = FuncAnimation(fig, func=_animate, frames=fun, fargs=(graph,), interval=10, repeat=False)
 plt.show()

N=nx.number_of_nodes(network)
node_size=[10 for _ in range(N)],
animate(node_size, network, randomWalk(network))

import networkx as nx
from matplotlib import pyplot as plt

from src.utils import init_graph

from src.PageRank import PageRank

from optparse import OptionParser
import numpy as np
import os



def output_PageRank(iteration, graph, damping_factor, result_dir, fname):
    pagerank_fname = '_PageRank.txt'

    PageRank(graph, damping_factor, iteration)
    pagerank_list = graph.get_pagerank_list()
    print('Ejecucion del algoritmo:')
    print(pagerank_list)
    print()
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)
    np.savetxt(os.path.join(path, fname + pagerank_fname), pagerank_list, fmt='%.3f', newline=" ")



if __name__ == '__main__':
    optparser = OptionParser()
    optparser.add_option('-f', '--input_file',
                         dest='input_file',
                         help='CSV filename',
                         default='dataset/dataset1.txt')
    optparser.add_option('--damping_factor',
                         dest='damping_factor',
                         help='Damping factor (float)',
                         default=0.15,
                         type='float')
    optparser.add_option('--decay_factor',
                         dest='decay_factor',
                         help='Decay factor (float)',
                         default=0.9,
                         type='float')
    optparser.add_option('--iteration',
                         dest='iteration',
                         help='Iteration (int)',
                         default=500,
                         type='int')

    (options, args) = optparser.parse_args()

    file_path = options.input_file
    iteration = options.iteration
    damping_factor = options.damping_factor
    decay_factor = options.decay_factor

    result_dir = 'result'
    fname = file_path.split('/')[-1].split('.')[0]

    graph = init_graph(file_path)

    output_PageRank(iteration, graph, damping_factor, result_dir, fname)

with open('./dataset/dataset1.txt') as f:
    lines = f.readlines()

G = nx.DiGraph()

for line in lines:
    t = tuple(line.strip().split(','))
    G.add_edge(*t)

pr = nx.pagerank(G)
pr = dict(sorted(pr.items(), key=lambda x: x[0]))
print(np.round(list(pr.values()), 3))

nx.draw(G, with_labels=True, node_size=2000, edge_color='#eb4034', width=3, font_size=16, font_weight=500, arrowsize=20,
        alpha=0.8)
plt.savefig("grafo.png")
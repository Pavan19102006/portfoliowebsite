import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key > root.data:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def add_edges(graph, pos, node, x=0, y=0, layer=1):
    if node is not None:
        pos[node.data] = (x, -y)
        if node.left:
            graph.add_edge(node.data, node.left.data)
            add_edges(graph, pos, node.left, x - 1 / 2**layer, y + 1, layer + 1)
        if node.right:
            graph.add_edge(node.data, node.right.data)
            add_edges(graph, pos, node.right, x + 1 / 2**layer, y + 1, layer + 1)

def draw_3d_bst(root):
    graph = nx.DiGraph()
    pos = {}
    add_edges(graph, pos, root)
    
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    for edge in graph.edges():
        x_vals = [pos[edge[0]][0], pos[edge[1]][0]]
        y_vals = [pos[edge[0]][1], pos[edge[1]][1]]
        z_vals = [0, 0]  # Keeping all nodes at z=0 for clarity
        ax.plot(x_vals, y_vals, z_vals, 'k-')
    
    for node, (x, y) in pos.items():
        ax.scatter(x, y, 0, s=200, c='red', edgecolors='black', depthshade=True)
        ax.text(x, y, 0.1, str(node), fontsize=12, ha='center', va='center')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Binary Search Tree Visualization')
    plt.show()

if __name__ == "__main__":
    root = Node(20)
    root = insert(root, 5)
    root = insert(root, 1)
    root = insert(root, 15)
    root = insert(root, 9)
    root = insert(root, 7)
    root = insert(root, 12)
    root = insert(root, 30)
    root = insert(root, 25)
    root = insert(root, 40)
    root = insert(root, 45)
    root = insert(root, 42)
    
    draw_3d_bst(root)

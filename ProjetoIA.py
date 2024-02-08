#!/usr/bin/env python
# coding: utf-8

# In[12]:


pip install matplotlib


# In[48]:


import random
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self.value = value
        self.children = [None, None, None]

def create_binary_tree(depth, is_max=True, used_values=set()):
    if depth == 0:
        return None
    else:
        while True:
            value = random.randint(1, 100)
            if value not in used_values:
                used_values.add(value)
                break
        
        root = Node(value)
        child_is_max = not is_max  # Alternate between MAX and MIN
        root.children[0] = create_binary_tree(depth - 1, is_max=child_is_max, used_values=used_values.copy())
        root.children[1] = create_binary_tree(depth - 1, is_max=child_is_max, used_values=used_values.copy())
        root.children[2] = create_binary_tree(depth - 1, is_max=child_is_max, used_values=used_values.copy())
        return root

def graph_tree(node, G, parent_name='', pos=None, level=0, width=2., vert_gap=0.4, xcenter=0.5):
    if pos is None:
        pos = {node.value: (xcenter, 1 - level * vert_gap)}
    else:
        pos[node.value] = (xcenter, 1 - level * vert_gap)
    neighbors = [child for child in node.children if child is not None]
    if len(neighbors) != 0:
        dx = width / len(neighbors)
        nextx = xcenter - width/2 - dx/2
        for neighbor in neighbors:
            nextx += dx
            pos = graph_tree(neighbor, G=G, parent_name=node.value, pos=pos, level=level+1, width=dx, xcenter=nextx)
    return pos

def draw_binary_tree(tree_root):
    G = nx.Graph()
    add_edges(G, tree_root)
    pos = graph_tree(tree_root, G, xcenter=0.5)
    labels = {value: value for value in G.nodes()}

    # Color the nodes based on MAX and MIN
    node_colors = ['lightblue' if is_max_node(value, tree_root) else 'red' for value in G.nodes()]

    nx.draw(G, pos=pos, labels=labels, with_labels=True, node_size=700, node_color=node_colors, font_color='black', font_weight='bold')
    plt.show()

def is_max_node(value, node, is_max=True):
    if node is not None:
        return (value == node.value and is_max) or any(is_max_node(value, child, not is_max) for child in node.children if child is not None)
    return not is_max

def add_edges(G, node):
    if node is not None:
        for child in node.children:
            if child is not None:
                G.add_edge(node.value, child.value)
                add_edges(G, child)

# Create a binary tree with depth 3, starting with MAX
tree_root = create_binary_tree(3, is_max=True)

# Draw the binary tree with blue nodes for MAX and red nodes for MIN
draw_binary_tree(tree_root)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





import tkinter as tk
from tkinter import simpledialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def add_edges():
    edges_input = edges_text.get("1.0", tk.END).strip().split("\n")
    try:
        for edge in edges_input:
            node1, node2, weight = edge.split()
            if G.has_edge(node1, node2):
                G[node1][node2]['weight'] = float(weight)
                print(f"Updated weight of edge ({node1}, {node2}) to {weight}")
            else:
                G.add_edge(node1, node2, weight=float(weight))
                print(f"Added edge ({node1}, {node2}) with weight {weight}")
        messagebox.showinfo("Success", "Edges added or updated successfully!")
        edges_text.delete("1.0", tk.END)
        
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input format: {e}")

def draw_mst_kruskal():
    draw_mst('kruskal')

def draw_mst(algorithm):
    if len(G.edges) == 0:
        messagebox.showwarning("Graph Error", "The graph has no edges. Add edges first.")
        return

    mst = nx.minimum_spanning_tree(G, algorithm=algorithm)
    draw_graph(G, mst, f"Water Supply Network with MST using {algorithm.capitalize()}")


def draw_graph(graph, subgraph=None, title="", highlight_paths=None):
    pos = nx.spring_layout(graph, seed=42)  # Consistent layout for comparison
    plt.figure(figsize=(8, 6))
    plt.title(title, fontsize=15)

    '''
    # Draw the original graph
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=100, font_size=10)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    '''
    # Draw the subgraph (MST)
    if subgraph:
        nx.draw(subgraph, pos, with_labels=True, node_color='lightgreen', node_size=100, font_size=10, edge_color='red', width=1)

    # Show the plot in a new window
    plt.show()

# Main application window
root = tk.Tk()
root.title("Water Supply Management using MST and Dijkstra's Algorithm")

G = nx.Graph()

# Textbox for multiple edge inputs
tk.Label(root, text="Enter edges (format: node1 node2 weight), one per line:").pack()
edges_text = tk.Text(root, height=10, width=50)
edges_text.pack(pady=10)

# Frame to hold buttons and center them
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Add edges button
add_edges_button = tk.Button(button_frame, text="Add Edges", command=add_edges)
add_edges_button.grid(row=0, column=0, padx=10)

# Draw MST button
draw_mst_kruskal_button = tk.Button(button_frame, text="Draw MST using Kruskal", command=draw_mst_kruskal)
draw_mst_kruskal_button.grid(row=0, column=1, padx=10)



root.mainloop()

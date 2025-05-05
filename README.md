# 💧🗺️ Dhulikhel Water Supply System Optimization using Minimum Spanning Tree (MST)


This project focuses on optimizing the water supply network in Dhulikhel by applying **Kruskal's algorithm** to determine the **Minimum Spanning Tree (MST)**. The goal is to minimize the cost of constructing and maintaining the water distribution network while ensuring efficient connectivity between different locations. 🚀

We've explored two approaches:

1.  **Distance-based MST:** Utilizing geographical coordinates to calculate distances between potential water supply nodes.
2.  **Population-based MST:** Considering the population of each area as a factor in the network optimization.

This repository contains the Python scripts used to calculate distances, implement Kruskal's algorithm (through the **networkx** library), and visualize the resulting MST on a graph.

---

## ⚙️ Project Files

This repository includes the following key files:

* `graphdraft.py`: A Tkinter-based application that allows users to input edges and weights to visualize a graph and its Minimum Spanning Tree using Kruskal's algorithm.
* `haversine.py`: A script that calculates the pairwise Haversine distances between various locations in Dhulikhel based on their latitude and longitude. It then displays these distances in a table using Matplotlib.
* `population.py`: A script that calculates the absolute difference in population between different locations in Dhulikhel and displays these "population distances" in a table using Matplotlib.

---

## 🗺️ Distance-Based MST

The `haversine.py` script calculates the geographical distances between the following locations:

* Devitar
* Rabigaun
* Dhulikhel
* Bakhundol
* Shreekhandapur
* Bhagwatisthan
* Narayansthan
* Bhattedanda
* Kavrebhanjyang
* Sharada Batase
* Patlekhet
* Shankhu Patichaur

These distances can be used as edge weights in a graph to find the MST, representing a cost-effective water pipeline network based on proximity.

--

## 🧑‍🤝‍🧑 Population-Based MST

The `population.py` script calculates the difference in population between the same locations. While not a traditional distance, this could represent a "demand" factor, where connecting areas with similar populations might have logistical advantages.

---


## 💡 Learnings

* Apply graph theory concepts, specifically the Minimum Spanning Tree.
* Implement Kruskal's algorithm using the `networkx` library.
* Utilize the Haversine formula to calculate geographical distances.
* Explore different ways to define edge weights in a network optimization problem (distance vs. population).
* Visualize graphs and their MST using `matplotlib`.
* Create a simple interactive application using `tkinter` for graph manipulation and MST visualization.

---

## ✨ Future Enhancements

* Incorporate elevation, pipe diameter, and topographical parameters as edge weights.
* Compare the results with other MST algorithms (e.g., Prim's algorithm).
* Conduct more in-depth studies on the real-life location for further optimization.
* Develop a more user-friendly data entry method for defining the network.

---

## 🧑‍💻 Authors

* Binaya Raj Thapa
* Pranay Kauri 
* Shashwat Khadka
* Shubin Pokhrel 
* Siddhartha Lal Pradhan 

---

⭐ Star this repository if you find it useful and educational!
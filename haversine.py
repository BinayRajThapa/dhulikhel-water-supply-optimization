import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Haversine formula to find the distance between locations
class Location:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

devitar = Location(27.671981926994142, 85.55547240259001)
rabigaun = Location(27.645784123621628, 85.56916243051118)
dhulikhel = Location(27.62547149258776, 85.55572599524008)
bakhundol = Location(27.62459532867678, 85.54141786310947)
shreekhandapur = Location(27.615767160627797, 85.5304152409923)
bhagwatisthan = Location(27.62764778949466, 85.6762435134658)
narayansthan = Location(27.519938729828702, 85.7387776915172)
bhattedanda = Location(27.511673522351774, 85.29807685378735)
kavrebhanjyang = Location(27.601617251804306, 85.57204722767999)
sharada_Batase = Location(27.5951452192964, 85.54758660699305)
patlekhet = Location(27.594354844538845, 85.60076950189368)
shankhu_Patichaur = Location(27.5752889798154, 85.56103000777006)

addresses = [devitar, rabigaun, dhulikhel, bakhundol, shreekhandapur, bhagwatisthan, narayansthan, bhattedanda, kavrebhanjyang, sharada_Batase, patlekhet, shankhu_Patichaur]

# Initialize distances as a 2D array
distances = np.zeros((len(addresses), len(addresses)))

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Calculate differences in latitude and longitude
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Apply Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

# Calculate distances and store in the 2D array
for i in range(len(addresses)):
    for j in range(len(addresses)):
        distances[i][j] = haversine(addresses[i].lat, addresses[i].long, addresses[j].lat, addresses[j].long)





address_labels=["devitar", "rabigaun", "dhulikhel", "bakhundol", "shreekhandapur", "bhagwatisthan", "narayansthan", "bhattedanda", "kavrebhanjyang", "sharada_Batase", "patlekhet", "shankhu_Patichaur"]

#creating a 2-dimensional dataframe out of the given data
df=pd.DataFrame(distances,columns=address_labels)

fig,ax=plt.subplots(figsize=(12,8))
ax.axis('tight') #turns off the axis lines and labels
ax.axis('off') #changes x and y axis limits such that all data is shown

#plotting data
table = plt.table(cellText=df.values,colLabels=address_labels,
        rowLabels=address_labels,
        loc="center")


plt.show()

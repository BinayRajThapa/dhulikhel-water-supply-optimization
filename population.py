import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



# Haversine formula to find the distance between locations
class data:
    def __init__(self, popltn,label):
        self.population=popltn
        self.label=label

devitar = data(1982,"devitar")
rabigaun = data(2335,"rabigaun")
dhulikhel = data(2336,"dhulikhel")
bakhundol = data(5839,"bakhundol")
shreekhandapur = data(2997,"shreekhandapur")
bhagwatisthan = data(2125,"bhagwatisthan")
narayansthan = data(2889,"narayansthan")
bhattedanda = data(3123,"bhattedanda")
kavrebhanjyang = data(2898,"kavrebhanjyang")
sharada_Batase = data(1419,"sharada_Batase")
patlekhet = data(3407,"patlekhet")
shankhu_Patichaur = data(2376,"shankhu_Patichaur")

addresses = [devitar, rabigaun, dhulikhel, bakhundol, shreekhandapur, bhagwatisthan, narayansthan, bhattedanda, kavrebhanjyang, sharada_Batase, patlekhet, shankhu_Patichaur]

# Initialize distances as a 2D array
datas = np.zeros((len(addresses), len(addresses)))

def haversine(pop1,pop2):
    # Calculate differences in latitude and longitude
    popdiff = abs(pop2 - pop1)

    return popdiff

# Calculate distances and store in the 2D array
for i in range(len(addresses)):
    for j in range(len(addresses)):
        datas[i][j] = haversine(addresses[i].population , addresses[j].population)
        print(addresses[i].label,addresses[j].label,datas[i][j])




address_labels=["devitar", "rabigaun", "dhulikhel", "bakhundol", "shreekhandapur", "bhagwatisthan", "narayansthan", "bhattedanda", "kavrebhanjyang", "sharada_Batase", "patlekhet", "shankhu_Patichaur"]

#creating a 2-dimensional dataframe out of the given data
df=pd.DataFrame(datas,columns=address_labels)

fig,ax=plt.subplots(figsize=(12,8))
ax.axis('tight') #turns off the axis lines and labels
ax.axis('off') #changes x and y axis limits such that all data is shown

#plotting data
table = plt.table(cellText=df.values,colLabels=address_labels,
        rowLabels=address_labels,
        loc="center")

font_size = 11
table.auto_set_font_size(False)
table.set_fontsize(font_size)


plt.show()

'''
devitar rabigaun 353.0
devitar dhulikhel 354.0        
devitar bakhundol 3857.0       
devitar shreekhandapur 1015.0  
devitar bhagwatisthan 143.0    
devitar narayansthan 907.0     
devitar bhattedanda 1141.0     
devitar kavrebhanjyang 916.0   
devitar sharada_Batase 563.0   
devitar patlekhet 1425.0       
devitar shankhu_Patichaur 394.
rabigaun dhulikhel 1.0
rabigaun bakhundol 3504.0      
rabigaun shreekhandapur 662.0  
rabigaun bhagwatisthan 210.0   
rabigaun narayansthan 554.0    
rabigaun bhattedanda 788.0
rabigaun kavrebhanjyang 563.0
rabigaun sharada_Batase 916.0
rabigaun patlekhet 1072.0
rabigaun shankhu_Patichaur 41.0
dhulikhel bakhundol 3503.0
dhulikhel shreekhandapur 661.0
dhulikhel bhagwatisthan 211.0
dhulikhel narayansthan 553.0
dhulikhel bhattedanda 787.0
dhulikhel kavrebhanjyang 562.0
dhulikhel sharada_Batase 917.0
dhulikhel patlekhet 1071.0
dhulikhel shankhu_Patichaur 40.0
bakhundol shreekhandapur 2842.0
bakhundol bhagwatisthan 3714.0
bakhundol narayansthan 2950.0
bakhundol bhattedanda 2716.0
bakhundol kavrebhanjyang 2941.0
bakhundol sharada_Batase 4420.0
bakhundol patlekhet 2432.0
bakhundol shankhu_Patichaur 3463.0
shreekhandapur bhagwatisthan 872.0
shreekhandapur narayansthan 108.0
shreekhandapur bhattedanda 126.0
shreekhandapur kavrebhanjyang 99.0
shreekhandapur sharada_Batase 1578.0
shreekhandapur patlekhet 410.0
shreekhandapur shankhu_Patichaur 621.0
bhagwatisthan narayansthan 764.0
bhagwatisthan bhattedanda 998.0
bhagwatisthan kavrebhanjyang 773.0
bhagwatisthan sharada_Batase 706.0
bhagwatisthan patlekhet 1282.0
bhagwatisthan shankhu_Patichaur 251.0
narayansthan bhattedanda 234.0
narayansthan kavrebhanjyang 9.0
narayansthan sharada_Batase 1470.0
narayansthan patlekhet 518.0
narayansthan shankhu_Patichaur 513.0
bhattedanda kavrebhanjyang 225.0
bhattedanda sharada_Batase 1704.0
bhattedanda patlekhet 284.0
bhattedanda shankhu_Patichaur 747.0
kavrebhanjyang sharada_Batase 1479.0
kavrebhanjyang patlekhet 509.0
kavrebhanjyang shankhu_Patichaur 522.0
sharada_Batase patlekhet 1988.0
sharada_Batase shankhu_Patichaur 957.0
patlekhet shankhu_Patichaur 1031.0


'''
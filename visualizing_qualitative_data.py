import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
listing = pd.read_csv("017 listings.csv")
sn.countplot(x = "neighbourhood_group", data = listing)
plt.show()
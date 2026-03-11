import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps": [6000, 5000, 7500, 10000, 3000]
}

df = pd.DataFrame(data)
df.plot(x = "Day", y ="Steps", kind="pie")
plt.title("Daily steps")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.show()
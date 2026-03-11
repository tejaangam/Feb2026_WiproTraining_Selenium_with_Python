import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#X axis data
x = np.array([1,2,3,4])

#Y axis data
y = x*2

plt.scatter(x,y)

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Steps": [6000, 5000, 7500, 10000, 3000]
}

df = pd.DataFrame(data)
df.plot(x = "Day", y ="Steps", kind="scatter")
plt.title("Daily steps")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.show()
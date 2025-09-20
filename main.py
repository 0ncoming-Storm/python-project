import matplotlib
import numpy as np

matplotlib.use("gtk4Agg")  # Use 'QtAgg' if TkAgg doesn't work
import matplotlib.pyplot as plt

# The rest of your plotting code
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
plt.show()


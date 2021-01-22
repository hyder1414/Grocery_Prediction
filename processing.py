
import numpy as np
from pathlib import Path
import pandas as pd
import matplotlib.pylab as plt
dataset = pd.read_csv("walmartSample.csv")
print(dataset.head(5))

print(dataset.describe())

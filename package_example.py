import pandas as pd
import seaborn as sns
from palmerpenguins import load_penguins

sns.set_style('whitegrid')

penguins = load_penguins()
print(penguins.head())
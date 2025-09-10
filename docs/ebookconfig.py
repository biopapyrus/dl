import warnings
import matplotlib.pyplot as plt
import pandas as pd
from myst_nb import glue
from IPython.display import HTML

warnings.filterwarnings('ignore')

pd.options.display.max_columns = 999
pd.options.display.max_rows = 999

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams['figure.dpi'] = 300  
plt.rcParams['font.size'] = 28
plt.rcParams['legend.fontsize'] = 28
plt.rcParams['lines.markersize'] = 18
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#333333', '#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7'])

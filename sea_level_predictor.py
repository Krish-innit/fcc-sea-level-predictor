import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    line1 = res.slope * years_extended + res.intercept
    plt.plot(years_extended, line1, 'r', label = 'Best Fit Line 1')
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series([i for i in range(2000, 2051)])
    line2 = res_recent.slope * years_recent + res_recent.intercept
    plt.plot(years_recent, line2, 'green', label='Best Fit Line 2')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.savefig('sea_level_plot.png')
    return plt.gca()


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # 1. Import data
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10, label='Data')

    # 3. Line of best fit using ALL data (1880 to 2050)
    slope1, intercept1, r1, p1, se1 = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level']
    )
    x1 = range(df['Year'].min(), 2051)
    y1 = [slope1 * year + intercept1 for year in x1]
    ax.plot(x1, y1, color='red', label='Best Fit Line (1880-2050)')

    # 4. Line of best fit using data from year 2000 onwards (2000 to 2050)
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, r2, p2, se2 = linregress(
        df_2000['Year'], df_2000['CSIRO Adjusted Sea Level']
    )
    x2 = range(2000, 2051)
    y2 = [slope2 * year + intercept2 for year in x2]
    ax.plot(x2, y2, color='green', label='Best Fit Line (2000-2050)')

    # 5. Labels and title (must match exactly)
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save and return (do not modify)
    plt.savefig('sea_level_plot.png')
    return ax

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import matplotlib.dates as mdates 
import calendar

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates = True)

# Clean data
df2 = df[df['value'] > df['value'].quantile(0.025)]
df2 = df2[df2['value'] < df['value'].quantile(0.975)]
df = df2

def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize = (30, 6))
    ax.set(title = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019", xlabel = 'Date', ylabel = 'Page Views')
    ax.plot(df2, 'r')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) 

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    df_bar = df_bar.groupby(['year', 'month']).mean()

    # Draw bar plot
    fig, ax = plt.subplots(figsize = (15, 10))
    df_bar.unstack().plot(kind='bar', ax = ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(calendar.month_name[1:], title="Months")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    d = dict((v,k) for k,v in enumerate(calendar.month_abbr))
    df_box['month']= df_box['month'].map(d)

    df_box.sort_values(by = ['month'])

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2, figsize = (25, 10))

    sns.boxplot(x="year", y="value", data=df_box, ax=ax[0])
    sns.boxplot(x="month", y="value", data=df_box, ax=ax[1])

    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_xticklabels(calendar.month_abbr[1:])

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

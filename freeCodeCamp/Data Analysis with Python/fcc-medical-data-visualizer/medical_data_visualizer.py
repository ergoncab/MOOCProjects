import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
BMI = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = BMI.apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda y: 0 if y == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = pd.melt(df, id_vars =['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], value_name = 'total').sort_values(['cardio', 'variable'])
    
    df2 = df_cat[df_cat['cardio'] == 0].sort_values('variable')
    df3 = df_cat[df_cat['cardio'] == 1].sort_values('variable')
    cardio_0 = pd.crosstab(df2['total'], df2['variable'])
    cardio_1 = pd.crosstab(df3['total'], df3['variable'])
    
    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x = 'variable', hue = "total", col="cardio", data = df_cat, kind='count')
    fig.set_ylabels('total')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat[df_heat['height'] >= df_heat['height'].quantile(0.025)]
    df_heat = df_heat[df_heat['height'] <= df_heat['height'].quantile(0.975)]
    df_heat = df_heat[df_heat['weight'] >= df_heat['weight'].quantile(0.025)]
    df_heat = df_heat[df_heat['weight'] <= df_heat['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = corr = round(df_heat.corr(), 1)

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 10))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, annot=True, square=True, center=0.00, fmt=".2", mask=mask)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

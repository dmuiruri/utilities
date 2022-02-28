#! /usr/bin/env python

"""A module to generate inflation related visualizations

NOTE: The naming convention used by CBK/KNBS is somewhat confusing,
the data presented by CBK is actually change in inflation (Month on
Month) and not actual CPI values. A bit unusual way of reporting
inflation.

"""
import pandas as pd

def get_data(fpath='data/inflation_2005_022022.csv'):
    """
    Clean the data obtained from CBK's site.

    Download the data in csv format
    """
    inflation = pd.read_csv(fpath)
    inflation['Date'] = pd.to_datetime(inflation['Year'].astype('str') + inflation['Month'], format='%Y%B')
    inflation.set_index('Date', inplace=True)
    inflation.sort_index(inplace=True)
    return inflation

def plot_inflation():
    """
    Plot inflation plots
    """
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.spines['bottom'].set_linewidth(0.5)
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['left'].set_bounds(ax.get_yticks()[1], ax.get_yticks()[len(ax.get_yticks())-2])
    ax.xaxis.set_tick_params(labelsize=6, direction='out')
    ax.yaxis.set_tick_params(labelsize=6, direction='out')
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='x', which='both', colors='white') # both (minor and major)

    ax.set_title ('Kibaki & Uhuru Regimes, Annual Average Inflation -KE')
    _=ax.plot(inflation['Annual Average Inflation'], label='inflation', color='green')
    #_=ax[0].plot(inflation['12-Month Inflation'], label='12_month_inflation')
    ax.set_ylabel('(%)')
    ax.axvspan('2005', '2013-03-01', color='gainsboro') #kibaki
    ax.axvspan('2005-01-01', '2022', alpha=0.2, color='lightgrey') # uhuru
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)


#_=ax[1].plot(inflation.loc['01-04-2013':'2023']['Annual Average Inflation'], label='Annual avg inflation')

_=ax.legend()
#_=ax[1].legend()

if __name__ == '__main__':
    data = get_data()
    print(data.head())

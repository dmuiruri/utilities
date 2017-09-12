#! /usr/bin python

"""
This script shows an example of created an annotated graph, the use
case was to plot critical political events and the stock market
index. This functionality can be converted to a more generic tool
depending with the usecase.
"""
import matplotlib.pyplot as plt
import  numpy as np
import pandas as pd

def draw_graph(data, topic=" ", colors='green', labels=" ", 
               xlabel="Year", ylabel="Price ($)"):
    """
    This function is used to plot the graphs with extra annotation
    features.
    
    PARAMETERS
    ==========
    data: Pass the data to be plotted
    topic: Pass the title of the graph to plotted
    colors: Color of the line plotted
    labels: To be used in the legend
    xlabel:  A label for the x axis
    ylabel:  A label for the y axis
    """
    # For fininancial crisis dates, Cheung et.al Global capital market
    # interdependence and spillover
    events_all = {
        'referendum_2005': '23/11/2005',
        'referendum_2010': '04/08/2010',
        'elections_2007': '24/12/2007',
        'elections_2013': '04/03/2013',
        }
    # Check if the dates are really avaible in the given data set and
    # create a new dictionary of available dates
    events = {event: events_all[event] 
              for event in events_all if pd.to_datetime(events_all[event]) 
              in data.index.tolist()}
    # Financial crisis events
    fin_crisis = {'financialCrisis_2007': '07/02/2007', 'financialCrisis_2009': '29/04/2009'}

    offset              = 300   # 300 For proper placement of the arrow and depending with the scale
    
    fig, ax = plt.subplots()
    fig.patch.set_fc('white')
    
    ax.spines['top'].set_visible(False) # Remove the top box border
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('left') # Remove the ticks from the right side
    ax.xaxis.set_ticks_position('bottom')
    ax.plot(data, color=colors, label=labels)
    ax.set_title(topic)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(loc='upper right')

    for key in events:
        event_str = key.split(sep='_')
        ax.annotate(''+event_str[-1]+'\n'+event_str[0],
                    xy = (events[key], data.loc[events[key]]), xycoords = 'data',
                    xytext =(events[key], offset + data.loc[events[key]]), 
                    textcoords ='data',
                    arrowprops = dict(facecolor='green', shrink=0.05),
                    horizontalalignment = 'center',
                    verticalalignment = 'bottom'
                    )
    
    # Financial Crisis
    ax.axvspan(fin_crisis['financialCrisis_2007'], fin_crisis['financialCrisis_2009'], facecolor='#D3D3D3', alpha=0.3)
    
    
    plt.show()


if __name__ == '__main__':
    """
    TODO: Implement a better test case using timeseries covering the
    dates contained in the events table. Implement a random walk
    model.
    """
    points = np.arange(1, 100, 1)
    draw_graph(points)

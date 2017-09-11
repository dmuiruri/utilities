#! /usr/bin python
"""
This script is used to clean the default matplotlib plot area settings
making the graph cleaner for embedding in other documents.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Canvas:

    fig, ax_ = plt.subplots()
    fig.patch.set_fc('white')
    ax_.spines['top'].set_visible(False)     # Remove the top box border
    ax_.spines['right'].set_visible(False)
    ax_.yaxis.set_ticks_position('left')     # Remove the ticks from the right side
    ax_.xaxis.set_ticks_position('bottom')
    
    def __init__(self):
        pass
    

    def plot_graph(self, data, topic=" ", xlabel= "Year", ylabel ="Price (€)"):
        """
        Method to plot a line Graph
        
        PARAMETERS
        ==========
        data: Pass the data to be plotted
        topic: Pass the title of the graph to plotted
        colors: Color of the line plotted
        labels: To be used in the legend
        """
        if type(data) == pd.Series:
            self.ax_.plot(data, label=data.name)
        elif type(data) == pd.DataFrame:
            for asset in data.columns: 
                self.ax_.plot(data[asset], label=asset)
        else:
            self.ax_.plot(data, label=topic)
        self.ax_.set_title(topic)
        self.ax_.set_xlabel(xlabel)
        self.ax_.set_ylabel(ylabel)
        # self.ax_.axhline(y=0.0, color='black')    # To demonstrate when a curve crosses 0.0
        self.ax_.legend(loc='upper center')
        
        plt.show()

if __name__ == '__main__':
    points = np.random.randn(1000)

    lGraph = Canvas()
    lGraph.plot_graph(points)

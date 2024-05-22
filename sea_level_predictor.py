import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    recent_data = data[(data['Year']>=2000)]
    # Create scatter plot
    x = data['Year']
    y = data['CSIRO Adjusted Sea Level']

    plt.figure(figsize=(10,6))

    plt.scatter(x,y,color='blue', label='Data')

    #Calculate Lineal regression general
    Slope, intercept, _, _, _ = linregress(x, y)
    x_values = np.array([x.min(),2050])
    y_values = Slope * x_values + intercept
    
    # Create first line of best fit
    plt.plot(x_values, y_values, color='red', label='Linear Fit (All Data)')

    plt.scatter(2050, Slope * 2050 + intercept, color='green', label='Point at X=2050')
    plt.text(2050, Slope * 2050 + intercept, '(2050, {:.2f})'.format(Slope * 2050 + intercept), horizontalalignment='left', verticalalignment='bottom')
    #Para los datos recientes
    x_recent = recent_data['Year']
    y_recent = recent_data['CSIRO Adjusted Sea Level']
    Sloperecent, interceptrecent, _, _, _ = linregress(x_recent, y_recent)
    x_values_recent = np.array([2000,2050])
    y_values_recent = Sloperecent * x_values_recent + interceptrecent

    #Create second line of best fit
    plt.plot(x_values_recent, y_values_recent, color='green', label='Linear Fit (2000-Recent)')
    plt.scatter(2050, Sloperecent * 2050 + interceptrecent, color='green', label='Point at X=2050')
    plt.text(2050, Sloperecent * 2050 + interceptrecent, '(2050, {:.2f})'.format(Sloperecent * 2050 + interceptrecent), horizontalalignment='left', verticalalignment='bottom')
    #Adjust limits
    plt.xlim(x.min(),2100)
    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel('Year')
    plt.ylabel('Sea level (inches)')

    plt.legend(['Data','Linear Fit','Linear Fit (Recent)'], loc='lower right')
    plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
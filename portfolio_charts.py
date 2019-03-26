''' 
    
    A collection of functions to perform portfolio analysis. 

    Max Gosselin, 2019
    
'''

import matplotlib as mpl
import matplotlib.pyplot as plt

def returns_chart(data, avg):
    ''' Plot the excess returns of all our portfolio constituents. '''

    fig, ax = plt.subplots(figsize=(12,9))

    ax.plot(data, alpha=0.75)
    ax.set_title('Excess Returns of Portfolio Constituents')
    ax.set_ylabel('Returns')
    ax.set_xlabel('Month')

    plt.show()


def portfolio_pie(data, pcs, title):
    ''' Make a pie chart out of portfolio weights '''

    fig, ax = plt.subplots(figsize=(18,9), subplot_kw=dict(aspect='equal'))



    def labler(pct):
        
        if pct > 1.5:
            return "{:.1f}%".format(pct)
        else:
            return ""
        

    wedges, texts, autotexts = ax.pie(data, autopct=labler,
                                    textprops=dict(color="w"))

    ax.legend(wedges, pcs,
            title="Portfolio Constituents",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title(title)

    plt.show()

def graph_together(monte_carlo_portfolios, efficient_data, maxsharpe_metrics, minvar_metrics, cal_x, cal_y):
        ''' Put it all together in one plot. '''
        
        eff_color = 'darkblue'

        fig, ax = plt.subplots(figsize=(12,9))

        ax.scatter(minvar_metrics['stdv'], minvar_metrics['return'], marker='o', color=eff_color, s=150)
        ax.scatter(maxsharpe_metrics['stdv'], maxsharpe_metrics['return'], marker='*', color=eff_color, s=300)
        ax.scatter(monte_carlo_portfolios['stdv'], monte_carlo_portfolios['return'],
                c=monte_carlo_portfolios['sharpe'], cmap='viridis')

        ax.plot(cal_x, cal_y, alpha=0.75, color='gold')
        ax.plot(efficient_data['stdv'], efficient_data['return'], color=eff_color)

        ax.axhline(0, color='gainsboro', linestyle ='dotted')
        ax.axvline(0, color='gainsboro', linestyle = 'dotted')
        ax.set_ylim([-0.005, 0.025])

        ax.set_title('Portfolio Efficient Frontier')
        ax.set_xlabel('Portfolio Standard Deviation')
        ax.set_ylabel('Portfolio Excess Return')

        ax.legend(['CAL', 'Efficient Frontier',])
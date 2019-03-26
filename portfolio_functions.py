''' 
    
    A collection of functions to perform portfolio analysis. 

    Max Gosselin, 2019
    
'''
import numpy as np
import pandas as pd
from scipy import optimize


def portfolio_metrics(weights, avg_xs_returns, covariance_matrix):
    ''' Compute basic portfolio metrics: return, stdv, sharpe ratio '''

    portfolio_return = np.sum(weights * avg_xs_returns)
    portfolio_stdv = np.sqrt(np.dot(weights.T, np.dot(weights, covariance_matrix)))
    
    portfolio_sharpe = portfolio_return / portfolio_stdv

    tickers = covariance_matrix.columns

    metrics = {
        'return': portfolio_return,
        'stdv': portfolio_stdv,
        'sharpe': portfolio_sharpe,
        'weights': weights
        }
    metrics.update(dict([(ticker, weight) for ticker, weight in zip(tickers, weights)]).items())

    return metrics

def simulate_portfolios(iters, xs_stats, covariance_matrix):
    ''' What we want here is to randomly generate portfolios that will sit 
        inside the efficiency frontier for illustrative purposes '''

    # Set up an empty array to store our generated portfolios
    simulations = []
    
    while iters > 1:
        
        weights = np.random.random(len(xs_stats.columns))
        weights /= np.sum(weights)
        
        simulations.append(portfolio_metrics(weights, xs_stats.loc['Avg'], covariance_matrix))
        
        iters -= 1

    return simulations

def solve_minvar(xs_avg, covariance_matrix):
    ''' Solve for the weights of the minimum variance portfolio 

        Constraints:
            sum of weights = 1,
            weights bound by [0, 0.2],

        Returns the weights and the jacobian used to generate the solution.
        
        '''

    def __minvar(weights, xs_avg, covariance_matrix):
        ''' Anonymous function to compute stdv '''
        return np.sqrt(np.dot(weights.T, np.dot(weights, covariance_matrix)))

    p_size = len(xs_avg)
    args = (xs_avg, covariance_matrix)   
    constraints = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1}]
    bounds = [(0, 0.2)] * p_size


    minimized_weights = optimize.minimize(__minvar, np.zeros(p_size), args=args,
                        method='SLSQP', bounds=bounds, constraints=constraints, options={'maxiter':1000})

    return minimized_weights

def solve_maxsharpe(xs_avg, covariance_matrix):
    ''' Solve for the weights of the maximum Sharpe ratio portfolio 

        Constraints:
            sum of weights = 1,
            weights bound by [0, 0.2],

        Returns the weights and the jacobian used to generate the solution.
        
        '''
    def __max_by_min_sharpe(weights, xs_avg, covariance_matrix):
        ''' Anonymous function to compute sharpe ratio, note that since scipy only minimizes we go negative. '''
        pm = portfolio_metrics(weights, xs_avg, covariance_matrix)    
        return -pm['return'] / pm['stdv']

    p_size = len(xs_avg)
    args = (xs_avg, covariance_matrix)   
    constraints = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1}]
    bounds = [(0, 0.2)] * p_size

    
    minimized_weights = optimize.minimize(__max_by_min_sharpe, ((1/p_size) * np.ones(p_size)), args=args,
                        method='SLSQP', bounds=bounds, constraints=constraints, options={'maxiter':1000})

    return minimized_weights

def solve_for_target_return(xs_avg, covariance_matrix, target):
    ''' Solve for the weights of the minimum variance portfolio which has
        a specific targeted return.

        Constraints:
            sum of weights = 1,
            weights bound by [0, 0.2],
            portfolio return = target return,

        Returns the weights and the jacobian used to generate the solution.
        
        '''

    def __minvar(weights, xs_avg, covariance_matrix):
        ''' Anonymous function to compute stdv '''
        return np.sqrt(np.dot(weights.T, np.dot(weights, covariance_matrix)))
    
    def __match_target(weights):
        ''' Anonymous function to check equality with the target return '''
        return np.sum(weights * xs_avg)

    p_size = len(xs_avg)
    args = (xs_avg, covariance_matrix)
    constraints = [
        {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
        {'type': 'eq', 'fun': lambda x: __match_target(x) - target},
    ]
    bounds = [(0, 0.2)] * p_size

    minimized_weights = optimize.minimize(__minvar, ((1/p_size) * np.ones(p_size)), args=args,
                        method='SLSQP', bounds=bounds, constraints=constraints, options={'maxiter':1000})

    return minimized_weights

def generate_efficient_frontier(targets, xs_avg, covariance_matrix):

    portfolios = []

    for target in targets:

        p_weights = solve_for_target_return(xs_avg, covariance_matrix, target)
        portfolios.append(portfolio_metrics(p_weights['x'], xs_avg, covariance_matrix))

    return portfolios

if __name__ == '__main__':
    for i in range(69):
        print('penis <3')
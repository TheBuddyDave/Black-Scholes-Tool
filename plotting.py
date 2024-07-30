
#lets import the basic libraries 
import numpy as np
import formulas as f 
import plotly.graph_objects as pt 


#-----------PLOTTING SCHEMES---------------

#This will extract the lin space 
def greek_x(S, X, T, R, sigma, range, type):
    #declare range of the x axis for better udnerstanding gamma sensitivies  
    match type:
        case 1:
            r1 = S*(1 - range)
            r2 = S*(1 + range)
        case 2:
            r1 = X*(1 - range)
            r2 = X*(1 + range)
        case 3:
            r1 = T*(1 - range)
            r2 = T*(1 + range)
        case 4:
            r1 = R*(1 - range)
            r2 = R*(1 + range)
        case 5: 
            r1 = sigma*(1 - range)
            r2 = sigma*(1 + range)
        
    return np.linspace(r1, r2, 500) 
#each greek with its respective changing var 
def delta_call_plot(S, X, T, R, sigma, range):
    x_axis = greek_x(S, X, T, R, sigma, range, 1)
    y_axis = [f.delta_call(price, X, T, R, sigma) for price in x_axis]
    fig = pt.Figure() 
    fig.add_trace(pt.Scatter(x=x_axis, y=y_axis, mode='lines', name='Line Plot'))
    fig.update_layout(title='Call Delta', xaxis_title='Stock Price', yaxis_title='Delta', width=800, height=400)
    return fig 

def delta_put_plot(S, X, T, R, sigma, range):
    x_axis = greek_x(S, X, T, R, sigma, range, 1)
    y_axis = [f.delta_put(price, X, T, R, sigma) for price in x_axis]
    fig = pt.Figure() 
    fig.add_trace(pt.Scatter(x=x_axis, y=y_axis, mode='lines', name='Line Plot'))
    fig.update_layout(title='Put Delta', xaxis_title='Stock Price', yaxis_title='Delta', width=800, height=400)
    return fig 

def gamma_plot(S, X, T, R, sigma, range):
    x_axis = greek_x(S, X, T, R, sigma, range, 1)
    y_axis = [f.gamma(price, X, T, R, sigma) for price in x_axis]
    fig = pt.Figure() 
    fig.add_trace(pt.Scatter(x=x_axis, y=y_axis, mode='lines', name='Line Plot'))
    fig.update_layout(title='Gamma', xaxis_title='Stock Price', yaxis_title='Gamma', width=800, height=400)
    return fig 

def vega_plot(S, X, T, R, sigma, range):
    x_axis = greek_x(S, X, T, R, sigma, range, 5)
    y_axis = [f.vega(S, X, T, R, vol) for vol in x_axis]
    fig = pt.Figure() 
    fig.add_trace(pt.Scatter(x=x_axis, y=y_axis, mode='lines', name='Line Plot'))
    fig.update_layout(title='Vega Plot', xaxis_title='Volatility', yaxis_title='Vega', width=800, height=400)
    return fig 

def theta_call_plot(S, X, T, R, sigma, range):
    x_axis = greek_x(S, X, T, R, sigma, range, 3)
    y_axis = [f.theta_call(S, X, time, R, sigma) for time in x_axis]
    fig = pt.Figure() 
    fig.add_trace(pt.Scatter(x=x_axis, y=y_axis, mode='lines', name='Line Plot'))
    fig.update_layout(title='Call Theta', xaxis_title='Time to Maturity', yaxis_title='Theta', width=800, height=400)
    return fig 

def theta_put_plot(S, X, T, R, sigma, range):
    x_axis = greek_x(S, X, T, R, sigma, range, 3)
    y_axis = [f.theta_put(S, X, time, R, sigma) for time in x_axis]
    fig = pt.Figure() 
    fig.add_trace(pt.Scatter(x=x_axis, y=y_axis, mode='lines', name='Line Plot'))
    fig.update_layout(title='Put Theta', xaxis_title='Time to Maturity', yaxis_title='Theta', width=800, height=400)
    return fig 

def rho_call_plot(S, X, T, R, sigma, range):
    x_axis = greek_x(S, X, T, R, sigma, range, 4)
    y_axis = [f.rho_call(S, X, T, r, sigma) for r in x_axis]
    fig = pt.Figure() 
    fig.add_trace(pt.Scatter(x=x_axis, y=y_axis, mode='lines', name='Line Plot'))
    fig.update_layout(title='Rho Call', xaxis_title='Interest Rate', yaxis_title='Rho', width=800, height=400)
    return fig 

def rho_put_plot(S, X, T, R, sigma, range):
    x_axis = greek_x(S, X, T, R, sigma, range, 4)
    y_axis = [f.rho_put(S, X, T, r, sigma) for r in x_axis]
    fig = pt.Figure() 
    fig.add_trace(pt.Scatter(x=x_axis, y=y_axis, mode='lines', name='Line Plot'))
    fig.update_layout(title='Rho Put', xaxis_title='Interest Rate', yaxis_title='Rho', width=800, height=400)
    return fig 

def vanna_plot(S, X, T, R, sigma, range):
    x_axis = greek_x(S, X, T, R, sigma, range, 5)
    y_axis = [f.vanna(S, X, T, R, vol) for vol in x_axis]
    fig = pt.Figure() 
    fig.add_trace(pt.Scatter(x=x_axis, y=y_axis, mode='lines', name='Line Plot'))
    fig.update_layout(title='Vanna', xaxis_title='Volatility', yaxis_title='Vanna', width=800, height=400)
    return fig 

def volga_plot(S, X, T, R, sigma, range):
    x_axis = greek_x(S, X, T, R, sigma, range, 5)
    y_axis = [f.volga(S, X, T, R, vol) for vol in x_axis]
    fig = pt.Figure() 
    fig.add_trace(pt.Scatter(x=x_axis, y=y_axis, mode='lines', name='Line Plot'))
    fig.update_layout(title='Volga', xaxis_title='Volatility', yaxis_title='Volga', width=800, height=400)
    return fig 

def charm_plot(S, X, T, R, sigma, range):
    x_axis = greek_x(S, X, T, R, sigma, range, 3)
    y_axis = [f.charm(S, X, time, R, sigma) for time in x_axis]
    fig = pt.Figure() 
    fig.add_trace(pt.Scatter(x=x_axis, y=y_axis, mode='lines', name='Line Plot'))
    fig.update_layout(title='Charm', xaxis_title='Time to Maturity', yaxis_title='Charm', width=800, height=400)
    return fig 



#Call and Put price heat map 
def call_heatmap(S, X, T, R, sigma): 
    x_axis = np.linspace(S*(0.9), S*(1.1), 10) 
    y_axis = np.linspace(X*(0.9), X*(1.1), 10) 
    matrix_zeros = np.zeros((10, 10))
    for i in range(10): 
        for j in range(10): 
            matrix_zeros[i, j] = f.black_scholes_call(x_axis[j], y_axis[i], T, R, sigma) 
    return matrix_zeros, x_axis, y_axis


def put_heatmap(S, X, T, R, sigma): 
    x_axis = np.linspace(S*(0.9), S*(1.1), 10)
    y_axis = np.linspace(X*(0.9), X*(1.1), 10) 
    matrix_zeros = np.zeros((10, 10))
    for i in range(10): 
        for j in range(10): 
            matrix_zeros[i, j] = f.black_scholes_put(x_axis[j], y_axis[i], T, R, sigma) 
    return matrix_zeros, x_axis, y_axis

























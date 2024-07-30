

#Libraries to make the math easier 
import numpy as np
from scipy.stats import norm
from scipy.optimize import least_squares
import yfinance as yf 
from datetime import datetime


#---------BLACK SCHOLES ---------------------
#Basic black scholes equation(s) 
#S-current stock price 
#X-strike price 
#T-tiem to maturity
#r risk-free interest rate 
#sigma - volatility 


#Standard black shcoles formula 
def black_scholes_call(S, X, T, R, sigma):
    d1 = (np.log(S/X) + (R + sigma**2 * 0.5) * T) / (sigma* np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    cp = S  * norm.cdf(d1) - X * np.exp(-R * T) * norm.cdf(d2)
    return cp


def black_scholes_put(S, X, T, R, sigma): 
    d1 = (np.log(S/X) + (R + sigma**2 * 0.5) * T) / (sigma* np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    pp = X * np.exp(-R * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return pp






#---------GREEKS---------------------

#1st order: 
def delta_call(S, X, T, R, sigma):
    d1 = (np.log(S/X) + (R + sigma**2 * 0.5) * T) / (sigma* np.sqrt(T))   
    return norm.cdf(d1)


def delta_put(S, X, T, R, sigma):
    d1 = (np.log(S/X) + (R + sigma**2 * 0.5) * T) / (sigma* np.sqrt(T))   
    return (norm.cdf(d1) - 1)

def theta_call(S, X, T, R, sigma):
    d1 = (np.log(S/X) + (R + sigma**2 * 0.5) * T) / (sigma* np.sqrt(T))  
    d2 = d1 - sigma * np.sqrt(T)
    theta = ((-S*sigma*norm.pdf(d1))/(2*np.sqrt(T))) - (R*X*np.exp(-R*T)*norm.cdf(d2)) 
    return theta

def theta_put(S, X, T, R, sigma): 
    d1 = (np.log(S/X) + (R + sigma**2 * 0.5) * T) / (sigma* np.sqrt(T))  
    d2 = d1 - sigma * np.sqrt(T)
    theta = ((-S*sigma*norm.pdf(d1))/(2*np.sqrt(T))) + (R*X*np.exp(-R*T)*norm.cdf(-d2))
    return theta


def vega(S, X, T, R, sigma): 
    d1 = (np.log(S/X) + (R + sigma**2 * 0.5) * T) / (sigma* np.sqrt(T))
    vega = S*np.sqrt(T)*norm.pdf(d1)
    return vega 

def rho_call(S, X, T, R, sigma): 
    d1 = (np.log(S/X) + (R + sigma**2 * 0.5) * T) / (sigma* np.sqrt(T))  
    d2 = d1 - sigma * np.sqrt(T)
    rho = T*X*np.exp(-R*T)*norm.cdf(d2)
    return rho 

def rho_put(S, X, T, R, sigma): 
    d1 = (np.log(S/X) + (R + sigma**2 * 0.5) * T) / (sigma* np.sqrt(T))  
    d2 = d1 - sigma * np.sqrt(T)
    rho = -T*X*np.exp(-R*T)*norm.cdf(-d2)
    return rho 


#2nd order: 
def gamma(S, X, T, R, sigma): 
    d1 = (np.log(S/X) + (R + sigma**2 * 0.5) * T) / (sigma* np.sqrt(T)) 
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    return gamma 

def vanna(S, X, T, R, sigma): 
    d1 = (np.log(S / X) + (R + sigma**2 * 0.5) * T) / (sigma * np.sqrt(T))
    vanna = S * np.sqrt(T) * norm.pdf(d1) * (1 - d1 / sigma)
    return vanna 

def volga(S, X, T, R, sigma): 
    d1 = (np.log(S/X) + (R + sigma**2 * 0.5) * T) / (sigma* np.sqrt(T)) 
    d2 = d1 - sigma * np.sqrt(T)
    volga = S*np.sqrt(T)*norm.pdf(d1)*((d1*d2 - 1)/(sigma))
    return volga 

def charm(S, X, T, R, sigma): 
    d1 = (np.log(S/X) + (R + sigma**2 * 0.5) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    charm = norm.pdf(d1) * ((2 * R * T - d2 * sigma * np.sqrt(T)) / (2 * T * sigma * np.sqrt(T)))
    return charm





#-------------VOLATILITY CACLULATIONS 
def calculate_historical_volatility(ticker):
    ticker = yf.Ticker(ticker)
    historical_data = ticker.history(period='1y')   #use last year of data 
    historical_data['Returns'] = historical_data['Close'].pct_change() #collect percent changes 
    volatility = historical_data['Returns'].std() * np.sqrt(252) #annualize it 
    return volatility


def get_options_data(ticker, risk_free_rate, type, min_days_to_expiration=60):
    
    #asset information 
    asset = yf.Ticker(ticker)
    current_price = asset.history(period='1d')['Close'].iloc[-1] 


    #filder expiration 
    expiration_dates = asset.options
    if not expiration_dates:
        raise ValueError("No expiration dates available for this ticker.")
    else: 
        valid_expiration_dates = [] 
        for date in expiration_dates: 
            expiration_date = datetime.strptime(date, '%Y-%m-%d')
            days_until_expiration = (expiration_date - datetime.now()).days
            if days_until_expiration >= min_days_to_expiration:
                valid_expiration_dates.append(date)  



    if not valid_expiration_dates:
        raise ValueError(f"No valid expiration dates found that are at least {min_days_to_expiration} days away.")
    expiration_date = valid_expiration_dates[0]

    #grab the first date 
    options_chain = asset.option_chain(expiration_date)
    calls = options_chain.calls  
    if calls.empty:
        raise ValueError("No call options available for the given expiration date.")
    

   #grab strike price based off the type of option you want 
    strike_prices = calls['strike'].to_numpy()
    if type == 'ATM': #ATM 
        strike_price = strike_prices[(np.abs(strike_prices - current_price)).argmin()]
    elif type == 'ITM': #ITM
        itm_strike_prices = strike_prices[strike_prices < current_price]
        if(len(itm_strike_prices) > 0): 
            strike_price = itm_strike_prices[-1]
        else: 
            raise ValueError(f"No ITM Strike Price Found") 
    else:         #OTM 
        otm_strike_prices = strike_prices[strike_prices > current_price]
        if(len(otm_strike_prices) > 0): 
            strike_price = otm_strike_prices[0] #im pickign 0 index here to make it work, it throws errors otheriwse (This poriton is a bit cheesed)
        else: 
            raise ValueError(f"No OTM Strike Price Found") 


    #time to maturity
    expiration = datetime.strptime(expiration_date, '%Y-%m-%d')
    time_to_maturity = (expiration - datetime.now()).days / 365.0
    if time_to_maturity <= 0:
        raise ValueError(f"Time to maturity is non-positive for the expiration date {expiration_date}.")
    
    # Get the option price
    call_option = calls[calls['strike'] == strike_price]
    if not call_option.empty:
        option_price = call_option.iloc[0]['lastPrice']
    else:
        raise ValueError(f"No call option found for strike price {strike_price} on {expiration_date}")
    return current_price, strike_price, time_to_maturity, risk_free_rate, option_price


def implied_volatility(S, X, R, T, OP): 
    def diff(sigma):
        return OP - black_scholes_call(S, X, T, R, sigma)
    
    result = least_squares(diff, 0.1, bounds=(0, 2)) 
    return result.x[0] if result.success else None























    



 






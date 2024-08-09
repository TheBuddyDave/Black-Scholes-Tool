
# Black Scholes Calculator, Explainer, Visualizer 



## CLICK HERE TO VIEW ONLINE: 
https://black-scholes-tool.streamlit.app/

NOTE: Sometimes the site is down as streamlit will put projects to sleep that aren't frequently viewed... 

This is a Black-Scholes Educational Tool. It contains a mathematical overview of the model, a standard calculator for the model, and can perform many other relevant calculations with visualizations such as the Greeks. It also calculates Historical and Implied Volatilities for a selected asset.



## Features

1. Standard Black-Scholes Option Calculation

- Calculates the price of call and put options using the Black-Scholes model.

2. Price Heat Map

- Visualizes the option prices for both call and put options across a range of strike prices and asset prices

3. Calculation and   Plots of Greeks
- Calculates the first and second order greeks. It plots them against changes in a variable that is particularly relevant to a given Greek. '

4. Mathematical Dive into the 
Black-Scholes Model
- Provides an in-depth mathematical explanation/road map of the Black-Scholes model, including probability theory, derivations and assumptions.

5. Implied vs Historical Volatility Analysis
- Select an asset, interest rate, and moneyness, and willl compute/compare its implied volatility with its historical volatility.





## Getting Started

### Prerequisites
Ensure that you look at the requirements.txt and create a virtual environmet with the specifications listed in the file. This can be done easily in command prompt after you cd into the file, create your own virtual environment and activate it by simply typing: 


```bash
pip install -r requirements.txt
```

### Running the App 

To run the application, navigate to the directory containing app.py and execute the following command:

```bash
streamlit run app.py
```


## Acknowledgements

 - streamlit, numpy, scipy, datetime, and yfinance 
 - Stochastic Calculus for Finance II: Continuous-Time Models by Steven Shreve 
 - An Introduction to Stochastic Differential Equations by Lawrence C Evans 
 



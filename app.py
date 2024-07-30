
#Libraries 
import streamlit as st
from formulas import black_scholes_call as bc
from formulas import black_scholes_put as bp
import plotting as getPlot 
import plotly.graph_objects as go
import formulas as f 


# -------------HEADER --------------- 
st.title('Black-Scholes Calculator, Visualizer, and Explainer')
st.subheader('By Github User: TheBuddyDave')
st.write('This program aims to provide users with an easy to understand Black Scholes Calculator with additional functionalities and explainations to enrich learning xperience')


# ----------------------------   THE MATHS ------------------------------------------

'''''
st.header('The Math')
with st.expander("CLICK TO SHOW AND HIDE THE MATH (its kinda long)"):

    image_files = ['BS1.jpg', 'BS2.jpg', 'BS3.jpg', 'BS4.jpg',
               'BS5.jpg', 'BS6.jpg', 'BS7.jpg', 'BS8.jpg',
               'BS9.jpg', 'BS10.jpg', 'BS11.jpg', 'BS12.jpg',
               'BS13.jpg'] 


#show the math images(couldnt get the pdf to work and wasnt worth the effort)
    for img in image_files:
            st.image(img)

''''' 

# -------------CALCULATOR --------------- 



#make a horizontal layout for inputs
st.header('Inputs')
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("**Stock Price**")
    stock_price_text = st.number_input("Stock Price", value=180.0, min_value=0.0, step=0.1, key='stock_price')
    stock_price = st.slider(" ", min_value=0.0, max_value=stock_price_text*2, value=stock_price_text, step=0.1, key='stock_price_slider')

with col2:
    st.markdown("**Strike Price**")
    strike_price_text = st.number_input("Strike Price", value=175.0, min_value=0.0, step=0.1, key='strike_price')
    strike_price = st.slider("  ", min_value=0.0, max_value=strike_price_text*2, value=strike_price_text, step=0.1, key='strike_price_slider')

with col3:
    st.markdown("**Maturity Time (yr)**")
    time_text = st.number_input("Maturity Time (yr)", value=1.5, min_value=0.1, step=0.1, key='maturity_time')
    time = st.slider("   ", min_value=0.1, max_value=time_text*2, value=time_text, step=0.1, key='maturity_time_slider')

with col4:
    st.markdown("**Interest Rate (%)**")
    interest_rate_text = st.number_input("Interest Rate (%)", value=0.15, min_value=0.01, step=0.01, key='interest_rate')
    interest_rate = st.slider("    ", min_value=0.01, max_value=1.0, value=interest_rate_text, step=0.01, key='interest_rate_slider')

with col5:
    st.markdown("**Volatility (%)**")
    volatility_text = st.number_input("Volatility (%)", value=0.05, min_value=0.001, step=0.01, key='volatility')
    volatility = st.slider("     ", min_value=0.001, max_value=1.0, value=volatility_text, step=0.01, key='volatility_slider')






#lets display the results 
st.header('Results')
call = bc(stock_price, strike_price, time, interest_rate, volatility)
put = bp(stock_price, strike_price, time, interest_rate, volatility)


col1, col2 = st.columns(2)
with col1:    
    st.markdown(
        f"""
        <div style="border: 2px solid #007bff; padding: 15px; border-radius: 10px; background-color: #f0f8ff; font-size: 20px; text-align: center; margin-bottom: 15px;">
            Call Price: <span style="font-weight: normal;">${call:.2f}</span>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style="border: 2px solid #28a745; padding: 15px; border-radius: 10px; background-color: #f0fff0; font-size: 20px; text-align: center;">
            Put Price: <span style="font-weight: normal;">${put:.2f}</span>
        </div>
        """, 
        unsafe_allow_html=True
    )



#Lets generate a heatmap to make it easier for users to visualize: 



#Call
call_map, x_call, y_call = getPlot.call_heatmap(stock_price, strike_price, time, interest_rate, volatility)
fig_put = go.Figure(data=go.Heatmap(
    z=call_map,
    x=x_call,
    y=y_call,
    colorscale='Inferno',  
    colorbar=dict(title='Value'),
    text=call_map,
    texttemplate='%{text:.2f}',
    textfont=dict(size=10),
    ))

fig_put.update_layout(
        title='Call Price Heat Map',
        xaxis_title='Asset Price',
        yaxis_title='Strike Price',
    )
st.plotly_chart(fig_put)


#Put 
put_map, x_put, y_put = getPlot.put_heatmap(stock_price, strike_price, time, interest_rate, volatility)
fig_put = go.Figure(data=go.Heatmap(
    z=put_map,
    x=x_put,
    y=y_put,
    colorscale='Inferno',  
    colorbar=dict(title='Value'),
    text=put_map,
    texttemplate='%{text:.2f}',
    textfont=dict(size=10),
    ))


fig_put.update_layout(
        title='Put Price Heat Map',
        xaxis_title='Asset Price',
        yaxis_title='Strike Price',
    )


#show it 
st.plotly_chart(fig_put)






#-----------------GREEKS-----------------------------------


# Plots section
st.header('The Greeks')
st.subheader("**Value Range for Sensitivity Analysis**")
range = st.slider("     ", min_value=0.001, max_value=1.0, value=0.5, step=0.01, key='greeks_range')
 
st.subheader('First Order Greeks')
with st.expander("Show/Hide First Order Plots"):
    zcol1, zcol2 = st.columns(2)
    # Call
    with zcol1:
        st.plotly_chart(getPlot.delta_call_plot(stock_price, strike_price, time, interest_rate, volatility, range))
        st.plotly_chart(getPlot.theta_call_plot(stock_price, strike_price, time, interest_rate, volatility, range))
        st.plotly_chart(getPlot.vega_plot(stock_price, strike_price, time, interest_rate, volatility, range))
        st.plotly_chart(getPlot.rho_call_plot(stock_price, strike_price, time, interest_rate, volatility, range))
    # Put
    with zcol2:
        st.plotly_chart(getPlot.delta_put_plot(stock_price, strike_price, time, interest_rate, volatility, range))
        st.plotly_chart(getPlot.theta_put_plot(stock_price, strike_price, time, interest_rate, volatility, range))
        st.plotly_chart(getPlot.vega_plot(stock_price, strike_price, time, interest_rate, volatility, range))
        st.plotly_chart(getPlot.rho_put_plot(stock_price, strike_price, time, interest_rate, volatility, range))

st.subheader('Second Order Greeks') 
with st.expander("Show/Hide Second Order Plots"):
    #second order are the same for both type of greeks 
    zcol1, zcol2 = st.columns(2)
    with zcol1:
        st.plotly_chart(getPlot.gamma_plot(stock_price, strike_price, time, interest_rate, volatility, range))
        st.plotly_chart(getPlot.vanna_plot(stock_price, strike_price, time, interest_rate, volatility, range))
    with zcol2:
        st.plotly_chart(getPlot.volga_plot(stock_price, strike_price, time, interest_rate, volatility, range))
        st.plotly_chart(getPlot.charm_plot(stock_price, strike_price, time, interest_rate, volatility, range))


#-----------------VOLATILITY-----------------------------------



st.header('Implied Volatility vs Historical Volatility (Call)')

#basic field selection 
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
selected_ticker = st.selectbox('Select a ticker:', tickers)
interest_rate_text2 = st.number_input("Interest Rate (%)", value=0.15, min_value=0.01, step=0.01, key='interest_rate_2')
moneyness = ['ATM', 'ITM', 'OTM']
selected_moneyness = st.selectbox('Select moneyness of strike price:', moneyness)

#execute 
current_price, strike_price, time_to_maturity, risk_free_rate, option_price = f.get_options_data(selected_ticker, interest_rate_text2, selected_moneyness)
iv = f.implied_volatility(current_price, strike_price, time_to_maturity, risk_free_rate, option_price)
hv = f.calculate_historical_volatility(selected_ticker)


#Display 
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        f"""
        <div style="border: 2px solid #007bff; padding: 15px; border-radius: 10px; background-color: #f0f8ff; font-size: 20px; text-align: center; margin-bottom: 15px;">
            Implied Volatility: <span style="font-weight: normal;">${iv:.2f}</span>
        </div>
        """, 
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        f"""
        <div style="border: 2px solid #28a745; padding: 15px; border-radius: 10px; background-color: #f0fff0; font-size: 20px; text-align: center;">
            Historical Volatiltiy: <span style="font-weight: normal;">${hv:.2f}</span>
        </div>
        """, 
        unsafe_allow_html=True
    )




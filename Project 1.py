import pandas as pd
ub = pd.read_csv('Uber.csv')
md= pd.read_csv('Moderna.csv')

#Lets me check the header of the columns
print (ub.head())
print (md.head())

#Takes out the $ from the data
ub=ub.replace({'\$':''}, regex = True)
md=md.replace({'\$':''}, regex = True)


#Switch data types
ub.columns = ['Date','Close','Volume', 'Open', 'High', 'Low']
ub = ub.astype(({"Close": float, "Volume": int, "Open": float, "High": float, "Low": float}))

md.columns = ['Date','Close','Volume', 'Open', 'High', 'Low']
md = md.astype(({"Close": float, "Volume": int, "Open": float, "High": float, "Low": float}))

#Lets me know the types in each column
print(ub.dtypes)
print(md.dtypes)

#Stats on CSV
print(ub.describe())
print(md.describe())

#Finding out the Closing Price of tomorrow 
ub['Price1']= ub['Close'].shift(-1)
md['Price1']= md['Close'].shift(-1)

#Finding the price difference 
ub['PriceDiff']= ub['Price1']- ub['Close']
md['PriceDiff']= md['Price1']- md['Close']

#Daily Return
ub['Return']= ub['PriceDiff']/ub['Close']
md['Return']= md['PriceDiff']/md['Close']

#Give direction to the data
ub['Direction'] = [1 if ub.loc[ei,'PriceDiff'] > 0 else -1
                   for ei in ub.index]
md['Direction'] = [1 if md.loc[ei,'PriceDiff'] > 0 else -1
                   for ei in md.index]
                       
#Moving Average 
#Short Term 5 Moving Avg Fast Signal
ub['Average5'] = ub['Close'].rolling(window=5).mean()
md['Average5'] = md['Close'].rolling(window=5).mean()

#Short Term 20 Moving Average Fast Signal
ub['Average20'] = ub['Close'].rolling(window=20).mean()
md['Average20'] = md['Close'].rolling(window=20).mean()

#Long Term 40 Moving Avg Slow Signal
ub['Average40'] = ub['Close'].rolling(window=40).mean()
md['Average40'] = md['Close'].rolling(window=40).mean()

#Long Term 60 Moving Avg Slow Signal
ub['Average60'] = ub['Close'].rolling(window=60).mean()
md['Average60'] = md['Close'].rolling(window=60).mean()

#Plot moving average 
ub['Close'].plot(legend=True)
ub['Average5'].plot(legend=True)
ub['Average20'].plot(legend=True)
ub['Average40'].plot(legend=True)
ub['Average60'].plot(legend=True)

md['Close'].plot(legend=True)
md['Average5'].plot(legend=True)
md['Average20'].plot(legend=True)
md['Average40'].plot(legend=True)
md['Average60'].plot(legend=True)

print(ub.plot())


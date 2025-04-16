# !pip install prophet
from google.colab import files
uploaded = files.upload()
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data_sample.csv", encoding="ISO-8859-1")
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
daily_sales = df.groupby('ORDERDATE')['SALES'].sum().reset_index()
prophet_df = daily_sales.rename(columns={'ORDERDATE': 'ds', 'SALES': 'y'})
model = Prophet()
model.fit(prophet_df)
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)
fig1 = model.plot(forecast)
plt.title("Sales Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv("sales_forecast.csv", index=False)
fig2 = model.plot_components(forecast)
plt.show()

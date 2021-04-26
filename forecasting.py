from pmdarima.arima import ADFTest
import pmdarima as pmd
from datetime import datetime
import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import register_matplotlib_converters
from sklearn.metrics import mean_squared_error
from math import sqrt
register_matplotlib_converters()
df = pd.read_csv('us-counties-clean-processed.csv')
dct = {}
for index,rows in df.iterrows():
    key = (rows.county,rows.state)
    if key in dct:
        dct[key].append([rows.cases, rows.date])
    else:
        dct[key] = [[rows.cases, rows.date]]
mydict = {}
for key, value in dct.items():
    listag = [lista[0] for lista in value]
    lenlista = len(listag)
    dwl = []
    dfl = []
    for i in range(lenlista):
        dwl.append(key[0])
    for i in range(lenlista):
        dfl.append(key[1])
    bl = [bo[1] for bo in value]
    train = listag[:int(0.8*(len(listag)))]
    valid = listag[int(0.8*(len(listag))):]
    arima_model = pmd.auto_arima(train,
                                  start_p=0,d = 1,start_q=0,
                                  test="adf", supress_warnings = True,
                                  trace=True)
    arima_model.summary()
    newt = arima_model.predict(n_periods = len(valid))
    arml = []
    for n in newt:
        arml.append(n)
    zerolist = []
    lenvalid = len(valid)
    lenzero = lenlista - lenvalid
    for i in range(lenzero):
        zerolist.append(0)
    mydict = [dwl, dfl, listag, bl, zerolist + arml]
    mydf = pd.DataFrame(mydict)
    this_df = mydf.T
    this_df.to_csv("us-counties-forecast.csv", mode='a', index=False, header=["County", "State", "Cases", "Date", "Forecast"])

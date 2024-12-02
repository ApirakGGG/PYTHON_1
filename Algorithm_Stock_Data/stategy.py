import ta
import ta.trend
import pandas as pd
import ta.momentum

def calculate_indicator(data):
    #แปลงเป็น 1D Array
    close = data['Close'].values.ravel()

    # คำนวณEMA 10/20/50
    data['EMA_10'] = ta.trend.ema_indicator(pd.Series(close), window=10)
    data['EMA_20'] = ta.trend.ema_indicator(pd.Series(close), window=20) 
    data['EMA_50'] = ta.trend.ema_indicator(pd.Series(close), window=50)

    #MACD Calculates
    macd = ta.trend.MACD(pd.Series(close))
    data['MACD'] = macd.macd()
    data['MACD_SIGNAL'] = macd.macd_signal()

     # RSI Calculates
    data['RSI'] = ta.momentum.rsi(pd.Series(close), window=14)
      # retuen ข้อมุูลData
    return data

def calculate_entry_price(data):
    # #create BUY/SELL Signal โดยอิงจาก EMA & MACD
    data['BUY_SIGNAL'] = (data['EMA_10'] > data['EMA_20']) & (data['EMA_10'] > data['EMA_50']) & (data['EMA_10'].shift(1) <= data['EMA_20'].shift(1))
    # data['SELL_SIGNAL'] = ((data['EMA_10'] < data['EMA_20']) & (data['MACD'] < data['MACD_SIGNAL']) & (data['RSI'] > 70))
    entry_price = None
    for i in range(len(data)):
        if data['BUY_SIGNAL'].iloc[i]:
            entry_price = data['Close'].iloc[i] #ตั้ง Entry Price เมื่อเกิดสัญญาณซื้อ
            break # หยุดเมื่อเจอจุดซื้อ
        return entry_price

  
import tkinter as tk
from tkinter import messagebox
import yfinance as yf
from stategy import calculate_indicator
from stategy import calculate_entry_price
import matplotlib.pyplot as plt
from ai_model import train_model
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TraindingApp:
    def __init__(self):
        #create Window from tkinter
        self.root = tk.Tk()
        self.root.title("Algorithm Training")
        self.root.geometry("1000x800")

        #create Input for insert Ticker Stock
        tk.Label(self.root, text="Ticker Stock:").pack()
        self.ticker_entry = tk.Entry(self.root)
        self.ticker_entry.pack()

        #Create Button Calculate result
        self.calculate_button = tk.Button(self.root, text="Analyst", command = self.calculate_signal)
        self.calculate_button.pack()

        self.figure , self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack()

    def calculate_signal(self):
        ticker = self.ticker_entry.get()
            # messagebox.showinfo(f"Ticker:{self.ticker_entry} ")
        print(f"Ticker:{ticker}")
        if not ticker :
            messagebox.showerror(f"Error", "Please Enter a Ticker:")
            return
        
        #ดีงข้อมูลจาก YahooFinance
        data = yf.download(ticker, period="6mo")
        if data.empty:
            messagebox.showerror(f"Error", "Please Enter Ticket:{ticker}")
        print(data.head())


        get_info = yf.Ticker(ticker)
        data1 = get_info.get_info()

        data = calculate_indicator(data)

        # require_columns = ['EMA_10', 'EMA_20', 'EMA_50','MACD','RSI','BUY_SIGNAL','SELL_SIGNAL']
        # for col in require_columns:
        #     messagebox.showerror(f"Error",f"Columns {col} is missing from data.")

        #current Price
        current_price = tk.Label(self.root ,text=f"Current Price: {data['Close'].iloc[1]}")
        current_price.pack()

        ##
        current_info = tk.Label(self.root, text=f"Information: {data1} ")
        current_info.pack()

        #คำนวณการเข้าซื้อด้วยเส้น EMA
        entry_price = calculate_entry_price(data)
        take_profit = entry_price * 1.05 if entry_price else None

        #แสดงEntry Price และ Take Profit
        if entry_price :
            entry_label = tk.Label(self.root, text=f"Entry Rptice (Base on EMA): {entry_price:.2f}")
            entry_label.pack()
        if take_profit :
            profit_label = tk.Label(self.root, text=f"Take Profit (5% Target): {take_profit:2f}")
            profit_label.pack()

        #Train model AI ในการทำนาย
        model = train_model(data)
        prediction = model.predict(data[['EMA_10', 'EMA_20', 'EMA_50', 'MACD', 'RSI']])
        data['AI_Prediction'] = (prediction > 0.5).astype(int)

        #Draw Graph
        self.ax.clear()
        self.ax.plot(data['Close'], label=f"Close Price:", color="blue")
        self.ax.plot(data['EMA_10'] , label=f"EMA 10: ", color="orange")
        self.ax.plot(data['EMA_20'], label=f'EMA 20: ' ,color='green')
        self.ax.plot(data['EMA_50'], label=f'EMA 50: ', color='red')

        if entry_price :
            self.ax.plot(data.index[data['BUY_SIGNAL']], data['Close'][data['BUY_SIGNAL']], 'go', label='BUY_SIGNAL')
        
        #ใส่ Entry & Take Profit
        for i in range(len(data)):
            if data['AI_Prediction'].iloc[i] == 1:
                self.ax.plot(data.index[i], data['Close'].iloc[i], 'go' ,label='BUY_SIGNAL')
            # elif data['SELL_SIGNAL'].iloc[i]:
            #     self.ax.plot(data.index[i],data['Close'].iloc[i], 'ro', label='SELL_SIGNAL')
        self.ax.set_title(f"Price Analysis:{ticker.capitalize()}")
        self.ax.legend(loc='best')
        self.canvas.draw()
    
    #start program
    def run(self):
        self.root.mainloop()
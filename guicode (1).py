
"""
Created on Sat Feb 26 11:19:47 2022

@author: rajeevkalose
"""

from tkinter import *
# Create a GUI window
root = Tk()
# create a global variables
variable1 = StringVar(root)
variable2 = StringVar(root)
variable1.set("currency")
variable2.set("currency")
# from one currency to another currency
def RealTimeCurrencyConversion():
 
    # importing required libraries
    import requests, json
 
    # currency code
    from_currency = variable1.get()
    to_currency = variable2.get()
 
    # enter your api key here
    api_key = "Your_Api_Key"
     
    # base_url variable store base url
    base_url = r"https://www.alphavantage.co/query?function = CURRENCY_EXCHANGE_RATE"
 
    # main_url variable store complete url
    main_url = base_url + "&from_currency =" + from_currency +"&to_currency =" + to_currency + "&apikey =" + api_key
 
    # get method of requests module
    # return response object
    req_ob = requests.get(main_url)
 
    # json method return json format
    # data into python dictionary data type.
     
    # result contains list of nested dictionaries
    result = req_ob.json()
    Exchange_Rate = float(result['Realtime Currency Exchange Rate'],['5. Exchange Rate'])
    # string from text entry box.
    amount = float(Amount1_field.get())
 
    # calculation for the conversion
    new_amount = round(amount * Exchange_Rate, 3)
    # value in the text entry box.
    Amount2_field.insert(0, str(new_amount))
 
 
# Function for clearing the Entry field
def clear_all() :
    Amount1_field.delete(0, END)
    Amount2_field.delete(0, END)
    
 
# Driver code
if __name__ == "__main__" :
 
    # Set the background colour of GUI window
    root.configure(background = 'blue')
    # Create welcome to Real Time Currency Convertor label
    headlabel = Label(root, text = 'welcome to Currency Convertor',
                      fg = 'black', bg = "red")
    # Creates a label
    label1 = Label(root, text = "From Currency",
                   fg = 'black')
    label2 = Label(root, text = "To Currency :",
                   fg = 'black')

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure . 
    headlabel.grid(row = 0, column = 1)
    label1.grid(row = 1, column = 1)
    label2.grid(row = 1, column = 2)
    # for filling or typing the information.
    Amount1_field = Entry(root)
    Amount2_field = Entry(root) 
    # ipadx argument sets width of entry space.
    Amount1_field.grid(row = 3, column = 1)
    Amount2_field.grid(row = 3, column = 2)
    # list of currency codes
    CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR","JPY"]
 
    # create a drop down menu using OptionMenu function
    FromCurrency_option = OptionMenu(root, variable1, *CurrenyCode_list)
    ToCurrency_option = OptionMenu(root, variable2, *CurrenyCode_list)
     
    FromCurrency_option.grid(row = 2, column = 1, ipadx = 10)
    ToCurrency_option.grid(row = 2, column = 2, ipadx = 10)
     
    # Create a Convert Button and attached
    # with RealTimeCurrencyExchangeRate function
    button1 = Button(root, text = "Convert", bg = "red", fg = "black",
                                command = RealTimeCurrencyConversion)
     
    button1.grid(row = 5, column = 1)
 
    # Create a Clear Button and attached
    # with delete function
    button2 = Button(root, text = "Clear", bg = "red",
                     fg = "black", command = clear_all)
    button2.grid(row = 5, column = 2)
   
    # Start the GUI
    root.mainloop()
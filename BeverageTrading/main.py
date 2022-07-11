import datetime as dt
import numpy as np
from scipy.stats.mstats import gmean
import beverage
from beverage import Beverage

def operations():

    """
    List of allowed operations

    :return:
    """
    print("#"*70)
    print()
    print("1)  Calculate Dividend Yield")
    print("2)  Calculate P/E Ratio")
    print("3)  Add a Trade Record")
    print("4)  Calculate volume Weighted Stock Price for the past 5 minutes")
    print("5)  Calculate GBCE Index of all the shares traded on GBCE")
    print("6)  Exit")
    print("#"*70)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print()
    print('--------------------- SUPER SIMPLE STOCK MARKET ---------------------')
    print()
    beverage = Beverage()
    operations()
    flag = 1
    while flag:
        try:
            option = int(input("Choose the operation: "))
            if option <1 or option >6:
                raise ValueError

            if option == 6:
                flag = 0

            if option in (1,2,3,4):
                ticker = beverage.check_ticker(input("Enter the Ticker Symbol: "))
                if ticker is None:
                    print("Ticker Symbol doesn't belong to the GBSE. \n")
                    continue

            if option in (1,2,3):
                price = float(input("Enter the Price: "))
                if price == 0:
                    raise ValueError

            if option == 1:
                div_yld = beverage.calculate_dividend_yield(ticker, price)
                print(f"Dividend yield of {ticker} is {div_yld*100} %")

            elif option == 2:
                pe_ratio = beverage.calculate_pe_ratio(ticker, price)
                print(f"P/E Ratio of {ticker} is {pe_ratio}")

            elif option == 3:
                quantity = int(input("Quantity Traded: "))
                direction = input("Buy  (b) or  Sell (s)?")
                if direction.strip().lower() == 'b' or direction.strip().lower() == 'buy':
                    direction = 'buy'
                elif direction.strip().lower() == 's' or direction.strip().lower() == 'sell':
                    direction = 'sell'
                else:
                    raise ValueError
                status = beverage.record_trade(ticker, quantity, direction, price)
                if status == 1:
                    print("Trade Record Successfully Updated")

            elif option == 4:
                vwap = beverage.calculate_volume_weighted_price(ticker, 5)
                print(f"Volume weighted average price of {ticker} for the last 5 minutes is {vwap}")

            elif option == 5:
                gbse = beverage.calculate_gbse_index()
                print(f"The GBCE All Share Index Level computed as a geometric mean of volume weighted average prices is {gbse}")

        except ValueError:
            print("Invalid Entry !!!")
            print()
        else:
            print()
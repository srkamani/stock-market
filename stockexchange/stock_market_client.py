from stockexchange.stock_market import StockMarket
from stockexchange.stock import StockType
from stockexchange.stock_market_validation import validate_price, validate_quantity, validate_buy_sell_indicator


def main():
    stock_market = StockMarket()

    # Add stocks to stock market
    # the dividend and PAR VALUE are in $
    stock_market.add_stock('TEA', StockType.COMMON, 0, par_value=100/100.0)
    stock_market.add_stock('POP', StockType.COMMON, 8/100.0, par_value=100/100.0)
    stock_market.add_stock('ALE', StockType.COMMON, 23/100.0, par_value=60/100.0)
    stock_market.add_stock('GIN', StockType.PREFERRED, 8/100.0, fixed_dividend=2, par_value=100/100.0)
    stock_market.add_stock('JOE', StockType.COMMON, 12/100.0, par_value=250/100.0)

    while True:
        print("\nOptions:")
        print("1. Calculate Dividend Yield")
        print("2. Calculate P/E Ratio")
        print("3. Record a Trade")
        print("4. Calculate Volume Weighted Stock Price")
        print("5. Calculate GBCE All Share Index")
        print("6. Print stocks")
        print("7. Print trades")
        print("8. Quit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            try:
                symbol = input("Enter stock symbol: ")
                price = validate_price(input("Enter price: "))
                dividend_yield = stock_market.dividend_yield(symbol, price)
                print("Dividend Yield:", dividend_yield)
            except ValueError as e:
                print("Error: ", e)
                continue

        elif choice == '2':
            try:
                symbol = input("Enter stock symbol: ")
                price = validate_price(input("Enter price: "))
                pe_ratio = stock_market.pe_ratio(symbol, price)
                print("P/E Ratio:", pe_ratio)
            except ValueError as e:
                print("Error: ", e)
                continue

        elif choice == '3':
            try:
                symbol = input("Enter stock symbol: ")
                quantity = validate_quantity(input("Enter quantity: "))
                buy_sell = input("Enter buy/sell indicator (buy/sell): ")
                traded_price = validate_price(input("Enter traded price: "))
                stock_market.record_trade(symbol, quantity, buy_sell, traded_price)
                print("Trade recorded successfully.")
            except ValueError as e:
                print("Error: ", e)
                continue

        elif choice == '4':
            try:
                symbol = input("Enter stock symbol: ")
                vws_price = stock_market.volume_weighted_stock_price(symbol)
                print("Volume Weighted Stock Price:", vws_price)
            except ValueError as e:
                print("Error: ", e)
                continue

        elif choice == '5':
            geometric_mean = stock_market.geometric_mean_all_trades()
            print("GBCE All Share Index:", geometric_mean)

        elif choice == '6':
            stock_market.print_stocks()

        elif choice == '7':
            stock_market.print_trades()

        elif choice == '8':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()

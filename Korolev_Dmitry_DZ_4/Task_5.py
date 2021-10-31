from Utils import currency_rates, currency_rates_dom

if __name__ == "__main__":
    import sys
    currency_rates(sys.argv[1])
    currency_rates_dom(sys.argv[1])
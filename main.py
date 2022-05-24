import requests
import number
import quotes

def main():

    print("\nThis is a random Ron Swanson quote from the NBC\ncomedy television series Parks and Recreation: \n")

    quote = quotes.Quotes()
    try:
        quote.getData()
    except:
        print("There seems to be a problem connecting to the API, so here is a saved quote: ")
        print("What's cholesteral?")
        past = 19
    else:
        for res in quote.r:
            print(res[2:-2])
            past = (len(res[2:-2]))

    print(f"\nThe length of that quote is {past} characters,\nand a significant historical event from {past} years ago is: \n")

    num = number.Number()
    try:
        num.getData(str(2021 - past))
    except:
        print(f"\nDue to a connection error, here is a \nsignificant historical event from {past} years ago: \n")
        print("2002 is the year that a Spanish-facilitated ceasefire begins in Sri Lanka.\n")
    else:
        for res in num.r:
            print(res)
main()

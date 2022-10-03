import requests,sys
def main():   
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    a=r.json()
    b=a["bpi"]["USD"]["rate"]
    b=float(b.replace(",",""))
    print(f"${b*float(sys.argv[1])}")


try:
    main()
except requests.RequestException:
    print("Failed to establish connection")

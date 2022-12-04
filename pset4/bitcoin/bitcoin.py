from sys import argv
import requests


def exit_msg(msg):
    print(msg)
    exit(1)


try:
    count = float(argv[1])
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    rate = res["bpi"]["USD"]["rate_float"]
    print(f"${rate * count:,}")
except IndexError:
    exit_msg("Missing command-line argument")
except ValueError:
    exit_msg("Command-line argument is not a number")
except requests.RequestException:
    exit_msg("Request failed")

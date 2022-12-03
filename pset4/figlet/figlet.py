from pyfiglet import Figlet
import argparse

# get a font from argument -f or --font using argparse
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--font")
args = ap.parse_args()
font = args.font

figlet = Figlet()
# set font to `font` arg from argparse if it is not `None`
if font:
    figlet.setFont()
print(figlet.renderText(input("")))

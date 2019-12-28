import argparse

import requests
from bs4 import BeautifulSoup as Soup
from markdown2 import Markdown

version = 1.0
style = False

text = 'This program takes the URL of a website with the target recipe, scraps it and stylises it. If the stylized argument is not passed, then it generates a vanilla HTML file'

parser = argparse.ArgumentParser(description = text)
parser.add_argument("-S", "--stylized", help="generate stylized html", action="store_true")
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("-U", "--url", help="input url")

args = parser.parse_args()

if args.version:
	print("Web2Recipe Version", version)
	exit
if args.stylized:
	style = True
if args.url:
	url = args.url
else:
	url = input("Enter Recipe Website URL: ")


markdowner = Markdown()

params = (('url', url),)
response = requests.get('https://ingredients.schollz.now.sh/', params=params)

json = response.json()
title = json["title"]
ingredients = []

def comment(x):
	try:
		c = "(" + str(x["comment"]) + ")"
		return c
	except:
		return ""

for x in json["ingredients"]:
	i = x["measure"]["amount"], x["measure"]["name"], x["name"], comment(x)
	ingredients.append(i)

def genSimpleHTML():
	html = markdowner.convert("#" + title) + markdowner.convert("## Ingredients")
	for x in ingredients:
		s = "* "
		for i in x:
			s = s + str(i) + " " 
		html = html + markdowner.convert(s)
	html = html + markdowner.convert('## Instructions')
	html = html + "<ol>"
	for x in json["instructions"]:
		html = html + "<li> " + x + "</li>"
	html = html + "</ol>"
	f = open("./simple.html", "w")
	f.write(html)
	f.close()
	print("Succesfuly generated file for the recipe: ", title)

def stylized():
	ing = "<ul>"
	for x in ingredients:
			s = "<li>"
			for i in x:
				s = s + str(i) + " "
			ing = ing + s
	ing = ing + "</li>" 
	ins = ""
	for x in json["instructions"]:
		ins = ins + "<div class=\"recipe-recipe__steps\"> " + x + "</div> <br>"
	f = open("html/template.html", "r")
	template = str(f.read())
	template = template.replace("REPLACE-RECIPE-TITLE",title)
	template = template.replace("REPLACE-INGREDIENTS",ing)
	template = template.replace("REPLACE-INSTRUCTIONS",ins)
	template = template.replace("REPLACE-IMG", json["image"])
	f = open("./stylized.html", "w")
	f.write(template)
	f.close()
	print("Succesfuly generated stylized file for the recipe: ", title)

if style:
	stylized()
else:
	genSimpleHTML()

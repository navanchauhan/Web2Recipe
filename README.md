# Web2Recipe

This is a simple Python script to scrap recipes from websites and then generate stylized/non-stylized (no-extra-crap) single page HTML pages

```
usage: web2recipe.py [-h] [-S] [-V] [-U URL]

This program takes the URL of a website with the target recipe, scraps it and
stylises it. If the stylized argument is not passed, then it generates a
vanilla HTML file

optional arguments:
  -h, --help         show this help message and exit
  -S, --stylized     generate stylized html
  -V, --version      show program version
  -U URL, --url URL  input url
```

### Screenshots

#### Simple

![non-stylized](https://raw.githubusercontent.com/navanchauhan/Web2Recipe/master/assets/ss1.png, "Non-Stylised")

![stylized](https://raw.githubusercontent.com/navanchauhan/Web2Recipe/master/assets/ss2.png, "Stylised")

![stylized-mobile](https://raw.githubusercontent.com/navanchauhan/Web2Recipe/master/assets/ss3.png, "Stylised (Mobile)")

### Requirements

* BeutifulSoup4
* Markdown2

### Acknowledgemnts

* Zack Schollz Github: schollz - Ingredients API
* CodePen: oliviale - Recipe Layout CSS
import requests
from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader('../templates'))
template = env.get_template('main.html')

def generate_content():
    # Add your content generation logic here
    return "Welcome to my money-making site!"

def build_site():
    html = template.render(
        title="Money Maker Hub",
        content=generate_content(),
        offers=[]
    )
    with open("../docs/index.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    build_site()
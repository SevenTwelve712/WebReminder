from flask import Flask
from webreminder_app.pages.navigation_bar import navbar_f as navbar

app = Flask(__name__)

# инициализируем страницы, написанные в init разделов
import webreminder_app.pages.java
import webreminder_app.pages.instructions
import webreminder_app.pages.linux.packages
import webreminder_app.pages.libraries
import webreminder_app.pages.net
import webreminder_app.pages.qt
import webreminder_app.pages.java.minecraft_modding


@app.route('/')
def main():
    return '<p>Hello, this is main page</p>'

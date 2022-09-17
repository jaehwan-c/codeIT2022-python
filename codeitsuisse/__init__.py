from flask import Flask
app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.tickerStream1
import codeitsuisse.routes.tickerStream2
import codeitsuisse.routes.calendarDays
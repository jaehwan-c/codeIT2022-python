from flask import Flask
app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.tickerStream1
import codeitsuisse.routes.tickerStream2
import codeitsuisse.routes.cryptocollapz
import codeitsuisse.routes.calendarDays
import codeitsuisse.routes.reversle
import codeitsuisse.routes.rubiks
import codeitsuisse.routes.quordleKeyboard
import codeitsuisse.routes.stig_warmup

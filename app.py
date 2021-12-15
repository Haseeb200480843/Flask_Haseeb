from os import name
from flask import Flask, request, render_template, Markup
from flask_pymongo import PyMongo, pymongo
import pymongo
from bson.json_util import dumps

app = Flask(__name__)

app.config['MONGO_DBNAME'] = "Covid_db"
app.config['MONGO_URI'] = "mongodb+srv://with_haseeb:Password@cluster0.r2210.mongodb.net/Covid_db?retryWrites=true&w=majority"
app.config['MONGO_COLLECTION_NAME'] = "Covid_data"
mongo = PyMongo(app)



@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template ('base.html')

@app.route('/data', methods = ['POST', 'GET'])
def Data():
    return render_template ('table.html')
 
@app.route('/population', methods = ['POST', 'GET'])
def Population():
    return render_template ('population.html')

@app.route('/visuals', methods = ['POST', 'GET'])
def Visuals():
    return render_template ('pie_chart.html')

@app.route('/cases', methods = ['POST', 'GET'])
def Totalcases():
    return render_template ('cases.html')

@app.route('/deaths', methods = ['POST', 'GET'])
def Totaldeaths():
    return render_template ('deaths.html')




if __name__ == '__main__':
    app.run(debug=True)
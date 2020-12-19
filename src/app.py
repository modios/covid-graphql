from flask import Flask
from flask_graphql import GraphQLView
from database.models import init_db
from datetime import date
from graphql_infrastructure.schema import schema
from mongoengine import connect
from database.models import CovidInfoByCountry
import os
from database.auto_update_helpers import update_data
import schedule
import time
import threading

mongoHost = os.environ.get('DB_HOST',"127.0.0.1")
#mongoUserName = os.environ.get('DB_USERNAME',None),
#mongoPassword = os.environ.get('DB_PASSWORD',None),
#mongoDatabase  =  os.environ.get('DB_Name',"covid19"),
mongoPort  =  int(os.environ.get('DB_Port','27017'))
connect('covid-19-db', host=mongoHost, port=mongoPort)

# When true, updates the data/databse once per day.
data_scheduler_enabled = False

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Covid-19 GraphQL API.</h1><p>Visit /graphql.</p> <p>Example : query{ Npho{ intesCareCases{ date intensiveCare }}} <p>"

schedule.every().day.at("00:14").do(update_data)

def initialize_data_scheduler():
     while True:
         schedule.run_pending()
         time.sleep(1)


if __name__ == "__main__":
    update_data()
    if(data_scheduler_enabled):
        t=threading.Thread(target=initialize_data_scheduler)
        t.start()
    init_db()
    Host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    Port = int(os.environ.get('FLASK_RUN_PORT', '5000'))
    Debug = bool(os.environ.get('FLASK_DEBUG', 'True'))
    app.run(host=Host,port=Port, debug=Debug)

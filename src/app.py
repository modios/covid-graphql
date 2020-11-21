from flask import Flask
from flask_graphql import GraphQLView
from database.models import init_db
from datetime import date
from graphql_infrastructure.schema import schema
from mongoengine import connect
from database.models import CovidInfoByCountry
import os

mongoHost = os.environ.get('DB_HOST',"127.0.0.1")
#mongoUserName = os.environ.get('DB_USERNAME',None),
#mongoPassword = os.environ.get('DB_PASSWORD',None),
#mongoDatabase  =  os.environ.get('DB_Name',"covid19"),
mongoPort  =  int(os.environ.get('DB_Port','27017'))
connect('covid19Hopkings', host=mongoHost, port=mongoPort)

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    init_db()
    Host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    Port = int(os.environ.get('FLASK_RUN_PORT', '5000'))
    Debug = bool(os.environ.get('FLASK_DEBUG', 'True'))
    app.run(host=Host,port=Port, debug=Debug)

from mongoengine.fields import (
    DateTimeField,
    ListField,
    StringField,
    IntField
)

from mongoengine import Document, EmbeddedDocument,EmbeddedDocumentField
import pandas as pd


class CovidInfo(EmbeddedDocument):
    meta = {"collection": "CovidInfo"}
    date = StringField()
    confirmed = IntField()
    recovered = IntField()
    deaths = IntField()

class CovidInfoByCountry(Document):
    meta = {"collection": "CovidInfoByCountry"}
    country = StringField(required=True)
    covidInfo = ListField(EmbeddedDocumentField(CovidInfo))


def dropCollections():
    CovidInfoByCountry.drop_collection()

def insertJohnsHopkinsCSSEPColection():
    df = pd.read_json('./data/all_countries/JohnsHopkinsCSSE/timeseries_per_country.json')
    df = df.dropna(0)
    countries = df.columns
    countriesByCovidInfo = None
    for country in countries:
        listOfInfo = list(map(lambda x: CovidInfo(date = x['date'], confirmed = x['confirmed'], recovered = x['recovered'], deaths = x['deaths']) , df[country].values.tolist()))
        info = CovidInfoByCountry(country = country, covidInfo = listOfInfo)
        info.save()

def init_db():
    dropCollections()
    insertJohnsHopkinsCSSEPColection()

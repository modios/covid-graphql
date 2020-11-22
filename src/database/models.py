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

class NphoIntensiveCareCases(Document):
    meta = {"collection": "NphoIntensiveCareCases"}
    date = StringField()
    intensive_care = IntField()

class NphoTotalTests(Document):
    meta = {"collection": "NphoTotalTests"}
    date = StringField()
    rapid_tests = IntField()
    tests = IntField()

def dropCollections():
    NphoTotalTests.drop_collection()
    NphoIntensiveCareCases.drop_collection()
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

def insertNphoIntensiveCareCases():
    df = pd.read_json('./data/greece/NPHO/intensive_care_cases.json')
    df = df['cases']
    for case in df:
        info = NphoIntensiveCareCases(date = case['date'], intensive_care = case['intensive_care'])
        info.save()

def insertNphoTests():
    df = pd.read_json('./data/greece/NPHO/tests.json')
    df = df['total_tests']
    for test in df:
        info = NphoTotalTests(date = test['date'], rapid_tests = test['rapid-tests'], tests = test['tests'])
        info.save()

def init_db():
    dropCollections()
    insertNphoIntensiveCareCases()
    insertNphoTests()
    insertJohnsHopkinsCSSEPColection()

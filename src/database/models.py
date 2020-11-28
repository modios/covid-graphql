from mongoengine.fields import (
    DateTimeField,
    ListField,
    StringField,
    IntField,
    FloatField
)

from mongoengine import Document, EmbeddedDocument,EmbeddedDocumentField
import pandas as pd
import json 
from pandas.io.json import json_normalize #package for flattening json in pandas df
import os

class NphoAgeGroups(EmbeddedDocument):
    zero_to_17 = IntField()
    eighteen_to_39 = IntField()
    fourthy_to_64 = IntField()
    sixtyfine_plus = IntField()  
   
    @staticmethod
    def jsonToModel(json_data):
        cases = NphoAgeGroups()
        cases.zero_to_17 = json_data['0-17']
        cases.eighteen_to_39 = json_data['18-39']
        cases.fourthy_to_64 = json_data['40-64']
        cases.sixtyfine_plus = json_data['65+']
        return cases

class NphoTotalForAgeGroups(EmbeddedDocument):
    cases = EmbeddedDocumentField(NphoAgeGroups)
    critical = EmbeddedDocumentField(NphoAgeGroups)
    deaths = EmbeddedDocumentField(NphoAgeGroups)

class NphoGenderAge(Document):
    meta = {"collection": "NphoGenderAge"}
    total_females_percentage = FloatField()
    total_males_percentage = FloatField()
    total_females = EmbeddedDocumentField(NphoTotalForAgeGroups)
    total_males = EmbeddedDocumentField(NphoTotalForAgeGroups)
    updated = StringField()

class NphoAgeData(Document):
    meta = {"collection": "NphoAgeData"}
    age_average = FloatField()
    average_death_age = FloatField()
    total_age_groups = EmbeddedDocumentField(NphoTotalForAgeGroups)
    updated = StringField()


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

    # drop this collection only in debug
    if(bool(os.environ.get('FLASK_DEBUG', 'True'))):
        NphoAgeData.drop_collection()
        NphoGenderAge.drop_collection()

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

def insertNphoAgeData():
    #load json object
    with open('./data/greece/NPHO/age_data.json') as f:
        d = json.load(f)
  
    cases = NphoAgeGroups.jsonToModel(d['total_age_groups']['cases'])
    critical = NphoAgeGroups.jsonToModel(d['total_age_groups']['critical'])
    deaths = NphoAgeGroups.jsonToModel(d['total_age_groups']['deaths'])

    total_age_groups = NphoTotalForAgeGroups(cases = cases, critical = critical, deaths = deaths)

    info = NphoAgeData(
        age_average= d['age_average'],
        average_death_age = d['average_death_age'], 
        updated = d['updated'], 
        total_age_groups = total_age_groups)

    info.save()

def insertGenderAge():
    #load json object
    with open('./data/greece/NPHO/gender_age_data.json') as f:
        d = json.load(f)
  
    #females
    cases_f = NphoAgeGroups.jsonToModel(d['total_age_groups']['females']['cases'])
    critical_f = NphoAgeGroups.jsonToModel(d['total_age_groups']['females']['critical'])
    deaths_f = NphoAgeGroups.jsonToModel(d['total_age_groups']['females']['deaths'])
     
    total_females = NphoTotalForAgeGroups(cases = cases_f, critical = critical_f, deaths = deaths_f)
   
    #males
    cases_m = NphoAgeGroups.jsonToModel(d['total_age_groups']['males']['cases'])
    critical_m = NphoAgeGroups.jsonToModel(d['total_age_groups']['males']['critical'])
    deaths_m = NphoAgeGroups.jsonToModel(d['total_age_groups']['males']['deaths'])
     
    total_males = NphoTotalForAgeGroups(cases = cases_m, critical = critical_m, deaths = deaths_m)
  
    info = NphoGenderAge(
        total_females_percentage= d['total_females_percentage'],
        total_males_percentage = d['total_males_percentage'], 
        updated = d['updated'], 
        total_males = total_males,
        total_females = total_females)

    info.save()

def init_db():
    dropCollections()
    insertNphoIntensiveCareCases()
    insertNphoTests()
    insertJohnsHopkinsCSSEPColection()
    insertNphoAgeData()
    insertGenderAge()

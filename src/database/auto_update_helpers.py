import json
import requests
import pandas as pd

def fech_and_save(url, save_path):
    timeseries = requests.get(url)
    data = timeseries.json()
    with open(save_path, 'w') as f:
        json.dump(data, f,indent=4, sort_keys=True)

def getJohnsHopkinsCSSEData():
    fech_and_save(
        'https://pomber.github.io/covid19/timeseries.json', 
        'data/all_countries/JohnsHopkinsCSSE/timeseries_per_country.json')


def getNHPOData():
    age_data_path = 'data/greece/NPHO/age_data.json'
    gender_age_data_path = 'data/greece/NPHO/gender_age_data.json'
    intensive_care_cases_path = 'data/greece/NPHO/intensive_care_cases.json'
    tests_path = 'data/greece/NPHO/tests.json'

    fech_and_save(
        'https://raw.githubusercontent.com/Covid-19-Response-Greece/covid19-data-greece/master/data/greece/age_distribution/age_data.json', 
        age_data_path)
    fech_and_save(
        'https://raw.githubusercontent.com/Covid-19-Response-Greece/covid19-data-greece/master/data/greece/gender_distribution/gender_age_data.json', 
        gender_age_data_path)
    fech_and_save(
        'https://raw.githubusercontent.com/Covid-19-Response-Greece/covid19-data-greece/master/data/greece/general/intensive_care_cases.json', 
        intensive_care_cases_path)
    fech_and_save(
        'https://raw.githubusercontent.com/Covid-19-Response-Greece/covid19-data-greece/master/data/greece/general/tests.json', 
        tests_path)



def update_data():
    getJohnsHopkinsCSSEData()
    getNHPOData()


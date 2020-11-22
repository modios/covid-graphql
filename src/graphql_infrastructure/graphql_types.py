from graphene import ObjectType,Field
from database.models import CovidInfoByCountry
from database.models import CovidInfo
import graphene
from database.models import NphoIntensiveCareCases, NphoTotalTests

class CovidInfoType(ObjectType):
    date = graphene.String()
    confirmed = graphene.Int()
    recovered = graphene.Int()
    deaths = graphene.Int()

    @staticmethod
    def model_to_type(covidInfo: CovidInfo):
       return CovidInfoType(date = covidInfo.date, 
       confirmed = covidInfo.confirmed,
       recovered = covidInfo.recovered, 
       deaths = covidInfo.deaths)

class CovidInfoByCountryType(ObjectType):
    country = graphene.String()
    covidInfo = graphene.List(CovidInfoType)

    @staticmethod
    def model_to_type(covidByCountry : CovidInfoByCountry):
       return CovidInfoByCountryType(
       country = covidByCountry.country,
       covidInfo = list(map(lambda x: CovidInfoType.model_to_type(x), covidByCountry.covidInfo)))

class NphoTotalTestsType(ObjectType):
    date =graphene.String()
    rapid_tests = graphene.Int()
    tests = graphene.Int()
    @staticmethod
    def model_to_type(nphoTotalTests : NphoTotalTests):
        return NphoTotalTestsType(
            date = nphoTotalTests.date,
            rapid_tests = nphoTotalTests.rapid_tests,
            tests = nphoTotalTests.tests)

class NphoIntensiveCareCasesType(ObjectType):
    date = graphene.String()
    intensive_care =  graphene.Int()

    @staticmethod
    def model_to_type(nphoIntensiveCareCases : NphoIntensiveCareCases):
       return NphoIntensiveCareCasesType(
            date = nphoIntensiveCareCases.date,
            intensive_care = nphoIntensiveCareCases.intensive_care)
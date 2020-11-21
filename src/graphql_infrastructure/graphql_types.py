from graphene import ObjectType,Field
from database.models import CovidInfoByCountry
from database.models import CovidInfo
import graphene


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
       covidInfo = list(map(lambda x: CovidInfoType.model_to_type(x), covidByCountry.covidInfo))
       )


from graphene import ObjectType,Field
from database.models import CovidInfoByCountry
from database.models import CovidInfo
import graphene
from database.models import NphoIntensiveCareCases, NphoTotalTests, NphoAgeData, NphoGenderAge, NphoTotalForAgeGroups,NphoAgeGroups

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


class NphoAgeGroupsType(ObjectType):
    zero_to_17 = graphene.Int()
    eighteen_to_39 = graphene.Int()
    fourthy_to_64 = graphene.Int()
    sixtyfine_plus = graphene.Int()
    @staticmethod
    def model_to_type(nphoAgeGroups : NphoAgeGroups):
       return NphoAgeGroupsType(
           zero_to_17 = nphoAgeGroups.zero_to_17,
           eighteen_to_39 = nphoAgeGroups.eighteen_to_39,
           fourthy_to_64 = nphoAgeGroups.fourthy_to_64,
           sixtyfine_plus = nphoAgeGroups.sixtyfine_plus)

class NphoTotalForAgeGroupsType(ObjectType):
    cases = graphene.Field(NphoAgeGroupsType)
    critical = graphene.Field(NphoAgeGroupsType)
    deaths = graphene.Field(NphoAgeGroupsType)

    @staticmethod
    def model_to_type(nphoTotalForAgeGroups : NphoTotalForAgeGroups):
       return NphoTotalForAgeGroupsType(
               cases = NphoAgeGroupsType.model_to_type(nphoTotalForAgeGroups.cases),
               critical = NphoAgeGroupsType.model_to_type(nphoTotalForAgeGroups.critical),
               deaths = NphoAgeGroupsType.model_to_type(nphoTotalForAgeGroups.deaths))

class NphoAgeDataType(ObjectType):
    age_average = graphene.Float()
    average_death_age = graphene.Float()
    total_age_groups = graphene.Field(NphoTotalForAgeGroupsType)
    updated = graphene.String()
    @staticmethod
    def model_to_type(nphoAgeData : NphoAgeData):
       return NphoAgeDataType(
            age_average = nphoAgeData.age_average,
            average_death_age = nphoAgeData.average_death_age,
            total_age_groups = NphoTotalForAgeGroupsType.model_to_type(nphoAgeData.total_age_groups),
            updated = nphoAgeData.update)
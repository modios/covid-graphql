from graphene import ObjectType,Field,List, String
from graphql_infrastructure.graphql_types import CovidInfoByCountryType, CovidInfoType 
from database.models import CovidInfoByCountry;
   
class GetAllCountriesQuery(ObjectType):
     get_all_countries_covid_info = Field(List(CovidInfoByCountryType))

     def resolve_get_all_countries_covid_info(root, info): 
            return list(map(lambda x: CovidInfoByCountryType.model_to_type(x), CovidInfoByCountry.objects.all()))


class JohnsHopkinsCSSE(ObjectType):
     all_countries = Field(GetAllCountriesQuery)
     covid_info_by_country = List(CovidInfoType, countryName = String())
     def resolve_all_countries(root, info):
          return {}
     
     def resolve_covid_info_by_country(root, info, countryName):
          return list(CovidInfoByCountry.objects(country=countryName).first().covidInfo)


class RootQuery(ObjectType):
     JohnsHopkinsCSSE = Field(JohnsHopkinsCSSE)

     def resolve_JohnsHopkinsCSSE(root, info):
          return {}

from graphene import ObjectType,Field,List
from graphql_infrastructure.graphql_types import CovidInfoByCountryType, CovidInfoType 
from database.models import CovidInfoByCountry;
   
class GetAllCountriesQuery(ObjectType):
     get_all_countries_covid_info = Field(List(CovidInfoByCountryType))

     def resolve_get_all_countries_covid_info(root, info): 
            return list(map(lambda x: CovidInfoByCountryType.model_to_type(x), CovidInfoByCountry.objects.all()))
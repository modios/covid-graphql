import graphene
from graphql_infrastructure.graphql_queries import GetAllCountriesQuery
from graphql_infrastructure.graphql_types import CovidInfoByCountryType, CovidInfoType

schema = graphene.Schema(query=GetAllCountriesQuery, types=[CovidInfoByCountryType, CovidInfoType])
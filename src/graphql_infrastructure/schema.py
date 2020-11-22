import graphene
from graphql_infrastructure.graphql_queries import GetAllCountriesQuery,RootQuery
from graphql_infrastructure.graphql_types import CovidInfoByCountryType, CovidInfoType

schema = graphene.Schema(query=RootQuery, types=[CovidInfoByCountryType, CovidInfoType])
# covid-graphql

# How to use.
 -Do docker-compose up, it should start intialize the library and start the application
 -Visit http://127.0.0.1:5000/graphql
 -Do for example :
     'query{
           getAllCountriesCovidInfo{
             country
             }
           }'

  It should return the list of countries for with we have data about the pandemic.

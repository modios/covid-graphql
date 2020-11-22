# covid-graphql
Experimenting with simple Graphql API that fetches covid-19 related data.

### References:

* https://github.com/Covid-19-Response-Greece/covid19-greece-api
* https://github.com/pomber/covid19
* https://github.com/CSSEGISandData/COVID-19


# How to use.
 * Do docker-compose up, it should start intialize the database and start the application
 * Visit http://127.0.0.1:5000/graphql
 * Do for example :
     'query{
           getAllCountriesCovidInfo{
             country
             }
           }'

  It should return the list of countries for with we have data about the pandemic.
  
### Todo
- [x] Fetch data for single country by providing the name as input.

- [ ] Add NPHO (EODY) Greek covid19 data.

- [ ] Add google mobility data https://www.google.com/covid19/mobility/

- [ ] Update data daily automatically.

- [ ] Add mutations.

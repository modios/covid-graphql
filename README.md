# covid-graphql
A simple API that fetches the covid19-data for the countries that are avaliable.
The data curently include the datasets provided by https://coronavirus.jhu.edu/map.html 
and NPHO.
(it's not the latest updated dataset).


This small project was inspired by 
* https://github.com/pomber/covid19
* https://github.com/Covid-19-Response-Greece/covid19-greece-api

# How to use.
 * Do docker-compose up, it should start intialize the library and start the application
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

- [ ] Add mutations.

- [ ] Update data daily automaticaly.

# Covid19-graphql
Experimenting with a simple Graphql API that fetches covid-19 related data.

### References:

* https://github.com/Covid-19-Response-Greece/covid19-greece-api
* https://github.com/pomber/covid19
* https://github.com/CSSEGISandData/COVID-19


# How to use.
 * Probaby the easiest way to get the application running is to run
 docker-compose up, it should intialize the database and start the application.
 * Visit http://127.0.0.1:5000/graphql
 * Then you can try to fetch the avaliable data, for example the cases in ICUs for all the avaliable dates :
 
 ```
{ 
  Npho{ 
    intesCareCases{
        date
        intensiveCare 
       }
      }
}
```

 Should return the list of countries for which we have data about the pandemic.
  
### Todo
- [x] Fetch data for single country by providing the name as input.

- [x] Add NPHO (EODY) Greek Covid-19 data.

- [x] Update data automatically.

- [ ] Add NPHO (EODY) Vaccination data.

# SPARQL and DBPedia

Just some playing around with SPARQL and DBPedia.  I was looking for a little project so figured I'd work on pulling out NHL players to see if that outliers thing is true about people being born in certain months being more likely to be pro athletes.

## Things I learned about Sparql/DBPedia

- There are built-in prefixes:
    dbo, dbp, dbr: http://stackoverflow.com/questions/19887558/get-a-gender-of-a-particular-person-in-sparql/19890881#19890881
- No nulls, you have to specify that something is optional
- Some kind of default limit of 10,000 records for things
    + I think you can specify a limit and pagination
- I can't use `?player a dbpedia:Person .` in my query, because of some stubby articles like this one: http://dbpedia.org/page/Ossie_Asmundson.  DBPedia doesn't know that Ossie is a person :(
- Sometimes DBPedia goes down for maintenance, and the Python package reports an HTTP 502 error.  Trying to submit a query through the [web interface](http://dbpedia.org/sparql) will show you a message like "The web-site you are currently trying to access is under maintenance at this time."
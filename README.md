# SPARQL and DBPedia

Just some playing around with SPARQL and DBPedia.  I was looking for a little project so figured I'd work on pulling out NHL players to see if that outliers thing is true about people being born in certain months being more likely to be pro athletes.

## Things I learned about Sparql/DBPedia

- There are built-in prefixes:
    dbo, dbp, dbr: http://stackoverflow.com/questions/19887558/get-a-gender-of-a-particular-person-in-sparql/19890881#19890881
- No nulls, you have to specify that something is optional
- Some kind of default limit of 10,000 records for things
    + I think you can specify a limit and pagination
import os
import json
from SPARQLWrapper import SPARQLWrapper, JSON
import datefinder
import datetime

LIST_PREFIX = 'http://dbpedia.org/resource/List_of'
DATA_FILE = 'players.txt'

def pull_data():
    """Pulls data from dbpedia and returns the results"""
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX category: <http://dbpedia.org/resource/Category:>
        PREFIX dcterms: <http://purl.org/dc/terms/>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

        SELECT DISTINCT ?player ?abstract ?name ?birthdate
        WHERE {
          ?player dcterms:subject ?cat .
          ?cat skos:broader category:National_Hockey_League_players .
          ?player dbo:abstract ?abstract .
          OPTIONAL { ?player dbp:name ?name } .
          OPTIONAL { ?player dbo:birthDate ?birthdate } .
          FILTER langMatches(lang(?abstract),'en')
        }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    res = results['results']['bindings']
    res = [r for r in res if not(r['player']['value'].startswith(LIST_PREFIX))]
    with open(DATA_FILE, 'w') as file_out:
        json.dump(file_out, res)


def birthdate_from_player(player):
    """Return the birthdate as a datetime.  Naively grab the first match if
    there isn't an actual birthdate."""
    try:
        return datetime.datetime.strptime()
    except:
        matches = datefinder.find_dates(abstract)
        if matches:
            return matches[0]
        else:
            return None


def process_data():
    """Pulls out dataframe

if __name__ == '__main__':
    if not os.path.isfile(DATA_FILE):
        pull_data()


#No: Doesn't get http://dbpedia.org/page/Ossie_Asmundson because dbpedia doesn't know he is a person?
'''
?player a dbpedia:Person .
'''

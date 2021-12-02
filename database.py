#nothing else is needed; import the sqlite module
import sqlite3
#denna funktionen använder vi när vi ska göra något
def run(query, values ={}):
    '''
    Helper funtion to update database.
    :param: query: The query to execute (SQL query is found in main.py)
    :param: values: The values to be used with the query
    '''
    #först, måste connecta till en databas. Finns den inte så skapas den automatiskt.
    conn = sqlite3.connect('music.db')

    cur = conn.cursor()
    #run query
    cur.execute(query, values)
    #must commit queries that does changes to the database
    conn.commit()
    #close connection
    conn.close()

#denna är för att hämta
def get(query, values ={}):
    '''
    Helper funtion to update database.
    :param: query: The query to execute (SQL query is found in main.py)
    :param: values: The values to be used with the query
    :return: The results from the query
    '''
    #först, måste connecta till en databas. Finns den inte så skapas den automatiskt.
    conn = sqlite3.connect('music.db')
    #vad ska vi få tillbaka (default är tuples, men man kan säga hur man vill ha den.) För att få en row,
    #så använder man rowfactory. row är bäst praxis.
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    #run SQL queryquery 
    cur.execute(query,values)
    #get results from executed query with fetchall
    results = cur.fetchall()
    #close connection
    conn.close()

    return results

    print(results)
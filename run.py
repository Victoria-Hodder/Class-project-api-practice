from museumsearch import app

import requests
import psycopg2
import psycopg2.extras
import pprint

host = "frauenloop.cpvjwjmdvltu.us-east-2.rds.amazonaws.com"
dbname = "frauenloop"
username = "student"
password = "learningsql"
#this is the data needed to access an external database

query='select e.exhibition_id, s.museum_id, e.museum_name museum, e.exhibition_title title, e.exhibition_subtitle subtitle, e.search_keywords keyword, e.description, e.exhibition_picture_url imgurl,    e.exhibition_picture_caption imgcaption, e.exhibition_duration_start statdate, e.exhibition_duration_end enddate FROM museum.exhibition e, museum.museumspace s WHERE e.museum_name = s.museum_name AND e.exhibition_duration_end > now() ORDER BY e.exhibition_duration_end ASC'
keywords_query = 'select e.search_keywords keyword FROM museum.exhibition e, museum.museumspace s WHERE e.museum_name = s.museum_name AND e.exhibition_duration_end > now() ORDER BY e.exhibition_duration_end ASC'

try:
    conn = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s'" % (host, dbname, username, password) )
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    print("WHOOOOO!!!! works")
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cur.execute(query)
    rows = cur.fetchall()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(rows)


except:
    print("I am unable to connect to the database")



if __name__ == "__main__":
    app.run(debug=True)
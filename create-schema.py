import sys
import os

import shapefile
import psycopg2

from config import DB

connection = psycopg2.connect(DB)
cursor = connection.cursor()

files = os.listdir(sys.argv[1])

shp = open('%s/%s' % (sys.argv[1], [s for s in files if ".shp" in s][0]), "r")
dbf = open('%s/%s' % (sys.argv[1], [s for s in files if ".dbf" in s][0]), "r")

sf = shapefile.Reader(shp=shp, dbf=dbf)
fields = sf.fields

names = [field[0] for field in fields]

cursor.execute('CREATE TABLE %s (id serial, geom geometry, %s text);' % (sys.argv[2], ' text, '.join(names[1:])))
cursor.execute('CREATE INDEX %s_gix on %s USING GIST (geom)' % (sys.argv[2], sys.argv[2]))
connection.commit()

shp.close()
dbf.close()

cursor.close()
connection.close()

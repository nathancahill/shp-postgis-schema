Requires ```shapefile``` and ```psycopg2```.

Edit ```config.py``` to add the database connection string.

Run with your shapefile directory in the current directory. Pass the directory name as the first parameter and the table name as the second parameter:

```$ python create-schema.py shapefile-directory table-name```

Creates a PostGIS table with a geometry column and a field for each field in the shapefile. Makes it easy to import shapefiles to the table afterwards.

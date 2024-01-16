
# Topics to be made into schedule
- What is binary? (lect 3)
- Counting in binary (lect 3)
- What is hex? (lect 3)
- Counting in hex (lect 3)
- Data types (ints, doubles, strings, booleans) (lect 3)
- Software engineering basic requirements analysis (lect 4)
- Project ideas (lect 5)
- History of python (lect 5a)
- Python basic stuff (lect 5a)
- Variable names (lect 5b)
- Operators (lect 5b)
- Type conversion (lect 5b)
- Conditionals, controls, comparison, functions (lect 6a)
- Scope (lect 6a)
- By value / by reference (lect 6a)
- Iteration (lect 6b)
- Strings (lect 7a)
- Regular expressions (lect 7b)
- Collections (lect 8)
- Tuples, lists, dictionaries (lect 8)
- Files (lect 9)
- OOP / Object oriented programming (lect 10)
- Objects and classes in python (lect 10)
- Exceptions and exception handling (lect 11)
- Modules (lect 12)
- Import vs from (lect 12)
- Lambdas, Map, Filter, Reduce, Generators (lect 13)
- ModelBuilder (lect 16)

"ArcPy is not a Pythonbased alternative to ArcGIS; it’s just a tool for using Python to tell ArcGIS what to do" by [this guy](http://www.nickeubank.com/wp-content/uploads/2015/10/ArcPy_IntroductoryTutorial.pdf)

# New ideas
[from here](http://pro.arcgis.com/en/pro-app/arcpy/get-started/describing-data.htm)
>
- Network stuff
    - Pulling data with rest from esri arcserver, as json, converting into geodatabase
    - Sending email
    - Formatting data as json, pushing to server
- ~~Cursors (lect 20)~~
    - Accessing data using cursors
    - Update cursor
    - Setting a cursor's spatial reference
- ~~Tool messages: [here](http://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/writing-messages-in-script-tools.htm) (lect 24)~~
- Describing data
- Using fields and indexes
- Using the spatial reference class
- Working with feature sets and record sets
- Checking for the existence of data
- Specifying a query in Python
- ~~Reading geometries (lect 25)~~
- ~~Writing geometries (lect 25)~~
- Working with NumPy in ArcGIS
- Working with SciPy in ArcGIS
- (Working with R & R-Bridge in ArcGIS)[https://github.com/R-ArcGIS/r-bridge-install]
- Using geometry objects with geoprocessing tools
- Validating table and field names in Python
- Executing SQL using an EGDB connection
- Create lists of data
- ~~Working with multivalue inputs (lect 27)~~
- Mapping input fields to output fields
- Additional tool input parameter types (check boxes, select lists, grid list, etc.) (Lect 26)
>
# Lab / Snippet ideas
- Creating a connection to an ArcServer / Portal
- Creating a connection to a database
- Grabbing data from ArcServer / Portal
- Grabbing data from a database
- Putting data into ArcServer / Portal
- Putting data into a database
- Selecting features from a layer, exporting to a new layer
- Creating vector data
- Adding a buffer layer
- Python calculator
- Loading a local shape file
- Loading a local csv
- Define a workspace
- Create a geodatabase
- Getting parameters from tool inside of arcpy
- Calling other tools from within arcpy
- Using different Python libraries (SciPy, lasio, etc)
- Using built in Python functions (round(), len(), split(), upper(), floor(), round())
- Error handling
- Raster creation
- Heatmap layer creation
- Viewshed analysis
- Something with water analysis

- Reproject data
- Define metadata

- Joins / Unions / Merge
- Cursors
- Clip / Intersect / Dissolve
- Model builder
- Convert different data types
- [Get MODIS data; convert to raster](https://modis.ornl.gov/files/exercises/GeospatialProgramming.pdf)
- Interfacing with GeoEvent Server

# Readings
1. Versioning lecture - make students read about [unromantic and unsentimental version numbers](http://sentimentalversioning.org/)

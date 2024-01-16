# TAMU GIS Programming
# Learning Objectives
- Outline the tool making process
- Create a basic arcpy-based tool
<!-- ## The tool should do the following:
- Allow the user to enter a distance (error checking that distance is a number value)
- Find all trees that are within that distance from a building
- Save trees that meet criteria as a new layer -->
# A tool of our own
Now that we've covered some of the required code to do basic operations within Python using arcpy, we will now touch on how to create a tool of our very own. This tool will appear inside the **Geoprocessing** pane of ArcGIS Pro just like any other. This tool will determine which buildings are nearby given a TAMU building number. This tool will incorporate user input to determine how big we want the search radius to be as well as to determine which building we want to buffer.
>
Keep in mind that this lecture is about creating the tool, and not creating the toolbox. Once we have a functioning tool we will be adding it to a toolbox in the next lecture.
>
## Handle user inputs
We start by importing arcpy and setting our workspace variable. Even if you do not use your workspace it is always good to set it to a default location just in case; at the very least it keeps you in the habit. 
>
```python
import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"
```
>
With that set, we then define a new variable **campus** that holds a reference to the geodatabase that contains all of our data layers from campus.
>
```python
# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb"
```
>
Now we can use the build-in method **input()** to require two values from the user: the number of the building they are looking for and the radius size of the buffer. We will need to be sure to cast the buffer input to an integer. Due to the way TAMU numbers their buildings, we can leave that as a string.
>
```python
# Setup our user input variables
buildingNumber_input = input("Please enter a building number: ")
bufferSize_input = int(input("Please enter a buffer size: "))
```
>
Now that we have a building number and a buffer radius, we can now check to make sure the building number the user provided is valid.
## Check for data
The first thing needed in order to check if the building exists or not within the **/Structures** feature class is to define a new variable **where_clause**. This variable is a simple SQL statement that we'll use to return those values in **/Structures** that match the provided building number.
>
```python
# Generate our where_clause
where_clause = "Bldg = '%s'" % buildingNumber_input
```
>
In this case, **where_clause** is a formated string which allows us to input a variable inside the string without opening and closing several quotations. It simply replaces the **%s** with the value of variable **buildingNumber_input**. This part is not required, we could have used quotes instead like we have many times before, but string formatting like this is the way that fancy programmers do it. Congrats, you are now a fancy programmer.
>
With our **where_clause** set, we then use the method **SearchCursor()** to search for our building. This method takes two parameters: an input layer and a where clause. 
>
```python
# Check if building exists
structures = campus + "/Structures"
cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
shouldProceed = False
```
>
We put in the path to our **Structures** layer that contains ALL buildings on campus as our input layer and our **where_clause** variable as the where_clause parameter. The cursor should query our input layer for all values that satisfy the where clause. We then create a variable that contains a boolean value that will determine if the building was found or not.
>
To determine if we should proceed or not, we use a for loop to iterate through the results of **SearchCursor()**. If a row in the cursor contains a row who's value for field **Bldg** equals that of our **buildingNumber_input**, then we set **shouldProceed** equal to True.
>
```python
for row in cursor:
    if row.getValue("Bldg") == buildingNumber_input:
        shouldProceed = True
```
>
## Operations
Now we need to finish the rest of our tool. We first need to check that we can proceed. We use an if statement to determine if we should continue working.
>
```python
# If we shouldProceed do so
if shouldProceed:
    # ...
else:
    print("Seems we couldn't find the building you entered")
```
>
Inside the if statement, we need to setup two new variables that will make our lives a little easier: one that generates a new layer name for our buffer layer and one that grabs a reference to our building from the **/Structures** layer. To get a reference to a specific building in **/Structures**, we use the **Select_analysis()** tool. It is important to use the same **where_clause** variable we created earlier when using **Select_analysis()**, or you may end up with a reference to something other than the building the user has specified.
>
```python
# Generate the name for our output buffer layer
buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferSize_input)
# Get reference to building
buildingFeature = arcpy.Select_analysis(structures, campus + "/building_%s" % (buildingNumber_input), where_clause)
```
>
The names we create are dynamic in that each feature class will have the building number in the name as to prevent trying to create a buffer layer when one exists already. With our names and references set, we can now move onto the important steps of buffering and clipping. The first step is to buffer our building with the buffer radius provided by the user. The output layer of the buffer operation will be named whatever the value of **buildingBuff** is. Now that we have the buffer, we can clip the **/Structures** layer using the buffer as a clip feature.
>
```python
# Buffer the selected building
arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
# Clip the structures to our buffered feature
arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
# Remove the feature class we just created
arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input))
```
>
And that's it! We can incorporate one more line that does a little house keeping for us by removing our buffer layer. This layer isn't really needed once the clip has been performed so we remove it to keep our geodatabase tidy. Be careful when using the **Delete_management()** method as it will not prompt you with any sort of warnings: it will remove anything without question.
>
![Finished](../images/modules/18/finished.png)
>
# <p>ourtool.py</p>
>
```python
import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"

# Define our geodatabase
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/17/Campus.gdb"

# Setup our user input variables
buildingNumber_input = input("Please enter a building number: ")
bufferSize_input = int(input("Please enter a buffer size: "))

# Generate our where_clause
where_clause = "Bldg = '%s'" % buildingNumber_input

# Check if building exists
structures = campus + "/Structures"
cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
shouldProceed = False

for row in cursor:
    if row.getValue("Bldg") == buildingNumber_input:
        shouldProceed = True

# If we shouldProceed do so
if shouldProceed:
    # Generate the name for our generated buffer layer
    buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferSize_input)
    # Get reference to building
    buildingFeature = arcpy.Select_analysis(structures, campus + "/building_%s" % (buildingNumber_input), where_clause)
    # Buffer the selected building
    arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
    # Clip the structures to our buffered feature
    arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
    # Remove the feature class we just created
    arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input))
    
else:
    print("Seems we couldn't find the building you entered")
```
>
# Additional resources
- http://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/a-quick-tour-of-python-toolboxes.htm
- http://pro.arcgis.com/en/pro-app/arcpy/geoprocessing_and_python/a-template-for-python-toolboxes.htm

## Videos
[Module5-Topic2](https://youtu.be/rI4hhA9G_o0)
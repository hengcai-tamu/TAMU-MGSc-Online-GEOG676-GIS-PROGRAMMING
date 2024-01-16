# TODO:

## 01
- Difference between automation, customization, and extension
  - fixed

## 02
- Use  your enterprise account to log into Esri
  - fixed
- Replace arcgis pro download link with google drive link. 
  - fixed
- Add enterprise login steps/screens

## 03
 - Error
    - Means that you have not opened arcgis pro and signed into ArcGIS
pro/tamu.maps.arcgis.com
```
PS C:\DevSource\GEOG676> & python c:/DevSource/GEOG676/topic/01/test.py
Traceback (most recent call last):
  File "c:/DevSource/GEOG676/topic/01/test.py", line 1, in <module>
    import arcpy
  File "C:\Program
Files\ArcGIS\Pro\Resources\ArcPy\arcpy\__init__.py", line 66, in
<module>
    from arcpy.geoprocessing import gp
  File "C:\Program
Files\ArcGIS\Pro\Resources\ArcPy\arcpy\geoprocessing\__init__.py",
line 14, in <module>
    from ._base import *
  File "C:\Program
Files\ArcGIS\Pro\Resources\ArcPy\arcpy\geoprocessing\_base.py", line
14, in <module>
    import arcgisscripting
RuntimeError: Not signed into Portal.
```
  - added to errors


 - ArcPy version of python does not show in the list in VSCode even
after updating the env variable? - is this good or bad?
 - You do not have to pick the ArcPy version of python (if it doesn't show)
 
 -Can not edit the env variable on GEOSAD comps or VOAL.  Ran setting setting.json.  Seems to work, but still need to login.

 ## 05
 - Name of lecture does not match Variable stuff & operators. Make them separate from conditionals/loops. Only one thing per section.

 ## 06
 - Seems short for scope. Some examples would be helpful

 ## 07
 - Show final output

 ## 08
 - Some screenshots of it waiting at the terminal/showing output would be good.

 # 2018-06-06
05__1.md
- add more examples: count += 1, -=, ++, --
  - fixed


05__2.md
- remove - print(x < y and x != y) # True, since both expressions are true - duplicate 
  - Not sure why?
- change title to opertaors
  - Done
- add examples of stringing together a series of nested operators
  


05__3.md
- Move nested loop to end
  - Fixed
- Add an example with a lot of elif's
  - Fixed


05__4.md
- add a counter example to the while loop about why they would have to keep track of a counter variable and what can happen
  - Fixed
- add small video talking about why and how a counter variable can go wrong
  - Fixed



06.md
- Add more arguments in list of parameters as the example.
  - Huh?

07.md
- Why is c a parameter? It is just getting overwritten
  - I think it makes it a little easier for beginners to read with a variable to use instead of printing (a + b) everytime. 
- print_vertically is never called, in "The whole thing vertically"
  - I think you fixed this
- Why is count always hard coded to 3? It's always starting at the 3rd one, since first and second = 1 & 2
  - Added an explanation in the lecture
- Add line break between while loop and pring array
  - Not necessary but I did (I'm assuming within print_horizontally())


08.md
 - Learning objective should be more descriptive - Use loops, variables, and conditionals to create a calculator application
  - Fixed
 - Add example output/use (screenshot)
  - Fixed
 - add iterator controls (break/continue, etc.)
  - Fixed


 # 2018-06-12

09 - slash explanation needed

11 - 

Class Truck (Attributes section - might fail since no blank constructor, double check)


12 - Remame links in TOCs to be "Built In Functions" instead of "Advanced Functions"
 - Verify if int() truncates or rounds

# 2018-06-22

13. - Diff of list - make sure those values are correct, there are some things in list two that are not shown

15. - should EOFError be IOError instead?

16. 
- Include complete code
- Add screenshot of where the tool python documentation is located. Bottom of each Esri tool page
 -- http://pro.arcgis.com/en/pro-app/tool-reference/data-management/create-file-gdb.htm

 17.
 - ~~Add images for each type of operation~~

 18. 
  - If we are going to use string formatting, we need a lecture about this, way earlier in the semester. Add now and we we throw in where we can.
  - ~~Need to have a separate lecture on cursors (search, update, etc.)~~
  - ~~Should have picture of the process/output happening~~


22.
- Top function (lambda) - should be isOdd, not isEven since the function def (full one) will return false for even numbers
- Add the full loop versions for map/reduce/filter to show how they are longer and different.

# 2018-06-27

21. 
 - Add example of how you would create your own package (using a path)

 # 2018-07-01

23. 
 - UniqueValue renderer - Add in description of what each color is showing, or at least show the legend along with the map. Also confusing why you are calling the graduated colors one a choropleth, weirdly specifically, and not this one.
 - GraduatedColorsRenderer - Is project.listColorRamps('Oranges') predefined or did you hav to create that in order to use it in the code?

  # 2018-07-03

25. 
 - Provide screenshots (or code blocks) and links to the full json and geojson files that you use in the examples. 

28.
- Add the landsat data to somewhere that is not Aaron's google drive - Canvas, etc.

# Additional Lectures:

1. ~~Exception Handling~~

2. Pretty Printing: return "Point3D(%d, %d, %d)" % (self.x, self.y, self.z)

3. Built in functions for objects that you can (and maybe should) override

4. Slice notation - https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation
``` python
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
```

5. ArcGIS for Python

6. Python API for ArcGIS

7. numpy

8. scipy

8b. Lecture on debugging

9. Using ArcGISPro "Record Python" -> record common actions, run them as script.

10. Packaging and distributing your code (with licensing [aka as an extension])

11. [Data science / visualizations](https://medium.com/activewizards-machine-learning-company/top-15-python-libraries-for-data-science-in-in-2017-ab61b4f9b4a7)

12. Never using ArcGIS again - Python has it all already, you just have to put it together - numPy + sciPy + [pySal](http://pysal.readthedocs.io/en/latest/developers/index.html) 

13. SQL connections (Was attempted, but is needlessly complicated and documentation sucks. Also I couldn't add a connection to our registered dbs through the GUI; maybe a license issue)




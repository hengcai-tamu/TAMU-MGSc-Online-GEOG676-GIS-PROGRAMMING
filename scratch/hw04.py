
import arcpy
arcpy.env.workspace = "C:/tmp/ArcGISPython"

# Set the gdb 
campus = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/homework/04/Campus.gdb"

# Input layers
garage = campus + "/GaragePoints"
buildings = campus + "/Structures"
garageBuffered = campus + "/GaragePoints_buffered"

# Buffer the garage
# garageBuffered = arcpy.Buffer_analysis(garage, campus + "/GaragePoints_buffered", 150)

# Intersect our buffer with the buildings
# arcpy.Intersect_analysis([garageBuffered, buildings], campus + "/garageBuildingIntersection", "ALL")

arcpy.TableToTable_conversion(campus + "/garageBuildingIntersection.dbf", "C:/tmp/ArcGISPython", "nearbyBuildings.csv")


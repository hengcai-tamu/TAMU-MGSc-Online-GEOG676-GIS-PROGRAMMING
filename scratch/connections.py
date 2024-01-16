import arcpy

#arcpy.ArcSDESQLExecute("gpserver3","5151","#","toolbox","toolbox")

# gdb_conn = arcpy.ArcSDESQLExecute(None, "geodb08.tamu.edu", "ArcMapRegisteredDatabase", "atharmon", "Paincakes14")
gdb_conn = arcpy.ArcSDESQLExecute("geodb08.tamu.edu", "5151", None, "atharmon", "Paincakes14")
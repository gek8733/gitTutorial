#-------------------------------------------------------------------------------
# Name:        Project1
#
# Author:      Grace
#
# Created:     25/02/2017
#-------------------------------------------------------------------------------

import arcpy
from arcpy import env

#Import csv file into a table in a geodatabase using Copy Rows
env.workspace = r"C:\Users\Grace\Documents\SLU\Prog for GIS"
JanOutput = r"C:\Users\Grace\Documents\SLU\Prog for GIS\Project1_Output\Project1_Output.gdb\January2017"
JanInput = r"C:\Users\Grace\Documents\SLU\Prog for GIS\January2017.csv"
arcpy.CopyRows_management(JanInput, JanOutput)
print "...CSV Imported..."

#Make XY Event Layer from the table
JanInput = r"C:\Users\Grace\Documents\SLU\Prog for GIS\Project1_Output\Project1_Output.gdb\January2017"
JanOutput = r"C:\Users\Grace\Documents\SLU\Prog for GIS\Project1_Output\Project1_Output.gdb\JanuaryPoints"
arcpy.MakeXYEventLayer_management(JanInput, "XCoord", "YCoord", JanOutput)
print "...Event Layer Made...."

#Convert XY Event layer to a feature class using Feature Class to Feature Class
JanInput = r"C:\Users\Grace\Documents\SLU\Prog for GIS\Project1_Output\Project1_Output.gdb\JanuaryPoints"
JanOutputPath = r"C:\Users\Grace\Documents\SLU\Prog for GIS\Project1_Output\Project1_Output.gdb"
arcpy.FeatureClassToFeatureClass_conversion(JanInput, JanOutputPath, "JanuaryPoints")
print "...Feature Class Made..."

#Define the Projection on the feature class you created
input_feature = r"C:\Users\Grace\Documents\SLU\Prog for GIS\Project1_Output\Project1_Output.gdb\JanuaryPoints"
output_feature = r"C:\Users\Grace\Documents\SLU\Prog for GIS\Project1_Output\Project1_Output.gdb\JanuaryPoints_Project"
out_coordinate_system = arcpy.SpatialReference('NAD 1983 StatePlane Missouri East FIPS 2401 (US Feet)')
arcpy.Project_management(input_feature,output_feature,out_coordinate_system)
print "...Projection Defined..."

print "Project Complete"
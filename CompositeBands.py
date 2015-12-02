import arcpy
from arcpy import env
env.workspace = "E:/Python/Project/Bulk Order 581575/L8 OLI_TIRS/theglovis.tar/theglovisone"
arcpy.CompositeBands_management("B1.TIF; B2.TIF; B3.TIF; B4.TIF; B5.TIF; B6.TIF; B7.TIF; B8.TIF; B9.TIF; B10.TIF; B11.TIF", "compositedtheglovisone.TIF")

import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "E:/Remote Sensing/Project"
inRaster = "compositedtheglovisone.TIF"
inMaskData = "SquareBoundary.shp"
arcpy.CheckOutExtension("Spatial")
outExtractByMask = ExtractByMask(inRaster, inMaskData)
outExtractByMask.save("E:/Remote Sensing/Project/extractmask.TIF")
# outExtractByMask = ExtractByMask("compositedtheglovisone.TIF", "SquareBoundary.shp")
# outExtractByMask.save("E:/Remote Sensing/Project/maskextract")

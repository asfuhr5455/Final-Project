import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = "E:/Remote Sensing/Project"

inRaster = "extractmask.TIF"
classes = 6
minMembers = 20
sampInterval = 10

arcpy.CheckOutExtension("Spatial")

outUnsupervised = IsoClusterUnsupervisedClassification(inRaster, classes, minMembers, sampInterval)
outUnsupervised.save("E:/Remote Sensing/Project/extractMaskUnSup6.TIF")

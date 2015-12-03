# Composite Bands

import arcpy
from arcpy import env
env.workspace = input('Enter env.workspace as string: ')
if env.workspace == "Done":
    pass
else:
    bands = input('Put bands to be composited in order as a string separated by a semicolon: ')
    output = input('Enter what you would like the ouptut value to be called as a sting, it will not save if name is too long: ')
    arcpy.CompositeBands_management(bands, output)
    print 'completed composite bands'
# env.workspace = "E:/Python/Project/Bulk Order 581575/L8 OLI_TIRS/theglovis.tar/theglovisone"
# arcpy.CompositeBands_management("B1.TIF; B2.TIF; B3.TIF; B4.TIF; B5.TIF; B6.TIF; B7.TIF; B8.TIF; B9.TIF; B10.TIF; B11.TIF", "compositedtheglovisone.TIF")

# Extract By Mask

import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = input('Enter env.workspace as stringfor Extract By Mask: ')
inRaster = input('Type main landsat image or other as string: ')
inMaskData = input('Type the boundary to clip from main image as string: ')
arcpy.CheckOutExtension("Spatial")
outExtractByMask = ExtractByMask(inRaster, inMaskData)
save_spot = input('Type place to save as a string with the .filetype: ')
outExtractByMask.save(save_spot)
print 'completed extract by mask'
# env.workspace = "E:/Remote Sensing/Project"
# inRaster = "compositedtheglovisone.TIF"
# inMaskData = "SquareBoundary.shp"
# outExtractByMask.save("E:/Remote Sensing/Project/extractmask.TIF")
# outExtractByMask = ExtractByMask("compositedtheglovisone.TIF", "SquareBoundary.shp")
# outExtractByMask.save("E:/Remote Sensing/Project/maskextract")

# Unsupervised Classification

import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = input('Enter env.workspace as string for Unsupervised Classification: ')

#env.workspace = "E:/Remote Sensing/Project"

inRasteru = input('Type main landsat image or other as string: ')
classes = input('Type how many classes you would like as a string: ')
minMembers = input('Type min members as string, default is 20 usually: ')
sampInterval = input('Type the sampal interval, default is usually 10: ')
# inRaster = "extractmask.TIF"
# classes = 6
# minMembers = 20
# sampInterval = 10

arcpy.CheckOutExtension("Spatial")

outUnsupervised = IsoClusterUnsupervisedClassification(inRasteru, classes, minMembers, sampInterval)
savespotuc = input('Where would you like to save (type as string with .file type): ')
outUnsupervised.save(savespotuc)
print 'completed Unsupervised Classification'
# outUnsupervised.save("E:/Remote Sensing/Project/extractMaskUnSup6.TIF")


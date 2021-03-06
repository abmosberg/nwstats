from fieldArray import FieldArray
from metaReader import get_pixel_size

path = 'data/images/main/png_steinar'
prep_path = 'data/images/main/prep'

scale = get_pixel_size('data/images/main/originals/Topdown_immersion_5kV86pA_Array_001.tif')
#Original scale is 4.8 nm per pixel. Processing is done on compressed (scaled) images, down to 1024 from 4096 px wide.
# So new scale should be 4x original scale.

# fields = FieldArray(8, 8, 15, 18, path, 4.8, '.png')
# fields = FieldArray(8, 8, 15, 18, path, scale*4, '.png')
fields = FieldArray(8, 8, 15, 18, prep_path, scale*4, '.png')
# fields = fields.prepFields(kernel_size=3, prep_path=prep_path)
# fld = fields.fields[0]
# fields.detectBlobs()
# fld.detectBlobs()
# fld.makeLattice()
# fld.lattice=loadLattice('D:/Dropbox/PhD/People/Steinar/Steinar_ImageRecognition_170516/data/lattices/main_001.p')
# fld.plotBlobs()
# fld.plotLattice()

fields.ensureBlobsByPoint()

# fields.detectBlobs()
# fields.ensureLattices()
# fields.readjustLattices()
# fields.plotLattices()

# fields.plotBlobs()

# fields.makeLattices()

# fields.plotLatticesWithBlobs()
# fields.plotYield(5)
# fields.plotYield(1)
# fields.plotMeanDiameters({'title': 'Mean droplet diameter'})
fields.plotMeanDiameters()
# fields.plotDiameterHistograms()
# fields.plotFancyDiameterHistogram()
# fields.plotDisplacementScatterPlots()
# fields.plotSingleScatterPlot(55)

# fields.fields[54].plotLikeTiles()
# fields.plotWithConnects(6)
# fields.plotWithConnects(56)
# fields.plotAllYields()

# doses = ds.doses_sorted()
# pos = ds.dose_argsort()

# diam = fields.getMedianDiameters()
# diam_s = [diam[i] for i in pos]

# plt.plot(doses,diam_s)

blobs = [fld.getBlobCount() for fld in fields.fields]
from fieldArray import FieldArray
from metaReader import get_pixel_size

path = 'data/images/main/png'
prep_path = 'data/images/main/prep'

scale = get_pixel_size('data/images/main/originals/Topdown_immersion_5kV86pA_Array_001.tif')


fields = FieldArray(8, 8, 15, 18, path, 4.8, '.png')
fields = fields.prepFields(kernel_size=3, prep_path=prep_path)

# fields.makeLattices()
#
# fields.plotLatticesWithBlobs()
# fields.plotYield(1)
# fields.plotYield(2)
# fields.plotMeanDiameters({'title': 'Mean droplet diameter'})
# fields.plotDiameterHistograms()
# fields.plotFancyDiameterHistogram()
# fields.plotDisplacementScatterPlots()


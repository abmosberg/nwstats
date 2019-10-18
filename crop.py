import numpy as np
from imageio import imread, imwrite
from glob import glob
from skimage import img_as_ubyte

def crop_array_FEI(folderpath, savepath):
    """
    Crops the databar out of FEI images and saves to lossless compressed png while maintaining metadata
    :param folderpath (string): folder string to search for .tif images in
    :param savepath (string): folder string to save .png images in
    :return:
    """
    fl = glob(f"{folderpath}/*.tif")

    print(fl)

    for f in fl:
        im = imread(f)
        im = img_as_ubyte(im)
        savename = f'{savepath}/{f[-13:-4]}.png'
        imwrite(savename, im[:3536,:])
        print(f"Saved {f[-13:-4]}")
        # del im

# for n in range(1, 65):
#     input_image = '../data/images/main/sideviews_2/' + str(n).zfill(3) + '.tif'
#
#     original_image = imread(input_image)
#
#     image = original_image[120:-240, :]
#     # ret, image = cv2.threshold(original_image, 150, 255, 0)
#
#     imwrite('../data/images/main/cs2/' + str(n).zfill(3) + '.tif', image)
#
#     print('Saved image ' + str(n).zfill(3))

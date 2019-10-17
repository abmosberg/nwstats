from imageio import imread


def get_pixel_size(filepath):
    """
    Utility function to read metadata from FEI .tif images and return the pixel width in nm

    :param filepath: Path to .tif image
    :return: scale (float): Pixel size of image in nm
    """

    im = imread(filepath, format='FEI')
    meta = im.meta
    return meta['EScan']['PixelWidth'] * 10 ** 9

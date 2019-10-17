from PIL import Image

def get_pixel_size(filepath):
    """
    Utility function to read metadata from FEI .tif images and return the pixel width in nm

    :param filepath: Path to .tif image
    :return: scale (float): Pixel size of image in nm
    """

    metastr = Image.open(filepath).tag[34682][0]
    meta = {}
    for cat in metastr.split('[')[1:]:
        meta[cat[:cat.find("]")]] = dict([x.split("=") for x in cat[cat.find("]") + 1:].split('\r\n') if x])

    scale = float(meta['EScan']['PixelWidth'])*10**9
    return scale
#!/usr/bin/env python3
import sys

try:
    from PIL import Image
except ImportError:
    print("Please install Pillow from: https://pypi.python.org/pypi/Pillow/3.0.0")
    sys.exit(1)


def watermark_with_transparency(input_image_path,
                                watermark_image_path):
    base_image = Image.open(input_image_path)

    if (base_image.size[0] < base_image.size[1]):
        base_image = base_image.rotate(-90, expand=True)

    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    # resize logo
    wsize = int(min(base_image.size[0], base_image.size[1]) * 0.20)
    wpercent = (wsize / float(watermark.size[0]))
    hsize = int((float(watermark.size[1]) * float(wpercent)))
    simage = watermark.thumbnail((wsize, hsize), Image.ANTIALIAS)
    simage = watermark.resize((wsize, hsize))
    mbox = base_image.getbbox()
    sbox = simage.getbbox()

    # right bottom corner
    box = (mbox[2] - sbox[2], mbox[3] - sbox[3])
    transparent.paste(watermark, box, mask=watermark)
    rgb_im = transparent.convert('RGB')
    return rgb_im

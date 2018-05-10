#!/usr/bin/env python3
import os
import sys
import traceback

try:
    from PIL import Image, ExifTags
except ImportError:
    print("Please install Pillow from: https://pypi.python.org/pypi/Pillow/3.0.0")
    sys.exit(1)


def watermark_with_transparency(input_image_path, watermark_image_path):
    base_image = Image.open(input_image_path)

    if hasattr(base_image, '_getexif'):
        orientation = 0x0112
        print(orientation)
        exif = base_image._getexif()
        if exif is not None:
            orientation = exif[orientation]
            rotations = {
                3: Image.ROTATE_180,
                6: Image.ROTATE_270,
                8: Image.ROTATE_90
            }
            if orientation in rotations:
                base_image = base_image.transpose(rotations[orientation])
    base_image.save(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    # resize logo
    wsize = int(min(base_image.size[0], base_image.size[1]) * 0.20)
    wpercent = (wsize / float(watermark.size[0]))
    hsize = int((float(watermark.size[1]) * float(wpercent)))
    simage = watermark.resize((wsize, hsize))
    mbox = base_image.getbbox()
    sbox = simage.getbbox()

    # right bottom corner
    box = (mbox[2] - sbox[2], mbox[3] - sbox[3])
    transparent.paste(watermark, box, mask=watermark)
    rgb_im = transparent.convert('RGB')
    return rgb_im

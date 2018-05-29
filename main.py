from paster import watermark_with_transparency
import re, sys


def beginPasting(dirPath, logoPath):
    import os
    for fn in os.listdir(dirPath):
        if fn.endswith(".jpg") or fn.endswith(".JPG"):
            fName = re.split("\.", fn)
            print(fName)
            new = watermark_with_transparency(dirPath + fn, logoPath)
            new.save("newImages/" + fName[0] + "_logo." + fName[1])


if len(sys.argv) >= 3:
    images, logo = sys.argv[1], sys.argv[1]
else:
    images, logo = "./images/", "./logos/ip9.png"
print(images,logo)
beginPasting(images, logo)

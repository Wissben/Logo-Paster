from paster import watermark_with_transparency
import re

def beginPasting(dirPath,logoPath) :
    import os
    for fn in os.listdir(dirPath):
        if os.path.isfile(fn) and fn.endswith(".JPG"):
            fName = re.split("\.",fn)
            print(fName)
            new  = watermark_with_transparency(fn,logoPath)
            new.save("newImages/"+fName[0]+"_logo."+fName[1])


beginPasting(".","./logos/ip9.png")
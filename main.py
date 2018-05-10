from paster import watermark_with_transparency
import re

def beginPasting(dirPath,logoPath) :
    import os
    for fn in os.listdir(dirPath):
        if fn.endswith(".JPG"):
            print(fn)
            fName = re.split("\.",fn)
            print(fName)
            new  = watermark_with_transparency(dirPath+fn,logoPath)
            new.save("newImages/"+fName[0]+"_logo."+fName[1])


beginPasting("./images/","./logos/ip9.png")
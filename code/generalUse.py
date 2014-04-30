from os import path
from psychopy import gui
from PIL import Image, ImageFilter

gaussBlur = ImageFilter.GaussianBlur(radius=100)


filenames = gui.fileOpenDlg(allowed="*.*")
for fileN, thisFilename in enumerate(filenames):
    #print thisFilename
    fileNoExt, fileExt = path.splitext(thisFilename)
    folder, filenameAndExt = path.split(thisFilename)
    
    outName = "%s/face%03i.jpg" %(folder, fileN)
    blurName = "%s/face%03i_blur.jpg" %(folder, fileN)
    
    thisImg = Image.open(thisFilename)
    #thisImg.save(fileNoExt+'NEW.jpg')
    filtered = thisImg.filter(gaussBlur)
    
    thisImg.save(outName)
    filtered.save(blurName) 
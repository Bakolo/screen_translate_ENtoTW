from PIL import Image
import pytesseract as tsr
import time


def func_time(func):
    def fTime(*args, **kargs):
        ts = time.time()
        ret = func(*args, **kargs)
        te = time.time()
        print(f"==>tool time: {te-ts}sec")
        return ret
    return fTime

@func_time
def read(img_path):
    img = Image.open(img_path)
    text = tsr.image_to_string(img, lang="eng") 
    print(text)

#@func_time
def read_image(img_in):
    text = tsr.image_to_string(img_in, lang="eng") 
    return text



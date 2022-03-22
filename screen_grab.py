from PIL import ImageGrab as IG

def screen_grab(x=0, y=0, w=800, h=600):
#Bbox used to capture a specific area
    screen = IG.grab(bbox=(x,y,w,h))
#make grayscale
#w = screen.convert('L')
#w.save(temp.png)

#    screen.save('temp.png')
    return screen



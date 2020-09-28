from PIL import Image

img = Image.open("aditi.png")
win = image.ImageWin(img.getWidth(),img.getHeight())
img.draw(win)
img.delay(15)
for row in range(img.getHeight):
	for col in range(img.getWidth):
		p=img.getPixel(col,row)
		newred=255-p.getRed()
		newgreen=255-p.getGreen()
		newblue=255-p.getBlue()
		newPixel=image.Pixel(newred,newgreen,newblue)
		img.setPixel(col,row,newPixel)
img.draw(win)
win.exitonclick()
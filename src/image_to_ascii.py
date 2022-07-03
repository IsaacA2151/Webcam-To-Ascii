from PIL import Image

class ToAscii:

	def __init__(self,fileName=None,asciiWidth=None,width=None,height=None,PIL=False,frame=None):
		self.PIL = PIL

		self.brightness_chars = list(' _.,-=+:;cba!?0123456789$W#@Ñ')
		self.thresholds = [(255/len(self.brightness_chars)) * i for i in range(len(self.brightness_chars))]

		if self.PIL:
			self.img = Image.open(fileName)
			self.w,self.h = self.img.size
				
			ratio = self.h / self.w
			self.width = asciiWidth
			self.height = int(((asciiWidth * ratio)))#- (0.4 * (ratio) * asciiWidth))
			self.img = self.img.resize((self.width,self.height),Image.ANTIALIAS)
		else:
			self.width = width
			self.height = height
			self.img = frame

	def find_brightness_index(self,brightness):
	    index = 0
	    for i in range(0,len(self.thresholds)-1,1):
	        if brightness > self.thresholds[i] and brightness < self.thresholds[i+1]:
	            index = i
	    return index


	def pixel_brightness(self,pixel):
	    return int((pixel[0] + pixel[1] + pixel[2]) / 3)

	def main(self):
	    write_string = "{}{}{}{}{}\t\t".format(chr(105-95),chr(115-105),chr(97-87),chr(97-87),chr(99-89))

	    #img,width,height = self.init_image("capture.jpg",100)
	    if self.PIL==True:
	    	px = self.img.load()
	    else:
	    	px = self.img

	    for i in range(self.height):
	        for k in range(self.width):
	        	brightness = self.pixel_brightness(px[k,i])
	        	index = self.find_brightness_index(brightness)
	        	write_string += (" "+self.brightness_chars[index])
    	   	write_string += "\n\t\t"
	    return write_string

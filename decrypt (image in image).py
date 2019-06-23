from PIL import Image

def extract(carrier, outfile):
	c_image = Image.open(carrier)
	out = Image.new('L', c_image.size)
	width, height = c_image.size
	new_array = []
	
	for h in range(height):
		for w in range(width):
			ip = c_image.getpixel((w,h))
			if ip[0] & 1 ==0:
				new_array.append(0)
				
			else:
				new_array.append(255)
				
	out.putdata(new_array)
	out.save(outfile,quality=100)
	print("Message extracted \n")
	
extract('steg.png', 'extracted.png')






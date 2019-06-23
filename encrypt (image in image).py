from PIL import Image

def hide_message(carrier, message, outfile):

    c_image = Image.open(carrier)
    hide = Image.open(message)
    hide = hide.resize(c_image.size, Image.ANTIALIAS)
    hide = hide.convert('1')
    out = Image.new('RGB', c_image.size)
        
    width, height = c_image.size
    new_array = []
        
    for h in range(height):
        for w in range(width):
            ip = c_image.getpixel((w,h))
            hp = hide.getpixel((w,h))
            if hp == 0:
                newred = ip[0] & 254
            else:
                newred = ip[0] | 1
            new_array.append((newred, ip[1], ip[2]))
                
    out.putdata(new_array)
    out.save(outfile, quality =100)
    print("Steg image save to " +outfile +".")

hide_message('carrier.png', 'flowers.png', 'steg.png')








            

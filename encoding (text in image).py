from PIL import Image

def Set_LSB(value, bit):
    if bit =='0':
        value = value & 254
    else:
        value = value | 1
    return value

def Hide_message(carrier, message, outfile):
    message += chr(0)
    c_image  = Image.open(carrier).convert('RGBA')
    out = Image.new('RGBA', c_image.size)
        
    pixel_list = list(c_image.getdata())
    new_array = []
        
    for i in range(len(message)):
        char_int = ord(message[i])
        cb = str(bin(char_int)) [2:].zfill(8)
        pix1 = pixel_list[i*2]
        pix2 = pixel_list[(i*2)+1]
        newpix1 = []
        newpix2 = []
            
        for j in range(0,4):
            newpix1.append(Set_LSB(pix1[j], cb[j]))
            newpix2.append(Set_LSB(pix2[j], cb[j+4]))
                
        new_array.append(tuple(newpix1))
        new_array.append(tuple(newpix2))
            
    new_array.extend(pixel_list[len(message)*2 :])
    out.putdata(new_array)
    out.save(outfile)
    print("Steg image saved.\n")
        
Hide_message('cats.png', 'Innotech2k17.', 'messagehidden.png')


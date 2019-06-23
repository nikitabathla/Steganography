from PIL import Image

def get_pixel_pairs(iterable):
    a = iter(iterable)
    return zip(a,a)
    
def get_LSB(value):
    if value & 1 == 0:
        return '0'
    else:
        return '1'
        
def extract_message(carrier):
    c_image = Image.open(carrier).convert('RGBA')
    pixel_list = list(c_image.getdata())
    message = ""
    
    for pix1, pix2 in get_pixel_pairs(pixel_list):
        message_byte = "0b"
        for p in pix1:
            message_byte += get_LSB(p)
        for p in pix2:
            message_byte += get_LSB(p)
            
        if message_byte == "0b00000000":
            break
        message += chr(int(message_byte,2))
    return message 

print(extract_message('messagehidden.png'))








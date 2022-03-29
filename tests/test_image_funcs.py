from PIL import Image
brightness_chars = list(' _.,-=+:;cba!?0123456789$W#@Ñ')


thresholds = [(255/len(brightness_chars)) * i for i in range(len(brightness_chars))]

def init_image(file,new_width):
    img = Image.open(file)
    width,height = img.size

    new_height = int(new_width * height / width)
    img = img.resize((new_width,new_height),Image.ANTIALIAS)

    return img,new_width,new_height


def find_brightness_index(brightness):
    index = 0
    for i in range(0,len(thresholds)-1,1):
        if brightness > thresholds[i] and brightness < thresholds[i+1]:
            index = i
    return index


def pixel_brightness(pixel):
    return int((pixel[0] + pixel[1] + pixel[2]) / 3)


def main():
    f = open("ascii_image.txt","w+")
    write_string = ""

    img,width,height = init_image("capture.jpg",100)
    px = img.load()

    for i in range(height):
        for k in range(width):
            brightness = pixel_brightness(px[k,i])
            index = find_brightness_index(brightness)
            write_string += brightness_chars[index]
        write_string += "\n"

    f.write(write_string)    

main()

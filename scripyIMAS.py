import PIL.Image
from PIL import Image

ASCII_CHARS = ["@","#","$","%","&","*","+","=","-","."," "]

def resize_image(image, new_width=150):
    width, height = image.size
    ratio = height / width /1.6
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)

def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)

def convASCI (image):
    pixels = image.getdata()
    char = "".join([ASCII_CHARS[pixel//20] for pixel in pixels])
    return (char)
    

def main(new_width = 150):
    #path = r"C:\Users\Nikol Ladanev\Documents\code\testimages\11.png"
    path = input("Enter the path:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "not valid")
        
    new_image_data = convASCI(grayify(resize_image(image)))
    
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
        
        
        #print result
    print(ascii_image)
    
    with open("ascii_image.txt","w") as f:
        f.write(ascii_image)
    
main()
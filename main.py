from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()


coordinates = (50, 0, red.width, red.height)  
cropped_left = red.crop(coordinates)

new_image = Image.open("image.jpg")
coordinates = (25, 0, red.width-25, red.height) 
cropped_middle = red.crop(coordinates) 

blended_image = Image.blend(cropped_middle, cropped_left, 0.5)


coordinates = (0, 0, blue.width-50, blue.height)  
cropped_right = blue.crop(coordinates) 

new_image = Image.open("image.jpg")
coordinates = (25, 0, blue.width-25, blue.height) 
crop_middle = blue.crop(coordinates) 

blended_image_middle_right = Image.blend(crop_middle, cropped_right, 0.5)


coordinates = (25, 0, green.width-25, green.height)  
cropped_right_left = green.crop(coordinates)


new_image = Image.merge("RGB", (blended_image, cropped_right_left, blended_image_middle_right))
new_image.save("new.jpg")
new_image.thumbnail((80, 80)) 
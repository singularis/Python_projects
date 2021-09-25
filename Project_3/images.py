from PIL import Image, ImageFilter

img = Image.open('./Images/(Follower of) Agnolo Gaddi, Italian, active Florence, 1369 - d. Florence, 1396.jpg')

filtered_image = img.convert('L')

crooked_images = filtered_image.rotate(180)
print(img.size)
img.thumbnail((400,400))
img.show()
print(img.size)
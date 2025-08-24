from PIL import Image
from rembg import remove

src_image = Image.open('photo.jpg')
dst_image = remove(src_image)
dst_image.save("rm_photo.png")
print("Background Remove Complete")
from rembg import remove
from PIL import Image

output_path = 'rembg.png'
input = Image.open("removebg.jpg")
output = remove(input)
output.save(output_path)


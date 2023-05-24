from rembg import remove
from PIL import Image

input_path = 'picture.png'
output_path = 'rembg.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)


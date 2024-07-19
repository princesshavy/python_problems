from rembg import remove 
from PIL import Image
input_path = 'dolphin.jpg'
output_path = 'dolphin_output.png'
inp = Image.open(input_path)
output = remove(inp) 
output.save(output_path)
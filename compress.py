from PIL import Image
import PIL
import os
import glob

# Get imgs in img/original directory
path_origin = os.path.abspath('./img/original')
path_compressed = os.path.abspath('./img/compressed')

imgs = glob.glob(os.path.join(path_origin, '*.png'))

for img in imgs:
    picture = Image.open(img)
    dim = picture.size

    file_name = os.path.basename(img)
    compressed_file_name = file_name.replace('.', '-comp.')

    compressed_file_path = os.path.join(path_compressed, compressed_file_name)
    picture.save(compressed_file_path, optimize=True, quality=20)
    print(f"Compressed file: {file_name}")

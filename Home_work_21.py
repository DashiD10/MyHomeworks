from PIL import Image
from pillow_heif import register_heif_opener, from_pillow as heif_from_pillow

import pillow_avif 



sauna = r"C:\Users\Admin\Pictures\1\sauna.jpg"

register_heif_opener()

source_image = Image.open(sauna)

source_image.save("output.webp", format="WEBP", quality=40)


heif_file = heif_from_pillow(source_image)
heif_file.save("output.heic", quality=40)
source_image.save("output.avif", quality=45)

from PIL import Image
from pillow_heif import register_heif_opener, from_pillow as heif_from_pillow

import pillow_avif 
import os

sauna = r"C:\Users\Admin\Pictures\1\sauna.jpg"

register_heif_opener()

ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png", "dng"]

source_path = r"C:\Users\Admin\Desktop\Academy TOP\MyHomeworks"

# files = os.listdir(source_path)
# for file in files:
#     full_path = os.path.join(source_path, file)
#     if os.path.isfile(full_path):
#         print(f"Найден файл: {full_path}")

# for root, dirs, files in os.walk(source_path):
#     for file in files:
#         full_path = os.path.join(root, file)
#         print(f"Найден файл: {full_path}")


# source_image = Image.open(sauna)

# source_image.save("output.webp", format="WEBP", quality=40)


# heif_file = heif_from_pillow(source_image)
# heif_file.save("output.heic", quality=40)
# source_image.save("output.avif", quality=45)

def compress_image(file_path: str, quality: int = 50, format: str = "avif"): 
    suported_formats = ["avif", "webp", "heic"]
    if format not in suported_formats:
        raise ValueError(f"Формат {format} не поддерживается")
    image = Image.open(file_path)
    if format in ["webp", "avif"]:
        image.save(f"{file_path}.{format}", format=format, quality=quality)
        return
    
    if format == "heic":
        heif_file = heif_from_pillow(image)
        heif_file.save(f"{file_path}.{format}", quality=quality) 
        return
    

def get_images_paths(source_path: str, allowed_extensions: list[str]) ->
    images_paths = []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            full_path = os.path.join(root, file)
            if os.path.isfile(full_path) and os.path.splitext(file)[1][1:] in allowed_extensions:
                images_paths.append(full_path)
    return images_paths
    

compress_image(sauna, format="webp")

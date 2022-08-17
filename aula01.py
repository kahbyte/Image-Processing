from PIL import Image

def image_converter(input_file, output_file, format):
    image = Image.open(input_file)
    image.save(output_file, format=format, optimize=True, quality=75)
    image.thumbnail((75,75))
    image.save("thumb.jpg")

def image_format(input_file):
    image = Image.open(input_file)
    print(f"Formato: {image.format_description}")

if __name__ == "__main__":
    imageJPG = "./assets/mcdonalds.jpg"
    imagePNG = "./assets/mcdonalds.png"
    format = "jpeg"
    image_converter(imagePNG, imageJPG, format)
    image_format(imageJPG)
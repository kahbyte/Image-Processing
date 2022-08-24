from PIL import ImageColor

def pega_valor_rgba(color):
    return ImageColor.getcolor(color, 'CMYK')

def main():
    for color in ImageColor.colormap:
        print(f"{color} = {pega_valor_rgba(color)}")

if __name__ == "__main__":
    main()

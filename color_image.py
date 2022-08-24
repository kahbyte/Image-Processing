from PIL import Image


def pega_cores_da_imagem(imagem):
    imagem = Image.open(imagem)
    colors = imagem.getpixel(imagem.size[0]*imagem.size[1])
    #colors = imagem.getcolors(imagem.size[0]*imagem.size[1])
    for pixel in colors:
        print(pixel)

def main():
    pega_cores_da_imagem("./assets/colors.png")

if __name__ == "__main__":
    main()
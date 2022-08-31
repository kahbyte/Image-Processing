from PIL import Image

def muda_para_cinza(input, output):
    imagem = Image.open(input)
    imagem = imagem.convert("P", palette=Image.Palette.ADAPTIVE, colors=4)
    imagem.save(output)

def main():
    muda_para_cinza("./assets/mcdonalds.jpg", "./assets/mcdonalds-4cores.png")
if __name__ == "__main__":
    main()
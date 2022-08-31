from PIL import Image


def muda_para_cinza(input, output):
    imagem = Image.open(input)
    imagem = imagem.convert("L")
    imagem.save(output)

def main():
    muda_para_cinza("./assets/mcdonalds.jpg", "./assets/mcdonalds-cinza.jpg")
if __name__ == "__main__":
    main()
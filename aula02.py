import io
import os
import PySimpleGUI as sg
from PIL import Image

def main():
    layout = [
        [sg.Image(key="-IMAGE-", size=(500,500))],
        [
            sg.Text("Arquivo de Imagem"),
            sg.Input(size=(25,1), key="-FILE-"),
            sg.FileBrowse(file_types=[("JPEF (*.jpg)", "*.jpg"), ("Todos os Arquivos", "*.*")]),
            sg.Button("Carregar Imagem")
        ]
    ]

    window = sg.Window("Visualizador de Imagem", layout=layout)
    
    while True:
        event, value = window.read()
        
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            break
        
        if event == "Carregar Imagem":
            filename = value["-FILE-"]
            if os.path.exists(filename):
                size = (500,500)
                image = Image.open(filename)
                image.thumbnail(size)
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data = bio.getvalue(), size=size)
    
    window.close()


if __name__ == "__main__":
    main()
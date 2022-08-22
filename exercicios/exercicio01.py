import io
import os
from copy import copy
import PySimpleGUI as sg
import requests
from PIL import Image

currentImage = None

def main():
    layout = [
        [sg.Image(key='-IMAGE-', size=(500,500))],
        [
            sg.Text('Arquivo de Imagem'),
            sg.Input(size=(25,1), key='-FILE-'),
            sg.FileBrowse(file_types=[('JPEF (*.jpg)', '*.jpg'), ('Todos os Arquivos', '*.*')]),
            sg.Button('Carregar Imagem')
        ],
        [
            sg.Button('Baixar Imagem')
        ],
        [            
            sg.Button('Salvar Thumbnail'),
            sg.Button('Salvar Imagem'),
            sg.Combo(['PNG', 'JPEG', 'BMP', 'GIF'], size=(15,1), default_value='PNG', key='-FORMAT-')
        ],
        [sg.Text('', key='-LOG-', text_color= 'yellow')]
    ]

    window = sg.Window('Visualizador de Imagem', layout=layout)

    while True:
        event, value = window.read()

        if event == 'Exit' or event == sg.WINDOW_CLOSED:
            break
        if event == 'Carregar Imagem':
            load_image(value['-FILE-'], window)
        if event == 'Baixar Imagem':
            download_image(value['-FILE-'], window)
        if event == 'Salvar Thumbnail':
            save_thumbnail(value['-FORMAT-'], window)
        if event == 'Salvar Imagem':
            save_image(value['-FORMAT-'], window)
    
    window.close()

def load_image(filename, window):
    if os.path.exists(filename):
        image = Image.open(filename)
        show_image(image, window)
        update_log('LOG: IMAGE LOADED', window)
    else:
        update_log('ERROR: FILE NOT FOUND', window)
    
def save_thumbnail(format, window):
    try:
        image = copy(currentImage)
        image.thumbnail((50,50))
        image.save(f'thumbnail.{get_format_extension(format)}',format=format, optimize=True,quality=75) 
        update_log('LOG: THUMBNAIL SAVED', window)
    except:
        update_log('ERROR: ERROR SAVING THUMBNAIL', window)

def save_image(format, window):
    try:
        image = copy(currentImage)
        image.save(f'savedImage.{get_format_extension(format)}',format=format,optimize=True,quality=10) 
        update_log('LOG: IMAGE SAVED', window)
    except:
        update_log('ERROR: ERROR SAVING IMAGE', window)

def download_image(url, window):
    try: 
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        show_image(image, window)
        update_log('LOG: IMAGE DOWNLOADED', window)
    except:
        update_log('ERROR: IMAGE COULD NOT BE DOWNLOADED', window)

def show_image(image, window):
    global currentImage
    size = (500,500)
    image.thumbnail(size)
    bio = io.BytesIO()
    image.save(bio, format='PNG')
    window['-IMAGE-'].update(data = bio.getvalue(), size=size)
    currentImage = image


def get_format_extension(format):
    extensions = {
        'PNG' : 'png',
        'JPEG' : 'jpg',
        'BMP' : 'bmp',
        'GIF' : 'gif'
    }
    return extensions[format]

def update_log(log, window):
    window['-LOG-'].update(log)

if __name__ == '__main__':
    main()
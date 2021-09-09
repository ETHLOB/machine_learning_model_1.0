#!/usr/bin/env python3

'''
    -----> Andres Felipe Miguel Ethorimn Lobarb

    Español
    Esta funcion esta pensada para ser mejorar en el futuro. La idea es que sea util y especializada
    para cualquier archivo que se encuentre en el repositorio de Machine Learning de la UCI
    
    En general, esta pequena herramienta es util para descargar un archivo desde alguna direccion 
    url en https://archive.ics.uci.edu//ml/datasets, pero de momento es imprecisa porque solo funciona
    con la tarea. De momento, lo unico que precisa para usarla es conocer la direccion exacta donde se aloja el archivo y especificar la direccion donde quiera guardarla en su sistema.

    English
    This function is planned to be improved in the future. The goal is to make it useful and specialized
    for every file within the UCI Machine Learning repository.

    In general, this simple toop is usefil for downloading a file from any direction in 
    https://archive.ics.uci.edu//ml/datasets, buy it is vague by the moment because it only works with
    the task's files. Right now, the only thing you need to use this is to knowi the direccion where
    the datasheets are located and to specificate the saving directory in your device.
'''

import os

from wget import download
from zipfile import ZipFile

def make_dataset(loc: str, url: str) -> None:
    os.chdir(loc)

    data_dir = os.getcwd()

    download(url, data_dir)

    with ZipFile("dataset_diabetes.zip", "r") as zip_file:
        for zip_info in zip_file.infolist():
            if zip_info.filename[-1] == '/':
                continue
            zip_info.filename = os.path.basename(zip_info.filename)
            zip_file.extract(zip_info, data_dir)

    os.remove("dataset_diabetes.zip")

if __name__ == "__main__":
    print("The script was directly ran")
else:
    print("The script was called from another module")
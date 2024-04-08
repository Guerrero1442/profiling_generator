import pandas as pd
from ydata_profiling import ProfileReport
import os
import webbrowser
from tkinter import filedialog


def load_data(file: str, file_type: str, delimiter=None) -> pd.DataFrame:
    if file_type == 'csv' or file_type == 'txt':
        try:
            return pd.read_csv(file, delimiter=delimiter)
        except Exception as e:
            print(e)
            print('No se pudo leer el archivo con el delimitador especificado')
            return pd.read_csv(file, delimiter=delimiter, encoding='latin1')
    elif file_type == 'excel':
        return pd.read_excel(file)
    else:
        raise ValueError('Tipo de archivo no soportado')


def generate_report(data: pd.DataFrame, title: str, output_file: str, minimal: bool, explorative: bool) -> ProfileReport:
    profile = ProfileReport(
        data, title=title, explorative=explorative, minimal=minimal)
    profile.to_file(f'{output_file}/{title}.html')
    return profile


if __name__ == '__main__':
    # Pedir datos al usuario
    file = filedialog.askopenfilename(title='Selecciona el archivo')

    file_type = input('Ingresa el tipo de archivo (csv, txt, excel): ')

    if file_type == 'csv' or file_type == 'txt':
        delimiter = input('Ingresa el delimitador: ')
    else:
        delimiter = None

    # Profundidad de la exploración
    explorative = input('¿Deseas una exploración profunda? (si, no): ')
    if explorative == 'si':
        explorative = True
    else:
        explorative = False

    # Parametri minimal para el reporte
    minimal = input('¿Deseas un reporte minimal? (si, no): ')
    if minimal == 'si':
        minimal = True
    else:
        minimal = False

    title = input('Ingresa el titulo del reporte: ')
    output_file = input('Ingresa la ruta donde quieres dejar el archivo: ')

    default_output_file = r"G:\Mi unidad\Requerimientos_normativos_camilo\reqs"

    if not os.path.exists(output_file):
        output_file = default_output_file
        print(f'La ruta no existe, se guardará en {output_file}')

    data = load_data(file, file_type, delimiter)
    generate_report(data, title, output_file, minimal, explorative)

    abs_path = os.path.abspath(f'{output_file}/{title}.html')
    # Abrir el archivo HTML en el navegador predeterminado
    webbrowser.open('file://' + abs_path)

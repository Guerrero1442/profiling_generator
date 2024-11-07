# Proyecto de Perfilamiento de Datos con Pandas Profiling

Este proyecto utiliza `pandas-profiling` para realizar un análisis exploratorio de datos de manera automática.

## Instalación de Dependencias

Para instalar las dependencias del proyecto, sigue los siguientes pasos:

1. Clona el repositorio en tu máquina local:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. Crea un entorno virtual con `venv`:
    ```sh
    python -m venv venv
    ```

3. Activa el entorno virtual:

    - En Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - En macOS y Linux:
        ```sh
        source venv/bin/activate
        ```

4. Instala las dependencias requeridas:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar el perfilamiento de datos, simplemente ejecuta el script principal:
```sh
python main.py
```

### Selecciona el archivo de datos
Al iniciar el script, se abrirá una ventana emergente para seleccionar el archivo de datos que deseas analizar. Asegúrate de elegir un archivo en formato compatible (`csv`, `txt`, `excel`).

### Especifica el tipo de archivo
Luego de seleccionar el archivo, ingresa el tipo de archivo cuando el script te lo pida:
- `csv` para archivos de tipo CSV.
- `txt` para archivos de texto.
- `excel` para archivos de Excel.

### Ingresa el delimitador (opcional)
Si seleccionaste un archivo `CSV` o `TXT`, se te pedirá el delimitador utilizado en el archivo (por ejemplo, `,` para CSV o `\t` para archivos delimitados por tabulaciones). Si es un archivo `Excel`, puedes omitir este paso.

### Determina la profundidad del análisis
El script te preguntará si deseas una exploración profunda. Responde `sí` para un análisis exhaustivo o `no` para un análisis estándar, según tus necesidades.

### Selecciona el nivel de detalle del reporte
Puedes optar por un reporte minimalista si solo necesitas un análisis básico. Responde `sí` para un reporte minimalista o `no` para un reporte completo.

### Asigna un título al reporte
Ingresa un título que describa el contenido del reporte, el cual se reflejará en el archivo HTML generado.

### Define la ruta de salida del archivo
Especifica la ubicación donde deseas guardar el reporte HTML. Si la ruta no existe, el archivo se guardará en la ubicación predeterminada (`G:\Mi unidad\Requerimientos_Demanda\Requerimientos`).

### Generación y apertura automática del reporte
Después de ingresar todos los parámetros, el script generará el reporte HTML en la ubicación seleccionada y lo abrirá automáticamente en el navegador predeterminado.


## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.

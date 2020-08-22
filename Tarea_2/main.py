import LectorJson
import LectorCSV
import Lectorxml


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('-----------Archivos del json------------')
    LectorJson.CargarDatos(r'C:\Users\Alejandro\Desktop\201800939_TareasLFP\Tarea_2\DatosJson.json')
    print('-----------Archivos del csv------------')
    LectorCSV.LeerDatos(r'C:\Users\Alejandro\Desktop\201800939_TareasLFP\Tarea_2\Datoscsv.csv')
    print('-----------Archivos del xml------------')
    Lectorxml.LeerDatos(r'C:\Users\Alejandro\Desktop\201800939_TareasLFP\Tarea_2\Datosxml.xml')
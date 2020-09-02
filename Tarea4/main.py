import Lectorcsv
import webbrowser

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Lectorcsv.LeerDatos(r'C:\Users\Alejandro\Desktop\201800939_TareasLFP\Tarea4\Datoscsv.csv')

f=open('lista.html','w')
f.write("""<html>
<head></head>
<body>""")
mensaje =f"""
Lectorcsv.LeerDatos(r'C:\Users\Alejandro\Desktop\201800939_TareasLFP\Tarea4\Datoscsv.csv')
"""
f.write(mensaje)
f.write("""</body>
</html>""")
f.close()
webbrowser.open_new_tab('lista.html')
import webbrowser
import Persona


Carlos = Persona.persona('Carlos', 32, 'true', 8500)
Pedro = Persona.persona('Pedro', 48, 'true', 5500)
Juan = Persona.persona('Juan', 37, 'true', 4300)
Rodrigo = Persona.persona('Rodrigo', 35, 'true', 2200)
Sebastian = Persona.persona('Sebastian', 18, 'true', 1020)
Andrea = Persona.persona('Andrea', 19, 'true', 3500)
Alejandro = Persona.persona('Alejandro', 21, 'true', 6500)
Luis = Persona.persona('Luis', 32, 'true', 4200)
Ricardo = Persona.persona('Ricardo', 28, 'true', 7500)
Mario = Persona.persona('Mario', 39, 'true', 8700)


Lista = [Carlos, Pedro, Juan, Rodrigo, Sebastian, Andrea, Alejandro, Luis, Ricardo, Mario]
f = open('Lista.html' ,'w')
f.write("""<html>
<head></head>
<body>""")
for i in Lista:
    mensaje = f"""
        <p>Nombre: {i.Nombre}</p>
        <p>Edad: {i.Edad}</p>
        <p>Activo: {i.Activo}</p>
        <p>Saldo: {i.Saldo}</p>
        <br>
        """
    f.write(mensaje)
f.write("""</body>
</html>""")
f.close()
webbrowser.open_new_tab('Lista.html')

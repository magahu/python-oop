''' Un módulo permite agrupar funcionalidad y ocultar la complejidad.
Para poder incluir un módulo podemos utilizar import '''



from lamp import Lamp
lamp = Lamp(is_turned_on = True)
lamp._display_image()

import lamp
lamp = lamp.Lamp(is_turned_on = False)
lamp._display_image()



''' En Python la comunidad comparte su código usando PyPi (python package index),
Pip es un repositorio utilizado para instalar módulos de la comunidad.
Con pip install [package_name] se puede instalar el paquete que se desea e 
importarlo a nuestro código con el keyword import. '''

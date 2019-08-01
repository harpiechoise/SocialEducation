import yaml
import os
class Entidad:
    def __init__(self, nombre, imagen):
        self.nombre = nombre
        self.imagen = imagen

    def getNombre(self):
        return self.nombre
    
    def getImagen(self):
        return self.imagen


class Historia:
    def __init__(self, historia):
        self.historia = historia
        self.entidades = []
    
    def ___analizarEntidades(self):
        raise NotImplementedError
    
    def ___Ingresar(self):
        raise NotImplementedError

class YamlParser:
    def __init__(self, caminoYAML, demo=False):
        if demo is True:
            caminoYAML = os.path.join(os.path.dirname(os.path.realpath(__file__)),caminoYAML)
        with open(caminoYAML) as file:
            contenido = file.read()
        plantilla = yaml.load(contenido)

        self.historia = plantilla['historia']
        self.entidades = plantilla['entidades']

    def getHistoria(self):
        return self.historia
    
    def getEntidades(self):
        return self.entidades

if __name__ == "__main__":
    
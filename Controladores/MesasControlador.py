from repositoros.RepositorioMesas import RepositorioMesas

from Modelos.MesasModelo import MesasModelo


class MesasControlador():
    def __init__(self):
        self.repositorioMesas = RepositorioMesas()



    def index(self):
        return self.repositorioMesas.findAll()

    def create(self, infoMesas):
        nuevaMesa = MesasModelo(infoMesas)
        return self.repositorioMesas.save(nuevaMesa)

    def show(self, id):
        laMesa = MesasModelo(self.repositorioMesas.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesa):
        mesaActual = MesasModelo(self.repositorioMesas.findById(id))
        mesaActual.cedulas_inscritas = infoMesa["cedulas_inscritas"]
        mesaActual.cantidad_votantes = infoMesa["cantidad_votantes"]
        print("mesa actual votos", mesaActual.votos)
        mesaActual.votos.append(infoMesa["votos"][0])
        return self.repositorioMesas.save(mesaActual)

    def delete(self, id):
        return self.repositorioMesas.delete(id)

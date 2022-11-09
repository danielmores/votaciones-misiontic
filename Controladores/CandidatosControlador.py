from repositoros.CandidatosRepositorio import CandidatosRepositorio

from Modelos.CandidatosModelo import CandidatosModelo


class CandidatosControlador():
    def __init__(self):
        self.candidatosRepositorio = CandidatosRepositorio()

    def index(self):
        return self.candidatosRepositorio.findAll()

    def create(self, infoVotos):
        nuevoCandidato = CandidatosModelo(infoVotos)
        return self.candidatosRepositorio.save(nuevoCandidato)

    def show(self, id):
        elCandidato = CandidatosRepositorio(self.candidatosRepositorio.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        candidatoActual = CandidatosModelo(self.candidatosRepositorio.findById(id))
        candidatoActual.id = infoCandidato["id"]
        candidatoActual.cedulas_inscritas = infoCandidato["cedulas_inscritas"]
        candidatoActual.cantidad_votantes = infoCandidato["cantidad_votantes"]
        return self.candidatosRepositorio.save(candidatoActual)

    def delete(self, id):
        return self.candidatosRepositorio.delete(id)

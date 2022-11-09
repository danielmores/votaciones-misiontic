from repositoros.VotosRepositorio import VotosRepositorio
from repositoros.RepositorioMesas import RepositorioMesas
from repositoros.CandidatosRepositorio import CandidatosRepositorio

from Modelos.VotosModelo import VotosModelo
from Modelos.MesasModelo import MesasModelo
from Modelos.CandidatosModelo import CandidatosModelo


class VotosControlador():
    def __init__(self):
        self.votosRepositorio = VotosRepositorio()
        self.mesasRepositorio = RepositorioMesas()
        self.candidatoRepositorio = CandidatosRepositorio()

    def index(self):
        return self.votosRepositorio.findAll()

    def create(self, infoVotos, id_mesa, id_candidato):
        votoActual = VotosModelo(self.votosRepositorio.findById(id))

        votoActual.votos_por_candidato = infoVotos["votos_por_candidato"]
        votoActual.id = infoVotos["id"]

        laMesa = MesasModelo(self.mesasRepositorio.findById(id_mesa))
        elCandidato = CandidatosModelo(self.candidatoRepositorio.findById(id_candidato))

        votoActual.candidato = elCandidato
        votoActual.mesa = laMesa
        return self.votosRepositorio.save(votoActual)


    def show(self, id):
        elVoto = VotosRepositorio(self.votosRepositorio.findById(id))
        return elVoto.__dict__


    def update(self, id, infoVotos, id_mesa, id_candidato):
        votoActual = VotosModelo(self.votosRepositorio.findById(id))

        votoActual.votos_por_candidato = infoVotos["votos_por_candidato"]
        votoActual.id = infoVotos["id"]

        laMesa = MesasModelo(self.mesasRepositorio.findById(id_mesa))
        elCandidato = CandidatosModelo(self.candidatoRepositorio.findById(id_candidato))

        votoActual.candidato = elCandidato
        votoActual.mesa = laMesa

        return self.votosRepositorio.save(votoActual)

    def delete(self, id):
        return self.votosRepositorio.delete(id)

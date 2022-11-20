from repositoros.InterfaceRepositorio import InterfaceRepositorio
from Modelos.VotosModelo import VotosModelo
from Modelos.MesasModelo import MesasModelo

from bson import ObjectId

class VotosRepositorio(InterfaceRepositorio[MesasModelo]):

    def getResultadoCandidatos(self):
        unwind = {
                '$unwind': {
                    'path': '$votos'
                }
            }
        group = {
                '$group': {
                    '_id': {
                        'candidato': '$votos.candidato',
                        'partido': '$votos.partido_politico'
                    },
                    'totalVotos': {
                        '$sum': '$votos.cantidad_votos'
                    }
                }
         }
        sort = {
                '$sort': {
                    'totalVotos': -1
                }

            }

        pipeline = [unwind, group, sort]
        return self.queryAggregation(pipeline)

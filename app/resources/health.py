from flask_restful import Resource

class Health(Resource):
    def get(self):
        return {'mensagem': 'A API está funcionando'}
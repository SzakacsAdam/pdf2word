from flask.views import MethodView

class RoutePdf(MethodView):
    def get(self, pdf_hash:str):
        pass
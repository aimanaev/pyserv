from bean.ai import ai

class Api():
    def __init__(self):
        self.example = "Example"
        
    def get(self, request):
        if request.path == "/api/100":
            ai.setCalc(100)
        elif request.path == "/api/200":
            ai.setCalc(200)
        elif request.path == "/api/reinit":
            ai.init()
        return f"get path:{request.path} ai: {ai.getBean()}"
    
    def post(self, request):
        return "post"

api = Api()

del Api
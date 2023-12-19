class Ai():
    def __init__(self):
        self.my_bean = {}
        
    def init(self):
        self.my_bean = {"name":"Example", "value": 100}
    
    def isBeanActive(self):
        
        #TODO check initialization
        
        return True
    
    def getBean(self):
        return self.my_bean
        
    def setCalc(self, value):
        self.my_bean["value"] = self.my_bean["value"] + value
        

ai = Ai()
ai.init()

del Ai
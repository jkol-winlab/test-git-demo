class module(object):
    def __init__(self, name, onmessage, datamessage):
        self.name=name
        self.on_message=onmessage
        self.data_message=datamessage

    def start(self):
        print("%s : %s"%(self.name, self.on_message))

    def stop(self):
        print("%s : %s"%(self.name, "turning off"))

    def getData(self):
        print("%s : %s"%(self.name, self.data_message))

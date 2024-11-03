class base_meth():

    def __init__(self):
        raise NotImplementedError("subclasses implement")
    
    def create(self):
        raise NotImplementedError("Subclasses implement")
    
    def read_all(self):
        raise NotImplementedError("Subclasses implement")
    
    def update(self, id, *args):
        raise NotImplementedError("Subclasses implement")
    
    def delete(self, id):
        raise NotImplementedError("Subclasses implement")
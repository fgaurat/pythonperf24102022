

class Singleton(type):

    instance = None

    def __call__(self, *args, **kwargs):
        if Singleton.instance is None:
            Singleton.instance = super(Singleton,self).__call__(*args, **kwargs)
        
        return Singleton.instance
        


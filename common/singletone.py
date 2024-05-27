class Singletone(object):
    instance: "Singletone" = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Singletone, cls).__new__(cls)
        return cls.instance


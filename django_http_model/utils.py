
class ClassProperty(property):
    """
    Thanks http://stackoverflow.com/a/7864317!
    """

    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()

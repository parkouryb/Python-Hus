class AnyClass:
    def __init__(self, **data):
        for k, v in data.items():
            setattr(self, k, v)

    def __str__(self):
        attrs = ["%s=%s" % (k, v) for (k, v) in self.__dict__.items()]
        classname = self.__class__.__name__
        return "%s %s" % (classname, " ".join(attrs))

    def anyParas(self, *pars):
        print(list(pars))


sample = AnyClass(name="12", age=212)
sample.anyParas(123, 12, "|!@!#")
# sample = AnyClass(name="Nam", age=18)
# print(sample)
# sample1 = AnyClass(Brand="HONDA", name="SH", price=10000)
# print(sample1)

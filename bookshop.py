class BookShop():
    def __init__(self):
        pass

    def method1(self, orders):
        lt100 = lambda x, y: x*y if x*y > 100 else x*y + 10
        return list(map(lambda inner: list(map(lambda x: x if type(x) == int else (x[0], lt100(x[1],x[2])), inner)), orders))

    def method2(self, orders):
        return list(map(lambda inner: list(filter(lambda x: x == min(inner[1:]), inner)), orders))

    def method3(self, orders):
        return list(map(lambda inner: list(filter(lambda x: x == max(inner[1:]), inner)), orders))

    def method4(self, orders):
        pass
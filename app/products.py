class Product:
    id = 1

    def __init__(self, name, price, features=None):
        self.name = name
        self.price = price
        self.features = []
        self.id = Product.id
        if isinstance(features, list):
            self.add_features(features)
        elif isinstance(features, str):
            self.add_feature(features)
        else:
            print('given features should be a list or a string for single feature')
        Product.id += 1

    def add_feature(self, feature):
        self.features.append(feature)

    def add_features(self, features):
        self.features.extend(features)

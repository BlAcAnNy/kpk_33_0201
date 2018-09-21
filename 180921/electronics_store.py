class Electronics:
    def __init__(self, name, characteristic, guarantee, producing_country, price):
        self.name = name
        self.characteristic = characteristic
        self.guarantee = guarantee
        self.producing_country = producing_country
        self.price = price

    def __str__(self):
        return f'Электроника: {self.name}, ({self.characteristic}), {self.guarantee} мес, {self.producing_country}, {self.price} руб.'

    @classmethod
    def import_from_file(cls, file_name):
        items_source = open(file_name, 'r', encoding='utf-8').readlines()
        items_source = list(map(lambda x: x.replace('\n', '').split(', '), items_source))
        items_schema = items_source.pop(0)
        items_source_as_dict = list(map(lambda x: dict(zip(items_schema, x)), items_source))
        items = []
        for item_dict in items_source_as_dict:
            _item = cls(**item_dict)
            items.append(_item)
        return items

class Smartphone(Electronics):

    def __init__(self, name, characteristic, guarantee, producing_country, price, *args, **kwargs):
        super().__init__(name, characteristic, guarantee, producing_country, price, *args, **kwargs)

    def __str__(self):
        return f'Смартфоны: {self.name}, ({self.characteristic}), {self.guarantee} мес, {self.producing_country}, {self.price} руб.'




class Laptop(Electronics):

    def __init__(self, name, characteristic, guarantee, producing_country, price, *args, **kwargs):
        super().__init__(name, characteristic, guarantee, producing_country, price, *args, **kwargs)

    def __str__(self):
            return f'Ноутбуки: {self.name}, ({self.characteristic}), {self.guarantee} мес, {self.producing_country}, {self.price} руб.'

class TV(Electronics):

    def __init__(self, name, characteristic, guarantee, producing_country, price, *args, **kwargs):
        super().__init__(name, characteristic, guarantee, producing_country, price, *args, **kwargs)

    def __str__(self):
        return f'Телевизоры: {self.name}, ({self.characteristic}), {self.guarantee} мес, {self.producing_country}, {self.price} руб.'




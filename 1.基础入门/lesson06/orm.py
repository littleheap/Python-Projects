class Field:
    def __init__(self, name, col_type):
        self.name = name
        self.col_type = col_type


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'integer')


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(1024)')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Model name: %s' % name)
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Field name: %s' % k)
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kvs):
        super(Model, self).__init__(**kvs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'." % key)

    def __setattr__(self, key, value):
        print('__setattr__')
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s(%s) values(%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('sql:', sql)
        print('args:', args)


class User(Model):
    id = IntegerField('id')
    name = StringField('name')


# u = User(id = 100, name = 'Tom')
u = User()
u.id = 100
u.name = 'Tom'
u.save()

class Shoes:
    def __init__(self, sex, type_sh, color, price, brand, size):
        self.shoes_data = {
            'sex': sex,
            'type': type_sh,
            'color': color,
            'price': price,
            'brand': brand,
            'size': size
        }

    def get_data(self):
        '''Возвращаем все данные по экземпляру обуви'''
        return self.shoes_data

    def change_data(self, type_of_data, data):
        '''Изменяем выбранное поле(например, цену) для обуви'''
        if type_of_data in self.shoes_data.keys():
            self.shoes_data[type_of_data] = data
            return None
        else:
            return 'Type error!'

    def translate_keys(self, en_key):
        '''Переводим имена ключей на русский. Потребуется для эстетики в модуле View'''
        ru_key = ''
        if en_key not in self.shoes_data:
            return 'Key error!'
        else:
            if en_key == 'sex':
                ru_key = 'пол'
            if en_key == 'type':
                ru_key = 'тип обуви'
            if en_key == 'color':
                ru_key = 'цвет обуви'
            if en_key == 'price':
                ru_key = 'цена'
            if en_key == 'brand':
                ru_key = 'фирма'
            if en_key == 'size':
                ru_key = 'размер обуви'
        return ru_key

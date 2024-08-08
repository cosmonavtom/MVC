class ShoesController:
    def __init__(self, model):
        self.model = model

    def get_ad_info(self):
        '''Возвращает рекламную инфу про обувь. Тип - Бренд - Цена'''
        data = self.model.get_data()
        ad_info = f'{data['type'].capitalize()} фирмы "{data['brand']}" всего за {data['price']}!!!'
        return ad_info

    def get_all_data(self):
        '''Возвращает полную информацию об экземпляре обуви'''
        data = self.model.get_data()
        all_data = (f'Обувь для: {data['sex']}\n'
                    f'Тип: {data['type']}\n'
                    f'Цвет: {data['color']}\n'
                    f'Цена: {data['price']}\n'
                    f'Марка: {data['brand']}\n'
                    f'Размер: {data['size']}\n')
        return all_data

    def change_data(self, type_of_data, data, permission):
        '''Изменять данные можно только директору и старшему менеджеру Гали.
        Кстати, не могу понять почему не работает закоменнченная строчка проверки'''
        # if self.model.change_data == 'Type error!':
        if type_of_data not in self.model.shoes_data:
            return 'Type error!'
        elif permission in ['director', 'Galya']:
            self.model.change_data(type_of_data, data)
            return 'Сhanges applied!'
        else:
            return 'No access!'

    def translate_keys(self, en_key):
        return self.model.translate_keys(en_key)

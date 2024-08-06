class ShoesView:

    def __init__(self, controller):
        self.controller = controller

    def print_ad_info(self):
        data = self.controller.get_ad_info()
        print(f'*** Рекламная акция! Только пока не купите! ***\n{data}\n')

    def print_all_data(self):
        data = self.controller.get_all_data()
        print(data)

    def print_change_data(self, type_of_data, data, permission):
        changed_data = self.controller.change_data(type_of_data, data, permission)
        if changed_data == 'No access!':
            print('Изменять параметры могут только директор и Галя\n')
        elif changed_data == 'Type error!':
            print('Такого параметра у обуви нет\n')
        else:
            print(f'Изменен {self.controller.translate_keys(type_of_data)} на {data}. Ответственный за изменение: {permission}\n')


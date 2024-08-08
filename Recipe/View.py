class View:
    def __init__(self, controller):
        self.controller = controller

    def print_base_data(self):
        data = self.controller.get_data()
        base_data = f'Блюдо {', '.join(data['name'])} от {', '.join(data['cook'])}!!! Родина: {', '.join(data['homeland'])}\n'
        print(base_data)

    def print_all_data(self):
        data = self.controller.get_data()
        print(f'Название :: {', '.join(data['name'])}\n'
              f'Автор :: {', '.join(data['cook'])}\n'
              f'Тип блюда :: {', '.join(data['type_of_dish'])}\n'
              f'Описание :: {', '.join(data['description'])}\n'
              f'Ингредиенты :: {', '.join(data['ingredients'])}\n'
              f'Страна происхождения :: {', '.join(data['homeland'])}\n'
              f'Ссылка :: {data['link']}\n'
              )

    def print_change_description(self, new_description):
        self.controller.change_description(new_description)
        print('Описание изменено\n')

    def add_data(self, key, data):
        if self.controller.add_data(key, data) == 'Key error!':
            print('Такого ключа нет\n')
        else:
            print(f'В значение {key} добавлен(о,а) {data}\n')

    def remove_data(self, key, data):
        if self.controller.remove_data(key, data) == 'Key or value error!':
            print('Неправильный ключ или значение!\n')
        else:
            # self.controller.remove_data(key, data)
            print(f'Значение "{data}" удалено из {key}\n')

    def clear_data(self, key):
        if self.controller.clear_data(key) == 'Key error!':
            print('Неверный ключ!\n')
        else:
            print(f'Категория "{key}" очищена!\n')

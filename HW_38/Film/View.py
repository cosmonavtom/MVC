class View:
    def __init__(self, controller):
        self.controller = controller

    def print_data(self):
        print(self.controller.get_data())

    def print_ad_info(self):
        print(self.controller.get_ad_info(), end='\n\n')

    def change_data(self, type_of_data, data):
        ch_data = self.controller.change_data(type_of_data, data)
        if ch_data == 'Type error!':
            print('Такого параметра у фильма нет!\n')
        else:
            print(f'{type_of_data} изменён на {data}\n')

    def add_actors(self, actor, role):
        new_actor = self.controller.add_actors(actor, role)
        if new_actor == 'This actor already exists':
            print(f'Этот актёр уже есть в списках\n')
        else:
            print(f'Актёр {actor} добавлен в роли "{role}"!\n')
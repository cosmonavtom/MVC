class ArtView:

    def __init__(self, controller):
        self.__controller = controller

    def print_default_info(self):
        # print(self.controller.get_default_info)
        data = self.__controller.get_default()
        for key, value in data.items():
            print(f'{key} :: {value}')
        print()

    def print_title_and_author(self):
        ptitle, pauthor = self.__controller.get_title_and_author()
        print(f'Статья {ptitle} автора {pauthor}\n')

    def change_title(self, new_title):
        self.__controller.change_title(new_title)
        print(f'Статья переименована как {new_title}\n')



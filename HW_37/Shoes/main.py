from Model import Shoes
from View import ShoesView
from Controller import ShoesController

if __name__ == "__main__":
    shoes = Shoes('М', 'валенки', 'индиго', 1_200, 'Карельский Скороход', 45)
    controller = ShoesController(shoes)
    viewer = ShoesView(controller)


    #Тестим рекламную вывеску
    viewer.print_ad_info()
    #Смотри всю информациб об обуви
    viewer.print_all_data()
    #Покупатель пытается снизить цену на продукцию
    viewer.print_change_data('price', 1000, 'buyer')
    viewer.print_all_data()
    #У Гали как раз 45 размер и она делает валенки женскими
    viewer.print_change_data('sexy', 'F', 'Galya')
    #Упс. Неправильный параметр. Вторая попытка
    viewer.print_change_data('sex', 'F', 'Galya')
    viewer.print_all_data()
    #Директор решил снизить цену
    viewer.print_change_data('price', 1000, 'director')
    viewer.print_all_data()
    #И снова рекламная акция!
    viewer.print_ad_info()









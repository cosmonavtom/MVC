import Article, ArtController, ArtView

article = Article.Article('Article', ' Author', 132, 'www.site.com', 'description')
controller = ArtController.ArtController(article)
view = ArtView.ArtView(controller)

# Полная инфа
view.print_default_info()
# Только автор и название статьи
view.print_title_and_author()
# Изменяем название статьи
view.change_title('New Article')
# Смотрим изменение
view.print_default_info()

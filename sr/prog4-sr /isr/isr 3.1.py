# Разработка классов и объектов «запись», «комментарий» для приложения «Блог» (использование наследования).

class Post():
    def __init__(self, author, title):
        self.__title = title
        self.__author = author
        self.__comments = []

    def show_comment(self, comment):
        print(f"""{comment.author}
              {comment.title} 
              {comment.text}""")
        
    def show_post_comments(self):
        pass
        
        

class Comment(Post):
    def __init__(self, title, text, author):
        self.__title = title
        self.__text = text 
        self.__author = author
        
   
    @property
    def title(self):
        return self.__title
    
    @property
    def text(self):
        return self.__text

    @property
    def author(self):
        return self.__author


r1 = Post('author', 'first record')
c1 = Comment('first comment', 'hello world', 'author')
r1.show_comment(c1)
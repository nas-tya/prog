# Создание геттеров и сеттеров для классов «запись», «комментарий» приложения «Гостевая книга». Создание функций для вывода на печать информации, хранящийся в объектах.

class HostBook():
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
        
        

class Comment(HostBook):
    def __init__(self, title, text, author, post: HostBook):
        self.__title = title
        self.__text = text 
        self.__author = author
        
   
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self._title = title
    
    @property
    def text(self):
        return self.__text

    @property
    def author(self):
        return self.__author

    @property
    def post(self):
        return self._post

    @post.setter
    def post(self, post: HostBook):
        self._post = post


r1 = HostBook('author', 'first record')
c1 = Comment('first comment', 'hello world', 'author', r1)
r1.show_comment(c1)
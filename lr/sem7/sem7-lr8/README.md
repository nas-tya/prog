# Инструкция 

Создаём томы 

![1](/1.png)
![2](/2.png)
![3](/3.png)


Локально создаем директорию для ЛР, переносим туда файлы из репла (все, кроме docker-compose)

![4](/4.png)

Создаем контейнер

![5](/5.png)

Запускаем

![6](/6.png)

Через curl localhost (localhost/initdb, localhost/stat и тд) можно протестировать, работает ли всё

Затем переносим в директорию файл docker-compose и останавливаем всё с помощью docker stop

![7](/7.png)

Удаляем образы

![8](/8.png)

Выполняем команду docker-compose -f docker-compose.dev.yml up --build

В результате всё работает:

![9](/9.png)

Ссылка на хаб: https://hub.docker.com/r/brazhkinanastya/sem7lr8/tags


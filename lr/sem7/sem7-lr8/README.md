# Инструкция 

Создаём томы 

![1](https://github.com/nas-tya/prog/blob/main/lr/sem7/sem7-lr8/1.png)
![2](https://github.com/nas-tya/prog/blob/main/lr/sem7/sem7-lr8/2.png)
![3](https://github.com/nas-tya/prog/blob/main/lr/sem7/sem7-lr8/3.png)


Локально создаем директорию для ЛР, переносим туда файлы из репла (все, кроме docker-compose)

![4](https://github.com/nas-tya/prog/blob/main/lr/sem7/sem7-lr8/4.png)

Создаем контейнер

![5](https://github.com/nas-tya/prog/blob/main/lr/sem7/sem7-lr8/5.png)

Запускаем

![6](https://github.com/nas-tya/prog/blob/main/lr/sem7/sem7-lr8/6.png)

Через curl localhost (localhost/initdb, localhost/stat и тд) можно протестировать, работает ли всё

Затем переносим в директорию файл docker-compose и останавливаем всё с помощью docker stop

![7](https://github.com/nas-tya/prog/blob/main/lr/sem7/sem7-lr8/7.png)

Удаляем образы

![8](https://github.com/nas-tya/prog/blob/main/lr/sem7/sem7-lr8/8.png)

Выполняем команду docker-compose -f docker-compose.dev.yml up --build

В результате всё работает:

![9](https://github.com/nas-tya/prog/blob/main/lr/sem7/sem7-lr8/9.png)

Ссылка на хаб: https://hub.docker.com/r/brazhkinanastya/sem7lr8/tags


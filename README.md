# Технологии и методы программирования (часть 4/4)
Технологии и методы программирования, 6 семестр, Крайников Александр БИСО-02-20

## Практическая работа №0
Цель работы: познакомиться с инструмментом PlantUml и системой котнтроля версий GIT.
Задачи:
1. Составить диаграмму вариантов исмользованя на языке PlantUml 
2. Загрузить диаграмму с репозиторий Git
3. прикрепить ссылку не репозиторий к практической работе

UML-скрипт:

    @startuml
    left to right direction
    rectangle Гейм-дев_отдел{
    Дизайнер -- (Создание концепта)
    Руководитель -- (Согласование концепта)
    Руководитель -- (Согласование модели)
    (Одобрение концепта) <. (Согласование концепта)
    (Согласование концепта) <.. (Создание концепта)
    3D_моделлер -- (Создание модели)
    (Создание модели) <. (Одобрение концепта)
    (Согласование модели) <.. (Создание модели)
    (Одобрение модели) <. (Согласование модели)
    Аниматор -- (Анимирование модели)
    (Анимирование модели) <. (Одобрение модели)
    }
    @enduml

Диаграмма:

![Prac-work_0](https://user-images.githubusercontent.com/90748885/232142845-4fed59aa-b7da-47fc-8e9e-098f25e9c7ba.png)

## Практическая работа №1
### Вариант задания: 12 – Система автоматического тестирования

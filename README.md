# Технологии и методы программирования (часть 4/4)
Технологии и методы программирования, 6 семестр, Крайников Александр БИСО-02-20

## Практическая работа №0
##### Цель работы:
Познакомиться с инструмментом PlantUml и системой котнтроля версий GIT.
##### Задачи:
1. Составить диаграмму вариантов исмользованя на языке PlantUml 
2. Загрузить диаграмму с репозиторий Git
3. прикрепить ссылку не репозиторий к практической работе

##### UML-скрипт:

    @startuml "Практическая работа 0"
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

##### Диаграмма:

![Prac-work_0](https://user-images.githubusercontent.com/90748885/232142845-4fed59aa-b7da-47fc-8e9e-098f25e9c7ba.png)


## Практическая работа №1
### Вариант задания: 12 – Система автоматического тестирования
#### Обзор: Система позволяет автоматически запускать тесты, отслеживать результаты их выполнения и выдавать отчеты.
##### Задачи:
1.	При помощи программы PlantUML либо любого редактора построить UML-диаграмму вариантов использования, диаграмму классов проектируемой информационной системы в соответствии с вариантом задания, а также диаграмму последовательности для наиболее часто используемых прецедентов . При построении диаграммы классов нужно добиться достаточной детализации информационной системы. Убедитесь в том, что использовали отношения dependency, aggregation/composition, generalization, описали размещение классов по пакетам проекта.
2.	Подготовить отчет с включением диаграмм. Загрузить в GIT. Прикрепить ссылку

##### UML-скрипт:

    @startuml "Практическая работа 1-1"
    left to right direction
    title Система автоматического тестирования
    actor Пользователь
    actor ПО_автоматизированного_тестирования
    rectangle Система {
    Пользователь -- (Определение тестовых данных)
    (Определение тестовых данных) ..>(Выполнение тестирования):<<include>>
    (Определение тестовых данных) ..> (Сопровождение тестирования):<<include>>
    ПО_автоматизированного_тестирования -- (Выполнение тестирования)
    (Выполнение тестирования) ..>(Сбор статистики выполнения):<<include>>
    (Сбор статистики выполнения) ..> (Оценка результатов выполнения):<<include>>
    (Сопровождение тестирования) ..> (Оценка результатов выполнения):<<include>>
    }
    @enduml
    
    @startuml "Практическая работа 2-2"
    class Пользователь{
    Определение тестовых данных()
    Отслеживание тестирования()
    Анализ результатов()
    }
    class ПО_автоматизированного_тестирования{
    Приём тестовых данных()
    Выполнение тестирования()
    Вывод результаты выполнения()
    }
    class Тестовые_данные{
    +Тестовые данные
    }
    class Тестирование{
    +Номер тестирования
    +Время выполнения тестирования
    }
    class Результаты{
    +Номер тестирования
    +Результаты тестирования
    }
    Пользователь --> Тестовые_данные:Определяет
    ПО_автоматизированного_тестирования --> Тестовые_данные:Принимает
    ПО_автоматизированного_тестирования --> Тестирование:Выполняет
    ПО_автоматизированного_тестирования --> Результаты:Выводит
    Пользователь --> Тестирование:Отслеживает
    Пользователь --> Результаты:Анализирует
    Тестовые_данные ..> Тестирование
    Тестирование ..> Результаты

##### Диаграммы:

![Prac-work_1](https://user-images.githubusercontent.com/90748885/232153209-e3e880f8-baf4-4197-9d51-b6ad7ac0dc79.png)

![Prac-work_1-2](https://user-images.githubusercontent.com/90748885/232159187-7587295b-7e52-4104-88d1-823589a721af.png)


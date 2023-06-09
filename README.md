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
    
    @startuml "Практическая работа 1-2"
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
Скриншот 1. Диаграмма вариантов использования
  
![Prac-work_1-2](https://user-images.githubusercontent.com/90748885/232159187-7587295b-7e52-4104-88d1-823589a721af.png)  
Скриншот 2. Диаграмма классов проектируемой информационной системы  
  
  
## Практическая работа №2  
### Вариант задания: 12 – Система автоматического тестирования
##### Задачи:
1.	При помощи программы PlantUML либо любого редактора реализовать диаграммы последовательностей и развёртывания по варианту из практической работы №1.
2.	Подготовить отчет с включением диаграмм. Загрузить в GIT. Прикрепить ссылку

##### UML-скрипт:

    @startuml "Практическая работа 2-1" 
    title Система автоматического тестирования: диаграмма последовательности 
    skinparam backgroundcolor AntiqueWhite/Grey 
    participant Пользователь 
    participant Тестирование 
    participant Программное_обеспечение 
    activate Пользователь 
    Пользователь -> Тестирование: Определяет тестовые данные 
    activate Тестирование 
    Пользователь -> Программное_обеспечение: Выдает тестовые данные 
    deactivate Пользователь 
    activate Программное_обеспечение 
    Программное_обеспечение -> Тестирование:Приступает к выполнению тестирования 
    Программное_обеспечение -> Тестирование:Выполняет тестирование 
    deactivate Тестирование 
    Программное_обеспечение -> Пользователь:Выводит результаты тестирования 
    deactivate Программное_обеспечение 
    activate Пользователь 
    activate Тестирование 
    Пользователь -> Тестирование:Анализирует результаты тестирования 
    deactivate Пользователь 
    deactivate Тестирование 
    @enduml
    
    @startuml "Практическая работа 2-2"
    left to right direction
    title Система автоматического тестирования: диаграмма развертывания
    skinparam backgroundcolor AntiqueWhite/Grey
    database Тестирования
    node ПК_Пользователь
    node ПК_Программное_обеспечение
    node Тестовые_данные
    node Система_тестирования
    ПК_Пользователь - Тестовые_данные: Выдаёт
    ПК_Программное_обеспечение - Тестовые_данные: Использует
    ПК_Программное_обеспечение - Тестирования: Выполняет
    ПК_Пользователь - Система_тестирования: Проверка выполнения тестирования
    Система_тестирования - Тестирования
    @enduml

##### Диаграммы:

![Prac-work_2-1](https://user-images.githubusercontent.com/90748885/235373479-3ed0ed27-d2c2-49b6-907c-276f69c0cba4.png)  
Скриншот 1. Диаграмма последовательности

![Prac-work_2-2](https://user-images.githubusercontent.com/90748885/235373506-e23e71a0-3f7f-4396-8082-d7a65f5698da.png)  
Скриншот 2. Диаграмма развертывания  



## Практическая работа №3  

##### UML-скрипт:

    @startuml
    title Пратическая работа 3: Template Method
    class Algorithm{
    template_method()
    flagstock()
    draw_1()
    draw_2()
    draw_3()
    final()
    printer()
    }
    note right of Algorithm::"template_method()"
    self.flagstock()
    self.draw_1()
    self.draw_2()
    self.draw_3()
    self.final()
    self.printer()
    end note
    
    class colors{
    painwhite()
    painred()
    painblue()
    painblack()
    painyel()
    }
    
    class RussianFlag{
    z = colors
    z.pain
    draw_1()
    draw_2()
    draw_3()
    final()
    }
    class  GermanFlag{
    z = colors
    z.pain
    draw_1()
    draw_2()
    draw_3()
    }
    
    Algorithm <|-- GermanFlag : Немецкий флаг
    Algorithm <|-- RussianFlag : Российский флаг
    
    RussianFlag -  GermanFlag 
    (RussianFlag, GermanFlag) - colors:Задает цвет
    
    @enduml
  
    @startuml 
    title Пратическая работа 3: Strategy 
    
    class Variant{ 
    selection() 
    } 
    class Game{ 
    strategy: Variant 
    init() 
    play() 
    } 
    
    class Rock{ 
    selection() 
    } 
    class Paper{ 
    selection() 
    } 
    class Clippers{ 
    selection() 
    } 
    class main{ 
    int n 
    str vibor 
    playtime() 
    player1.play(player2) 
    } 
    note right of main::"playtime()" 
    player1 = playtime(vibor) 
    player2 = playtime(vibor) 
    end note 
    
    Paper --> Variant 
    Rock --> Variant 
    Clippers --> Variant 
    main *--> Variant 
    main --Game 
    
    @enduml 

##### Диаграммы:
![Prac-work_3-method](https://github.com/A-Kraynikov/Tehnologii-Methody-6/assets/90748885/56c56b81-b687-4a5c-a591-45160c809f98)  
Скриншот 1. Диаграмма шаблонного метода
  
![Prac-work_3-strategy](https://github.com/A-Kraynikov/Tehnologii-Methody-6/assets/90748885/72000095-c931-4811-8651-cefe2b46ca55)  
Скриншот 2. Диаграмма стратегии  



## Практическая работа №4: Итератор, посетитель  

UML-скрипт: https://github.com/A-Kraynikov/Tehnologii-Methody-6/blob/main/Programs/Prac-work_4.puml

Итератор: https://github.com/A-Kraynikov/Tehnologii-Methody-6/blob/main/Programs/prac_4-1.py

Посетитель: https://github.com/A-Kraynikov/Tehnologii-Methody-6/blob/main/Programs/prac_4-2.py  

##### Диаграммы:
![Prac-work_4-iterator](https://github.com/A-Kraynikov/Tehnologii-Methody-6/assets/90748885/5e836642-ee4a-410d-88d7-89f948b8a46e)  
Скриншот 1. Диаграмма итератора
  
![Prac-work_4-visitor](https://github.com/A-Kraynikov/Tehnologii-Methody-6/assets/90748885/1f5ea4bf-e00b-45ac-ae66-883f57eef394)  
Скриншот 2. Диаграмма посетителя  



## Практическая работа №5: Абстрактная фабрика. Посредник. Строитель. Адаптер  

Абстрактная фабрика: https://github.com/A-Kraynikov/Tehnologii-Methody-6/blob/main/Programs/prac_5-1.py  

Посредник: https://github.com/A-Kraynikov/Tehnologii-Methody-6/blob/main/Programs/prac_5-4.py  

Строитель: https://github.com/A-Kraynikov/Tehnologii-Methody-6/blob/main/Programs/prac_5-2.py  

Адаптер: https://github.com/A-Kraynikov/Tehnologii-Methody-6/blob/main/Programs/prac_5-3.py  



## Практическая работа №6: Инверсия управления. Заместитель, Компоновщик  

Инверсия управления: https://github.com/A-Kraynikov/Tehnologii-Methody-6/tree/main/Programs/prac_6_Inversion-of-control  

Заместитель: https://github.com/A-Kraynikov/Tehnologii-Methody-6/blob/main/Programs/prac_6-2.py  

Компоновщик:  https://github.com/A-Kraynikov/Tehnologii-Methody-6/blob/main/Programs/prac_6-3.py  

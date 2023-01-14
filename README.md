<h1 align="center">Проект по тестированию страницы сайта demoqa.com</h1>

&#8287;&#8287;&#8287;&#8287;&#8287;
## :open_book: Содержание:
- [Технологии и инструменты](#gear-проект-реализован-с-использованием)
- [Что проверяем](#heavy_check_mark-описание)
- [Запуск тестов из Jenkins](#-запуск-тестов-из-jenkins)
- [Запуск тестов из терминала](#computer-запуск-тестов-из-терминала)
- [Отчеты](#bar_chart-отчеты-о-прохождении-тестов)
  - [Allure](#-allure)
  - [Telegram](#-telegram)
- [Тестовые артефакты](#movie_camera-тестовые-артефакты)

&#8287;&#8287;&#8287;&#8287;&#8287;
## :gear: Проект реализован с использованием
  <p align="center">
    <img src="/README/icons/python.svg" title="Python" width="50" height="50"  alt="python"/>
    <img src="/README/icons/pycharm.svg" title="Pycharm" width="50" height="50"  alt="pycharm"/>
    <img src="/README/icons/pytest.svg" title="Pytest" width="50" height="50"  alt="pytest"/>
    <img src="/README/icons/selene.png" title="Selene" width="50" height="50"  alt="selene"/>
    <img src="/README/icons/selenoid.svg" title="Selenoid" width="50" height="50"  alt="selenoid"/>
    <img src="/README/icons/jenkins.svg" title="Jenkins" width="50" height="50"  alt="jenkins"/>
    <img src="/README/icons/allure.svg" title="Allure" width="50" height="50"  alt="allure"/>
    <img src="/README/icons/telegram.svg" title="Telegram" width="50" height="50"  alt="telegram"/>
 </p>


&#8287;&#8287;&#8287;&#8287;&#8287;
## :heavy_check_mark: Описание
<p>Реализована проверка отправки формы учебного сайта demoqa.com.</p>
<p>Для тестирования был создан page object формы в парадигме ООП. Была создана модель как на заполнение формы, так  универсальные инструменты работы с отдельными элементами.</p>
<p>Тесты запускаются в Jenkins, проходят в Selenoid и далее создается Allure отчет и отправляется уведомление в Telegram. В процессе прохождения тестов собираются тестовые артефакты.</p>

&#8287;&#8287;&#8287;&#8287;&#8287;
## <img src="/README/icons/jenkins.svg" width="50" height="50"  alt="jenkins"/> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/002_Clorhexidinum_diploma_python/)
  
  Для запуска тестов из Jenkins

  <p>1. Необходимо нажать кнопку "Собрать с параметрами".</p>
  
  <p>2. Выбрать параметры.</p>
  
  <p>3. Нажать кнопку "Собрать"</p>
  
  ### :heavy_plus_sign: Параметры сборки

> - browser_name - название браузера
> - browser_version - версия браузера
> - window_size - размер окна браузера
  
&#8287;&#8287;&#8287;&#8287;&#8287;
## :computer: Запуск тестов из терминала

Для локального запуска необходимо выполнить команду:
```
pytest *test_folder*
```

&#8287;&#8287;&#8287;&#8287;&#8287;
## :bar_chart: Отчеты о прохождении тестов 
  
### <img src="/README/icons/allure.svg" width="50" height="50"  alt="allure"/> Allure

После прохождения тестов формируется отчет в Allure report
  
  
&#8287;&#8287;&#8287;&#8287;&#8287;
### <img src="/README/icons/telegram.svg" width="50" height="50"  alt="telegram"/> Telegram

И отправляется краткий отчет в Telegram
  
&#8287;&#8287;&#8287;&#8287;&#8287;
## :movie_camera: Тестовые артефакты

В результате прохождения тестов собираются следующие артефакты:
  

  <p>Скриншот страницы</p>

  <p>Логи браузера</p>
  
  <p>Дамп страницы</p>
  
  <p>Видео прохождения</p>


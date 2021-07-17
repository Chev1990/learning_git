# learning_git and Python
## Git readme.md format 
> https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax

## Commands Git
### git stash - позволяет на время «сдать в архив» (или отложить) изменения, сделанные в рабочей копии, чтобы вы могли применить их позже. Откладывание изменений полезно, если вам необходимо переключить контекст и вы пока не готовы к созданию коммита.
### git stash pop - применить ранее отложенные изменения. При извлечении отложенных изменений они удаляются из набора и применяются к рабочей копии.
### git stash pop apply - применить изменения к рабочей копии, не удаляя их из набора отложенных изменений. 
> *по умолчанию Git не создает отложенные изменения для неотслеживаемых или игнорируемых файлов*
### git-restore - восстанавливает файлы рабочего дерева
### git checkout -f name_branch - переключать ветки, даже если у вас есть неэтапные изменения (другими словами, индекс рабочего дерева отличается от HEAD). По сути, его можно использовать для удаления локальных изменений.

## Commands Python
### alert -  Alert является модальным окном: это означает, что пользователь не может взаимодействовать дальше с интерфейсом, пока не закроет alert. Для этого нужно сначала переключиться на окно с alert, а затем принять его с помощью команды accept().
> alert = browser.switch_to.alert
> alert.accept()
### confirm - вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него, называется confirm. Для переключения на окно confirm используется та же команда, что и в случае с alert.
> confirm = browser.switch_to.alert
> confirm.accept()
#### confirm.dismiss() - метод для отказа для confirm-окон.
### prompt - модальное окно имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys()
> prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
### switch_to.window - для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти. Это делается с помощью данной команды.
> browser.switch_to.window(window_name)
### window_handles - чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
> new_window = browser.window_handles[1]
>> current_window = browser.current_window_handle - имя текущей вкладки
### implicitly_wait - неявное ожидание. специальный способ организации такого ожидания, который позволяет задать ожидание при инициализации драйвера, чтобы применить его ко всем теста
>> говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
### element_to_be_clickable  - вернет элемент, когда он станет кликабельным, или вернет False в ином случае.
>>говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
>>> функция until, в которую передается правило ожидания, элемент, а также значение, по которому мы будем искать элемент.
>>> Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно задать негативное правило с помощью метода until_not:
>>>> говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
### Про Exceptions
Теперь мы знаем, как настроить ожидание поиска элемента. Во время поиска WebDriver каждые 0.5 секунды проверяет, появился ли нужный элемент в DOM-модели браузера (Document Object Model — «объектная модель документа», интерфейс для доступа к HTML-содержимому сайта). Если произойдет ошибка, то WebDriver выбросит одно из следующих исключений (exceptions):

Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился, то получим StaleElementReferenceException. Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры), и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.

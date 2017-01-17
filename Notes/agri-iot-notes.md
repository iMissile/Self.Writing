# Настройка репозиториев
- [Репозиторий кода](https://github.com/iMissile/agri-iot-code)
- [Репозиторий данных](https://github.com/iot-rus/agri-iot-data)

На машине-сборщике эти репозитории частично мапируются на директории scripts & data. В scripts делаем выгрузку скриптов, а в data делаем клон репозитория данных.

## Настройка прав на стороне клиента

`git commit` после инициализации репозитория и добавления файлов дает такое сообщение":

```
*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.
```
Надо настроить git клиента для этого репозитория.

## Генерируем ключ для подключения к репозиториям
- Создаем пару открытый\закрытый ключ командой `ssh-keygen -t rsa`. Ключи размещаются в системной директории `/root/.ssh/id_rsa`
- Смотрим ключ командами `cd ~/.ssh/`, `cat id_rsa.pub`
- [Добавляем ключ в аккаунт GitHub\Adding a new SSH key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)

### Генерация нескольких ключей
Для простых задач можно ограничиться одним ключом, но есть возможность для каждого хоста сделать свой RSA ключ.
Для этого надо сделать несколько отдельных ключей и прописать их в файле `$HOME/.ssh/config`:

``
Host mt-zoo-ubuntu01 mt-zoo-ubuntu01.media-tel.ru
   HostName mt-zoo-ubuntu01
   IdentityFile ~/.ssh/id_rsa
   User kirill

Host mt-zoo-kirill01 mt-zoo-kirill01.media-tel.ru
   HostName mt-zoo-kirill01
   IdentityFile ~/.ssh/id_rsa_2
   User kirill
```

# Технические шаги
## Выгрузка репозитория погоды
Репозиторий данных ручками создали на GitHub. На машине-сборщике первоначальную инсталляцию делаем руками. В верхней директории запускаем команду `git clone https://github.com/iot-rus/agri-iot-data data`. Имя директории меняем.

В принципе, надо делать пустные файлы данных сразу на GitHub. Тогда не придется их добавлять ручками на клиентской стороне. Но если не сделал, то можно это исправить командой `git add <name>` 

## Первоначальная выгрузка скриптов на linux машине
- Проверка установленной версии git командой `git version`
- Обновляем последние версии скриптов из репозитория. Существует несколько вариантов
	
**Вариант 1**. Используем средства GIT

[How to checkout only one file from git repository?](http://stackoverflow.com/questions/2466735/how-to-checkout-only-one-file-from-git-repository) 

Now we can! As this is the first result on google, I thought I'd update this to the latest standing. With the advent of git 1.7.9.5, we have the git archive command which will allow you to retrieve a single file from a remote host.

`git archive --remote=git://git.foo.com/project.git HEAD:path/to/directory filename | tar -x`

See answer in full here [http://stackoverflow.com/a/5324532/290784](http://stackoverflow.com/a/5324532/290784)
	
**Вариант 2**. Используем веб функционал для выгрузки.

For me `wget` to the raw url turned out to be the best and easiest way to download one particular file.

Open the file in the browser and click on "Raw" button. Now refresh your browser, copy the url and do a wget or curl on it.

`wget https://github.abc.abc.com/raw/abc/folder1/master/folder2/myfile.py?token=DDDDnkl92Kw8829jhXXoxBaVJIYW-h7zks5Vy9I-wA%3D%3D -O myfile.py`

This is the easiest solution, and works for any raw txt one could find. `curl https://example.com/raw.txt > savedFile.txt`

## Не забываем делать скрипты sh исполняемыми
- [Администратор в Ubuntu, или Что такое sudo](http://help.ubuntu.ru/wiki/%D1%81%D1%83%D0%BF%D0%B5%D1%80%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C_%D0%B2_ubuntu).
- Отмечаем скрипт как исполняемый: `sudo chmod 777 путь_к_файлу` или `sudo chmod +x путь_к_файлу`.  
Чтобы запустить из командной строки, необходимо указывать полный путь: `/root/...` либо `./...`

- Следующий вопрос. Как получить в sh скрипте путь запуска скрипта? Суть в том, что данные он должен выкачивать в структуре, относительной своего расположения, а на разных машинах его размещение может меняться. Ответ смотрим здесь: [Handling positional parameters](http://wiki.bash-hackers.org/scripting/posparams). Но задача не так проста как кажется. Вот длинные дебаты: ["Getting the source directory of a Bash script from within"](http://stackoverflow.com/questions/59895/getting-the-source-directory-of-a-bash-script-from-within).
- После ответа на предыдущий вопрос натыкаемся на следующую задачу: развернуть '..' в композитном пути в полный путь. И опять начинаются дебаты и различные альтернативы. Смотрим, например, [How to convert “..” in path names to absolute name in a bash script?](http://stackoverflow.com/questions/6643853/how-to-convert-in-path-names-to-absolute-name-in-a-bash-script) или [Normalizing Path Names with Bash](http://www.linuxjournal.com/content/normalizing-path-names-bash)


## Детали по просмотру файловой структуры
Q: [How to list all the files in a tree (a directory and its subdirs)?](http://askubuntu.com/questions/15419/how-to-list-all-the-files-in-a-tree-a-directory-and-its-subdirs)  

Для просмотра древовидной структуры возможна масса вариантов.  
- `ls -alR`
- `sudo yum install tree` &  потом `tree filepath`

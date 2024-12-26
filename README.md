# auto-clean-directory
Автоочистка директрории по заполненному пространству в МБ или ГБ


## Python 3.12.2
Скрипт не имеет сторонних зависимостей/библиотек, все зависимости/библиотеки стандартные

Скрипт проверяет заполненность пространства директории, если превышен лимит, то очищает директорию


## Команда для копирования репозитория

```
git clone https://github.com/Scar333/auto-clean-directory.git
```


## Пример использования
```
# cleaner = CleaningTheDirectory(path_to_folder=r"C:\path\to\folder", memory_limit=100, unit='MB')
cleaner = CleaningTheDirectory(path_to_folder=r"C:\path\to\folder", memory_limit=1.5, unit='GB')
cleaner.start_cleaning()
```
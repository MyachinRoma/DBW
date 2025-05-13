from configparser import ConfigParser

def config(filename="database.ini", section="postgresql"):
    # Создание парсера
    parser = ConfigParser()
    # Чтение конфигурационного файла
    parser.read(filename)

    # Словарь для параметров подключения
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for key, value in params:
            db[key] = value
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename)
        )

    return db
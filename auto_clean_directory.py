# Пример использования
# cleaner = CleaningTheDirectory(path_to_folder=r"C:\path\to\folder", memory_limit=100, unit='MB')
# cleaner.start_cleaning()


import os
import shutil
import time


class CleaningTheDirectory:
    """Класс Автоочистки директории при наступлении лимита по ГБ или МБ"""

    def __init__(self, path_to_folder: str, unit: str, memory_limit: int | float) -> None:
        """Инициализация параметров

        param path_to_folder: путь до директории
        param unit: единица измерения ('GB' или 'MB')
        param memory_limit: размер в 'GB' или 'MB'
        """
        self.path_to_folder = path_to_folder
        self.unit = unit
        self.memory_limit = memory_limit

    def __check_size_folder(self) -> float:
        """Общий размер директории"""
        total_size = 0.0
        for dirpath, dirnames, filenames in os.walk(self.path_to_folder):
            for filename in filenames:
                path_to_file = os.path.join(dirpath, filename)
                total_size += os.path.getsize(path_to_file)

        if self.unit == 'GB':
            size_in_unit = total_size / (1024 ** 3)
            print(f"Размер директории: {size_in_unit:.2f} ГБ")
        elif self.unit == 'MB':
            size_in_unit = total_size / (1024 ** 2)
            print(f"Размер директории: {size_in_unit:.2f} МБ")
        else:
            raise ValueError("Неподдерживаемая единица измерения. Используйте 'GB' или 'MB'.")

        return total_size

    def start_cleaning(self) -> None:
        """Запускает проверку размера директории и удаляет её при превышении лимита"""
        total_size = self.__check_size_folder()

        if self.unit == 'GB':
            limit_in_bytes = self.memory_limit * (1024 ** 3)
        elif self.unit == 'MB':
            limit_in_bytes = self.memory_limit * (1024 ** 2)
        else:
            raise ValueError("Неподдерживаемая единица измерения. Используйте 'GB' или 'MB'.")

        if total_size > limit_in_bytes:
            print(f"Директория превышает {self.memory_limit} {self.unit}. Очистка директории...")
            shutil.rmtree(self.path_to_folder)
            time.sleep(3)
            os.makedirs(self.path_to_folder, exist_ok=True)
            print("Директория была очищена.")
        else:
            print(f"Директория меньше {self.memory_limit} {self.unit}. Очистка не требуется.")

import csv
from abc import ABC, abstractmethod


class TableOperation(ABC):

    def save_table(self, filename: str, table_to_save: list):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for item in table_to_save:
                writer.writerow(item)

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def find_new_primary_key(self):
        pass

# -*- coding: utf-8 -*-
from os import system, listdir
from abspaths import finished_structures


class LibrariesUpdater:
    @staticmethod
    def update(directory: str):
        """
        Запускает все файлы из directory
        """
        system('../../venv/Scripts/activate')
        for path in listdir(directory):
            system(f"python {directory + '/' + path}")


updater = LibrariesUpdater()
updater.update(finished_structures)

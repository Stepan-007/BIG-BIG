import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

SCREEN_SIZE = [600, 450]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)

        self.z = 17

        self.get_image()

    def get_image(self):
        map_server = "http://static-maps.yandex.ru/1.x/"
        map_params = {'ll': '37.620070,55.753630',
                      'z': self.z,
                      'l': 'map'}
        response = requests.get(map_server, map_params)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

        pixmap = QPixmap(self.map_file)
        self.image.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if self.z < 17:
                self.z += 1
            self.get_image()
        elif event.key() == Qt.Key_PageDown:
            if self.z > 0:
                self.z -= 1
            self.get_image()

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
import sys
import asyncio
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.button = QPushButton("Run Async Task", self)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.start_async_task)

    async def async_task(self):
        print("Async Task: Start")
        await asyncio.sleep(3)  # Simulate asynchronous task
        print("Async Task: End")

    def start_async_task(self):
        # Запуск асинхронной задачи в цикле событий Qt
        loop = asyncio.get_event_loop()
        loop.create_task(self.async_task())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
import sys
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import cmath
import math

# ---Функции------------------------------------------------------------------------------------------------------------
def e(x):
    return cmath.exp(x)

def ln(x):
    return cmath.log10(x)

def log(x, a):
    return cmath.log(x, a)

def cos(x):
     return cmath.cos(x)

def sin(x):
    return cmath.sin(x)

def cot(x):
    return cmath.cos(x) / cmath.sin(x)

def tan(x):
    return cmath.tan(x)

def sqrt(x):
    return cmath.sqrt(x)

def abs(x):
    return math.fabs(x)

def acos(x):
    return cmath.acos(x)

def asin(x):
    return cmath.asin(x)

def atan(x):
    return cmath.atan(x)

def acot(x):
    return cmath.atan(x) ** -1

def acosh(x):
    return cmath.acosh(x)

def asinh(x):
    return cmath.asinh(x)

def atanh(x):
    return cmath.atanh(x)

def acoth(x):
    return cmath.atanh(x) ** -1

def cosh(x):
    return cmath.cosh(x)

def sinh(x):
    return cmath.sinh(x)

def tanh(x):
    return cmath.tanh(x)

def coth(x):
    return cmath.tanh(x) ** -1

# ----------------------------------------------------------------------------------------------------------------------

def setIcon(self):                                                                                              # иконка
    appIcon = QIcon("C:\Python IMG\icon.ico")
    self.setWindowIcon(appIcon)

def show_error_message_amount_of_points(self):
    msg = QMessageBox()
    appIcon_error = QIcon("C:\Python IMG\icon1.ico")
    msg.setWindowIcon(appIcon_error)
    msg.setWindowTitle('Error')
    msg.setText('Input Error: amount of points.')
    msg.setIcon(QMessageBox.Warning)
    msg.setInformativeText("You entered not a number, or this number is not an integer")
    x = msg.exec_()

def show_step_error_step(self):
    msg = QMessageBox()
    appIcon_error = QIcon("C:\Python IMG\icon1.ico")
    msg.setWindowIcon(appIcon_error)
    msg.setWindowTitle('Error')
    msg.setText('Input Error: step.')
    msg.setIcon(QMessageBox.Warning)
    msg.setInformativeText("Non-integers are written with a dot, not a comma. or it's not a number")
    x = msg.exec_()

def show_error_function(self):
    msg = QMessageBox()
    appIcon_error = QIcon("C:\Python IMG\icon1.ico")
    msg.setWindowIcon(appIcon_error)
    msg.setWindowTitle('Error')
    msg.setText('Input Error: function.')
    msg.setIcon(QMessageBox.Warning)
    msg.setInformativeText("Invalid function")
    x = msg.exec_()

# ----------------------------------------------------------------------------------------------------------------------
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        self.setWindowTitle("Function Builder")                                                                   # Титл
        setIcon(self)                                                                            # установка иконки окна
        layout = QtWidgets.QVBoxLayout(self._main)                                                    # Создание лэйаута
        grid = QtWidgets.QGridLayout()                                                                           # сетка
        # --------------------------------------------------------------------------------------------------------------
        self.amount_of_points_line = QLineEdit()                                                          # кол-во точек
        self.amount_of_points_line.setAlignment(Qt.AlignCenter)
        self.amount_of_points_line.setStyleSheet("background-color: #2c2d2f; color: white; font: 14pt 'Arial'; border: 1px solid black; border-radius: 7px;")
        # --------------------------------------------------------------------------------------------------------------
        self.step_line = QLineEdit()                                                                               # шаг
        self.step_line.setAlignment(Qt.AlignCenter)
        self.step_line.setStyleSheet("background-color: #2c2d2f; color: white; font: 14pt 'Arial'; border: 1px solid black; border-radius: 7px;")
        # --------------------------------------------------------------------------------------------------------------
        self.func_line = QLineEdit()                                                                           # функция
        self.func_line.setAlignment(Qt.AlignCenter)
        self.func_line.setStyleSheet("background-color: #2c2d2f; color: white; font: bold 14pt 'Arial'; border: 1px solid black; border-radius: 7px;")
        # --------------------------------------------------------------------------------------------------------------
        self.amount_of_points_label = QLabel('Number of points', self)                            # Кол-во точек подпись
        self.amount_of_points_label.setStyleSheet("background-color: #2c2d2f; color: white; font: 12pt 'Arial'; border: 1px solid black; border-radius: 7px;")
        self.amount_of_points_label.setMinimumSize(QSize(100, 30))
        self.amount_of_points_label.setMaximumSize(QSize(10000, 30))
        self.amount_of_points_label.setAlignment(Qt.AlignCenter)
        # --------------------------------------------------------------------------------------------------------------
        self.step_label = QLabel('Step', self)                                                             # Шаг подпись
        self.step_label.setStyleSheet("background-color: #2c2d2f; color: white; font: 12pt 'Arial'; border: 1px solid black; border-radius: 7px;")
        self.step_label.setMinimumSize(QSize(15, 30))
        self.step_label.setMaximumSize(QSize(10000, 30))
        self.step_label.setAlignment(Qt.AlignCenter)
        # --------------------------------------------------------------------------------------------------------------
        self.func_label = QLabel('Function', self)                                                     # Функция подпись
        self.func_label.setStyleSheet("background-color: #2c2d2f; color: white; font: 12pt 'Arial'; border: 1px solid black; border-radius: 7px;")
        self.func_label.setMinimumSize(QSize(100, 30))
        self.func_label.setMaximumSize(QSize(10000, 30))
        self.func_label.setAlignment(Qt.AlignCenter)
        # --------------------------------------------------------------------------------------------------------------
        self.button = QPushButton('Plot a graph')                                                     # Кнопка построить
        self.button.setMinimumSize(300, 40)
        self.button.setFocus()
        self.button.setStyleSheet("""
                QPushButton{
                    font-weight: bold;
                    border-radius: 7px;
                    color: #ffffff;
                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #1e65d9, stop:0.90 #681999);
                    font: 12pt 'Arial'
                }
                """)
        # --------------------------------------------------------------------------------------------------------------
        self.button_clear = QPushButton('Clear')                                                        # Кнопка очистки
        self.button_clear.setMinimumSize(300, 40)
        self.button_clear.setStyleSheet("""
                        QPushButton{
                            font-weight: bold;
                            border-radius: 7px;
                            color: #ffffff;
                            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #da066d, stop:0.90 #f65f1a);
                            font: 12pt 'Arial'
                        }
                        """)
        #---пустой график-----------------------------------------------------------------------------------------------
        graph = FigureCanvas(Figure(figsize=(4, 3)))                              # Добавление пустого графика на лэйаут
        graph.setMinimumSize(QSize(400, 400))
        self.graph_plot = graph.figure.subplots()
        NavigationToolbar.toolitems = (
            ('Home', 'Reset original view', 'home', 'home'),
            ('Back', 'Back to previous view', 'back', 'back'),
            ('Forward', 'Forward to next view', 'forward', 'forward'),
            ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
            ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
            ('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'),
            ("Customize", "Edit axis, curve and image parameters", "qt4_editor_options", "edit_parameters"),
            ('Save', 'Save the figure', 'filesave', 'save_figure'),
        )
        toolbar = NavigationToolbar(graph, self)
        toolbar.setStyleSheet("background-color: none; font: 10pt 'Arial'")
        #---Цвета-------------------------------------------------------------------------------------------------------
        self._main.setStyleSheet("""
                        QWidget {
                            background-color: #191919;
                            }
                        """)
        graph.figure.set_facecolor('#191919')
        self.graph_plot.grid(color='#565656')
        self.graph_plot.set_facecolor('#191919')
        self.graph_plot.spines['bottom'].set_color('#565656')
        self.graph_plot.spines['top'].set_color('#565656')
        self.graph_plot.spines['right'].set_color('#565656')
        self.graph_plot.spines['left'].set_color('#565656')
        self.graph_plot.xaxis.label.set_color('white')
        self.graph_plot.yaxis.label.set_color('white')
        self.graph_plot.tick_params(axis='x', colors='white')
        self.graph_plot.tick_params(axis='y', colors='white')


        #---Нажатия на кнопки-------------------------------------------------------------------------------------------
        self.button.clicked.connect(self.click_on_button)                      # при нажатии на кнопку перейти к функции
        self.button_clear.clicked.connect(self.clear_graph)

        #---Отрисовка---------------------------------------------------------------------------------------------------
        layout.addWidget(toolbar)
        layout.addLayout(grid)                                                                 # добавить сетку в лэйаут
        grid.addWidget(self.amount_of_points_line, 2, 0, 1, 1)                 # разметка лайн едитов, лэйблов и кнопоки
        grid.addWidget(self.amount_of_points_label, 1, 0, 1, 1)
        grid.addWidget(self.step_line, 2, 1, 1, 1)
        grid.addWidget(self.step_label, 1, 1, 1, 1)
        grid.addWidget(self.func_line, 4, 0, 1, 2)
        grid.addWidget(self.func_label, 3, 0, 1, 2)
        layout.addWidget(self.button, alignment=Qt.AlignHCenter)
        layout.addWidget(graph)
        layout.addWidget(self.button_clear, alignment=Qt.AlignHCenter)
    # ---Функции нажатия кнопок на клавиатуре---------------------------------------------------------------------------
    def keyPressEvent(self, e):
        if e.key() in [QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return]:
            self.click_on_button()
        elif e.key() in [QtCore.Qt.Key_Alt]:
            self.clear_graph()

    # ---Аа, вспомннил! Геометрия блять---------------------------------------------------------------------------------
    def click_on_button(self):
        amount_of_points = self.amount_of_points_line.text()
        # ---Ввод кол-ва точек------------------------------------------------------------------------------------------
        amount_of_points = self.amount_of_points_line.text()
        while type(amount_of_points) != int:
            try:
                amount_of_points = int(amount_of_points)
            except ValueError:
                show_error_message_amount_of_points(self)
                amount_of_points = self.amount_of_points_line.text()
                return

        # ---Взятие кол-ва точек по модулю, чтобы нельзя было ввести отрицаетльное число--------------------------------
        amount_of_points = math.fabs(amount_of_points)

        # ---ШАГ--------------------------------------------------------------------------------------------------------
        step = self.step_line.text()
        while type(step) != float:
            try:
                step = float(step)
            except ValueError:
                show_step_error_step(self)
                step = self.step_line.text()
                return

        # ---Взятие шага по модулю, чтобы нельзя было ввести отрицаетльное число----------------------------------------
        step = math.fabs(step)

        # ---диапозон точек x от минус кол-ва точек до плюс кол-ва точек------------------------------------------------
        x = [i for i in np.arange(-(int(amount_of_points)), int(amount_of_points), float(step))]

        # ---Ввод функции построения графика----------------------------------------------------------------------------
        introduced_function = str(self.func_line.text())

        # lower необходим чтобы убрать разницу между верхними и нижними регистрами букв X и x, COS и cos----------------
        introduced_function_lower = introduced_function.lower()

        # ---исключение ошибок при вводе--------------------------------------------------------------------------------
        while True:
            try:
                Y_points = [eval(introduced_function_lower) for x in
                            np.arange(-(int(amount_of_points)), int(amount_of_points), float(step))]

                break
            except (SyntaxError, NameError, ValueError, ZeroDivisionError):
                show_error_function(self)
                introduced_function = self.func_line.text()
                introduced_function_lower = introduced_function.lower()
                return
        # ---Построение графика-----------------------------------------------------------------------------------------
        try:
            self.graph_plot.plot(x, Y_points)
            self.graph_plot.figure.canvas.draw()
        except (TypeError, SyntaxError, NameError, ValueError, ZeroDivisionError):
            show_error_function(self)
            introduced_function = self.func_line.text()
            introduced_function_lower = introduced_function.lower()
            return

    def clear_graph(self):
        self.graph_plot.clear()
        self.graph_plot.grid()
        self.graph_plot.figure.canvas.draw()


if __name__ == "__main__":                                                               # Постройка окна, и вся хренота
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec_()
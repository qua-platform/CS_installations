from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.qt_compat import QtWidgets, QtCore
from matplotlib.figure import Figure
import numpy as np

class LivePlotWindow(QtWidgets.QMainWindow):
    def __init__(self, job, timer=50):
        super().__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        self.last_poll = 0
        self.job = job
        # Window Layout
        self.setWindowTitle("QM live plotter")
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)
        # Figure
        canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.canvas = canvas
        layout.addWidget(NavigationToolbar(canvas, self))
        layout.addWidget(canvas)
        # Add pause / resume buttons
        layout_buttons = QtWidgets.QHBoxLayout()
        pause = QtWidgets.QPushButton('Pause')
        resume = QtWidgets.QPushButton('Resume')
        layout_buttons.addWidget(pause)
        layout_buttons.addWidget(resume)
        layout_buttons.addStretch()
        layout.addLayout(layout_buttons)
        self.layout_buttons = layout_buttons
        self.create_axes()
        # Polling timer
        self.timer = QtCore.QTimer(self) #in ms
        self.timer.timeout.connect(self.polldata)
        self.timer.start(timer)
        # Timer button
        pause.clicked.connect(self.timer.stop)
        resume.clicked.connect(self.timer.start)

    def create_axes(self):
        # Create plot axes
        self.ax = self.canvas.figure.subplots()

    def closeEvent(self, event):
        print("Terminating QM job.")
        self.job.halt()
        self.timer.timeout.disconnect(self.polldata)
        self.timer.stop()


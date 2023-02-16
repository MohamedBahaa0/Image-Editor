from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

    
class MplWidget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

    def Draw(self,arr):
        self.canvas.axes.clear()
        self.canvas.axes.imshow(arr,'gray')
        self.canvas.draw()
    
    def Plot(self,arr1,arr2):

        self.canvas.axes.clear()
        self.canvas.axes.bar(arr1,arr2)
        self.canvas.draw()
    
    def Clear(self):
        self.canvas.axes.clear()
        self.canvas.draw()
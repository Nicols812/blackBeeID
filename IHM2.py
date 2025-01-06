import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QGridLayout,
    QSizePolicy,
    QTabWidget
)
from PyQt5.QtGui import QPixmap

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtGui, QtWidgets



class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.setWindowTitle("Fenêtre d'édition")

    def display(self, fileName):
        layout = QVBoxLayout(self)
        label = QLabel(self)
        pixmap = QPixmap(fileName)
        label.setPixmap(pixmap)
        self.setCentralWidget(label) 
        self.setLayout(layout)
    
    def display_error_message(self):
        label = QLabel("Veuillez d'abord charger une image avant de l'éditer")
        layout = QVBoxLayout()
        self.setCentralWidget(label)
        self.setLayout(layout)
        

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Analyse des ailes d'abeilles")

        self.tab_widget = Tab(self)
        self.setCentralWidget(self.tab_widget)


class Tab(QWidget): 
    def __init__(self, parent): 
        super(QWidget, self).__init__(parent)

        self.fileName1 = "im1.png"
        self.fileName2 = "im2.png"
        self.fileName3 = "im3.png"
        self.fileName4 = "im4.png"
        self.fileName5 = "im5.png"
        self.fileName6 = "im6.png"
        self.fileName7 = "im7.png"
        self.fileName8 = "im8.png"
        self.fileName9 = "im9.png"
        self.fileName10 = "im10.png"
        self.fileName11 = "im11.png"

        self.layout = QVBoxLayout(self)
  
        # Initialize tab screen 
        self.tabs = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tab7 = QWidget()
        self.tab8 = QWidget()
        self.tab9 = QWidget()
        self.tab10 = QWidget()

        # self.tabs.resize(300, 200)
  
        # Add tabs 
        self.tabs.addTab(self.tab1, "1-5")
        self.tabs.addTab(self.tab2, "6-10")
        self.tabs.addTab(self.tab3, "11-15")
        self.tabs.addTab(self.tab4, "16-20")
        self.tabs.addTab(self.tab5, "21-25")
        self.tabs.addTab(self.tab6, "26-30")
        self.tabs.addTab(self.tab7, "31-35")
        self.tabs.addTab(self.tab8, "36-40")
        self.tabs.addTab(self.tab9, "41-45")
        self.tabs.addTab(self.tab10, "46-50")
   
        self.width = 500
        self.height = 500

        nb_tabs = 2

        self.label_left = [QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self)]
        
        self.label_right = [QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self),
                           QLabel(self), QLabel(self), QLabel(self), QLabel(self), QLabel(self)]
        
        self.dialog = [Second(self), Second(self), Second(self), Second(self), Second(self),
                        Second(self), Second(self), Second(self), Second(self), Second(self),
                        Second(self), Second(self), Second(self), Second(self), Second(self)]

        connections_load = {1:self.browseFile1, 2:self.browseFile2, 3:self.browseFile3, 4:self.browseFile4, 5:self.browseFile5,
                       6:self.browseFile6, 7:self.browseFile7, 8:self.browseFile8, 9:self.browseFile9, 10:self.browseFile10}
        
        connections_edit = {1:self.editFile1, 2:self.editFile2, 3:self.editFile3, 4:self.editFile4, 5:self.editFile5,
                       6:self.editFile6, 7:self.editFile7, 8:self.editFile8, 9:self.editFile9, 10:self.editFile10}

        self.grids = list()

        for num_tab in range(1, nb_tabs+1):

            self.grids.append(QGridLayout())

            for i in range(5):

                num_image = 5 * (num_tab - 1) + i + 1

                pixmap = QPixmap(f"im{num_image}.png")
                label_left = self.label_left[num_image-1]
                label_left.setPixmap(pixmap)
                self.grids[-1].addWidget(label_left, i, 1)

                pixmap = QPixmap(f"im{num_image}.png")
                label_right = self.label_right[num_image-1]
                label_right.setPixmap(pixmap)
                self.grids[-1].addWidget(label_right, i, 3)

                btn1 = QPushButton("Load")
                btn1.resize(50, 150)
                btn1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

                btn2 = QPushButton("Edit")
                btn2.resize(50, 150)
                btn2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

                self.grids[-1].addWidget(btn1, i, 0)
                self.grids[-1].addWidget(btn2, i, 2)

                btn1.clicked.connect(connections_load[num_image])
                btn2.clicked.connect(connections_edit[num_image])
                # btn2.clicked.connect(self.editFile)

        # Create first tab 
        self.tab1.layout = self.grids[0]
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab 
        self.tab2.layout = self.grids[1]
        self.tab2.setLayout(self.tab2.layout)

        # Final step
        # #######
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
    def editFile1(self):
        if self.fileName1 == "im1.png":
            self.dialog = Second()
            self.dialog.display_error_message()
        else:
            self.dialog = Second()
            self.dialog.display(self.fileName1)
        self.dialog.show()
        
    def editFile2(self):
        if self.fileName2 == "im2.png":
            self.dialog = Second()
            self.dialog.display_error_message()
        else:
            self.dialog = Second()
            self.dialog.display(self.fileName2)
        self.dialog.show()
    
    def editFile3(self):
        if self.fileName3 == "im3.png":
            self.dialog = Second()
            self.dialog.display_error_message()
        else:
            self.dialog = Second()
            self.dialog.display(self.fileName3)
        self.dialog.show()
    
    def editFile4(self):
        if self.fileName4 == "im4.png":
            self.dialog = Second()
            self.dialog.display_error_message()
        else:
            self.dialog = Second()
            self.dialog.display(self.fileName4)
        self.dialog.show()

    def editFile5(self):
        if self.fileName5 == "im5.png":
            self.dialog = Second()
            self.dialog.display_error_message()
        else:
            self.dialog = Second()
            self.dialog.display(self.fileName5)
        self.dialog.show()
    
    def editFile6(self):
        if self.fileName6 == "im6.png":
            self.dialog = Second()
            self.dialog.display_error_message()
        else:
            self.dialog = Second()
            self.dialog.display(self.fileName6)
        self.dialog.show()
    
    def editFile7(self):
        if self.fileName7 == "im7.png":
            self.dialog = Second()
            self.dialog.display_error_message()
        else:
            self.dialog = Second()
            self.dialog.display(self.fileName7)
        self.dialog.show()
    
    def editFile8(self):
        if self.fileName8 == "im8.png":
            self.dialog = Second()
            self.dialog.display_error_message()
        else:
            self.dialog = Second()
            self.dialog.display(self.fileName8)
        self.dialog.show()
    
    def editFile9(self):
        if self.fileName9 == "im9.png":
            self.dialog = Second()
            self.dialog.display_error_message()
        else:
            self.dialog = Second()
            self.dialog.display(self.fileName8)
        self.dialog.show()
    
    def editFile10(self):
        if self.fileName10 == "im10.png":
            self.dialog = Second()
            self.dialog.display_error_message()
        else:
            self.dialog = Second()
            self.dialog.display(self.fileName10)
        self.dialog.show()
        
    def browseFile1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName1, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if self.fileName1 != "":
            pixmap = QPixmap(self.fileName1)
            pixmap = pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.label_left[0].setPixmap(pixmap)
            self.grids[0].addWidget(self.label_left[0], 0, 1)
        else:
            pass
        # self.label_left[0].mousePressEvent = self.getPos

    def browseFile2(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName2, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if self.fileName2 != "":
            pixmap = QPixmap(self.fileName2)
            pixmap = pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.label_left[1].setPixmap(pixmap)
            self.grids[0].addWidget(self.label_left[1], 1, 1)
        else:
            pass
        # self.label_left[2].mousePressEvent = self.getPos

    def browseFile3(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName3, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if self.fileName3 != "":
            pixmap = QPixmap(self.fileName3)
            pixmap = pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.label_left[2].setPixmap(pixmap)
            self.grids[0].addWidget(self.label_left[2], 2, 1)
        else:
            pass
        # self.label_left[2].mousePressEvent = self.getPos

    def browseFile4(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName4, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if self.fileName4 != "":
            pixmap = QPixmap(self.fileName4)
            pixmap = pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.label_left[3].setPixmap(pixmap)
            self.grids[0].addWidget(self.label_left[3], 3, 1)
        else:
            pass
        # self.label_left[-1].mousePressEvent = self.getPos

    def browseFile5(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName5, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if self.fileName5 != "":
            pixmap = QPixmap(self.fileName5)
            pixmap = pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.label_left[4].setPixmap(pixmap)
            self.grids[0].addWidget(self.label_left[4], 4, 1)
        else:
            pass
        # self.label_left[-1].mousePressEvent = self.getPos

    def browseFile6(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName6, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if self.fileName6 != "":
            pixmap = QPixmap(self.fileName6)
            pixmap = pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.label_left[5].setPixmap(pixmap)
            self.grids[1].addWidget(self.label_left[5], 0, 1)
        else:
            pass
        # self.label_left[-1].mousePressEvent = self.getPos
    
    def browseFile7(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName7, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if self.fileName7 != "":
            pixmap = QPixmap(self.fileName7)
            pixmap = pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.label_left[6].setPixmap(pixmap)
            self.grids[1].addWidget(self.label_left[6], 1, 1)
        else:
            pass
        # self.label_left[7].mousePressEvent = self.getPos

    def browseFile8(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName8, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if self.fileName8 != "":
            pixmap = QPixmap(self.fileName8)
            pixmap = pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.label_left[7].setPixmap(pixmap)
            self.grids[1].addWidget(self.label_left[7], 2, 1)
        else:
            pass
        # self.label_left[8].mousePressEvent = self.getPos

    def browseFile9(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName9, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if self.fileName9 != "":
            pixmap = QPixmap(self.fileName9)
            pixmap = pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.label_left[8].setPixmap(pixmap)
            self.grids[1].addWidget(self.label_left[8], 3, 1)
        else:
            pass
        # self.label_left[9].mousePressEvent = self.getPos

    def browseFile10(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName10, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if self.fileName10 != "":
            pixmap = QPixmap(self.fileName10)
            pixmap = pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.label_left[9].setPixmap(pixmap)
            self.grids[1].addWidget(self.label_left[9], 4, 1)
        else:
            pass
        # self.label_left[10].mousePressEvent = self.getPos


    def getPos(self , event):
        x = event.pos().x()
        y = event.pos().y()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
import sys
import numpy as np
import cv2

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QDesktopWidget, QMainWindow, QPushButton, QHBoxLayout, \
    QLabel, QFileDialog, QGridLayout

import rlsb
import sp
import sxt
import wxf_test



class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.open_btn1 = QPushButton('相机单脸识别', self)
        self.open_btn1.clicked.connect(self.open)
        self.open_btn2 = QPushButton('视屏检测', self)
        self.open_btn2.clicked.connect(self.opensp)
        self.open_btn = QPushButton('打开图片', self)
        # self.open_btn.move(30,15)
        self.open_btn.clicked.connect(self.openImage)
        self.name=''

        self.open_img_show = QPixmap("")
        self.open_img_lable = QLabel(self)
        self.open_img_lable.setWordWrap(True)
        self.open_btn11 = QPushButton('相机多脸检测', self)
        self.open_btn11.clicked.connect(self.open1)




        self.test_btn = QPushButton('多脸检测', self)
        self.test_btn.clicked.connect(self.testImage)
        self.test_btn1 = QPushButton('单脸识别', self)


        self.test_btn1.clicked.connect(self.testImage1)

        self.test_img_show = QPixmap("")
        self.test_img_lable = QLabel(self)
        self.test_img_lable.setWordWrap(True)

        self.Lablename = QLabel("姓名:")
        self.Lablename1 = QLabel("")





        #self.test_info_lable = QLabel("test scores:  ", self)


        grid = QGridLayout()
        grid.setSpacing(10)


        grid.addWidget(self.open_btn, 1, 0)
        grid.addWidget(self.test_btn, 1, 1)
        grid.addWidget(self.open_img_lable, 4, 0, 11, 1)
        grid.addWidget(self.test_img_lable, 4, 1, 11, 1)
        grid.addWidget(self.Lablename,17,0)
        grid.addWidget(self.Lablename1, 17, 1)
        grid.addWidget(self.open_btn1, 2, 0)
        grid.addWidget(self.open_btn2,2,1)
        grid.addWidget(self.open_btn11, 3, 0)
        grid.addWidget(self.test_btn1, 3, 1)





        self.setLayout(grid)
        self.resize(800, 500)
        self.center()
        self.setWindowTitle('RetinaFace人脸识别')

        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def openImage(self):

        imgName, imgType = QFileDialog.getOpenFileName(self, "open", "", "*.jpg;;*.png;;All Files(*)")
        print(imgName)
        if imgName=='':
            pass
        else:
            self.name = imgName;
            open_img_show = QtGui.QPixmap(imgName)
            self.open_img_lable.setPixmap(open_img_show.scaled(self.frameGeometry().width() / 2,
                                                               self.frameGeometry().width() / 2 * open_img_show.height() / open_img_show.width()))


    def testImage1(self):
        if self.name=='':
            pass
        else:
            imagename = wxf_test.wxf(self.name)
            test_img_show = QtGui.QPixmap(imagename)
            name = rlsb.sb(self.name)
            self.test_img_lable.setPixmap(test_img_show.scaled(self.frameGeometry().width() / 2,
                                                               self.frameGeometry().width() / 2 * test_img_show.height() / test_img_show.width()))
            self.Lablename1.setText(name)
    def testImage(self):
        if self.name=='':
            pass
        else:
            imagename= wxf_test.wxf(self.name)
            test_img_show = QtGui.QPixmap(imagename)
            self.test_img_lable.setPixmap(test_img_show.scaled(self.frameGeometry().width() / 2,
                                                               self.frameGeometry().width() / 2 * test_img_show.height() / test_img_show.width()))

    def open(self):
        sxt.wxf()



    def open1(self):
        sxt.wxf2()



    def opensp(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "open", "", "*.MP4;;*.png;;All Files(*)")
        if imgName=='':
            pass
        else:
            sp.wxf(imgName)



    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "是否退出?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
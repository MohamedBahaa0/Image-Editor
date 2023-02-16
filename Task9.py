
from PyQt5 import QtCore, QtGui, QtWidgets
from re import T
import sys
import os
from turtle import clear, width
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pydicom
from tkinter import W, filedialog
from PIL import ImageQt
import PIL
from PyQt5 import QtCore, QtGui, QtWidgets
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
from matplotlib.widgets import RectangleSelector
from mplwidget import MplWidget
from skimage.transform import radon, rescale, rotate,iradon
from phantominator import shepp_logan


class Ui_DicomViewer(object):
    def setupUi(self, DicomViewer):
        DicomViewer.setObjectName("DicomViewer")
        DicomViewer.resize(1036, 990)
        self.centralwidget = QtWidgets.QWidget(DicomViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.Fourier = QtWidgets.QTabWidget(self.centralwidget)
        self.Fourier.setObjectName("Fourier")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.splitter_3 = QtWidgets.QSplitter(self.tab_3)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.information = QtWidgets.QTextBrowser(self.splitter_3)
        self.information.setObjectName("information")
        self.verticalLayout_5.addWidget(self.splitter_3)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Label_ImageView_3 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Label_ImageView_3.setFont(font)
        self.Label_ImageView_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_ImageView_3.setObjectName("Label_ImageView_3")
        self.verticalLayout_6.addWidget(self.Label_ImageView_3)
        self.ImageView_3 = QtWidgets.QGraphicsView(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageView_3.sizePolicy().hasHeightForWidth())
        self.ImageView_3.setSizePolicy(sizePolicy)
        self.ImageView_3.setObjectName("ImageView_3")
        self.verticalLayout_6.addWidget(self.ImageView_3)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.Fourier.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_NearestNeighbor = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_NearestNeighbor.setFont(font)
        self.label_NearestNeighbor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_NearestNeighbor.setObjectName("label_NearestNeighbor")
        self.verticalLayout_7.addWidget(self.label_NearestNeighbor)
        self.NearestNeighbor = QtWidgets.QGraphicsView(self.tab_4)
        self.NearestNeighbor.setObjectName("NearestNeighbor")
        self.verticalLayout_7.addWidget(self.NearestNeighbor)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(38, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_LinearInterpolation = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_LinearInterpolation.setFont(font)
        self.label_LinearInterpolation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LinearInterpolation.setObjectName("label_LinearInterpolation")
        self.verticalLayout_8.addWidget(self.label_LinearInterpolation)
        self.LinearInterpolation = QtWidgets.QGraphicsView(self.tab_4)
        self.LinearInterpolation.setObjectName("LinearInterpolation")
        self.verticalLayout_8.addWidget(self.LinearInterpolation)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_ZoomFactor = QtWidgets.QLabel(self.tab_4)
        self.label_ZoomFactor.setObjectName("label_ZoomFactor")
        self.horizontalLayout.addWidget(self.label_ZoomFactor)
        self.ZoomFactor = QtWidgets.QLineEdit(self.tab_4)
        self.ZoomFactor.setObjectName("ZoomFactor")
        self.horizontalLayout.addWidget(self.ZoomFactor)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_9, 2, 0, 1, 1)
        self.Size_textbrowser = QtWidgets.QTextBrowser(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Size_textbrowser.sizePolicy().hasHeightForWidth())
        self.Size_textbrowser.setSizePolicy(sizePolicy)
        self.Size_textbrowser.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Size_textbrowser.setObjectName("Size_textbrowser")
        self.gridLayout_2.addWidget(self.Size_textbrowser, 1, 0, 1, 1)
        self.Fourier.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.direction_textbrowser = QtWidgets.QTextBrowser(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.direction_textbrowser.sizePolicy().hasHeightForWidth())
        self.direction_textbrowser.setSizePolicy(sizePolicy)
        self.direction_textbrowser.setMaximumSize(QtCore.QSize(16777215, 40))
        self.direction_textbrowser.setObjectName("direction_textbrowser")
        self.verticalLayout.addWidget(self.direction_textbrowser)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_NearestNeighbor_4 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_NearestNeighbor_4.setFont(font)
        self.label_NearestNeighbor_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_NearestNeighbor_4.setObjectName("label_NearestNeighbor_4")
        self.verticalLayout_17.addWidget(self.label_NearestNeighbor_4)
        self.ImageT = QtWidgets.QGraphicsView(self.tab_2)
        self.ImageT.setObjectName("ImageT")
        self.verticalLayout_17.addWidget(self.ImageT)
        self.horizontalLayout_7.addLayout(self.verticalLayout_17)
        spacerItem3 = QtWidgets.QSpacerItem(38, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_LinearInterpolation_4 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_LinearInterpolation_4.setFont(font)
        self.label_LinearInterpolation_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LinearInterpolation_4.setObjectName("label_LinearInterpolation_4")
        self.verticalLayout_18.addWidget(self.label_LinearInterpolation_4)
        self.ImageTrotated = QtWidgets.QGraphicsView(self.tab_2)
        self.ImageTrotated.setObjectName("ImageTrotated")
        self.verticalLayout_18.addWidget(self.ImageTrotated)
        self.horizontalLayout_7.addLayout(self.verticalLayout_18)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.label_angle = QtWidgets.QLabel(self.tab_2)
        self.label_angle.setObjectName("label_angle")
        self.horizontalLayout_8.addWidget(self.label_angle)
        self.angleofrotation = QtWidgets.QLineEdit(self.tab_2)
        self.angleofrotation.setObjectName("angleofrotation")
        self.horizontalLayout_8.addWidget(self.angleofrotation)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.radioButton_Nearest = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_Nearest.setEnabled(True)
        self.radioButton_Nearest.setAutoFillBackground(False)
        self.radioButton_Nearest.setChecked(True)
        self.radioButton_Nearest.setObjectName("radioButton_Nearest")
        self.horizontalLayout_8.addWidget(self.radioButton_Nearest)
        self.radioButton_bilinear = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_bilinear.setObjectName("radioButton_bilinear")
        self.horizontalLayout_8.addWidget(self.radioButton_bilinear)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.gridLayout_9.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.Fourier.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4)
        self.shearedimage = QtWidgets.QGraphicsView(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shearedimage.sizePolicy().hasHeightForWidth())
        self.shearedimage.setSizePolicy(sizePolicy)
        self.shearedimage.setObjectName("shearedimage")
        self.verticalLayout_10.addWidget(self.shearedimage)
        self.gridLayout.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
        self.Fourier.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.Equlized_Image_label_3 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Equlized_Image_label_3.setFont(font)
        self.Equlized_Image_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Equlized_Image_label_3.setObjectName("Equlized_Image_label_3")
        self.verticalLayout_25.addWidget(self.Equlized_Image_label_3)
        self.EqualizedImage = QtWidgets.QGraphicsView(self.tab_5)
        self.EqualizedImage.setObjectName("EqualizedImage")
        self.verticalLayout_25.addWidget(self.EqualizedImage)
        self.gridLayout_7.addLayout(self.verticalLayout_25, 0, 0, 1, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.Histogram_label_3 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Histogram_label_3.setFont(font)
        self.Histogram_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Histogram_label_3.setObjectName("Histogram_label_3")
        self.verticalLayout_23.addWidget(self.Histogram_label_3)
        self.Original_Histogram = MplWidget(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Original_Histogram.sizePolicy().hasHeightForWidth())
        self.Original_Histogram.setSizePolicy(sizePolicy)
        self.Original_Histogram.setMinimumSize(QtCore.QSize(400, 400))
        self.Original_Histogram.setObjectName("Original_Histogram")
        self.verticalLayout_23.addWidget(self.Original_Histogram)
        self.gridLayout_6.addLayout(self.verticalLayout_23, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem7, 0, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem8, 1, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem9, 0, 0, 1, 1)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.Equalized_Histogram_label_3 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Equalized_Histogram_label_3.setFont(font)
        self.Equalized_Histogram_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Equalized_Histogram_label_3.setObjectName("Equalized_Histogram_label_3")
        self.verticalLayout_24.addWidget(self.Equalized_Histogram_label_3)
        self.EQ_Histogram = MplWidget(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EQ_Histogram.sizePolicy().hasHeightForWidth())
        self.EQ_Histogram.setSizePolicy(sizePolicy)
        self.EQ_Histogram.setMinimumSize(QtCore.QSize(500, 400))
        self.EQ_Histogram.setObjectName("EQ_Histogram")
        self.verticalLayout_24.addWidget(self.EQ_Histogram)
        self.gridLayout_6.addLayout(self.verticalLayout_24, 1, 2, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout_6)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem10)
        self.pushButton_histogram = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_histogram.setObjectName("pushButton_histogram")
        self.horizontalLayout_19.addWidget(self.pushButton_histogram)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem11)
        self.verticalLayout_13.addLayout(self.horizontalLayout_19)
        self.gridLayout_7.addLayout(self.verticalLayout_13, 1, 0, 1, 1)
        self.Fourier.addTab(self.tab_5, "")
        self.filter = QtWidgets.QWidget()
        self.filter.setObjectName("filter")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.filter)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_filtered_image = QtWidgets.QLabel(self.filter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_filtered_image.setFont(font)
        self.label_filtered_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_filtered_image.setObjectName("label_filtered_image")
        self.verticalLayout_3.addWidget(self.label_filtered_image)
        self.FilteredImage = QtWidgets.QGraphicsView(self.filter)
        self.FilteredImage.setObjectName("FilteredImage")
        self.verticalLayout_3.addWidget(self.FilteredImage)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.filterpushbutton = QtWidgets.QPushButton(self.filter)
        self.filterpushbutton.setObjectName("filterpushbutton")
        self.horizontalLayout_6.addWidget(self.filterpushbutton)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem14)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_kernelsize_3 = QtWidgets.QLabel(self.filter)
        self.label_kernelsize_3.setObjectName("label_kernelsize_3")
        self.horizontalLayout_14.addWidget(self.label_kernelsize_3)
        self.MultiplicationFactor = QtWidgets.QLineEdit(self.filter)
        self.MultiplicationFactor.setObjectName("MultiplicationFactor")
        self.horizontalLayout_14.addWidget(self.MultiplicationFactor)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem15)
        self.gridLayout_3.addLayout(self.horizontalLayout_13, 2, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem16)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_kernelsize = QtWidgets.QLabel(self.filter)
        self.label_kernelsize.setObjectName("label_kernelsize")
        self.horizontalLayout_5.addWidget(self.label_kernelsize)
        self.kernelsize = QtWidgets.QLineEdit(self.filter)
        self.kernelsize.setObjectName("kernelsize")
        self.horizontalLayout_5.addWidget(self.kernelsize)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_5)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem17)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)
        self.Fourier.addTab(self.filter, "")
        self.noise = QtWidgets.QWidget()
        self.noise.setObjectName("noise")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.noise)
        self.gridLayout_17.setObjectName("gridLayout_17")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem18, 3, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem19)
        self.Noisepushbutton = QtWidgets.QPushButton(self.noise)
        self.Noisepushbutton.setObjectName("Noisepushbutton")
        self.horizontalLayout_15.addWidget(self.Noisepushbutton)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem20)
        self.gridLayout_17.addLayout(self.horizontalLayout_15, 2, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_NearestNeighbor_6 = QtWidgets.QLabel(self.noise)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_NearestNeighbor_6.setFont(font)
        self.label_NearestNeighbor_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_NearestNeighbor_6.setObjectName("label_NearestNeighbor_6")
        self.verticalLayout_21.addWidget(self.label_NearestNeighbor_6)
        self.NoisyImage = QtWidgets.QGraphicsView(self.noise)
        self.NoisyImage.setObjectName("NoisyImage")
        self.verticalLayout_21.addWidget(self.NoisyImage)
        self.horizontalLayout_11.addLayout(self.verticalLayout_21)
        spacerItem21 = QtWidgets.QSpacerItem(38, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_11.addItem(spacerItem21)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_LinearInterpolation_6 = QtWidgets.QLabel(self.noise)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_LinearInterpolation_6.setFont(font)
        self.label_LinearInterpolation_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LinearInterpolation_6.setObjectName("label_LinearInterpolation_6")
        self.verticalLayout_22.addWidget(self.label_LinearInterpolation_6)
        self.DenoisedImage = QtWidgets.QGraphicsView(self.noise)
        self.DenoisedImage.setObjectName("DenoisedImage")
        self.verticalLayout_22.addWidget(self.DenoisedImage)
        self.horizontalLayout_11.addLayout(self.verticalLayout_22)
        self.gridLayout_17.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem22, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.noise)
        self.label_5.setGeometry(QtCore.QRect(50, 90, 256, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.Fourier.addTab(self.noise, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_mag = QtWidgets.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_mag.setFont(font)
        self.label_mag.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mag.setObjectName("label_mag")
        self.verticalLayout_19.addWidget(self.label_mag)
        self.Magnitude = QtWidgets.QGraphicsView(self.tab_6)
        self.Magnitude.setObjectName("Magnitude")
        self.verticalLayout_19.addWidget(self.Magnitude)
        self.horizontalLayout_9.addLayout(self.verticalLayout_19)
        spacerItem23 = QtWidgets.QSpacerItem(38, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_9.addItem(spacerItem23)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_LinearInterpolation_5 = QtWidgets.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_LinearInterpolation_5.setFont(font)
        self.label_LinearInterpolation_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LinearInterpolation_5.setObjectName("label_LinearInterpolation_5")
        self.verticalLayout_20.addWidget(self.label_LinearInterpolation_5)
        self.Logged_Magnitude = QtWidgets.QGraphicsView(self.tab_6)
        self.Logged_Magnitude.setObjectName("Logged_Magnitude")
        self.verticalLayout_20.addWidget(self.Logged_Magnitude)
        self.horizontalLayout_9.addLayout(self.verticalLayout_20)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_NearestNeighbor_7 = QtWidgets.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_NearestNeighbor_7.setFont(font)
        self.label_NearestNeighbor_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_NearestNeighbor_7.setObjectName("label_NearestNeighbor_7")
        self.verticalLayout_26.addWidget(self.label_NearestNeighbor_7)
        self.Phase = QtWidgets.QGraphicsView(self.tab_6)
        self.Phase.setObjectName("Phase")
        self.verticalLayout_26.addWidget(self.Phase)
        self.horizontalLayout_10.addLayout(self.verticalLayout_26)
        spacerItem24 = QtWidgets.QSpacerItem(38, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_10.addItem(spacerItem24)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_LinearInterpolation_7 = QtWidgets.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_LinearInterpolation_7.setFont(font)
        self.label_LinearInterpolation_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LinearInterpolation_7.setObjectName("label_LinearInterpolation_7")
        self.verticalLayout_27.addWidget(self.label_LinearInterpolation_7)
        self.Logged_Phase = QtWidgets.QGraphicsView(self.tab_6)
        self.Logged_Phase.setObjectName("Logged_Phase")
        self.verticalLayout_27.addWidget(self.Logged_Phase)
        self.horizontalLayout_10.addLayout(self.verticalLayout_27)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem25)
        self.Fourier_pushbutton = QtWidgets.QPushButton(self.tab_6)
        self.Fourier_pushbutton.setObjectName("Fourier_pushbutton")
        self.horizontalLayout_18.addWidget(self.Fourier_pushbutton)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem26)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.Fourier.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.label_FourierFiltered_4 = QtWidgets.QLabel(self.tab_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_FourierFiltered_4.setFont(font)
        self.label_FourierFiltered_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FourierFiltered_4.setObjectName("label_FourierFiltered_4")
        self.verticalLayout_36.addWidget(self.label_FourierFiltered_4)
        self.Fourier_Filtered = QtWidgets.QGraphicsView(self.tab_7)
        self.Fourier_Filtered.setObjectName("Fourier_Filtered")
        self.verticalLayout_36.addWidget(self.Fourier_Filtered)
        self.horizontalLayout_29.addLayout(self.verticalLayout_36)
        spacerItem27 = QtWidgets.QSpacerItem(38, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_29.addItem(spacerItem27)
        self.verticalLayout_37 = QtWidgets.QVBoxLayout()
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.label_DifferenceImage_ = QtWidgets.QLabel(self.tab_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_DifferenceImage_.setFont(font)
        self.label_DifferenceImage_.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DifferenceImage_.setObjectName("label_DifferenceImage_")
        self.verticalLayout_37.addWidget(self.label_DifferenceImage_)
        self.Difference_Image = QtWidgets.QGraphicsView(self.tab_7)
        self.Difference_Image.setObjectName("Difference_Image")
        self.verticalLayout_37.addWidget(self.Difference_Image)
        self.horizontalLayout_29.addLayout(self.verticalLayout_37)
        self.gridLayout_10.addLayout(self.horizontalLayout_29, 0, 0, 1, 1)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem28)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_kernelsize_6 = QtWidgets.QLabel(self.tab_7)
        self.label_kernelsize_6.setObjectName("label_kernelsize_6")
        self.horizontalLayout_31.addWidget(self.label_kernelsize_6)
        self.kernelsizeftt = QtWidgets.QLineEdit(self.tab_7)
        self.kernelsizeftt.setObjectName("kernelsizeftt")
        self.horizontalLayout_31.addWidget(self.kernelsizeftt)
        self.horizontalLayout_30.addLayout(self.horizontalLayout_31)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem29)
        self.gridLayout_10.addLayout(self.horizontalLayout_30, 1, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem30, 0, 0, 1, 1)
        self.frrfilterbtn = QtWidgets.QPushButton(self.tab_7)
        self.frrfilterbtn.setObjectName("frrfilterbtn")
        self.gridLayout_8.addWidget(self.frrfilterbtn, 0, 1, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem31, 0, 2, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_8, 2, 0, 1, 1)
        self.Fourier.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout()
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.label_FourierFiltered_5 = QtWidgets.QLabel(self.tab_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_FourierFiltered_5.setFont(font)
        self.label_FourierFiltered_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FourierFiltered_5.setObjectName("label_FourierFiltered_5")
        self.verticalLayout_38.addWidget(self.label_FourierFiltered_5)
        self.ImagePattern = QtWidgets.QGraphicsView(self.tab_8)
        self.ImagePattern.setObjectName("ImagePattern")
        self.verticalLayout_38.addWidget(self.ImagePattern)
        self.horizontalLayout_32.addLayout(self.verticalLayout_38)
        spacerItem32 = QtWidgets.QSpacerItem(38, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_32.addItem(spacerItem32)
        self.verticalLayout_39 = QtWidgets.QVBoxLayout()
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.label_DifferenceImage_1 = QtWidgets.QLabel(self.tab_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_DifferenceImage_1.setFont(font)
        self.label_DifferenceImage_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DifferenceImage_1.setObjectName("label_DifferenceImage_1")
        self.verticalLayout_39.addWidget(self.label_DifferenceImage_1)
        self.Patternremoved = QtWidgets.QGraphicsView(self.tab_8)
        self.Patternremoved.setObjectName("Patternremoved")
        self.verticalLayout_39.addWidget(self.Patternremoved)
        self.horizontalLayout_32.addLayout(self.verticalLayout_39)
        self.gridLayout_11.addLayout(self.horizontalLayout_32, 0, 0, 1, 1)
        self.Fourier.addTab(self.tab_8, "")
        self.ROI = QtWidgets.QWidget()
        self.ROI.setObjectName("ROI")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.ROI)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.Histogram_label_4 = QtWidgets.QLabel(self.ROI)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Histogram_label_4.setFont(font)
        self.Histogram_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Histogram_label_4.setObjectName("Histogram_label_4")
        self.verticalLayout_29.addWidget(self.Histogram_label_4)
        self.ROIHistogram = MplWidget(self.ROI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROIHistogram.sizePolicy().hasHeightForWidth())
        self.ROIHistogram.setSizePolicy(sizePolicy)
        self.ROIHistogram.setMinimumSize(QtCore.QSize(400, 300))
        self.ROIHistogram.setObjectName("ROIHistogram")
        self.verticalLayout_29.addWidget(self.ROIHistogram)
        self.gridLayout_12.addLayout(self.verticalLayout_29, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_12, 4, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem33)
        self.checkBox_uniform = QtWidgets.QCheckBox(self.ROI)
        self.checkBox_uniform.setObjectName("checkBox_uniform")
        self.horizontalLayout_4.addWidget(self.checkBox_uniform)
        spacerItem34 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem34)
        self.checkBox_gaussian = QtWidgets.QCheckBox(self.ROI)
        self.checkBox_gaussian.setObjectName("checkBox_gaussian")
        self.horizontalLayout_4.addWidget(self.checkBox_gaussian)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem35)
        self.pushROI = QtWidgets.QPushButton(self.ROI)
        self.pushROI.setObjectName("pushROI")
        self.horizontalLayout_4.addWidget(self.pushROI)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem36)
        self.gridLayout_13.addLayout(self.horizontalLayout_4, 2, 0, 1, 2)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.Histogram_label_5 = QtWidgets.QLabel(self.ROI)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Histogram_label_5.setFont(font)
        self.Histogram_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.Histogram_label_5.setObjectName("Histogram_label_5")
        self.verticalLayout_28.addWidget(self.Histogram_label_5)
        self.ROIimage = MplWidget(self.ROI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROIimage.sizePolicy().hasHeightForWidth())
        self.ROIimage.setSizePolicy(sizePolicy)
        self.ROIimage.setMinimumSize(QtCore.QSize(400, 300))
        self.ROIimage.setObjectName("ROIimage")
        self.verticalLayout_28.addWidget(self.ROIimage)
        self.gridLayout_13.addLayout(self.verticalLayout_28, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.ROI)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_13.addWidget(self.line_2, 1, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.ROI)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_13.addWidget(self.line, 3, 0, 1, 2)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.ROINoisedimage = QtWidgets.QLabel(self.ROI)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ROINoisedimage.setFont(font)
        self.ROINoisedimage.setAlignment(QtCore.Qt.AlignCenter)
        self.ROINoisedimage.setObjectName("ROINoisedimage")
        self.verticalLayout_30.addWidget(self.ROINoisedimage)
        self.Original_Histogram_6 = MplWidget(self.ROI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Original_Histogram_6.sizePolicy().hasHeightForWidth())
        self.Original_Histogram_6.setSizePolicy(sizePolicy)
        self.Original_Histogram_6.setMinimumSize(QtCore.QSize(400, 300))
        self.Original_Histogram_6.setObjectName("Original_Histogram_6")
        self.verticalLayout_30.addWidget(self.Original_Histogram_6)
        self.gridLayout_13.addLayout(self.verticalLayout_30, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.ROI)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.textbrowser_histogram_2 = QtWidgets.QTextBrowser(self.groupBox)
        self.textbrowser_histogram_2.setObjectName("textbrowser_histogram_2")
        self.gridLayout_15.addWidget(self.textbrowser_histogram_2, 0, 0, 1, 1)
        self.gridLayout_13.addWidget(self.groupBox, 5, 0, 1, 2)
        self.Fourier.addTab(self.ROI, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem37, 1, 2, 1, 1)
        self.SheppLogan = MplWidget(self.tab_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SheppLogan.sizePolicy().hasHeightForWidth())
        self.SheppLogan.setSizePolicy(sizePolicy)
        self.SheppLogan.setMinimumSize(QtCore.QSize(400, 300))
        self.SheppLogan.setObjectName("SheppLogan")
        self.gridLayout_20.addWidget(self.SheppLogan, 1, 1, 1, 1)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem38, 1, 0, 1, 1)
        self.ROINoisedimage_15 = QtWidgets.QLabel(self.tab_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ROINoisedimage_15.setFont(font)
        self.ROINoisedimage_15.setAlignment(QtCore.Qt.AlignCenter)
        self.ROINoisedimage_15.setObjectName("ROINoisedimage_15")
        self.gridLayout_20.addWidget(self.ROINoisedimage_15, 0, 1, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout_20)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout()
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.ROINoisedimage_14 = QtWidgets.QLabel(self.tab_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ROINoisedimage_14.setFont(font)
        self.ROINoisedimage_14.setAlignment(QtCore.Qt.AlignCenter)
        self.ROINoisedimage_14.setObjectName("ROINoisedimage_14")
        self.verticalLayout_47.addWidget(self.ROINoisedimage_14)
        self.Sinogram = MplWidget(self.tab_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sinogram.sizePolicy().hasHeightForWidth())
        self.Sinogram.setSizePolicy(sizePolicy)
        self.Sinogram.setMinimumSize(QtCore.QSize(400, 300))
        self.Sinogram.setObjectName("Sinogram")
        self.verticalLayout_47.addWidget(self.Sinogram)
        self.horizontalLayout_22.addLayout(self.verticalLayout_47)
        self.verticalLayout_48 = QtWidgets.QVBoxLayout()
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.ROINoisedimage_16 = QtWidgets.QLabel(self.tab_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ROINoisedimage_16.setFont(font)
        self.ROINoisedimage_16.setAlignment(QtCore.Qt.AlignCenter)
        self.ROINoisedimage_16.setObjectName("ROINoisedimage_16")
        self.verticalLayout_48.addWidget(self.ROINoisedimage_16)
        self.Laminogram = MplWidget(self.tab_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Laminogram.sizePolicy().hasHeightForWidth())
        self.Laminogram.setSizePolicy(sizePolicy)
        self.Laminogram.setMinimumSize(QtCore.QSize(400, 300))
        self.Laminogram.setObjectName("Laminogram")
        self.verticalLayout_48.addWidget(self.Laminogram)
        self.horizontalLayout_22.addLayout(self.verticalLayout_48)
        self.verticalLayout_11.addLayout(self.horizontalLayout_22)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.NoFilter = QtWidgets.QRadioButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NoFilter.sizePolicy().hasHeightForWidth())
        self.NoFilter.setSizePolicy(sizePolicy)
        self.NoFilter.setObjectName("NoFilter")
        self.horizontalLayout_3.addWidget(self.NoFilter)
        self.RamLak = QtWidgets.QRadioButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RamLak.sizePolicy().hasHeightForWidth())
        self.RamLak.setSizePolicy(sizePolicy)
        self.RamLak.setObjectName("RamLak")
        self.horizontalLayout_3.addWidget(self.RamLak)
        self.Hamming = QtWidgets.QRadioButton(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hamming.sizePolicy().hasHeightForWidth())
        self.Hamming.setSizePolicy(sizePolicy)
        self.Hamming.setObjectName("Hamming")
        self.horizontalLayout_3.addWidget(self.Hamming)
        self.gridLayout_16.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_21.addWidget(self.groupBox_6)
        spacerItem39 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_21.addItem(spacerItem39)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.Angle20 = QtWidgets.QRadioButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Angle20.sizePolicy().hasHeightForWidth())
        self.Angle20.setSizePolicy(sizePolicy)
        self.Angle20.setObjectName("Angle20")
        self.horizontalLayout_16.addWidget(self.Angle20)
        self.AllAngles = QtWidgets.QRadioButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AllAngles.sizePolicy().hasHeightForWidth())
        self.AllAngles.setSizePolicy(sizePolicy)
        self.AllAngles.setObjectName("AllAngles")
        self.horizontalLayout_16.addWidget(self.AllAngles)
        self.gridLayout_22.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)
        self.horizontalLayout_21.addWidget(self.groupBox_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem40 = QtWidgets.QSpacerItem(311, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem40)
        self.PBLamino_2 = QtWidgets.QPushButton(self.tab_9)
        self.PBLamino_2.setObjectName("PBLamino_2")
        self.horizontalLayout_20.addWidget(self.PBLamino_2)
        spacerItem41 = QtWidgets.QSpacerItem(311, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem41)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.verticalLayout_11.addLayout(self.verticalLayout_2)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.gridLayout_21.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.Fourier.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.groupBox_8.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.rB_Dilation = QtWidgets.QRadioButton(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rB_Dilation.sizePolicy().hasHeightForWidth())
        self.rB_Dilation.setSizePolicy(sizePolicy)
        self.rB_Dilation.setObjectName("rB_Dilation")
        self.horizontalLayout_17.addWidget(self.rB_Dilation)
        self.rB_Erosion = QtWidgets.QRadioButton(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rB_Erosion.sizePolicy().hasHeightForWidth())
        self.rB_Erosion.setSizePolicy(sizePolicy)
        self.rB_Erosion.setObjectName("rB_Erosion")
        self.horizontalLayout_17.addWidget(self.rB_Erosion)
        self.rB_Opening = QtWidgets.QRadioButton(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rB_Opening.sizePolicy().hasHeightForWidth())
        self.rB_Opening.setSizePolicy(sizePolicy)
        self.rB_Opening.setObjectName("rB_Opening")
        self.horizontalLayout_17.addWidget(self.rB_Opening)
        self.rB_Closing = QtWidgets.QRadioButton(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rB_Closing.sizePolicy().hasHeightForWidth())
        self.rB_Closing.setSizePolicy(sizePolicy)
        self.rB_Closing.setObjectName("rB_Closing")
        self.horizontalLayout_17.addWidget(self.rB_Closing)
        self.gridLayout_18.addLayout(self.horizontalLayout_17, 1, 0, 1, 1)
        self.gridLayout_19.addWidget(self.groupBox_8, 1, 0, 1, 1)
        self.verticalLayout_49 = QtWidgets.QVBoxLayout()
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.ROINoisedimage_17 = QtWidgets.QLabel(self.tab_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ROINoisedimage_17.setFont(font)
        self.ROINoisedimage_17.setAlignment(QtCore.Qt.AlignCenter)
        self.ROINoisedimage_17.setObjectName("ROINoisedimage_17")
        self.verticalLayout_49.addWidget(self.ROINoisedimage_17)
        self.Morph = MplWidget(self.tab_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Morph.sizePolicy().hasHeightForWidth())
        self.Morph.setSizePolicy(sizePolicy)
        self.Morph.setMinimumSize(QtCore.QSize(400, 300))
        self.Morph.setObjectName("Morph")
        self.verticalLayout_49.addWidget(self.Morph)
        self.gridLayout_19.addLayout(self.verticalLayout_49, 0, 0, 1, 1)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem42 = QtWidgets.QSpacerItem(311, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem42)
        self.PBLamino_3 = QtWidgets.QPushButton(self.tab_10)
        self.PBLamino_3.setObjectName("PBLamino_3")
        self.horizontalLayout_23.addWidget(self.PBLamino_3)
        spacerItem43 = QtWidgets.QSpacerItem(311, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem43)
        self.gridLayout_19.addLayout(self.horizontalLayout_23, 2, 0, 1, 1)
        self.Fourier.addTab(self.tab_10, "")
        self.gridLayout_14.addWidget(self.Fourier, 0, 0, 1, 1)
        DicomViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DicomViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1036, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        DicomViewer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DicomViewer)
        self.statusbar.setObjectName("statusbar")
        DicomViewer.setStatusBar(self.statusbar)
        self.actionBrowse = QtWidgets.QAction(DicomViewer)
        self.actionBrowse.setObjectName("actionBrowse")
        self.menuFile.addAction(self.actionBrowse)
        self.menubar.addAction(self.menuFile.menuAction())
        
        self.scene = QGraphicsScene()
        self.ImageView_3.setScene(self.scene)
        self.scene_nearest = QGraphicsScene()
        self.NearestNeighbor.setScene(self.scene_nearest)
        self.scene_bilinear = QGraphicsScene()
        self.LinearInterpolation.setScene(self.scene_bilinear)
        self.scene_imageT = QGraphicsScene()
        self.ImageT.setScene(self.scene_imageT)
        self.scene_imageTrotated = QGraphicsScene()
        self.ImageTrotated.setScene(self.scene_imageTrotated)
        self.scene_imagesheared = QGraphicsScene()
        self.shearedimage.setScene(self.scene_imagesheared)        
        self.scene_histogram = QGraphicsScene()
        self.EqualizedImage.setScene(self.scene_histogram) 
        self.scene_filteredimage = QGraphicsScene()
        self.FilteredImage.setScene(self.scene_filteredimage) 
        self.scene_noisyimage = QGraphicsScene()
        self.NoisyImage.setScene(self.scene_noisyimage) 
        self.scene_denoisedimage = QGraphicsScene()
        self.DenoisedImage.setScene(self.scene_denoisedimage) 
        self.scene_magnitude = QGraphicsScene()
        self.Magnitude.setScene(self.scene_magnitude)
        self.scene_loggedmagnitude = QGraphicsScene()
        self.Logged_Magnitude.setScene(self.scene_loggedmagnitude)        
        self.scene_loggedphase = QGraphicsScene()
        self.Logged_Phase.setScene(self.scene_loggedphase)
        self.scene_phase = QGraphicsScene()
        self.Phase.setScene(self.scene_phase)
        self.scene_fourierfilter = QGraphicsScene()
        self.Fourier_Filtered.setScene(self.scene_fourierfilter)
        self.Difference_scene= QGraphicsScene()
        self.Difference_Image.setScene(self.Difference_scene)
        self.scene_ImagePattern= QGraphicsScene()
        self.ImagePattern.setScene(self.scene_ImagePattern)
        self.scene_Patternremoved= QGraphicsScene()
        self.Patternremoved.setScene(self.scene_Patternremoved)

        self.actionBrowse.triggered.connect(self.imageSelect)
        self.pushButton.clicked.connect(self.imageShearing)
        self.ZoomFactor.returnPressed.connect(self.nearest_interpolation)
        self.ZoomFactor.returnPressed.connect(self.interpolate_bilinear)
        self.angleofrotation.returnPressed.connect(self.ImageRotation)
        self.imageTcreator()
        self.pushButton_histogram.clicked.connect(self.histogram)
        self.pushButton.clicked.connect(self.imageShearing)
        self.filterpushbutton.clicked.connect(self.filtering)
        self.Noisepushbutton.clicked.connect(self.Noisefilter)
        self.Fourier_pushbutton.clicked.connect(self.fourier)        
        self.frrfilterbtn.clicked.connect(self.fftfilter)  
        self.frrfilterbtn.clicked.connect(self.filteer) 
        self.showROIimage()
        self.DrawSheppLogan()
        self.pushROI.clicked.connect(self.showROINoise)
        #self.pushROI.clicked.connect(self.ROISelect)
        self.PBLamino_2.clicked.connect(self.DrawLaminogram)
        self.PBLamino_3.clicked.connect(self.Morphological)

        self.retranslateUi(DicomViewer)
        self.Fourier.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DicomViewer)

    def retranslateUi(self, DicomViewer):
        _translate = QtCore.QCoreApplication.translate
        DicomViewer.setWindowTitle(_translate("DicomViewer", "MainWindow"))
        self.label_3.setText(_translate("DicomViewer", "Information"))
        self.Label_ImageView_3.setText(_translate("DicomViewer", "Image Viewer"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.tab_3), _translate("DicomViewer", "Image"))
        self.label.setText(_translate("DicomViewer", "Size"))
        self.label_NearestNeighbor.setText(_translate("DicomViewer", "Nearest neighbor"))
        self.label_LinearInterpolation.setText(_translate("DicomViewer", "Linear interpolation"))
        self.label_ZoomFactor.setText(_translate("DicomViewer", "Zoom Factor"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.tab_4), _translate("DicomViewer", "Zoomed"))
        self.label_6.setText(_translate("DicomViewer", "size and direction"))
        self.label_NearestNeighbor_4.setText(_translate("DicomViewer", "image T"))
        self.label_LinearInterpolation_4.setText(_translate("DicomViewer", "rotated image"))
        self.label_angle.setText(_translate("DicomViewer", "Angle of rotation"))
        self.radioButton_Nearest.setText(_translate("DicomViewer", "Nearest"))
        self.radioButton_bilinear.setText(_translate("DicomViewer", "Bilinear"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.tab_2), _translate("DicomViewer", "Rotate"))
        self.label_4.setText(_translate("DicomViewer", "Sheared image"))
        self.pushButton.setText(_translate("DicomViewer", "Shear"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.tab), _translate("DicomViewer", "Shear"))
        self.Equlized_Image_label_3.setText(_translate("DicomViewer", "Equalized Image"))
        self.Histogram_label_3.setText(_translate("DicomViewer", "Histogram"))
        self.Equalized_Histogram_label_3.setText(_translate("DicomViewer", "Equalized Histogram"))
        self.pushButton_histogram.setText(_translate("DicomViewer", "Equalize"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.tab_5), _translate("DicomViewer", "Histogram"))
        self.label_filtered_image.setText(_translate("DicomViewer", "Filtered image"))
        self.filterpushbutton.setText(_translate("DicomViewer", "Filter"))
        self.label_kernelsize_3.setText(_translate("DicomViewer", "Multiplication Factor"))
        self.label_kernelsize.setText(_translate("DicomViewer", "Kernel size"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.filter), _translate("DicomViewer", "Filter"))
        self.Noisepushbutton.setText(_translate("DicomViewer", "Filter"))
        self.label_NearestNeighbor_6.setText(_translate("DicomViewer", "Noisy image"))
        self.label_LinearInterpolation_6.setText(_translate("DicomViewer", "De-noised image"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.noise), _translate("DicomViewer", "Noise "))
        self.label_mag.setText(_translate("DicomViewer", "Magnitude "))
        self.label_LinearInterpolation_5.setText(_translate("DicomViewer", "Logged Magnitude"))
        self.label_NearestNeighbor_7.setText(_translate("DicomViewer", "Phase"))
        self.label_LinearInterpolation_7.setText(_translate("DicomViewer", "Logged Phase"))
        self.Fourier_pushbutton.setText(_translate("DicomViewer", "Display"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.tab_6), _translate("DicomViewer", "Fourier "))
        self.label_FourierFiltered_4.setText(_translate("DicomViewer", "Filtered Image"))
        self.label_DifferenceImage_.setText(_translate("DicomViewer", "Difference Image"))
        self.label_kernelsize_6.setText(_translate("DicomViewer", "Kernel size"))
        self.frrfilterbtn.setText(_translate("DicomViewer", "Filter"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.tab_7), _translate("DicomViewer", "Filter Fourier"))
        self.label_FourierFiltered_5.setText(_translate("DicomViewer", " Image"))
        self.label_DifferenceImage_1.setText(_translate("DicomViewer", "Filtered Image"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.tab_8), _translate("DicomViewer", "Pattern"))
        self.Histogram_label_4.setText(_translate("DicomViewer", "Histogram"))
        self.checkBox_uniform.setText(_translate("DicomViewer", "Uniform"))
        self.checkBox_gaussian.setText(_translate("DicomViewer", "Gaussian"))
        self.pushROI.setText(_translate("DicomViewer", "Add noise"))
        self.Histogram_label_5.setText(_translate("DicomViewer", "Image"))
        self.ROINoisedimage.setText(_translate("DicomViewer", "Noised Image"))
        self.groupBox.setTitle(_translate("DicomViewer", "information"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.ROI), _translate("DicomViewer", "ROI"))
        self.ROINoisedimage_15.setText(_translate("DicomViewer", "Shepp-Logan"))
        self.ROINoisedimage_14.setText(_translate("DicomViewer", "Sinogram"))
        self.ROINoisedimage_16.setText(_translate("DicomViewer", "Laminogram"))
        self.groupBox_6.setTitle(_translate("DicomViewer", "Filters"))
        self.NoFilter.setText(_translate("DicomViewer", "No filter"))
        self.RamLak.setText(_translate("DicomViewer", "Ram-Lak"))
        self.Hamming.setText(_translate("DicomViewer", "Hamming"))
        self.groupBox_7.setTitle(_translate("DicomViewer", "Angles"))
        self.Angle20.setText(_translate("DicomViewer", "[20,40,60 ..]"))
        self.AllAngles.setText(_translate("DicomViewer", "[0,1,2,3..179]"))
        self.PBLamino_2.setText(_translate("DicomViewer", "Display"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.tab_9), _translate("DicomViewer", "Back Projection"))
        self.groupBox_8.setTitle(_translate("DicomViewer", "Process"))
        self.rB_Dilation.setText(_translate("DicomViewer", "Dilation"))
        self.rB_Erosion.setText(_translate("DicomViewer", "Erosion"))
        self.rB_Opening.setText(_translate("DicomViewer", "Opening"))
        self.rB_Closing.setText(_translate("DicomViewer", "Closing"))
        self.ROINoisedimage_17.setText(_translate("DicomViewer", "Morphological Figures"))
        self.PBLamino_3.setText(_translate("DicomViewer", "Display"))
        self.Fourier.setTabText(self.Fourier.indexOf(self.tab_10), _translate("DicomViewer", "Morphological"))
        self.menuFile.setTitle(_translate("DicomViewer", "File"))
        self.actionBrowse.setText(_translate("DicomViewer", "Browse"))



    def imageSelect(self):
       
        self.path = filedialog.askopenfilename(filetypes=[("Images" ,".dcm .jpg .bmp .png .jpeg" )])
        ext = os.path.splitext(self.path)[-1].lower()
        self.scene.clear()
        self.information.clear()
        if self.path == "": #handling if user didn't enter a photo
            return  
        if ext == ".dcm":
            # handling corrupt DICOM images
            try:
                dicomfile = pydicom.dcmread(self.path)
            except ( pydicom.errors.InvalidDicomError , SyntaxError) as e:
                self.information.append('Bad File')
                QMessageBox.critical(self.centralwidget,"Error","Corrupt file ")

                return
            dicomfile = pydicom.dcmread(self.path)
            fileinfo= pydicom.read_file(self.path)
            image=dicomfile.pixel_array.astype(float)
            rescaled_image = (np.maximum(image,0)/image.max())*255 # float pixels
            final_image = np.uint8(rescaled_image) # integers pixels (8 unsigned bits)
            final_image = PIL.Image.fromarray(final_image)
            final_image.save('now_image.jpg')  
            self.path ='now_image.jpg'
            
            #Dicom info 
            Age_line= 'Age = '+ str(fileinfo.get("PatientAge"))
            self.information.append(Age_line)
            self.information.append(" ")
            Modality_line= 'Modality = '+ str(fileinfo.get("Modality"))
            self.information.append(Modality_line)
            self.information.append(" ")
            Name_line= 'Patient Name = '+ str(fileinfo.get("PatientName"))
            self.information.append(Name_line)
            self.information.append(" ")
            BodyPart_line= 'Body Part Examined = '+ str(fileinfo.get("BodyPartExammined"))
            self.information.append(BodyPart_line)
        
        # handling corrupt images
        
        try:
            self.imgReady = PIL.Image.open(self.path)
        except (PIL.UnidentifiedImageError):
            self.information.append('COURRUPT File') 
            QMessageBox.critical(self.centralwidget,"Error","Corrupt photo ")

            return
        

        w, h = self.imgReady.size
        self.imgQ = ImageQt.ImageQt(self.imgReady)  # we need to hold reference to imgQ, or it will crash
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene.addPixmap(pixMap)
        SizeInBytes = int(os.stat(self.path).st_size)
        SizeInBits = SizeInBytes*8
#        self.ImageView.fitInView(QRectF(0, 0, w, h) , Qt.KeepAspectRatio)
        self.scene.update()
        
        mode_to_bitdepth = {'1':1, 'L':8, 'P':8, 'RGB':24, 'RGBA':32, 'CMYK':32, 'YCbCr':24, 'I':32, 'F':32}
        bitdepth = mode_to_bitdepth[self.imgReady.mode]
        self.information.append(" ")
        Color_line= 'Image Color = ' + str(self.imgReady.mode)
        self.information.append(Color_line) #RGB or Grayscale
        self.information.append(" ")
        Rows_line = ' Rows X Columns = '+ str(h) +" x "+ str(w) 
        self.information.append(Rows_line)
        self.information.append(" ")
        PixelDepth_line = 'Bit Depth = '+ str(bitdepth)
        self.information.append(PixelDepth_line)
        self.information.append(" ")
        Size_line= 'Size (Bits) =' + str(SizeInBits)
        self.information.append(Size_line)
        self.imgReady = PIL.Image.open(self.path).convert('L')

    def nearest_interpolation(self):
        '''Nearest neighbor interpolation method to convert small image to original image

        Returns:
        numpy.ndarray: Resized image
        '''
        self.Size_textbrowser.clear()
        self.scene_nearest.clear()
        try:
            float(self.ZoomFactor.text())           
        except:
            QMessageBox.critical(self.centralwidget,"Error","Please enter a number ")
            return

        try:
            self.imgReady is None           
        except:
            QMessageBox.critical(self.centralwidget,"Error","Please enter a photo first ")
            return
        if float(self.ZoomFactor.text())<=0:
            QMessageBox.warning(self.centralwidget,"Error","Please enter a postive number ")
            return
        width,height = self.imgReady.size
        dimension0= round(width* float(self.ZoomFactor.text()))
        dimension1=round(height * float(self.ZoomFactor.text()))
        new_image = np.zeros((dimension1, dimension0))

        for i in range(dimension0):
            for j in range(dimension1):
                row = math.floor(i /  float(self.ZoomFactor.text()))
                column = math.floor(j /  float(self.ZoomFactor.text()))

                new_image[j, i] = self.imgReady.getpixel((row,column))
        ImageNearest = PIL.Image.fromarray(new_image)
        w,h = ImageNearest.size
        ImageNearest = ImageNearest.convert('L')
        self.imgQ = ImageQt.ImageQt(ImageNearest)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_nearest.addPixmap(pixMap)
        self.scene.update() 
        self.Size_textbrowser.append(str(h)+'x'+str(w))
    
    def interpolate_bilinear(self):
        self.scene_bilinear.clear()
        try:
            float(self.ZoomFactor.text())           
            self.imgReady is None           
        except:
            return

        if float(self.ZoomFactor.text())<=0:
            return
        width,height = self.imgReady.size
        dimension0= round(width* float(self.ZoomFactor.text()))
        dimension1=round(height * float(self.ZoomFactor.text()))
        new_image = np.zeros((dimension1, dimension0))
        y_ratio = float(width - 1) / (dimension0 - 1) if dimension0 > 1 else 0
        x_ratio = float(height - 1) / (dimension1 - 1) if dimension1 > 1 else 0
        for i in range(dimension0):
            for j in range(dimension1):
                x_l, y_l = math.floor(x_ratio * j), math.floor(y_ratio * i)
                x_h, y_h = math.ceil(x_ratio * j), math.ceil(y_ratio * i)

                x_weight = (x_ratio * j) - x_l
                y_weight = (y_ratio * i) - y_l

                try:    
                    a = self.imgReady.getpixel((y_l, x_l))
                    b = self.imgReady.getpixel((y_l, x_h))
                    c = self.imgReady.getpixel((y_h, x_l))
                    d = self.imgReady.getpixel((y_h, x_h))

                    pixel = a * (1 - x_weight) * (1 - y_weight) + b * x_weight * (1 - y_weight) + c * y_weight * (1 - x_weight) + d * x_weight * y_weight
                
                    new_image[j][i] = pixel
                except:    
                    pass
        # Interpolate over layers
        Imagebilinear = PIL.Image.fromarray(new_image)
        Imagebilinear = Imagebilinear.convert('L')
        self.imgQ = ImageQt.ImageQt(Imagebilinear)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_bilinear.addPixmap(pixMap)
        self.scene_bilinear.update()


    def imageTcreator(self):
        self.imageTarray=np.zeros((128, 128))
        #Drawing Horiontal line of T 
        for i in range (29,99):
            for j in range (29,49):
                self.imageTarray[j,i]= 255
        #Drawing Vertical line of T 
        for i in range (54,74):
            for j in range (49,99):
                self.imageTarray[j,i]= 255
        imageT = PIL.Image.fromarray(self.imageTarray)
        imageT = imageT.convert('L')
        self.imgQ = ImageQt.ImageQt(imageT)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_imageT.addPixmap(pixMap)
        #self.ImageT.fitInView(QRectF(0, 0, 128, 128) , Qt.KeepAspectRatio)
        self.scene_imageT.update()

    def ImageRotation(self):

        self.direction_textbrowser.clear()

        self.direction_textbrowser.append('Image is rotated by '+self.angleofrotation.text() +' anti-clockwise')
        
        try:
            float(self.angleofrotation.text())           
        except:
            QMessageBox.critical(self.centralwidget,"Error","Please enter a number ")
            return
        rotation_amount_degree = float(self.angleofrotation.text())

        rotation_amount_rad = rotation_amount_degree * np.pi / 180.0
        (width,height) = self.imageTarray.shape
        width=int(width)
        height=int(height)
        rotated_image = np.zeros((width,height))
        self.direction_textbrowser.append('Image Dimension = '+ str(width) + 'x'+ str(height))

        rotated_height, rotated_width = 128,128
        mid_row = math.floor( (rotated_height+1)/2 )
        mid_col = math.floor( (rotated_width+1)/2 )


        for r in range(rotated_height):
            for c in range(rotated_width):
                #  apply rotation matrix, the other way
                y = (r-mid_col)*math.cos(rotation_amount_rad) + (c-mid_row)*math.sin(rotation_amount_rad)
                x = -(r-mid_col)*math.sin(rotation_amount_rad) + (c-mid_row)*math.cos(rotation_amount_rad)

                #  add offset
                y += mid_col
                x += mid_row

                if self.radioButton_Nearest.isChecked():
                    x = round(x)
                    y = round(y)

                    if (x >= 0 and y >= 0 and x < rotated_width and y < rotated_height):
                        rotated_image[r][c] = self.imageTarray[y][x]
                
                else:
                    # #Linear Interpolation
                    x_l, y_l = math.floor(x), math.floor(y)
                    if math.ceil(x) <  rotated_height -1:
                        x_h = math.ceil(x)
                    else:
                        x_h= rotated_height -1
                    if math.ceil(y) <  rotated_width -1:
                        y_h = math.ceil(y)
                    else:
                        y_h=rotated_width -1 
                    # if x_h > rotated_height-1:
                    #     x_h= rotated_height-1
                    # if x_l > rotated_height-1:
                    #     x_l= rotated_height-1
                    # if y_h > rotated_width-1:
                    #     y_h= rotated_width-1    
                    # if y_l > rotated_width-1:
                    #     y_l= rotated_width-1
                    if (x >= 0 and y >= 0 and x < rotated_width and y < rotated_height):
                        x_weight = x  - x_l
                        y_weight = y  - y_l
                        if (x_h == x_l) and (y_h == y_l):
                            pixel = self.imageTarray[int(y)][int(x)]
                        elif (y_h == y_l):
                            q1 = self.imageTarray[int(y)][ int(x_l)]
                            q2 = self.imageTarray[int(y)][ int(x_h)]
                            pixel = q1 * (1-x_weight) + q2 * (x_weight)
                        elif (x_h == x_l):
                            q1 = self.imageTarray[int(y_l)][int(x)]
                            q2 = self.imageTarray[int(y_h)][int(x)]
                            pixel = (q1 * (1-y_weight)) + (q2	 * (y_weight))
                        else:
                            PUpleft = self.imageTarray[y_l][x_l]
                            v2 = self.imageTarray[y_h][ x_l]
                            v3 = self.imageTarray[y_l][ x_h]
                            v4 = self.imageTarray[y_h][ x_h]

                            q1 = PUpleft * (1-y_weight) + v2 * (y_weight)
                            q2 = v3 * (1-y_weight) + v4 * (y_weight)
                            pixel = q1 * (1-x_weight) + q2 * (x_weight)

                        rotated_image[r][c] = pixel
        imageRotated = PIL.Image.fromarray(rotated_image)
        imageRotated = imageRotated.convert('L')            
        self.imgQ = ImageQt.ImageQt(imageRotated)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_imageTrotated.addPixmap(pixMap)
        #remember to clear image
        #self.ImageTrotated.fitInView(QRectF(0, 0, 128, 128) , Qt.KeepAspectRatio)
        self.scene_imageTrotated.update()

    def ImageRotate(self,Image ,rotation_amount_degree):
        rotation_amount_rad = rotation_amount_degree * np.pi / 180.0
        (width,height) = Image.shape
        width=int(width)
        height=int(height)
        rotated_image = np.zeros((width,height))

        rotated_height, rotated_width = Image.shape
        mid_row = math.floor( (rotated_height+1)/2 )
        mid_col = math.floor( (rotated_width+1)/2 )


        for r in range(rotated_height):
            for c in range(rotated_width):
                #  apply rotation matrix, the other way
                y = (r-mid_col)*math.cos(rotation_amount_rad) + (c-mid_row)*math.sin(rotation_amount_rad)
                x = -(r-mid_col)*math.sin(rotation_amount_rad) + (c-mid_row)*math.cos(rotation_amount_rad)

                #  add offset
                y += mid_col
                x += mid_row
                x = round(x)
                y = round(y)


                x_l, y_l = math.floor(x), math.floor(y)
                if math.ceil(x) <  rotated_height -1:
                    x_h = math.ceil(x)
                else:
                    x_h= rotated_height -1
                if math.ceil(y) <  rotated_width -1:
                    y_h = math.ceil(y)
                else:
                    y_h=rotated_width -1 
                if (x >= 0 and y >= 0 and x < rotated_width and y < rotated_height):
                    x_weight = x  - x_l
                    y_weight = y  - y_l
                    if (x_h == x_l) and (y_h == y_l):
                        pixel = Image[int(y)][int(x)]
                    elif (y_h == y_l):
                        q1 = Image[int(y)][ int(x_l)]
                        q2 = Image[int(y)][ int(x_h)]
                        pixel = q1 * (1-x_weight) + q2 * (x_weight)
                    elif (x_h == x_l):
                        q1 = Image[int(y_l)][int(x)]
                        q2 = Image[int(y_h)][int(x)]
                        pixel = (q1 * (1-y_weight)) + (q2	 * (y_weight))
                    else:
                        PUpleft = Image[y_l][x_l]
                        v2 = Image[y_h][ x_l]
                        v3 = Image[y_l][ x_h]
                        v4 = Image[y_h][ x_h]

                        q1 = PUpleft * (1-y_weight) + v2 * (y_weight)
                        q2 = v3 * (1-y_weight) + v4 * (y_weight)
                        pixel = q1 * (1-x_weight) + q2 * (x_weight)

                    rotated_image[r][c] = pixel
        return rotated_image

    
    def imageShearing(self):
        self.scene_imagesheared.clear()
        (w,h) = self.imageTarray.shape
        ShearFactor= 0.8
        Shearedx=math.ceil(w +ShearFactor*h) 
        sheared_image = np.empty((h,Shearedx))
        for r in range(w):
            for c in range(h):
                if (r >= 0 and c >= 0 and r < w and c < h):
                    if round(r +ShearFactor*c) < Shearedx:
                        sheared_image[r][round(r +ShearFactor*c)] = self.imageTarray[r][c]
                    else:
                        sheared_image[r][Shearedx-1] = self.imageTarray[r][c]    
        #sheared_image= sheared_image[:,int(28):int(w +ShearFactor*h)]
        sheared_image = PIL.Image.fromarray(sheared_image)
        sheared_image = sheared_image.convert('L')            
        self.imgQ = ImageQt.ImageQt(sheared_image)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_imagesheared.addPixmap(pixMap)
        #self.shearedimage.fitInView(QRectF(0, 0, Shearedx, y) , Qt.KeepAspectRatio)
        self.scene_imagesheared.update()


    def histogram(self):
        self.scene_histogram.clear()
        
        pixels=[]
        
        for x in range(256):
            pixels.append(x)

        #set width and height of image
        width,height=self.imgReady.size
        size=width*height
        counts=[]
        equalized_image=np.zeros((height,width))
        Imagearray = np.array(self.imgReady)

        #for each intensity level
        for i in pixels:

        #set counter to 0
            temp=0

        #traverse through the pixels
            for x in range(width):
                for y in range(height):

                #if pixel intensity is equal to intensity level
                #increment counter
                    if (self.imgReady.getpixel((x,y))==i):
                        temp=temp+1
            
            #append frequency of intensity level
            counts.append(temp)

        #initialize list for frequency probabilities
        pdf=[]
        for i in counts:
            pdf.append(i/size)

        #initialize list for cumulative probability 
        cdf=[]
        total=0
        for i in pdf:
            total=total+i
            cdf.append(total)

        #intialize list for mapping cdf
        tr=[]
        for i in cdf:
            t=round(i*255)
            tr.append(t)

        for x in range(width):
            for y in range(height):
                equalized_image[y,x]=tr[Imagearray[y,x]]
        equalized_image = PIL.Image.fromarray(equalized_image)
        equalized_image = equalized_image.convert('L')            
        self.imgQ = ImageQt.ImageQt(equalized_image)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_histogram.addPixmap(pixMap)
        #self.shearedimage.fitInView(QRectF(0, 0, Shearedx, y) , Qt.KeepAspectRatio)
        self.scene_histogram.update()
        self.Original_Histogram.Plot(pixels,counts)
        #initialize list containing new frequencies for equalized hist
        hs=[]
        for i in pixels:
            count=0
            tot=0
            for j in tr:
                if (j==i):
                    tot=tot+counts[count]
                count=count+1
            hs.append(tot)
 
        #plot equalized histogram
        self.EQ_Histogram.Plot(pixels,hs)
        self.EQ_Histogram.update()
        self.Original_Histogram.update()

    def filtering(self):
        
        self.scene_filteredimage.clear()
        try:
            int(self.kernelsize.text())
            float(self.MultiplicationFactor.text())           
        except:
            QMessageBox.critical(self.centralwidget,"Error","Please enter a number ")
            return
        filtersize = int(self.kernelsize.text())
        if filtersize % 2 ==0 :
            QMessageBox.warning(self.centralwidget,"Error","Kernel size must be odd ")
            return
        try:
            self.imgReady is None           
        except:
            QMessageBox.critical(self.centralwidget,"Error","Please enter a photo first ")
            return
        if float(self.kernelsize.text())<=0:
            QMessageBox.warning(self.centralwidget,"Error","Please enter a postive number ")
            return
        
        # Creating Box Filter
        boxfilter =np.zeros((filtersize,filtersize))
        boxfilter.fill(1/(filtersize*filtersize))
        
        # Padding image 
        col,row=self.imgReady.size  
        padsize = filtersize//2     
        paddedimage = np.zeros((row+padsize*2,col+padsize*2))
        self.blur= np.zeros((row+padsize*2,col+padsize*2))
        image= np.array(self.imgReady)
        for i in range(padsize, self.blur.shape[0] - padsize):
            for j in range(padsize, self.blur.shape[1] - padsize):
                paddedimage[i][j] = image[i-padsize][j-padsize]
        
        # Convolution 

        for i in range(row):
            for j in range(col):
                for x in range(filtersize):
                    for y in range(filtersize):
                        self.blur[i,j] += boxfilter[x,y] * paddedimage[i-x,j-y]


        print(paddedimage.shape)
        self.blur=self.blur[padsize:self.blur.shape[0] - padsize,padsize:self.blur.shape[1] - padsize]
        print(self.blur.shape)
        c = np.zeros((image.shape[0],image.shape[1]))
        c = image-self.blur
        c = c * int(self.MultiplicationFactor.text())
        output = self.blur + c
        output = np.subtract(output, output.min())
        final_image = 255*(output/output.max())
        final_image = np.uint8(final_image)
        
        output = PIL.Image.fromarray(final_image)
        #output = output.convert('L')            
        self.imgQ = ImageQt.ImageQt(output)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_filteredimage.addPixmap(pixMap)

        
    def Noisefilter(self):
        self.scene_noisyimage.clear()
        self.scene_denoisedimage.clear()
        NoisedImage = PIL.Image.open(self.path).convert('L')
    #  Adding noise to image

        row,col=self.imgReady.size
        size=row*col
        numnoise = random.randint(int(size/100), int(size/25))
        for i in range(numnoise):
            x=random.randint(0, row - 1)
            y=random.randint(0, col - 1)
            NoisedImage.putpixel((x,y) , (255))
            x=random.randint(0, row - 1)
            y=random.randint(0, col - 1)
            NoisedImage.putpixel((x,y) , (0))

        NoisedImage = NoisedImage.convert('L')            
        self.imgQ = ImageQt.ImageQt(NoisedImage)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_noisyimage.addPixmap(pixMap)
        img_denoised = np.zeros([col, row])
        
        for i in range(1, row-1):
            for j in range(1, col-1):
                filterlist = [
                    NoisedImage.getpixel((i-1, j-1)),
                    NoisedImage.getpixel((i-1, j)),
                    NoisedImage.getpixel((i-1, j + 1)),
                    NoisedImage.getpixel((i, j-1)),
                    NoisedImage.getpixel((i, j)),
                    NoisedImage.getpixel((i, j + 1)),
                    NoisedImage.getpixel((i + 1, j-1)),
                    NoisedImage.getpixel((i + 1, j)),
                    NoisedImage.getpixel((i + 1, j + 1))
                    ]
                
                filterlist = self.sort(filterlist)
                #picking median value
                img_denoised[j, i]= filterlist[4]

        img_denoised = PIL.Image.fromarray(img_denoised)
        img_denoised = img_denoised.convert('L')            
        self.imgQ = ImageQt.ImageQt(img_denoised)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_denoisedimage.addPixmap(pixMap)

    def sort(self, array):
    #  O(n)= n Log(n)  Worst case = O(n^2)  
    # Using quick sort method to sort the array
    # 
        if len(array) <= 1:
            return array
        else:
            smaller = []
            Greater =[]
            pivot = array[0]
    # Dividing array each loop to 2 arrays
    # one containing bigger items and another containing smaller items  
            for i in array[1:]:
                if i <= pivot:
                    smaller.append(i)
                else:
                    Greater.append(i)
    # Using recursion to sort the two arrays
        return self.sort(smaller) + [pivot] + self.sort(Greater)

    def fourier(self):
        self.scene_loggedphase.clear()
        self.scene_loggedmagnitude.clear()
        self.scene_phase.clear()
        self.scene_magnitude.clear()

        Imagearray = np.array(self.imgReady)
        fft_image = np.fft.fft2(Imagearray)
        #fft_image = np.fft.fftshift(f)

      ### Magnitude  
        magnitudeSpectrum = np.sqrt(fft_image.real**2+fft_image.imag**2)
        img_magnitudeSpectrum = PIL.Image.fromarray(magnitudeSpectrum/255)
        img_magnitudeSpectrum = img_magnitudeSpectrum.convert('L')            
        self.imgQ = ImageQt.ImageQt(img_magnitudeSpectrum)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_magnitude.addPixmap(pixMap)


        maxPixelValue = np.max(magnitudeSpectrum)
        c = 255 / (np.log(1 + maxPixelValue))
        loggedImage = c * np.log(1+ magnitudeSpectrum)
        loggedImage = np.subtract(loggedImage, loggedImage.min())
        loggedImage = 255*(loggedImage/loggedImage.max())
        loggedImage = np.uint8(loggedImage)

        img_logged = PIL.Image.fromarray(loggedImage)
        img_logged = img_logged.convert('L')            
        self.imgQ = ImageQt.ImageQt(img_logged)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_loggedmagnitude.addPixmap(pixMap)

    #### Phase
        phaseSpectrum = np.angle(fft_image) 
        print(phaseSpectrum)
        phaseSpectrum = np.subtract(phaseSpectrum, phaseSpectrum.min())
        phaseSpectrum = 255*(phaseSpectrum/phaseSpectrum.max())
        img_phasespectrum = np.uint8(phaseSpectrum)
        img_phasespectrum = PIL.Image.fromarray(img_phasespectrum)
        img_phasespectrum = img_phasespectrum.convert('L')            
 
        self.imgQ = ImageQt.ImageQt(img_phasespectrum)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_phase.addPixmap(pixMap)

        maxPValue = np.max(phaseSpectrum)
        c = 255 / (np.log(1 + maxPValue))
        loggedPhase = c * np.log(1+ phaseSpectrum) 
        loggedPhase = np.subtract(loggedPhase, loggedPhase.min())
        loggedPhase = 255*(loggedPhase/loggedPhase.max())
        loggedPhase = np.uint8(loggedPhase)       

        img_loggedPhase = PIL.Image.fromarray(loggedPhase)
        img_loggedPhase = img_loggedPhase.convert('L')            
        self.imgQ = ImageQt.ImageQt(img_loggedPhase)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_loggedphase.addPixmap(pixMap)

    def fftfilter(self):

        self.scene_fourierfilter.clear()
        self.Difference_scene.clear()
        
        try:
            int(self.kernelsizeftt.text())        
        except:
            QMessageBox.critical(self.centralwidget,"Error","Please enter a number ")
            return
        filtersize = int(self.kernelsizeftt.text())
        if filtersize % 2 ==0 :
            QMessageBox.warning(self.centralwidget,"Error","Kernel size must be odd ")
            return
        try:
            self.imgReady is None           
        except:
            QMessageBox.critical(self.centralwidget,"Error","Please enter a photo first ")
            return
        if float(self.kernelsizeftt.text())<=0:
            QMessageBox.warning(self.centralwidget,"Error","Please enter a postive number ")
            return


        boxfilter =np.zeros((filtersize,filtersize))
        boxfilter.fill(1/(filtersize*filtersize))
        
        # Padding image 
        col,row=self.imgReady.size  
        padsize = filtersize//2     
        paddedimage = np.zeros((row+padsize*2,col+padsize*2))
        self.blur= np.zeros((row+padsize*2,col+padsize*2))
        image= np.array(self.imgReady)
        for i in range(padsize, self.blur.shape[0] - padsize):
            for j in range(padsize, self.blur.shape[1] - padsize):
                paddedimage[i][j] = image[i-padsize][j-padsize]
        
        # Convolution in spatial domain

        for i in range(row):
            for j in range(col):
                for x in range(filtersize):
                    for y in range(filtersize):
                        self.blur[i,j] += boxfilter[x,y] * paddedimage[i-x,j-y]


        self.blur=self.blur[padsize:self.blur.shape[0] - padsize,padsize:self.blur.shape[1] - padsize]



        c,r=self.imgReady.size
        strtptx=((r-filtersize)//2)-1
        strtpty=((c-filtersize)//2)-1

        filter = np.zeros((r,c))
        for i in range(strtptx, strtptx +filtersize):
            for j in range(strtpty, strtpty + filtersize):
                filter[i][j] = 1/(filtersize*filtersize)

        Imagearray =np.array(self.imgReady)       
        f = np.fft.fft2(Imagearray)
        fourierImg = np.fft.fftshift(f)
         
        FourierFilter=np.fft.fft2(filter)
        ffilter=np.fft.fftshift(FourierFilter)
        
        BlurredFourier=ffilter*fourierImg
        BlurredFourier=np.fft.ifftshift(BlurredFourier)
        BlurredFourier=np.fft.ifft2(BlurredFourier)
        BlurredFourier=np.fft.fftshift(BlurredFourier)
        BlurredFourier=np.abs(BlurredFourier)

        ImageBlurred=PIL.Image.fromarray(BlurredFourier)
        ImageBlurred = ImageBlurred.convert('L')            
        self.imgQ = ImageQt.ImageQt(ImageBlurred)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_fourierfilter.addPixmap(pixMap)       

        DifferenceImage= BlurredFourier-self.blur

        ImageBlurred=PIL.Image.fromarray(DifferenceImage)
        ImageBlurred = ImageBlurred.convert('L')            
        self.imgQ = ImageQt.ImageQt(ImageBlurred)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.Difference_scene.addPixmap(pixMap)       
        self.Difference_scene.update()       

    def notch_reject_filter(self, d0=9, u_k=0, v_k=0):
        r, c = self.imgReady.size 
        H = np.zeros((c, r))
        for u in range(0, c):
            for v in range(0, r):
                D_uv = np.sqrt((u - c / 2 + u_k) ** 2 + (v - r / 2 + v_k) ** 2)
                D_muv = np.sqrt((u - c / 2 - u_k) ** 2 + (v - r / 2 - v_k) ** 2)

                if D_uv <= d0 or D_muv <= d0:
                    H[u, v] = 0.0
                else:
                    H[u, v] = 1.0

        return H

    def filteer(self):
        self.scene_ImagePattern.clear()
        self.scene_Patternremoved.clear()

        Imagearray =np.array(self.imgReady)       
        f = np.fft.fft2(Imagearray)
        fshift = np.fft.fftshift(f)



        H1 = self.notch_reject_filter(4, 38, 30)
        H2 = self.notch_reject_filter( 4, -42, 27)
        H3 = self.notch_reject_filter( 2, 80, 30)
        H4 = self.notch_reject_filter( 2, -82, 28)

        NotchFilter = H1*H2*H3*H4
        NotchRejectCenter = fshift * NotchFilter 
        NotchReject = np.fft.ifftshift(NotchRejectCenter)
        inverse_NotchReject = np.fft.ifft2(NotchReject)  # Compute the inverse DFT of the result


        Result = np.abs(inverse_NotchReject)
        Result=PIL.Image.fromarray(Result)
        Result = Result.convert('L')            
        self.imgQ = ImageQt.ImageQt(self.imgReady)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_ImagePattern.addPixmap(pixMap)       
        self.scene_ImagePattern.update()         

         
        self.imgQ = ImageQt.ImageQt(Result)  
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene_Patternremoved.addPixmap(pixMap)       
        self.scene_Patternremoved.update()     

    def showROIimage(self):
            self.ROIarray=np.zeros((256,256))
            self.ROIarray.fill(50)           
            for i in range(28,230):
                for j in range(28,230):
                    self.ROIarray[i][j]=150

            for u in range(256):
                for v in range(256):
                    D_uv = np.sqrt((u - 256 / 2 ) ** 2 + (v - 256 / 2 ) ** 2)
                    D_muv = np.sqrt((u - 256 / 2 ) ** 2 + (v - 256 / 2 ) ** 2)
                    if D_uv <= 64 or D_muv <=64:
                        self.ROIarray[u, v] = 250
            self.ROIimage.Draw(self.ROIarray)

    def showROINoise(self):

            Uniform=np.random.uniform(-10,10,(256,256))
            Gaussian=np.random.normal(0,5,(256,256)) 
            if self.checkBox_gaussian.isChecked() and self.checkBox_uniform.isChecked() :
                Noise = Uniform + Gaussian
                self.ROInoisearray= self.ROIarray + Noise
            elif self.checkBox_gaussian.isChecked():
                Noise =  Gaussian
                self.ROInoisearray= self.ROIarray + Noise
            elif self.checkBox_uniform.isChecked():
                Noise = Uniform 
                self.ROInoisearray= self.ROIarray + Noise
            else:
                self.ROInoisearray= self.ROIarray

            for i in range(255):
                for j in range(255):
                    if self.ROInoisearray[i,j]>255:
                        self.ROInoisearray[i,j]=255
            self.Original_Histogram_6.Draw(self.ROInoisearray)
            prop = dict(facecolor='blue', alpha=0.5)
            self.rect_selector = RectangleSelector(
            self.Original_Histogram_6.canvas.axes, self.ShowROIHistogram,  spancoords='pixels', drawtype='box', 
            button=[1],props=prop, useblit=True,)

        
    def ShowROIHistogram(self,eclick, erelease):
        self.textbrowser_histogram.clear()
        self.extent = self.rect_selector.extents
        self.x_l,self.x_h,self.y_l,self.y_h=self.rect_selector.extents
        c=np.zeros(256)
        for i in range(round(self.x_l),round(self.x_h)):
            for j in range(round(self.y_l),round(self.y_h)):
                x=round(self.ROInoisearray[i][j])
                c[x]+=1

        mean = 0
        var = 0
        sum_of_Pixels = np.sum(c)

        if sum_of_Pixels != 0:
            cdf = c/sum_of_Pixels
            for i in range(256):
                mean += i * cdf[i]
            for i in range(256):
                var += (i-mean)**2 *cdf[i]
            std = np.sqrt(var)

            self.ROIHistogram.Plot(range(256),c)
            
            self.textbrowser_histogram.append('Mean =' + str(round(mean,4)))
            self.textbrowser_histogram.append('Standard deviation =' + str(round(std, 4)))
            self.textbrowser_histogram.append('Points = (' + str(round(self.x_l))+','+str(round(self.y_l))+ ')'+'(' + str(round(self.x_h))+','+str(round(self.y_h))+ ')')
        else: 
            self.ROIHistogram.Clear()
            self.textbrowser_histogram.append('Select more than one point!!')


    def DrawSheppLogan(self):
        self.SheppLoganArr=shepp_logan(256)
        self.SheppLogan.Draw(self.SheppLoganArr)
        theta = np.linspace(0., 180., 180, endpoint=False)
        self.sinogramArr = radon(self.SheppLoganArr, theta=theta)
        self.Sinogram.Draw(self.sinogramArr)
        #######################
        ############## Built-in ######################
        # numAngles = len(theta)
        # sinogram = np.zeros((256,numAngles))

        # for n in range(numAngles):
        #     rotatedImg = self.ImageRotate(self.SheppLoganArr,theta[n])
        #     sinogram[:,n] = sum(rotatedImg)
        # self.Sinogram.Draw(sinogram)
    
    def DrawLaminogram(self):
        laminogram=np.zeros((256,256))        
        if self.NoFilter.isChecked() and self.Angle20.isChecked():
            laminogram=iradon(self.sinogramArr[:,range(0,160,20)],range(0,160,20),filter_name=None)
            self.Laminogram.Draw(laminogram)

        if self.NoFilter.isChecked() and self.AllAngles.isChecked():     
            laminogram=iradon(self.sinogramArr[:,range(0,179)],range(0,179), filter_name=None)
            self.Laminogram.Draw(laminogram)
        
        if self.RamLak.isChecked() and self.AllAngles.isChecked(): 

            laminogram=iradon(self.sinogramArr,filter_name="ramp")
            self.Laminogram.Draw(laminogram)        
        
        if self.Hamming.isChecked() and self.AllAngles.isChecked(): 
            laminogram=iradon(self.sinogramArr,filter_name="hamming")
            self.Laminogram.Draw(laminogram)

    def Erosion(self,Image:np.ndarray,StructureElement):
        (row , col )= Image.shape 
        (k , kL )= StructureElement.shape
        StructureElement= np.array([[None,1,1,1,None],
                        [1,1,1,1,1],
                        [1,1,1,1,1],
                        [1,1,1,1,1],
                        [None,1,1,1,None]])
        
        offset= (k-1)//2
        imgErode= np.zeros((row,col), dtype=np.uint8)
        for i in range(offset, row-offset):
            for j in range(offset,col-offset):
                temp= Image[i-offset:i+offset+1, j-offset:j+offset+1]
                product= self.MorphMult(temp,StructureElement,'Erosion')
                imgErode[i,j]= np.min(product)
        return imgErode

    def Dilation(self, Image:np.ndarray,StructureElement):
        (row , col ) = Image.shape 

        imgDilate= np.zeros((row,col), dtype=np.uint8) 
        (k , kL )= StructureElement.shape
        offset= (k-1)//2
        for i in range(offset, row-offset):
            for j in range(offset,col-offset):
                temp= Image[i-offset:i+offset+1, j-offset:j+offset+1]
                product= self.MorphMult(temp,StructureElement,'Dilation')
                imgDilate[i,j]= np.max(product)
        return imgDilate

    def MorphMult(self,Matrix1,Matrix2,type):
        result=np.zeros(Matrix1.shape)
        for i in range (Matrix1.shape[0]):
            for j in range(Matrix1.shape[1]):
                
                if Matrix1[i][j] is None or Matrix2[i][j] is None :
                    if type == 'Erosion':
                        result[i][j]=255
                    elif type == 'Dilation':
                        result[i][j]=0
                else:
                    result[i][j]=Matrix1[i][j]*Matrix2[i][j]

        return result

    def Opening(self,image,SE):
        Eroded=  self.Erosion(image,SE)
        OpeningImage = self.Dilation(Eroded,SE)
        return OpeningImage

    def Closing(self,image,SE):
        Dilated= self.Dilation(image,SE)
        ClosingImage = self.Erosion(Dilated,SE)
        return ClosingImage


    def Morphological(self):
        StructureElement= np.array([ [None,1,1,1,None],
                        [1,1,1,1,1],
                        [1,1,1,1,1],
                        [1,1,1,1,1],
                        [None,1,1,1,None]])
        if self.rB_Dilation.isChecked() :
            result = self.Dilation(np.asarray(self.imgReady),StructureElement)
            self.Morph.Draw(result)
        if self.rB_Erosion.isChecked() :
            result = self.Erosion(np.asarray(self.imgReady),StructureElement)
            self.Morph.Draw(result)
        if self.rB_Opening.isChecked() :
            result = self.Opening(np.asarray(self.imgReady),StructureElement)
            self.Morph.Draw(result)        
        if self.rB_Closing.isChecked() :
            result = self.Closing(np.asarray(self.imgReady),StructureElement)
            self.Morph.Draw(result)
        else :
            StructureElement= np.array(
                [
                [1, 1,1],
                [1,None,1],
                [1,1,1]
                ]
            )
            result = self.Opening(np.asarray(self.imgReady),StructureElement)
            Finalresult = self.Closing(result,StructureElement)
            self.Morph.Draw(Finalresult)
            
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DicomViewer = QtWidgets.QMainWindow()
    ui = Ui_DicomViewer()
    ui.setupUi(DicomViewer)
    DicomViewer.show()
    sys.exit(app.exec_())

'''设置窗口，自定义词条收益权重'''

import os

from modules.zzz.zzz_data import data

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QWidget,
    QGridLayout,
    QDoubleSpinBox
)


class SetWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), 'src/keqing.ico')))
        self.setWindowTitle("得分权重设置")
        self.setFocusPolicy(Qt.StrongFocus)
        self.move(340, 0)

        # 初始化数值
        self.character = ""
        self.config = {}

        self.openFileButton = QPushButton('打开文件')
        self.dataUpdateButton = QPushButton('更新数据')
        # 显示当前角色
        self.heroNameLabel = QLabel("")
        # 显示得分权重
        self.entryNum = {}
        for keyName in data.getEntryArray():
            numText = QDoubleSpinBox()
            numText.setMinimum(0)
            numText.setMaximum(2)
            numText.setSingleStep(0.1)
            numText.setValue(0)
            numText.setAlignment(Qt.AlignRight)
            self.entryNum[keyName] = numText
        # 添加保存按钮
        self.saveButton = QPushButton('确认修改')

        # 注意事项
        self.tipsLabel1 = QLabel('注意事项：')
        self.tipsLabel1.setStyleSheet("color:red;")
        self.tipsLabel2 = QLabel('1.小词条（固定值）得分为大词条（百分比）的一半')
        self.tipsLabel2.setStyleSheet("color:red;")

        # 弹窗内容
        layout = QGridLayout()
        layout.addWidget(self.openFileButton, 0, 0, 1, 1)
        layout.addWidget(self.dataUpdateButton, 0, 1, 1, 1)
        layout.addWidget(QLabel('当前角色：'), 1, 0)
        layout.addWidget(self.heroNameLabel, 1, 1)
        counter = 0
        for keyName in self.entryNum:
            layout.addWidget(QLabel(keyName), counter + 2, 0)
            layout.addWidget(self.entryNum[keyName], counter + 2, 1)
            counter += 1
        layout.addWidget(self.saveButton, 100, 0, 1, 2)
        layout.addWidget(self.tipsLabel1, 101, 0, 1, 2)
        layout.addWidget(self.tipsLabel2, 102, 0, 1, 2)
        self.setLayout(layout)

        # 注册按钮事件
        self.openFileButton.clicked.connect(self.openFile)
        self.dataUpdateButton.clicked.connect(self.updateData)
        self.saveButton.clicked.connect(self.btn_save)

    def update(self, character):
        self.character = character
        self.updateUI()

    def updateUI(self):
        herConfig = data.getCharacters()
        # 兼容数据异常情况
        if not self.character in herConfig or herConfig[self.character] == {}:
            self.heroNameLabel.setText("请正确的选择角色")
            for keyName in self.entryNum:
                self.entryNum[keyName].setValue(0)
        else:
            self.heroNameLabel.setText(self.character)
            for keyName in self.entryNum:
                self.entryNum[keyName].setValue(herConfig[self.character][keyName])

    def btn_save(self):
        herConfig = data.getCharacters()
        tempConfig = {}
        for keyName in self.entryNum:
            tempConfig[keyName] = self.entryNum[keyName].value()
        herConfig[self.character] = tempConfig
        data.setCharacters(herConfig)
        self.close()

    # 数据更新
    def updateData(self):
        data.loadData()

    # 打开文件夹
    def openFile(self):
        os.startfile(data.getUserDataPath())

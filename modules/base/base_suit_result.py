'''圣遗物推荐方案生成弹窗'''

import os
from extention import ExtendedComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QWidget,
    QGridLayout
)


class BaseSuitResultWindow(QWidget):

    def __init__(self, params):
        super().__init__()

        # 获取子类参数
        self.data = params.get("data", {})
        self.position = params.get("position", (0, 0))

        # 初始化变量
        self.character = "全属性"
        self.resultArray = []

        # 初始化UI
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), '../../src/keqing.ico')))
        self.setWindowTitle("生成方案")
        self.setFocusPolicy(Qt.StrongFocus)
        self.move(*self.position)

        # 创建界面UI
        self.programmeCombobox = ExtendedComboBox()
        self.posNameLabel = {}
        self.artifactNameLabel1 = {}
        self.artifactScoreLabel1 = {}
        self.artifactOwnerLabel1 = {}
        self.artifactNameLabel2 = {}
        self.artifactScoreLabel2 = {}
        self.artifactOwnerLabel2 = {}
        self.artifactScoreSubLabel = {}
        for posItem in self.data.getPosName():
            self.posNameLabel[posItem] = QLabel(posItem)
            self.artifactNameLabel1[posItem] = QLabel("无装备")
            self.artifactScoreLabel1[posItem] = QLabel("0")
            self.artifactOwnerLabel1[posItem] = QLabel("0")
            self.artifactNameLabel2[posItem] = QLabel("无装备")
            self.artifactScoreLabel2[posItem] = QLabel("0")
            self.artifactOwnerLabel2[posItem] = QLabel("无人装备")
            self.artifactScoreSubLabel[posItem] = QLabel("0")
        self.equipTips = QLabel("将推荐装备全部标记")
        self.equipTips.setStyleSheet("color:red;qproperty-alignment: 'AlignCenter';")
        self.equipButton = QPushButton('全部装备')

        # 弹窗内容
        layout = QGridLayout()
        layout.addWidget(QLabel("当前方案："), 0, 0, 1, 1)
        layout.addWidget(self.programmeCombobox, 0, 1, 1, 10)
        counter = 0
        for posItem in self.data.getPosName():
            layout.addWidget(self.posNameLabel[posItem], 1 + 3 * counter + 1, 0, 2, 1)
            layout.addWidget(QLabel("当前："), 1 + 3 * counter + 1, 1, 1, 1)
            layout.addWidget(self.artifactNameLabel1[posItem], 1 + 3 * counter + 1, 2, 1, 1)
            layout.addWidget(self.artifactOwnerLabel1[posItem], 1 + 3 * counter + 1, 3, 1, 1)
            layout.addWidget(self.artifactScoreLabel1[posItem], 1 + 3 * counter + 1, 4, 1, 1)
            layout.addWidget(QLabel("推荐："), 2 + 3 * counter + 1, 1, 1, 1)
            layout.addWidget(self.artifactNameLabel2[posItem], 2 + 3 * counter + 1, 2, 1, 1)
            layout.addWidget(self.artifactOwnerLabel2[posItem], 2 + 3 * counter + 1, 3, 1, 1)
            layout.addWidget(self.artifactScoreLabel2[posItem], 2 + 3 * counter + 1, 4, 1, 1)
            layout.addWidget(self.artifactScoreSubLabel[posItem], 1 + 3 * counter + 1, 5, 2, 1)
            layout.addWidget(QLabel(" "), 4 + 3 * counter, 0, 1, 4)
            counter += 1
        layout.addWidget(self.equipTips, 100, 0, 1, 10)
        layout.addWidget(self.equipButton, 101, 0, 1, 10)
        self.setLayout(layout)

        # 注册事件
        self.programmeCombobox.currentIndexChanged.connect(self.programmeCurrentIndexChanged)
        self.equipButton.clicked.connect(self.allEquip)

    def updateUI(self):
        oldArtifactsData = self.data.getArtifactOwner(self.character)
        newArtifactsData = self.resultArray[self.programmeCombobox.currentIndex()]["combinationName"]
        config = self.data.getCharactersByCharacter(self.character)
        for posItem in self.data.getPosName():
            oldScore = 0
            if posItem in oldArtifactsData:
                self.artifactNameLabel1[posItem].setText(oldArtifactsData[posItem])

                oldArtifactItem = self.data.getArtifactItem(posItem, oldArtifactsData[posItem])
                oldScore = 0
                if "normalTags" in oldArtifactItem:
                    oldScore = self.data.cal_score(oldArtifactItem["normalTags"], config)[1]
                self.artifactScoreLabel1[posItem].setText(str(oldScore))

            if posItem in newArtifactsData:
                self.artifactNameLabel2[posItem].setText(newArtifactsData[posItem])
                newArtifactItem = self.data.getArtifactItem(posItem, newArtifactsData[posItem])
                newScore = 0
                if "normalTags" in newArtifactItem:
                    newScore = self.data.cal_score(newArtifactItem["normalTags"], config)[1]
                self.artifactScoreLabel2[posItem].setText(str(newScore))

                ownerCharacter = self.data.getOwnerCharacterByArtifactId(posItem, newArtifactsData[posItem])
                if ownerCharacter:
                    newOwnerStr = ownerCharacter
                else:
                    newOwnerStr = "无人装备"
                self.artifactOwnerLabel2[posItem].setText(newOwnerStr)

            if newOwnerStr != "无人装备" and newOwnerStr != self.character:
                newOwnerconfig = self.data.getCharactersByCharacter(newOwnerStr)
                newOwnerScore = self.data.cal_score(newArtifactItem["normalTags"], newOwnerconfig)[1]
                self.artifactOwnerLabel1[posItem].setText(str(newOwnerScore))
            else:
                self.artifactOwnerLabel1[posItem].setText("")

            scoreSub = round(newScore - oldScore, 1)
            if scoreSub > 0:
                scoreSub = "+" + str(scoreSub)
                scoreStyle = "color:green;"
            elif scoreSub < 0:
                scoreStyle = "color:red;"
            else:
                scoreStyle = "color:black;"
            self.artifactScoreSubLabel[posItem].setText(str(scoreSub))
            self.artifactScoreSubLabel[posItem].setStyleSheet(scoreStyle)

    def update(self, character, array):
        self.character = character
        self.resultArray = array
        # 添加下拉框item
        self.programmeCombobox.clear()
        for item in self.resultArray:
            tempKey = item["combinationType"] + "_" + str(item["scoreSum"])
            self.programmeCombobox.addItem(tempKey)

    # 英雄名称
    def programmeCurrentIndexChanged(self):
        self.updateUI()

    # 全部装备
    def allEquip(self):
        print("全部装备")
        self.equipTips.setText(self.character + "已全部装备")
        newArtifactsData = self.resultArray[self.programmeCombobox.currentIndex()]["combinationName"]
        self.data.setArtifactOwner(self.character, newArtifactsData)
        self.updateUI()

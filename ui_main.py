# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controle_de_notas.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1094, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(self.main_container)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setEnabled(True)
        self.header_frame.setLayoutDirection(Qt.LeftToRight)
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.btn_menu = QPushButton(self.header_frame)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setMinimumSize(QSize(0, 0))
        self.btn_menu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu.setLayoutDirection(Qt.RightToLeft)
        self.btn_menu.setAutoFillBackground(False)
        self.btn_menu.setStyleSheet(u"background-color: None;\n"
"border: None;\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/botao-de-menu-de-tres-linhas-horizontais (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_menu, 0, Qt.AlignRight)

        self.lb_title = QLabel(self.header_frame)
        self.lb_title.setObjectName(u"lb_title")

        self.horizontalLayout_2.addWidget(self.lb_title, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy1)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.main_frame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_compras = QWidget()
        self.pg_compras.setObjectName(u"pg_compras")
        self.verticalLayout_26 = QVBoxLayout(self.pg_compras)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.tb_widget_compras = QTabWidget(self.pg_compras)
        self.tb_widget_compras.setObjectName(u"tb_widget_compras")
        self.tb_compras_list = QWidget()
        self.tb_compras_list.setObjectName(u"tb_compras_list")
        self.verticalLayout_28 = QVBoxLayout(self.tb_compras_list)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_14 = QLabel(self.tb_compras_list)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_28.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.txt_search_compras = QLineEdit(self.tb_compras_list)
        self.txt_search_compras.setObjectName(u"txt_search_compras")

        self.verticalLayout_28.addWidget(self.txt_search_compras)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.table_compras = QTableWidget(self.tb_compras_list)
        if (self.table_compras.columnCount() < 4):
            self.table_compras.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_compras.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_compras.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_compras.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_compras.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_compras.setObjectName(u"table_compras")
        self.table_compras.setSortingEnabled(True)

        self.horizontalLayout_8.addWidget(self.table_compras)

        self.frame_10 = QFrame(self.tb_compras_list)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.btn_compra_excluir = QPushButton(self.frame_10)
        self.btn_compra_excluir.setObjectName(u"btn_compra_excluir")
        self.btn_compra_excluir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_27.addWidget(self.btn_compra_excluir)

        self.btn_compra_editar = QPushButton(self.frame_10)
        self.btn_compra_editar.setObjectName(u"btn_compra_editar")
        self.btn_compra_editar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_27.addWidget(self.btn_compra_editar)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_16)


        self.horizontalLayout_8.addWidget(self.frame_10)


        self.verticalLayout_28.addLayout(self.horizontalLayout_8)

        self.tb_widget_compras.addTab(self.tb_compras_list, "")
        self.tb_compras_cadastro = QWidget()
        self.tb_compras_cadastro.setObjectName(u"tb_compras_cadastro")
        self.verticalLayout_29 = QVBoxLayout(self.tb_compras_cadastro)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_15 = QLabel(self.tb_compras_cadastro)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_29.addWidget(self.label_15, 0, Qt.AlignHCenter)

        self.frame_11 = QFrame(self.tb_compras_cadastro)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.txt_compra_data = QLineEdit(self.frame_11)
        self.txt_compra_data.setObjectName(u"txt_compra_data")
        self.txt_compra_data.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.txt_compra_data, 0, 5, 1, 1)

        self.txt_compra_quant = QLineEdit(self.frame_11)
        self.txt_compra_quant.setObjectName(u"txt_compra_quant")
        self.txt_compra_quant.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.txt_compra_quant, 1, 5, 1, 1)

        self.lb_compra_medida = QLabel(self.frame_11)
        self.lb_compra_medida.setObjectName(u"lb_compra_medida")

        self.gridLayout_5.addWidget(self.lb_compra_medida, 1, 6, 1, 1)

        self.select_compra_pagamento = QComboBox(self.frame_11)
        self.select_compra_pagamento.addItem("")
        self.select_compra_pagamento.addItem("")
        self.select_compra_pagamento.addItem("")
        self.select_compra_pagamento.addItem("")
        self.select_compra_pagamento.addItem("")
        self.select_compra_pagamento.setObjectName(u"select_compra_pagamento")

        self.gridLayout_5.addWidget(self.select_compra_pagamento, 2, 0, 1, 1)

        self.select_compra_fornecedor = QComboBox(self.frame_11)
        self.select_compra_fornecedor.addItem("")
        self.select_compra_fornecedor.setObjectName(u"select_compra_fornecedor")

        self.gridLayout_5.addWidget(self.select_compra_fornecedor, 0, 0, 1, 5)

        self.label_17 = QLabel(self.frame_11)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 0, 6, 1, 1)

        self.select_compra_produto = QComboBox(self.frame_11)
        self.select_compra_produto.addItem("")
        self.select_compra_produto.setObjectName(u"select_compra_produto")

        self.gridLayout_5.addWidget(self.select_compra_produto, 1, 0, 1, 2)

        self.btn_add_produto_compra = QPushButton(self.frame_11)
        self.btn_add_produto_compra.setObjectName(u"btn_add_produto_compra")
        self.btn_add_produto_compra.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_5.addWidget(self.btn_add_produto_compra, 2, 4, 1, 2, Qt.AlignHCenter)

        self.select_compra_status = QComboBox(self.frame_11)
        self.select_compra_status.addItem("")
        self.select_compra_status.addItem("")
        self.select_compra_status.addItem("")
        self.select_compra_status.addItem("")
        self.select_compra_status.setObjectName(u"select_compra_status")

        self.gridLayout_5.addWidget(self.select_compra_status, 2, 1, 1, 1)

        self.txt_compra_vencimento = QLineEdit(self.frame_11)
        self.txt_compra_vencimento.setObjectName(u"txt_compra_vencimento")
        self.txt_compra_vencimento.setEnabled(False)
        self.txt_compra_vencimento.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.txt_compra_vencimento, 2, 2, 1, 1)

        self.txt_compra_precmedida = QLineEdit(self.frame_11)
        self.txt_compra_precmedida.setObjectName(u"txt_compra_precmedida")
        self.txt_compra_precmedida.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.txt_compra_precmedida, 1, 2, 1, 3)

        self.lb_compra_vencimento = QLabel(self.frame_11)
        self.lb_compra_vencimento.setObjectName(u"lb_compra_vencimento")
        self.lb_compra_vencimento.setEnabled(False)

        self.gridLayout_5.addWidget(self.lb_compra_vencimento, 2, 3, 1, 1)


        self.verticalLayout_29.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.tb_compras_cadastro)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_12)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tb_produtos_compra_widget = QTableWidget(self.frame_12)
        if (self.tb_produtos_compra_widget.columnCount() < 4):
            self.tb_produtos_compra_widget.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_produtos_compra_widget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_produtos_compra_widget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_produtos_compra_widget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_produtos_compra_widget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tb_produtos_compra_widget.setObjectName(u"tb_produtos_compra_widget")

        self.horizontalLayout_9.addWidget(self.tb_produtos_compra_widget)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_13)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.btn_remover_produto_compra = QPushButton(self.frame_13)
        self.btn_remover_produto_compra.setObjectName(u"btn_remover_produto_compra")
        self.btn_remover_produto_compra.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_30.addWidget(self.btn_remover_produto_compra)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_17)


        self.horizontalLayout_9.addWidget(self.frame_13)


        self.verticalLayout_31.addLayout(self.horizontalLayout_9)

        self.lb_total_compra = QLabel(self.frame_12)
        self.lb_total_compra.setObjectName(u"lb_total_compra")
        self.lb_total_compra.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.verticalLayout_31.addWidget(self.lb_total_compra, 0, Qt.AlignHCenter)

        self.btn_compra_registrar = QPushButton(self.frame_12)
        self.btn_compra_registrar.setObjectName(u"btn_compra_registrar")
        self.btn_compra_registrar.setMinimumSize(QSize(150, 30))
        self.btn_compra_registrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_31.addWidget(self.btn_compra_registrar, 0, Qt.AlignHCenter)


        self.verticalLayout_29.addWidget(self.frame_12)

        self.tb_widget_compras.addTab(self.tb_compras_cadastro, "")

        self.verticalLayout_26.addWidget(self.tb_widget_compras)

        self.Pages.addWidget(self.pg_compras)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lb_logo = QLabel(self.pg_home)
        self.lb_logo.setObjectName(u"lb_logo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lb_logo.sizePolicy().hasHeightForWidth())
        self.lb_logo.setSizePolicy(sizePolicy2)
        self.lb_logo.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.lb_logo, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer)

        self.btn_inicia_semana = QPushButton(self.pg_home)
        self.btn_inicia_semana.setObjectName(u"btn_inicia_semana")

        self.horizontalLayout_20.addWidget(self.btn_inicia_semana)

        self.btn_fecha_semana = QPushButton(self.pg_home)
        self.btn_fecha_semana.setObjectName(u"btn_fecha_semana")

        self.horizontalLayout_20.addWidget(self.btn_fecha_semana)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_20)

        self.Pages.addWidget(self.pg_home)
        self.pg_vendas = QWidget()
        self.pg_vendas.setObjectName(u"pg_vendas")
        self.verticalLayout_21 = QVBoxLayout(self.pg_vendas)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.tb_widget_vendas = QTabWidget(self.pg_vendas)
        self.tb_widget_vendas.setObjectName(u"tb_widget_vendas")
        self.tb_vendas_list = QWidget()
        self.tb_vendas_list.setObjectName(u"tb_vendas_list")
        self.verticalLayout_24 = QVBoxLayout(self.tb_vendas_list)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_7 = QLabel(self.tb_vendas_list)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_24.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.txt_vendas_pesquisar = QLineEdit(self.tb_vendas_list)
        self.txt_vendas_pesquisar.setObjectName(u"txt_vendas_pesquisar")

        self.verticalLayout_24.addWidget(self.txt_vendas_pesquisar)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tb_vendas = QTableWidget(self.tb_vendas_list)
        if (self.tb_vendas.columnCount() < 4):
            self.tb_vendas.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_vendas.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_vendas.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_vendas.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_vendas.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.tb_vendas.setObjectName(u"tb_vendas")
        self.tb_vendas.setSortingEnabled(True)

        self.horizontalLayout_7.addWidget(self.tb_vendas)

        self.frame_9 = QFrame(self.tb_vendas_list)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.btn_venda_excluir = QPushButton(self.frame_9)
        self.btn_venda_excluir.setObjectName(u"btn_venda_excluir")
        self.btn_venda_excluir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_23.addWidget(self.btn_venda_excluir)

        self.btn_venda_edit = QPushButton(self.frame_9)
        self.btn_venda_edit.setObjectName(u"btn_venda_edit")
        self.btn_venda_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_23.addWidget(self.btn_venda_edit)

        self.btn_venda_print = QPushButton(self.frame_9)
        self.btn_venda_print.setObjectName(u"btn_venda_print")
        self.btn_venda_print.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_23.addWidget(self.btn_venda_print)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_11)


        self.horizontalLayout_7.addWidget(self.frame_9)


        self.verticalLayout_24.addLayout(self.horizontalLayout_7)

        self.tb_widget_vendas.addTab(self.tb_vendas_list, "")
        self.tb_vendas_cadastro = QWidget()
        self.tb_vendas_cadastro.setObjectName(u"tb_vendas_cadastro")
        self.verticalLayout_25 = QVBoxLayout(self.tb_vendas_cadastro)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_3 = QLabel(self.tb_vendas_cadastro)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_25.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.tb_vendas_cadastro)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lb_vendas_medida = QLabel(self.frame_7)
        self.lb_vendas_medida.setObjectName(u"lb_vendas_medida")

        self.gridLayout_4.addWidget(self.lb_vendas_medida, 1, 9, 1, 1)

        self.select_pagamento_venda = QComboBox(self.frame_7)
        self.select_pagamento_venda.addItem("")
        self.select_pagamento_venda.addItem("")
        self.select_pagamento_venda.addItem("")
        self.select_pagamento_venda.addItem("")
        self.select_pagamento_venda.addItem("")
        self.select_pagamento_venda.setObjectName(u"select_pagamento_venda")

        self.gridLayout_4.addWidget(self.select_pagamento_venda, 2, 0, 1, 3)

        self.txt_venda_vencimento = QLineEdit(self.frame_7)
        self.txt_venda_vencimento.setObjectName(u"txt_venda_vencimento")
        self.txt_venda_vencimento.setEnabled(False)
        self.txt_venda_vencimento.setMaximumSize(QSize(150, 16777215))
        self.txt_venda_vencimento.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.txt_venda_vencimento, 2, 3, 1, 1)

        self.tb_vendas_itens = QTableWidget(self.frame_7)
        if (self.tb_vendas_itens.columnCount() < 4):
            self.tb_vendas_itens.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_vendas_itens.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_vendas_itens.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_vendas_itens.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_vendas_itens.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        self.tb_vendas_itens.setObjectName(u"tb_vendas_itens")
        self.tb_vendas_itens.setMinimumSize(QSize(0, 0))

        self.gridLayout_4.addWidget(self.tb_vendas_itens, 3, 0, 1, 9)

        self.lb_vencimento_venda = QLabel(self.frame_7)
        self.lb_vencimento_venda.setObjectName(u"lb_vencimento_venda")
        self.lb_vencimento_venda.setEnabled(False)

        self.gridLayout_4.addWidget(self.lb_vencimento_venda, 2, 4, 1, 1)

        self.select_status_venda = QComboBox(self.frame_7)
        self.select_status_venda.addItem("")
        self.select_status_venda.addItem("")
        self.select_status_venda.addItem("")
        self.select_status_venda.addItem("")
        self.select_status_venda.setObjectName(u"select_status_venda")

        self.gridLayout_4.addWidget(self.select_status_venda, 2, 5, 1, 2)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setMaximumSize(QSize(150, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_8)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.btn_remove_venda_register = QPushButton(self.frame_8)
        self.btn_remove_venda_register.setObjectName(u"btn_remove_venda_register")
        self.btn_remove_venda_register.setMaximumSize(QSize(150, 16777215))
        self.btn_remove_venda_register.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_22.addWidget(self.btn_remove_venda_register)

        self.btn_cancel_venda = QPushButton(self.frame_8)
        self.btn_cancel_venda.setObjectName(u"btn_cancel_venda")

        self.verticalLayout_22.addWidget(self.btn_cancel_venda)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_12)


        self.gridLayout_4.addWidget(self.frame_8, 3, 9, 1, 1)

        self.txt_venda_quantidade = QLineEdit(self.frame_7)
        self.txt_venda_quantidade.setObjectName(u"txt_venda_quantidade")
        self.txt_venda_quantidade.setMaximumSize(QSize(150, 16777215))
        self.txt_venda_quantidade.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.txt_venda_quantidade, 1, 6, 1, 3)

        self.txt_venda_data = QLineEdit(self.frame_7)
        self.txt_venda_data.setObjectName(u"txt_venda_data")
        self.txt_venda_data.setMaximumSize(QSize(150, 16777215))
        self.txt_venda_data.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.txt_venda_data, 0, 6, 1, 3)

        self.label_19 = QLabel(self.frame_7)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 9, 1, 1)

        self.label_22 = QLabel(self.frame_7)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_4.addWidget(self.label_22, 1, 0, 1, 1)

        self.select_client_venda = QComboBox(self.frame_7)
        self.select_client_venda.setObjectName(u"select_client_venda")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.select_client_venda.sizePolicy().hasHeightForWidth())
        self.select_client_venda.setSizePolicy(sizePolicy3)
        self.select_client_venda.setEditable(True)

        self.gridLayout_4.addWidget(self.select_client_venda, 0, 1, 1, 5)

        self.select_produto_venda = QComboBox(self.frame_7)
        self.select_produto_venda.setObjectName(u"select_produto_venda")
        sizePolicy3.setHeightForWidth(self.select_produto_venda.sizePolicy().hasHeightForWidth())
        self.select_produto_venda.setSizePolicy(sizePolicy3)
        self.select_produto_venda.setMinimumSize(QSize(250, 0))
        self.select_produto_venda.setEditable(True)

        self.gridLayout_4.addWidget(self.select_produto_venda, 1, 1, 1, 5)

        self.lb_venda_total = QLabel(self.frame_7)
        self.lb_venda_total.setObjectName(u"lb_venda_total")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lb_venda_total.sizePolicy().hasHeightForWidth())
        self.lb_venda_total.setSizePolicy(sizePolicy4)
        self.lb_venda_total.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.gridLayout_4.addWidget(self.lb_venda_total, 4, 3, 1, 4, Qt.AlignHCenter)

        self.btn_venda_addProduto = QPushButton(self.frame_7)
        self.btn_venda_addProduto.setObjectName(u"btn_venda_addProduto")
        self.btn_venda_addProduto.setMaximumSize(QSize(150, 35))
        self.btn_venda_addProduto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_venda_addProduto, 2, 9, 1, 1)


        self.verticalLayout_25.addWidget(self.frame_7)

        self.btn_venda_cadastrar = QPushButton(self.tb_vendas_cadastro)
        self.btn_venda_cadastrar.setObjectName(u"btn_venda_cadastrar")
        self.btn_venda_cadastrar.setMinimumSize(QSize(150, 0))
        self.btn_venda_cadastrar.setMaximumSize(QSize(150, 16777215))
        self.btn_venda_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_25.addWidget(self.btn_venda_cadastrar, 0, Qt.AlignHCenter)

        self.tb_widget_vendas.addTab(self.tb_vendas_cadastro, "")
        self.tb_vendas_produtos_semanal = QWidget()
        self.tb_vendas_produtos_semanal.setObjectName(u"tb_vendas_produtos_semanal")
        self.verticalLayout_54 = QVBoxLayout(self.tb_vendas_produtos_semanal)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.lb_pedido_da_semana = QLabel(self.tb_vendas_produtos_semanal)
        self.lb_pedido_da_semana.setObjectName(u"lb_pedido_da_semana")

        self.verticalLayout_54.addWidget(self.lb_pedido_da_semana, 0, Qt.AlignHCenter)

        self.txt_semanal_search = QLineEdit(self.tb_vendas_produtos_semanal)
        self.txt_semanal_search.setObjectName(u"txt_semanal_search")

        self.verticalLayout_54.addWidget(self.txt_semanal_search)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.tab_pedido_semana = QTableWidget(self.tb_vendas_produtos_semanal)
        if (self.tab_pedido_semana.columnCount() < 3):
            self.tab_pedido_semana.setColumnCount(3)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tab_pedido_semana.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tab_pedido_semana.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tab_pedido_semana.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        self.tab_pedido_semana.setObjectName(u"tab_pedido_semana")
        self.tab_pedido_semana.setSortingEnabled(True)

        self.horizontalLayout_19.addWidget(self.tab_pedido_semana)


        self.verticalLayout_54.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_3)

        self.btn_download_list = QPushButton(self.tb_vendas_produtos_semanal)
        self.btn_download_list.setObjectName(u"btn_download_list")

        self.horizontalLayout_21.addWidget(self.btn_download_list)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_4)


        self.verticalLayout_54.addLayout(self.horizontalLayout_21)

        self.tb_widget_vendas.addTab(self.tb_vendas_produtos_semanal, "")

        self.verticalLayout_21.addWidget(self.tb_widget_vendas)

        self.Pages.addWidget(self.pg_vendas)
        self.pg_cliente_detail = QWidget()
        self.pg_cliente_detail.setObjectName(u"pg_cliente_detail")
        self.verticalLayout_32 = QVBoxLayout(self.pg_cliente_detail)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.tb_widget_client_detail = QTabWidget(self.pg_cliente_detail)
        self.tb_widget_client_detail.setObjectName(u"tb_widget_client_detail")
        self.tb_client_detail_info = QWidget()
        self.tb_client_detail_info.setObjectName(u"tb_client_detail_info")
        self.horizontalLayout_10 = QHBoxLayout(self.tb_client_detail_info)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_14 = QFrame(self.tb_client_detail_info)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_14)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_16)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lb_nome_cliente_detail = QLabel(self.frame_16)
        self.lb_nome_cliente_detail.setObjectName(u"lb_nome_cliente_detail")

        self.gridLayout_6.addWidget(self.lb_nome_cliente_detail, 1, 0, 1, 1)

        self.lb_cpf_cliente_detail = QLabel(self.frame_16)
        self.lb_cpf_cliente_detail.setObjectName(u"lb_cpf_cliente_detail")

        self.gridLayout_6.addWidget(self.lb_cpf_cliente_detail, 2, 0, 1, 1)

        self.lb_telefone_cliente_detail = QLabel(self.frame_16)
        self.lb_telefone_cliente_detail.setObjectName(u"lb_telefone_cliente_detail")

        self.gridLayout_6.addWidget(self.lb_telefone_cliente_detail, 2, 1, 1, 1)

        self.lb_endereco_cliente_detail = QLabel(self.frame_16)
        self.lb_endereco_cliente_detail.setObjectName(u"lb_endereco_cliente_detail")

        self.gridLayout_6.addWidget(self.lb_endereco_cliente_detail, 3, 0, 1, 1)

        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_6.addWidget(self.label_23, 0, 0, 1, 2, Qt.AlignHCenter)


        self.verticalLayout_33.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_17)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_20 = QLabel(self.frame_17)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_7.addWidget(self.label_20, 0, 1, 1, 1, Qt.AlignHCenter)

        self.lb_total_gasto_cliente = QLabel(self.frame_17)
        self.lb_total_gasto_cliente.setObjectName(u"lb_total_gasto_cliente")

        self.gridLayout_7.addWidget(self.lb_total_gasto_cliente, 1, 2, 1, 1)

        self.lb_num_pedidos_cliente = QLabel(self.frame_17)
        self.lb_num_pedidos_cliente.setObjectName(u"lb_num_pedidos_cliente")

        self.gridLayout_7.addWidget(self.lb_num_pedidos_cliente, 1, 0, 1, 1)

        self.lb_status_cliente = QLabel(self.frame_17)
        self.lb_status_cliente.setObjectName(u"lb_status_cliente")

        self.gridLayout_7.addWidget(self.lb_status_cliente, 2, 0, 1, 1)


        self.verticalLayout_33.addWidget(self.frame_17)

        self.btn_contato_cliente = QPushButton(self.frame_14)
        self.btn_contato_cliente.setObjectName(u"btn_contato_cliente")
        self.btn_contato_cliente.setMinimumSize(QSize(150, 0))
        self.btn_contato_cliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_33.addWidget(self.btn_contato_cliente, 0, Qt.AlignHCenter)

        self.frame_22 = QFrame(self.frame_14)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 80))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_24)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_27 = QLabel(self.frame_24)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_36.addWidget(self.label_27, 0, Qt.AlignHCenter)


        self.horizontalLayout_12.addWidget(self.frame_24)

        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_23)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_28 = QLabel(self.frame_23)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_37.addWidget(self.label_28, 0, Qt.AlignHCenter)


        self.horizontalLayout_12.addWidget(self.frame_23)


        self.verticalLayout_33.addWidget(self.frame_22)


        self.horizontalLayout_10.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.tb_client_detail_info)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_15)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy5)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_18)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_19)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_25 = QLabel(self.frame_19)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.horizontalLayout.addWidget(self.label_25, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_34.addWidget(self.frame_19)

        self.frame_graph_cliente = QFrame(self.frame_18)
        self.frame_graph_cliente.setObjectName(u"frame_graph_cliente")
        sizePolicy5.setHeightForWidth(self.frame_graph_cliente.sizePolicy().hasHeightForWidth())
        self.frame_graph_cliente.setSizePolicy(sizePolicy5)
        self.frame_graph_cliente.setFrameShape(QFrame.StyledPanel)
        self.frame_graph_cliente.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_graph_cliente)
        self.gridLayout_9.setObjectName(u"gridLayout_9")

        self.verticalLayout_34.addWidget(self.frame_graph_cliente)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_anterior_graph_cliente = QPushButton(self.frame_21)
        self.btn_anterior_graph_cliente.setObjectName(u"btn_anterior_graph_cliente")
        self.btn_anterior_graph_cliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_anterior_graph_cliente, 0, Qt.AlignHCenter)

        self.lb_ano_graph_cliente = QLabel(self.frame_21)
        self.lb_ano_graph_cliente.setObjectName(u"lb_ano_graph_cliente")

        self.horizontalLayout_11.addWidget(self.lb_ano_graph_cliente, 0, Qt.AlignHCenter)

        self.btn_proximo_graph_cliente = QPushButton(self.frame_21)
        self.btn_proximo_graph_cliente.setObjectName(u"btn_proximo_graph_cliente")
        self.btn_proximo_graph_cliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.btn_proximo_graph_cliente, 0, Qt.AlignHCenter)


        self.verticalLayout_34.addWidget(self.frame_21)


        self.verticalLayout_35.addWidget(self.frame_18)


        self.horizontalLayout_10.addWidget(self.frame_15)

        self.tb_widget_client_detail.addTab(self.tb_client_detail_info, "")
        self.tb_client_detail_pedidos = QWidget()
        self.tb_client_detail_pedidos.setObjectName(u"tb_client_detail_pedidos")
        self.verticalLayout_39 = QVBoxLayout(self.tb_client_detail_pedidos)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_29 = QLabel(self.tb_client_detail_pedidos)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_39.addWidget(self.label_29, 0, Qt.AlignHCenter)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tb_widget_vendas_cliente_detail = QTableWidget(self.tb_client_detail_pedidos)
        if (self.tb_widget_vendas_cliente_detail.columnCount() < 4):
            self.tb_widget_vendas_cliente_detail.setColumnCount(4)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_widget_vendas_cliente_detail.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_widget_vendas_cliente_detail.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_widget_vendas_cliente_detail.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_widget_vendas_cliente_detail.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        self.tb_widget_vendas_cliente_detail.setObjectName(u"tb_widget_vendas_cliente_detail")
        self.tb_widget_vendas_cliente_detail.setSortingEnabled(True)

        self.horizontalLayout_13.addWidget(self.tb_widget_vendas_cliente_detail)

        self.frame_25 = QFrame(self.tb_client_detail_pedidos)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_25)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.btn_excluir_venda_cliente_detail = QPushButton(self.frame_25)
        self.btn_excluir_venda_cliente_detail.setObjectName(u"btn_excluir_venda_cliente_detail")
        self.btn_excluir_venda_cliente_detail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_38.addWidget(self.btn_excluir_venda_cliente_detail)

        self.btn_editar_venda_cliente_detail = QPushButton(self.frame_25)
        self.btn_editar_venda_cliente_detail.setObjectName(u"btn_editar_venda_cliente_detail")
        self.btn_editar_venda_cliente_detail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_38.addWidget(self.btn_editar_venda_cliente_detail)

        self.btn_imprimir_venda_cliente_detail = QPushButton(self.frame_25)
        self.btn_imprimir_venda_cliente_detail.setObjectName(u"btn_imprimir_venda_cliente_detail")
        self.btn_imprimir_venda_cliente_detail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_38.addWidget(self.btn_imprimir_venda_cliente_detail)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_19)


        self.horizontalLayout_13.addWidget(self.frame_25)


        self.verticalLayout_39.addLayout(self.horizontalLayout_13)

        self.tb_widget_client_detail.addTab(self.tb_client_detail_pedidos, "")

        self.verticalLayout_32.addWidget(self.tb_widget_client_detail)

        self.Pages.addWidget(self.pg_cliente_detail)
        self.pg_clientes = QWidget()
        self.pg_clientes.setObjectName(u"pg_clientes")
        self.verticalLayout_9 = QVBoxLayout(self.pg_clientes)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tb_widget_clientes = QTabWidget(self.pg_clientes)
        self.tb_widget_clientes.setObjectName(u"tb_widget_clientes")
        sizePolicy.setHeightForWidth(self.tb_widget_clientes.sizePolicy().hasHeightForWidth())
        self.tb_widget_clientes.setSizePolicy(sizePolicy)
        self.tab_clientes_list = QWidget()
        self.tab_clientes_list.setObjectName(u"tab_clientes_list")
        self.verticalLayout_12 = QVBoxLayout(self.tab_clientes_list)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lb_clientes = QLabel(self.tab_clientes_list)
        self.lb_clientes.setObjectName(u"lb_clientes")

        self.verticalLayout_12.addWidget(self.lb_clientes, 0, Qt.AlignHCenter)

        self.txt_search_client = QLineEdit(self.tab_clientes_list)
        self.txt_search_client.setObjectName(u"txt_search_client")
        self.txt_search_client.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.txt_search_client)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tb_clientes = QTableWidget(self.tab_clientes_list)
        if (self.tb_clientes.columnCount() < 4):
            self.tb_clientes.setColumnCount(4)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tb_clientes.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        self.tb_clientes.setObjectName(u"tb_clientes")
        self.tb_clientes.setSortingEnabled(True)

        self.horizontalLayout_4.addWidget(self.tb_clientes)

        self.frame_2 = QFrame(self.tab_clientes_list)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.btn_client_edit = QPushButton(self.frame_2)
        self.btn_client_edit.setObjectName(u"btn_client_edit")
        self.btn_client_edit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.btn_client_edit)

        self.btn_client_remove = QPushButton(self.frame_2)
        self.btn_client_remove.setObjectName(u"btn_client_remove")
        self.btn_client_remove.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.btn_client_remove)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_4)

        self.tb_widget_clientes.addTab(self.tab_clientes_list, "")
        self.tab_clientes_register = QWidget()
        self.tab_clientes_register.setObjectName(u"tab_clientes_register")
        self.tab_clientes_register.setEnabled(True)
        self.verticalLayout_10 = QVBoxLayout(self.tab_clientes_register)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.frame = QFrame(self.tab_clientes_register)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(570, 0))
        self.frame.setMaximumSize(QSize(16777215, 137))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_estado_cliente = QLineEdit(self.frame)
        self.txt_estado_cliente.setObjectName(u"txt_estado_cliente")
        self.txt_estado_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_estado_cliente, 4, 3, 1, 1)

        self.txt_endereco_cliente = QLineEdit(self.frame)
        self.txt_endereco_cliente.setObjectName(u"txt_endereco_cliente")
        self.txt_endereco_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_endereco_cliente, 3, 0, 1, 4)

        self.txt_nome_cliente = QLineEdit(self.frame)
        self.txt_nome_cliente.setObjectName(u"txt_nome_cliente")
        self.txt_nome_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome_cliente, 1, 0, 1, 4)

        self.txt_telefone_cliente = QLineEdit(self.frame)
        self.txt_telefone_cliente.setObjectName(u"txt_telefone_cliente")
        self.txt_telefone_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone_cliente, 2, 2, 1, 2)

        self.txt_numero_cliente = QLineEdit(self.frame)
        self.txt_numero_cliente.setObjectName(u"txt_numero_cliente")
        self.txt_numero_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_numero_cliente, 4, 0, 1, 1)

        self.txt_cpf_cliente = QLineEdit(self.frame)
        self.txt_cpf_cliente.setObjectName(u"txt_cpf_cliente")
        self.txt_cpf_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cpf_cliente, 2, 0, 1, 2)

        self.txt_cidade_cliente = QLineEdit(self.frame)
        self.txt_cidade_cliente.setObjectName(u"txt_cidade_cliente")
        self.txt_cidade_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cidade_cliente, 4, 2, 1, 1)

        self.txt_bairro_cliente = QLineEdit(self.frame)
        self.txt_bairro_cliente.setObjectName(u"txt_bairro_cliente")
        self.txt_bairro_cliente.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro_cliente, 4, 1, 1, 1)

        self.lb_client_cadastro = QLabel(self.frame)
        self.lb_client_cadastro.setObjectName(u"lb_client_cadastro")
        self.lb_client_cadastro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_client_cadastro, 0, 1, 1, 2)


        self.verticalLayout_10.addWidget(self.frame)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.btn_cadastrar_cliente = QPushButton(self.tab_clientes_register)
        self.btn_cadastrar_cliente.setObjectName(u"btn_cadastrar_cliente")
        self.btn_cadastrar_cliente.setMinimumSize(QSize(150, 30))
        self.btn_cadastrar_cliente.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.btn_cadastrar_cliente, 0, Qt.AlignHCenter)

        self.tb_widget_clientes.addTab(self.tab_clientes_register, "")

        self.verticalLayout_9.addWidget(self.tb_widget_clientes)

        self.Pages.addWidget(self.pg_clientes)
        self.pg_fornecedores = QWidget()
        self.pg_fornecedores.setObjectName(u"pg_fornecedores")
        self.verticalLayout_15 = QVBoxLayout(self.pg_fornecedores)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tb_widget_fornecedores = QTabWidget(self.pg_fornecedores)
        self.tb_widget_fornecedores.setObjectName(u"tb_widget_fornecedores")
        self.tab_fornecedores_list = QWidget()
        self.tab_fornecedores_list.setObjectName(u"tab_fornecedores_list")
        self.verticalLayout_14 = QVBoxLayout(self.tab_fornecedores_list)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lb_fornecedores = QLabel(self.tab_fornecedores_list)
        self.lb_fornecedores.setObjectName(u"lb_fornecedores")

        self.verticalLayout_14.addWidget(self.lb_fornecedores, 0, Qt.AlignHCenter)

        self.txt_search_fornecedores = QLineEdit(self.tab_fornecedores_list)
        self.txt_search_fornecedores.setObjectName(u"txt_search_fornecedores")

        self.verticalLayout_14.addWidget(self.txt_search_fornecedores)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tb_fornecedores = QTableWidget(self.tab_fornecedores_list)
        if (self.tb_fornecedores.columnCount() < 4):
            self.tb_fornecedores.setColumnCount(4)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tb_fornecedores.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        self.tb_fornecedores.setObjectName(u"tb_fornecedores")
        self.tb_fornecedores.setSortingEnabled(True)

        self.horizontalLayout_5.addWidget(self.tb_fornecedores)

        self.frame_4 = QFrame(self.tab_fornecedores_list)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.btn_editar_fornecedor = QPushButton(self.frame_4)
        self.btn_editar_fornecedor.setObjectName(u"btn_editar_fornecedor")
        self.btn_editar_fornecedor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.btn_editar_fornecedor)

        self.btn_excluir_fornecedor = QPushButton(self.frame_4)
        self.btn_excluir_fornecedor.setObjectName(u"btn_excluir_fornecedor")
        self.btn_excluir_fornecedor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_13.addWidget(self.btn_excluir_fornecedor)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_7)


        self.horizontalLayout_5.addWidget(self.frame_4)


        self.verticalLayout_14.addLayout(self.horizontalLayout_5)

        self.tb_widget_fornecedores.addTab(self.tab_fornecedores_list, "")
        self.Tab_fornecedores_cadastro = QWidget()
        self.Tab_fornecedores_cadastro.setObjectName(u"Tab_fornecedores_cadastro")
        self.verticalLayout_5 = QVBoxLayout(self.Tab_fornecedores_cadastro)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.frame_3 = QFrame(self.Tab_fornecedores_cadastro)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_nome_fornecedor = QLineEdit(self.frame_3)
        self.txt_nome_fornecedor.setObjectName(u"txt_nome_fornecedor")
        self.txt_nome_fornecedor.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_nome_fornecedor, 2, 0, 1, 2)

        self.txt_telefone_fornecedor = QLineEdit(self.frame_3)
        self.txt_telefone_fornecedor.setObjectName(u"txt_telefone_fornecedor")
        self.txt_telefone_fornecedor.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_telefone_fornecedor, 3, 1, 1, 1)

        self.lb_cadastro_fornecedor = QLabel(self.frame_3)
        self.lb_cadastro_fornecedor.setObjectName(u"lb_cadastro_fornecedor")

        self.gridLayout_2.addWidget(self.lb_cadastro_fornecedor, 1, 0, 1, 2, Qt.AlignHCenter)

        self.txt_cidade_fornecedor = QLineEdit(self.frame_3)
        self.txt_cidade_fornecedor.setObjectName(u"txt_cidade_fornecedor")
        self.txt_cidade_fornecedor.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cidade_fornecedor, 3, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.btn_cadastrar_fornecedor = QPushButton(self.Tab_fornecedores_cadastro)
        self.btn_cadastrar_fornecedor.setObjectName(u"btn_cadastrar_fornecedor")
        self.btn_cadastrar_fornecedor.setMinimumSize(QSize(150, 30))
        self.btn_cadastrar_fornecedor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_cadastrar_fornecedor, 0, Qt.AlignHCenter)

        self.tb_widget_fornecedores.addTab(self.Tab_fornecedores_cadastro, "")

        self.verticalLayout_15.addWidget(self.tb_widget_fornecedores)

        self.Pages.addWidget(self.pg_fornecedores)
        self.pg_fornecedores_detail = QWidget()
        self.pg_fornecedores_detail.setObjectName(u"pg_fornecedores_detail")
        self.verticalLayout_40 = QVBoxLayout(self.pg_fornecedores_detail)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.tab_widget_fornecedor_detail = QTabWidget(self.pg_fornecedores_detail)
        self.tab_widget_fornecedor_detail.setObjectName(u"tab_widget_fornecedor_detail")
        self.tb_fornecedor_detail_detalhe = QWidget()
        self.tb_fornecedor_detail_detalhe.setObjectName(u"tb_fornecedor_detail_detalhe")
        self.horizontalLayout_14 = QHBoxLayout(self.tb_fornecedor_detail_detalhe)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_27 = QFrame(self.tb_fornecedor_detail_detalhe)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_27)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_26 = QFrame(self.frame_27)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_26)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.lb_nome_fornecedor_detail = QLabel(self.frame_26)
        self.lb_nome_fornecedor_detail.setObjectName(u"lb_nome_fornecedor_detail")

        self.gridLayout_11.addWidget(self.lb_nome_fornecedor_detail, 1, 0, 1, 1)

        self.lb_cidade_fornecedor_detail = QLabel(self.frame_26)
        self.lb_cidade_fornecedor_detail.setObjectName(u"lb_cidade_fornecedor_detail")

        self.gridLayout_11.addWidget(self.lb_cidade_fornecedor_detail, 2, 0, 1, 1)

        self.lb_telefone_fornecedor_detail = QLabel(self.frame_26)
        self.lb_telefone_fornecedor_detail.setObjectName(u"lb_telefone_fornecedor_detail")

        self.gridLayout_11.addWidget(self.lb_telefone_fornecedor_detail, 2, 2, 1, 1)

        self.label_5 = QLabel(self.frame_26)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 3)


        self.verticalLayout_41.addWidget(self.frame_26)

        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_28)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lb_num_compras_fornecedor_detail = QLabel(self.frame_28)
        self.lb_num_compras_fornecedor_detail.setObjectName(u"lb_num_compras_fornecedor_detail")

        self.gridLayout_10.addWidget(self.lb_num_compras_fornecedor_detail, 1, 0, 1, 1)

        self.lb_total_gasto_fornecedor_detail = QLabel(self.frame_28)
        self.lb_total_gasto_fornecedor_detail.setObjectName(u"lb_total_gasto_fornecedor_detail")

        self.gridLayout_10.addWidget(self.lb_total_gasto_fornecedor_detail, 1, 1, 1, 1)

        self.lb_status_fornecedor_detail = QLabel(self.frame_28)
        self.lb_status_fornecedor_detail.setObjectName(u"lb_status_fornecedor_detail")

        self.gridLayout_10.addWidget(self.lb_status_fornecedor_detail, 2, 0, 1, 1)

        self.label_21 = QLabel(self.frame_28)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_21, 0, 0, 1, 2)


        self.verticalLayout_41.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_29)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.btn_contato_fornecedor = QPushButton(self.frame_29)
        self.btn_contato_fornecedor.setObjectName(u"btn_contato_fornecedor")
        self.btn_contato_fornecedor.setMinimumSize(QSize(150, 0))
        self.btn_contato_fornecedor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_48.addWidget(self.btn_contato_fornecedor, 0, Qt.AlignHCenter)

        self.frame_33 = QFrame(self.frame_29)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 80))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_33)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_30 = QLabel(self.frame_33)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_43.addWidget(self.label_30)


        self.verticalLayout_48.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_29)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_34)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_32 = QLabel(self.frame_34)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_47.addWidget(self.label_32, 0, Qt.AlignHCenter)


        self.verticalLayout_48.addWidget(self.frame_34)


        self.verticalLayout_41.addWidget(self.frame_29)


        self.horizontalLayout_14.addWidget(self.frame_27)

        self.frame_20 = QFrame(self.tb_fornecedor_detail_detalhe)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_20)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_31 = QFrame(self.frame_20)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_31)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_31 = QLabel(self.frame_31)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_44.addWidget(self.label_31, 0, Qt.AlignHCenter)


        self.verticalLayout_42.addWidget(self.frame_31)

        self.frame_graph_fornecedor_detail = QFrame(self.frame_20)
        self.frame_graph_fornecedor_detail.setObjectName(u"frame_graph_fornecedor_detail")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_graph_fornecedor_detail.sizePolicy().hasHeightForWidth())
        self.frame_graph_fornecedor_detail.setSizePolicy(sizePolicy6)
        self.frame_graph_fornecedor_detail.setFrameShape(QFrame.StyledPanel)
        self.frame_graph_fornecedor_detail.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_graph_fornecedor_detail)
        self.gridLayout_12.setObjectName(u"gridLayout_12")

        self.verticalLayout_42.addWidget(self.frame_graph_fornecedor_detail)

        self.frame_32 = QFrame(self.frame_20)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_anterior_ano_fornecedor_detail = QPushButton(self.frame_32)
        self.btn_anterior_ano_fornecedor_detail.setObjectName(u"btn_anterior_ano_fornecedor_detail")
        self.btn_anterior_ano_fornecedor_detail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_15.addWidget(self.btn_anterior_ano_fornecedor_detail)

        self.lb_ano_fornecedor_detail = QLabel(self.frame_32)
        self.lb_ano_fornecedor_detail.setObjectName(u"lb_ano_fornecedor_detail")

        self.horizontalLayout_15.addWidget(self.lb_ano_fornecedor_detail, 0, Qt.AlignHCenter)

        self.btn_proximo_ano_fornecedor_detail = QPushButton(self.frame_32)
        self.btn_proximo_ano_fornecedor_detail.setObjectName(u"btn_proximo_ano_fornecedor_detail")
        self.btn_proximo_ano_fornecedor_detail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_15.addWidget(self.btn_proximo_ano_fornecedor_detail)


        self.verticalLayout_42.addWidget(self.frame_32)


        self.horizontalLayout_14.addWidget(self.frame_20)

        self.tab_widget_fornecedor_detail.addTab(self.tb_fornecedor_detail_detalhe, "")
        self.tab_compras_fornecedor_detail = QWidget()
        self.tab_compras_fornecedor_detail.setObjectName(u"tab_compras_fornecedor_detail")
        self.verticalLayout_46 = QVBoxLayout(self.tab_compras_fornecedor_detail)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_16 = QLabel(self.tab_compras_fornecedor_detail)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_46.addWidget(self.label_16, 0, Qt.AlignHCenter)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.tableWidget = QTableWidget(self.tab_compras_fornecedor_detail)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSortingEnabled(True)

        self.horizontalLayout_16.addWidget(self.tableWidget)

        self.frame_30 = QFrame(self.tab_compras_fornecedor_detail)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_30)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.btn_excluir_compra_fornecedor_detail = QPushButton(self.frame_30)
        self.btn_excluir_compra_fornecedor_detail.setObjectName(u"btn_excluir_compra_fornecedor_detail")
        self.btn_excluir_compra_fornecedor_detail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_45.addWidget(self.btn_excluir_compra_fornecedor_detail)

        self.btn_editar_compra_fornecedor_detail = QPushButton(self.frame_30)
        self.btn_editar_compra_fornecedor_detail.setObjectName(u"btn_editar_compra_fornecedor_detail")
        self.btn_editar_compra_fornecedor_detail.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_45.addWidget(self.btn_editar_compra_fornecedor_detail)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_45.addItem(self.verticalSpacer_20)


        self.horizontalLayout_16.addWidget(self.frame_30)


        self.verticalLayout_46.addLayout(self.horizontalLayout_16)

        self.tab_widget_fornecedor_detail.addTab(self.tab_compras_fornecedor_detail, "")

        self.verticalLayout_40.addWidget(self.tab_widget_fornecedor_detail)

        self.Pages.addWidget(self.pg_fornecedores_detail)
        self.pg_produtos_detail = QWidget()
        self.pg_produtos_detail.setObjectName(u"pg_produtos_detail")
        self.verticalLayout_49 = QVBoxLayout(self.pg_produtos_detail)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_35 = QFrame(self.pg_produtos_detail)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_36)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_38 = QFrame(self.frame_36)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_38)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.lb_nome_produto_detail = QLabel(self.frame_38)
        self.lb_nome_produto_detail.setObjectName(u"lb_nome_produto_detail")

        self.gridLayout_13.addWidget(self.lb_nome_produto_detail, 1, 0, 1, 1)

        self.lb_medida_produto_detail = QLabel(self.frame_38)
        self.lb_medida_produto_detail.setObjectName(u"lb_medida_produto_detail")

        self.gridLayout_13.addWidget(self.lb_medida_produto_detail, 2, 0, 1, 1)

        self.lb_valor_medida_produto_detail = QLabel(self.frame_38)
        self.lb_valor_medida_produto_detail.setObjectName(u"lb_valor_medida_produto_detail")

        self.gridLayout_13.addWidget(self.lb_valor_medida_produto_detail, 2, 1, 1, 1)

        self.label_18 = QLabel(self.frame_38)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_13.addWidget(self.label_18, 0, 0, 1, 2, Qt.AlignHCenter)


        self.verticalLayout_50.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_36)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_39)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.lb_best_fornecedor_produto = QLabel(self.frame_39)
        self.lb_best_fornecedor_produto.setObjectName(u"lb_best_fornecedor_produto")

        self.gridLayout_14.addWidget(self.lb_best_fornecedor_produto, 1, 0, 1, 2)

        self.lb_best_fornecedor_produto_valor_medida = QLabel(self.frame_39)
        self.lb_best_fornecedor_produto_valor_medida.setObjectName(u"lb_best_fornecedor_produto_valor_medida")

        self.gridLayout_14.addWidget(self.lb_best_fornecedor_produto_valor_medida, 1, 2, 1, 1)

        self.lb_produto_valor_gasto = QLabel(self.frame_39)
        self.lb_produto_valor_gasto.setObjectName(u"lb_produto_valor_gasto")

        self.gridLayout_14.addWidget(self.lb_produto_valor_gasto, 2, 0, 1, 1)

        self.label_35 = QLabel(self.frame_39)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_14.addWidget(self.label_35, 2, 1, 1, 1)

        self.lb_produto_valor_ganho = QLabel(self.frame_39)
        self.lb_produto_valor_ganho.setObjectName(u"lb_produto_valor_ganho")

        self.gridLayout_14.addWidget(self.lb_produto_valor_ganho, 2, 2, 1, 1)

        self.lb_lucro_margem = QLabel(self.frame_39)
        self.lb_lucro_margem.setObjectName(u"lb_lucro_margem")

        self.gridLayout_14.addWidget(self.lb_lucro_margem, 3, 0, 1, 2)

        self.label_26 = QLabel(self.frame_39)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout_14.addWidget(self.label_26, 0, 0, 1, 3, Qt.AlignHCenter)


        self.verticalLayout_50.addWidget(self.frame_39)


        self.horizontalLayout_17.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_37)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_41 = QFrame(self.frame_37)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_41)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_39 = QLabel(self.frame_41)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_52.addWidget(self.label_39, 0, Qt.AlignHCenter)


        self.verticalLayout_51.addWidget(self.frame_41)

        self.frame_graph_produto = QFrame(self.frame_37)
        self.frame_graph_produto.setObjectName(u"frame_graph_produto")
        sizePolicy6.setHeightForWidth(self.frame_graph_produto.sizePolicy().hasHeightForWidth())
        self.frame_graph_produto.setSizePolicy(sizePolicy6)
        self.frame_graph_produto.setFrameShape(QFrame.StyledPanel)
        self.frame_graph_produto.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_graph_produto)
        self.gridLayout_15.setObjectName(u"gridLayout_15")

        self.verticalLayout_51.addWidget(self.frame_graph_produto)

        self.frame_43 = QFrame(self.frame_37)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_anterior_graph_produto = QPushButton(self.frame_43)
        self.btn_anterior_graph_produto.setObjectName(u"btn_anterior_graph_produto")

        self.horizontalLayout_18.addWidget(self.btn_anterior_graph_produto)

        self.lb_ano_graph_produto = QLabel(self.frame_43)
        self.lb_ano_graph_produto.setObjectName(u"lb_ano_graph_produto")

        self.horizontalLayout_18.addWidget(self.lb_ano_graph_produto, 0, Qt.AlignHCenter)

        self.btn_proximo_graph_produto = QPushButton(self.frame_43)
        self.btn_proximo_graph_produto.setObjectName(u"btn_proximo_graph_produto")

        self.horizontalLayout_18.addWidget(self.btn_proximo_graph_produto)


        self.verticalLayout_51.addWidget(self.frame_43)


        self.horizontalLayout_17.addWidget(self.frame_37)


        self.verticalLayout_49.addWidget(self.frame_35)

        self.Pages.addWidget(self.pg_produtos_detail)
        self.pg_produtos = QWidget()
        self.pg_produtos.setObjectName(u"pg_produtos")
        self.verticalLayout_17 = QVBoxLayout(self.pg_produtos)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.tb_widget_produtos = QTabWidget(self.pg_produtos)
        self.tb_widget_produtos.setObjectName(u"tb_widget_produtos")
        self.tab_produtos_list = QWidget()
        self.tab_produtos_list.setObjectName(u"tab_produtos_list")
        self.verticalLayout_18 = QVBoxLayout(self.tab_produtos_list)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label = QLabel(self.tab_produtos_list)
        self.label.setObjectName(u"label")

        self.verticalLayout_18.addWidget(self.label, 0, Qt.AlignHCenter)

        self.txt_search_produtos = QLineEdit(self.tab_produtos_list)
        self.txt_search_produtos.setObjectName(u"txt_search_produtos")

        self.verticalLayout_18.addWidget(self.txt_search_produtos)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tb_produtos = QTableWidget(self.tab_produtos_list)
        if (self.tb_produtos.columnCount() < 4):
            self.tb_produtos.setColumnCount(4)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tb_produtos.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        self.tb_produtos.setObjectName(u"tb_produtos")
        self.tb_produtos.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tb_produtos.setSortingEnabled(True)

        self.horizontalLayout_6.addWidget(self.tb_produtos)

        self.frame_5 = QFrame(self.tab_produtos_list)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.btn_edit_product = QPushButton(self.frame_5)
        self.btn_edit_product.setObjectName(u"btn_edit_product")
        self.btn_edit_product.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.btn_edit_product)

        self.btn_excluir_product = QPushButton(self.frame_5)
        self.btn_excluir_product.setObjectName(u"btn_excluir_product")
        self.btn_excluir_product.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.btn_excluir_product)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_8)


        self.horizontalLayout_6.addWidget(self.frame_5)


        self.verticalLayout_18.addLayout(self.horizontalLayout_6)

        self.tb_widget_produtos.addTab(self.tab_produtos_list, "")
        self.tab_produtos_cadastrar = QWidget()
        self.tab_produtos_cadastrar.setObjectName(u"tab_produtos_cadastrar")
        sizePolicy.setHeightForWidth(self.tab_produtos_cadastrar.sizePolicy().hasHeightForWidth())
        self.tab_produtos_cadastrar.setSizePolicy(sizePolicy)
        self.verticalLayout_19 = QVBoxLayout(self.tab_produtos_cadastrar)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_10)

        self.frame_6 = QFrame(self.tab_produtos_cadastrar)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.txt_nome_produto = QLineEdit(self.frame_6)
        self.txt_nome_produto.setObjectName(u"txt_nome_produto")
        self.txt_nome_produto.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_nome_produto, 2, 0, 1, 2)

        self.lb_cadastro_produto = QLabel(self.frame_6)
        self.lb_cadastro_produto.setObjectName(u"lb_cadastro_produto")
        self.lb_cadastro_produto.setLayoutDirection(Qt.LeftToRight)
        self.lb_cadastro_produto.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_cadastro_produto, 1, 0, 1, 2)

        self.select_medida_produto = QComboBox(self.frame_6)
        self.select_medida_produto.addItem("")
        self.select_medida_produto.addItem("")
        self.select_medida_produto.addItem("")
        self.select_medida_produto.addItem("")
        self.select_medida_produto.addItem("")
        self.select_medida_produto.addItem("")
        self.select_medida_produto.addItem("")
        self.select_medida_produto.setObjectName(u"select_medida_produto")
        self.select_medida_produto.setMinimumSize(QSize(250, 0))

        self.gridLayout_3.addWidget(self.select_medida_produto, 3, 0, 1, 1)

        self.txt_preco_produto = QLineEdit(self.frame_6)
        self.txt_preco_produto.setObjectName(u"txt_preco_produto")
        self.txt_preco_produto.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_preco_produto, 3, 1, 1, 1)


        self.verticalLayout_19.addWidget(self.frame_6)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_9)

        self.btn_cadastrar_produto = QPushButton(self.tab_produtos_cadastrar)
        self.btn_cadastrar_produto.setObjectName(u"btn_cadastrar_produto")
        self.btn_cadastrar_produto.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_cadastrar_produto.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar_produto.setSizePolicy(sizePolicy7)
        self.btn_cadastrar_produto.setMinimumSize(QSize(150, 30))
        self.btn_cadastrar_produto.setMaximumSize(QSize(180, 29))
        self.btn_cadastrar_produto.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_produto.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_19.addWidget(self.btn_cadastrar_produto, 0, Qt.AlignHCenter)

        self.tb_widget_produtos.addTab(self.tab_produtos_cadastrar, "")

        self.verticalLayout_17.addWidget(self.tb_widget_produtos)

        self.Pages.addWidget(self.pg_produtos)

        self.verticalLayout_20.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_copy = QLabel(self.footer_frame)
        self.lb_copy.setObjectName(u"lb_copy")

        self.horizontalLayout_3.addWidget(self.lb_copy, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.footer_frame)


        self.gridLayout_8.addWidget(self.main_container, 0, 1, 1, 1)

        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(0, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_frame = QFrame(self.left_container)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.logo_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.logo_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.logo_frame)

        self.buttons_frame = QFrame(self.left_container)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.buttons_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.toolBox = QToolBox(self.buttons_frame)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 108, 531))
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_menu_home = QPushButton(self.page)
        self.btn_menu_home.setObjectName(u"btn_menu_home")
        self.btn_menu_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_menu_home)

        self.btn_menu_clientes = QPushButton(self.page)
        self.btn_menu_clientes.setObjectName(u"btn_menu_clientes")
        self.btn_menu_clientes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_menu_clientes)

        self.btn_menu_fornecedores = QPushButton(self.page)
        self.btn_menu_fornecedores.setObjectName(u"btn_menu_fornecedores")
        self.btn_menu_fornecedores.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_menu_fornecedores)

        self.btn_menu_produtos = QPushButton(self.page)
        self.btn_menu_produtos.setObjectName(u"btn_menu_produtos")
        self.btn_menu_produtos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_menu_produtos)

        self.btn_menu_vendas = QPushButton(self.page)
        self.btn_menu_vendas.setObjectName(u"btn_menu_vendas")
        self.btn_menu_vendas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_menu_vendas)

        self.btn_menu_compras = QPushButton(self.page)
        self.btn_menu_compras.setObjectName(u"btn_menu_compras")
        self.btn_menu_compras.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_menu_compras)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 170, 531))
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_7.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_15)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_14)

        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_7.addWidget(self.label_11)

        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_7.addWidget(self.label_12)

        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_7.addWidget(self.label_13)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_13)

        self.toolBox.addItem(self.page_2, u"Informa\u00e7\u00f5es")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.buttons_frame)


        self.gridLayout_8.addWidget(self.left_container, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)
        self.tb_widget_compras.setCurrentIndex(0)
        self.tb_widget_vendas.setCurrentIndex(0)
        self.tb_widget_client_detail.setCurrentIndex(0)
        self.tb_widget_clientes.setCurrentIndex(0)
        self.tb_widget_fornecedores.setCurrentIndex(0)
        self.tab_widget_fornecedor_detail.setCurrentIndex(0)
        self.tb_widget_produtos.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText("")
        self.lb_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">CONTROLE DE NOTAS</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"COMPRAS", None))
        self.txt_search_compras.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem = self.table_compras.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_compras.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"FORNECEDOR", None));
        ___qtablewidgetitem2 = self.table_compras.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"DATA", None));
        ___qtablewidgetitem3 = self.table_compras.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.btn_compra_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_compra_editar.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.tb_widget_compras.setTabText(self.tb_widget_compras.indexOf(self.tb_compras_list), QCoreApplication.translate("MainWindow", u"Compras", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Compra", None))
        self.txt_compra_data.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Compra", None))
        self.txt_compra_quant.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.lb_compra_medida.setText(QCoreApplication.translate("MainWindow", u"Medida: ", None))
        self.select_compra_pagamento.setItemText(0, QCoreApplication.translate("MainWindow", u"Forma de Pagamento", None))
        self.select_compra_pagamento.setItemText(1, QCoreApplication.translate("MainWindow", u"A vista", None))
        self.select_compra_pagamento.setItemText(2, QCoreApplication.translate("MainWindow", u"Credito", None))
        self.select_compra_pagamento.setItemText(3, QCoreApplication.translate("MainWindow", u"D\u00e9bito", None))
        self.select_compra_pagamento.setItemText(4, QCoreApplication.translate("MainWindow", u"Prazo", None))

        self.select_compra_fornecedor.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione o Fornecedor", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Data da Compra", None))
        self.select_compra_produto.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione um Produto", None))

        self.btn_add_produto_compra.setText(QCoreApplication.translate("MainWindow", u"Adicionar Produto", None))
        self.select_compra_status.setItemText(0, QCoreApplication.translate("MainWindow", u"Status da Compra", None))
        self.select_compra_status.setItemText(1, QCoreApplication.translate("MainWindow", u"AGUARDANDO PAGAMENTO", None))
        self.select_compra_status.setItemText(2, QCoreApplication.translate("MainWindow", u"PAGO", None))
        self.select_compra_status.setItemText(3, QCoreApplication.translate("MainWindow", u"ATRASADO", None))

        self.txt_compra_vencimento.setText("")
        self.txt_compra_vencimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Vencimento", None))
        self.txt_compra_precmedida.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o / Medida", None))
        self.lb_compra_vencimento.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None))
        ___qtablewidgetitem4 = self.tb_produtos_compra_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem5 = self.tb_produtos_compra_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem6 = self.tb_produtos_compra_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o / Medida", None));
        ___qtablewidgetitem7 = self.tb_produtos_compra_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Subtotal", None));
        self.btn_remover_produto_compra.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.lb_total_compra.setText(QCoreApplication.translate("MainWindow", u"Total R$ ", None))
        self.btn_compra_registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.tb_widget_compras.setTabText(self.tb_widget_compras.indexOf(self.tb_compras_cadastro), QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.lb_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/Logo.png\"/></p></body></html>", None))
        self.btn_inicia_semana.setText(QCoreApplication.translate("MainWindow", u"Inicia Semana", None))
        self.btn_fecha_semana.setText(QCoreApplication.translate("MainWindow", u"Fechar Semana", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"VENDAS", None))
        self.txt_vendas_pesquisar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem8 = self.tb_vendas.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem9 = self.tb_vendas.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem10 = self.tb_vendas.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem11 = self.tb_vendas.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.btn_venda_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_venda_edit.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_venda_print.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.tb_widget_vendas.setTabText(self.tb_widget_vendas.indexOf(self.tb_vendas_list), QCoreApplication.translate("MainWindow", u"Vendas", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VENDA", None))
        self.lb_vendas_medida.setText(QCoreApplication.translate("MainWindow", u"Medida: ", None))
        self.select_pagamento_venda.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione o Tipo de Pagamento", None))
        self.select_pagamento_venda.setItemText(1, QCoreApplication.translate("MainWindow", u"A vista", None))
        self.select_pagamento_venda.setItemText(2, QCoreApplication.translate("MainWindow", u"Credito", None))
        self.select_pagamento_venda.setItemText(3, QCoreApplication.translate("MainWindow", u"Debito", None))
        self.select_pagamento_venda.setItemText(4, QCoreApplication.translate("MainWindow", u"Prazo", None))

        self.txt_venda_vencimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Vencimento", None))
        ___qtablewidgetitem12 = self.tb_vendas_itens.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem13 = self.tb_vendas_itens.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem14 = self.tb_vendas_itens.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o / Medida", None));
        ___qtablewidgetitem15 = self.tb_vendas_itens.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"SubTotal", None));
        self.lb_vencimento_venda.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None))
        self.select_status_venda.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione o status da venda", None))
        self.select_status_venda.setItemText(1, QCoreApplication.translate("MainWindow", u"PAGO", None))
        self.select_status_venda.setItemText(2, QCoreApplication.translate("MainWindow", u"AGUARDANDO PAGAMENTO", None))
        self.select_status_venda.setItemText(3, QCoreApplication.translate("MainWindow", u"ATRASADO", None))

        self.btn_remove_venda_register.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.btn_cancel_venda.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.txt_venda_quantidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.txt_venda_data.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data de Venda", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Data da Venda", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.select_client_venda.setCurrentText("")
        self.lb_venda_total.setText(QCoreApplication.translate("MainWindow", u"Total: R$ 0,00", None))
        self.btn_venda_addProduto.setText(QCoreApplication.translate("MainWindow", u"Add Produto", None))
        self.btn_venda_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.tb_widget_vendas.setTabText(self.tb_widget_vendas.indexOf(self.tb_vendas_cadastro), QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.lb_pedido_da_semana.setText(QCoreApplication.translate("MainWindow", u"Pedidos da semana", None))
        self.txt_semanal_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem16 = self.tab_pedido_semana.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Produto", None));
        ___qtablewidgetitem17 = self.tab_pedido_semana.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Medida", None));
        ___qtablewidgetitem18 = self.tab_pedido_semana.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        self.btn_download_list.setText(QCoreApplication.translate("MainWindow", u"Download excel", None))
        self.tb_widget_vendas.setTabText(self.tb_widget_vendas.indexOf(self.tb_vendas_produtos_semanal), QCoreApplication.translate("MainWindow", u"Pedidos da Semana", None))
        self.lb_nome_cliente_detail.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.lb_cpf_cliente_detail.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.lb_telefone_cliente_detail.setText(QCoreApplication.translate("MainWindow", u"Telefone: ", None))
        self.lb_endereco_cliente_detail.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"DADOS", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"RESUMO", None))
        self.lb_total_gasto_cliente.setText(QCoreApplication.translate("MainWindow", u"Total Gasto: R$", None))
        self.lb_num_pedidos_cliente.setText(QCoreApplication.translate("MainWindow", u"N\u00ba de Pedidos:", None))
        self.lb_status_cliente.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.btn_contato_cliente.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/whats.png\"/></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Acesso Via Whatapp Web", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"EVOLU\u00c7\u00c3O DOS PEDIDOS", None))
        self.btn_anterior_graph_cliente.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.lb_ano_graph_cliente.setText(QCoreApplication.translate("MainWindow", u"2023", None))
        self.btn_proximo_graph_cliente.setText(QCoreApplication.translate("MainWindow", u"Prox\u00edmo", None))
        self.tb_widget_client_detail.setTabText(self.tb_widget_client_detail.indexOf(self.tb_client_detail_info), QCoreApplication.translate("MainWindow", u"Detalhe", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Pedidos / Vendas", None))
        ___qtablewidgetitem19 = self.tb_widget_vendas_cliente_detail.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem20 = self.tb_widget_vendas_cliente_detail.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"DATA", None));
        ___qtablewidgetitem21 = self.tb_widget_vendas_cliente_detail.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"TOTAL", None));
        ___qtablewidgetitem22 = self.tb_widget_vendas_cliente_detail.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.btn_excluir_venda_cliente_detail.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_editar_venda_cliente_detail.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_imprimir_venda_cliente_detail.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.tb_widget_client_detail.setTabText(self.tb_widget_client_detail.indexOf(self.tb_client_detail_pedidos), QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.lb_clientes.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.txt_search_client.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem23 = self.tb_clientes.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem24 = self.tb_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem25 = self.tb_clientes.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None));
        ___qtablewidgetitem26 = self.tb_clientes.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        self.btn_client_edit.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_client_remove.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tb_widget_clientes.setTabText(self.tb_widget_clientes.indexOf(self.tab_clientes_list), QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.txt_estado_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_endereco_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.txt_nome_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_telefone_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_numero_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numero", None))
        self.txt_cpf_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_cidade_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.txt_bairro_cliente.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.lb_client_cadastro.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None))
        self.btn_cadastrar_cliente.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.tb_widget_clientes.setTabText(self.tb_widget_clientes.indexOf(self.tab_clientes_register), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.lb_fornecedores.setText(QCoreApplication.translate("MainWindow", u"FORNECEDORES", None))
        self.txt_search_fornecedores.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem27 = self.tb_fornecedores.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem28 = self.tb_fornecedores.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem29 = self.tb_fornecedores.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None));
        ___qtablewidgetitem30 = self.tb_fornecedores.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        self.btn_editar_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_excluir_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tb_widget_fornecedores.setTabText(self.tb_widget_fornecedores.indexOf(self.tab_fornecedores_list), QCoreApplication.translate("MainWindow", u"Fornecedores", None))
        self.txt_nome_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_telefone_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.lb_cadastro_fornecedor.setText(QCoreApplication.translate("MainWindow", u"FORNECEDOR", None))
        self.txt_cidade_fornecedor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.btn_cadastrar_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tb_widget_fornecedores.setTabText(self.tb_widget_fornecedores.indexOf(self.Tab_fornecedores_cadastro), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.lb_nome_fornecedor_detail.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.lb_cidade_fornecedor_detail.setText(QCoreApplication.translate("MainWindow", u"Cidade: ", None))
        self.lb_telefone_fornecedor_detail.setText(QCoreApplication.translate("MainWindow", u"Telefone: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"DADOS", None))
        self.lb_num_compras_fornecedor_detail.setText(QCoreApplication.translate("MainWindow", u"N\u00ba de Compras: ", None))
        self.lb_total_gasto_fornecedor_detail.setText(QCoreApplication.translate("MainWindow", u"Total Gasto: R$", None))
        self.lb_status_fornecedor_detail.setText(QCoreApplication.translate("MainWindow", u"Status: ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"RESUMO", None))
        self.btn_contato_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/whats.png\"/></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Acesso Via Whatapp Web", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Evolu\u00e7\u00e3o de Pedidos", None))
        self.btn_anterior_ano_fornecedor_detail.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.lb_ano_fornecedor_detail.setText(QCoreApplication.translate("MainWindow", u"2023", None))
        self.btn_proximo_ano_fornecedor_detail.setText(QCoreApplication.translate("MainWindow", u"Proximo", None))
        self.tab_widget_fornecedor_detail.setTabText(self.tab_widget_fornecedor_detail.indexOf(self.tb_fornecedor_detail_detalhe), QCoreApplication.translate("MainWindow", u"Detalhe", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Compras", None))
        ___qtablewidgetitem31 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem32 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"DATA", None));
        ___qtablewidgetitem33 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"TOTAL", None));
        ___qtablewidgetitem34 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        self.btn_excluir_compra_fornecedor_detail.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_editar_compra_fornecedor_detail.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.tab_widget_fornecedor_detail.setTabText(self.tab_widget_fornecedor_detail.indexOf(self.tab_compras_fornecedor_detail), QCoreApplication.translate("MainWindow", u"Compras", None))
        self.lb_nome_produto_detail.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.lb_medida_produto_detail.setText(QCoreApplication.translate("MainWindow", u"Medida: ", None))
        self.lb_valor_medida_produto_detail.setText(QCoreApplication.translate("MainWindow", u"Valor / Medida:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"DADOS", None))
        self.lb_best_fornecedor_produto.setText(QCoreApplication.translate("MainWindow", u"Melhor Fornecedor:", None))
        self.lb_best_fornecedor_produto_valor_medida.setText(QCoreApplication.translate("MainWindow", u"Valor / Medida:", None))
        self.lb_produto_valor_gasto.setText(QCoreApplication.translate("MainWindow", u"Total Gasto Compra: R$", None))
        self.label_35.setText("")
        self.lb_produto_valor_ganho.setText(QCoreApplication.translate("MainWindow", u"Total Ganho Venda: R$", None))
        self.lb_lucro_margem.setText(QCoreApplication.translate("MainWindow", u"Lucro / Margem: R$ / %", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"RESUMO", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Vendas no Ano", None))
        self.btn_anterior_graph_produto.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.lb_ano_graph_produto.setText(QCoreApplication.translate("MainWindow", u"2023", None))
        self.btn_proximo_graph_produto.setText(QCoreApplication.translate("MainWindow", u"Pr\u00f3ximo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PRODUTOS", None))
        self.txt_search_produtos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem35 = self.tb_produtos.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem36 = self.tb_produtos.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem37 = self.tb_produtos.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"MEDIDA", None));
        ___qtablewidgetitem38 = self.tb_produtos.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"PRE\u00c7O / MEDIDA", None));
        self.btn_edit_product.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_excluir_product.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tb_widget_produtos.setTabText(self.tb_widget_produtos.indexOf(self.tab_produtos_list), QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.txt_nome_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lb_cadastro_produto.setText(QCoreApplication.translate("MainWindow", u"PRODUTO", None))
        self.select_medida_produto.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione a Medida do Produto", None))
        self.select_medida_produto.setItemText(1, QCoreApplication.translate("MainWindow", u"Caixa", None))
        self.select_medida_produto.setItemText(2, QCoreApplication.translate("MainWindow", u"Fardo", None))
        self.select_medida_produto.setItemText(3, QCoreApplication.translate("MainWindow", u"Kg", None))
        self.select_medida_produto.setItemText(4, QCoreApplication.translate("MainWindow", u"Litro", None))
        self.select_medida_produto.setItemText(5, QCoreApplication.translate("MainWindow", u"Saco", None))
        self.select_medida_produto.setItemText(6, QCoreApplication.translate("MainWindow", u"Unidade", None))

        self.select_medida_produto.setCurrentText(QCoreApplication.translate("MainWindow", u"Selecione a Medida do Produto", None))
        self.txt_preco_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o por Medida", None))
        self.btn_cadastrar_produto.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.tb_widget_produtos.setTabText(self.tb_widget_produtos.indexOf(self.tab_produtos_cadastrar), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.lb_copy.setText(QCoreApplication.translate("MainWindow", u"Copyright @ OffsetDev 2023", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Controle de Notas</span></p></body></html>", None))
        self.btn_menu_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_menu_clientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_menu_fornecedores.setText(QCoreApplication.translate("MainWindow", u"Fornecedores", None))
        self.btn_menu_produtos.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.btn_menu_vendas.setText(QCoreApplication.translate("MainWindow", u"Vendas / Pedidos", None))
        self.btn_menu_compras.setText(QCoreApplication.translate("MainWindow", u"Compras", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Erros e Bugs contatar:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Offset Dev ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"@offset.dev", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"(84) 99907-3360", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Rua.  Professor Emiliano Anauld", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"n 107, sala 02, centro", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Alexandria - RN", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
    # retranslateUi


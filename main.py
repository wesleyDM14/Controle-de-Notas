# -*- coding: utf-8 -*-
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QColor
from PySide6 import QtCore, QtWidgets
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from ui_main import Ui_MainWindow
from qt_material import apply_stylesheet
from database import Data_base
from escpos.printer import Usb

import datetime
import sys
import webbrowser
import pandas as pd


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle de Notas")
        appIcon = QIcon(":/icons/icone.png")
        self.setWindowIcon(appIcon)

        self.db = Data_base()
        self.today = datetime.date.today()
        
        self.search_clients()
        self.search_fornecedores()
        self.search_produtos()
        self.search_vendas()
        self.search_compras()
        self.search_produtos_semanal()

        self.ListProductsVenda = []
        self.ListProductsCompra = []
        self.ListProductsSemanal = []

        self.clienteAtual = None
        self.produtoAtual = None
        self.fornecedorAtual = None
        self.semanaAtual = db.get_open_week()

        self.strBobina = ""

        self.btn_menu.clicked.connect(self.leftMenu)

        headerClient = self.tb_clientes.horizontalHeader()
        headerClient.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headerClient.setSectionResizeMode(1, QHeaderView.Stretch)
        headerClient.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headerClient.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        headerFornecedores = self.tb_fornecedores.horizontalHeader()
        headerFornecedores.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headerFornecedores.setSectionResizeMode(1, QHeaderView.Stretch)
        headerFornecedores.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headerFornecedores.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        headerProduto = self.tb_produtos.horizontalHeader()
        headerProduto.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headerProduto.setSectionResizeMode(1, QHeaderView.Stretch)
        headerProduto.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headerProduto.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        headerVenda = self.tb_vendas.horizontalHeader()
        headerVenda.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headerVenda.setSectionResizeMode(1, QHeaderView.Stretch)
        headerVenda.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headerVenda.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        headerVenda.setSectionResizeMode(4, QHeaderView.ResizeToContents)

        headerVendaItens = self.tb_vendas_itens.horizontalHeader()
        headerVendaItens.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headerVendaItens.setSectionResizeMode(1, QHeaderView.Stretch)
        headerVendaItens.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headerVendaItens.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        headerComprasItens = self.tb_produtos_compra_widget.horizontalHeader()
        headerComprasItens.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headerComprasItens.setSectionResizeMode(1, QHeaderView.Stretch)
        headerComprasItens.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headerComprasItens.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        headerCompras = self.table_compras.horizontalHeader()
        headerCompras.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headerCompras.setSectionResizeMode(1, QHeaderView.Stretch)
        headerCompras.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headerCompras.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        headerPedidosDetalhe = self.tb_widget_vendas_cliente_detail.horizontalHeader()
        headerPedidosDetalhe.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headerPedidosDetalhe.setSectionResizeMode(1, QHeaderView.Stretch)
        headerPedidosDetalhe.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headerPedidosDetalhe.setSectionResizeMode(3, QHeaderView.Stretch)

        headerComprasDetalhe = self.tableWidget.horizontalHeader()
        headerComprasDetalhe.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headerComprasDetalhe.setSectionResizeMode(1, QHeaderView.Stretch)
        headerComprasDetalhe.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headerComprasDetalhe.setSectionResizeMode(3, QHeaderView.Stretch)

        headerListPedidosProduto = self.tab_pedido_semana.horizontalHeader()
        headerListPedidosProduto.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        headerListPedidosProduto.setSectionResizeMode(0, QHeaderView.Stretch)
        headerListPedidosProduto.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.btn_menu_home.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_home)
        )
        self.btn_menu_clientes.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_clientes)
        )
        self.btn_menu_fornecedores.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_fornecedores)
        )
        self.btn_menu_produtos.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_produtos)
        )
        self.btn_menu_vendas.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_vendas)
        )
        self.btn_menu_compras.clicked.connect(
            lambda: self.Pages.setCurrentWidget(self.pg_compras)
        )

        self.btn_inicia_semana.clicked.connect(self.iniciar_nova_semana)
        self.btn_fecha_semana.clicked.connect(self.fechar_semana)

        self.btn_cadastrar_cliente.clicked.connect(self.register_client)
        self.btn_cadastrar_fornecedor.clicked.connect(self.register_fornecedor)
        self.btn_cadastrar_produto.clicked.connect(self.register_produto)
        self.btn_venda_cadastrar.clicked.connect(self.register_venda)
        self.btn_compra_registrar.clicked.connect(self.register_compra)

        self.btn_client_edit.clicked.connect(self.update_client)
        self.btn_editar_fornecedor.clicked.connect(self.update_fornecedor)
        self.btn_edit_product.clicked.connect(self.update_produto)
        self.btn_venda_edit.clicked.connect(self.update_venda)
        self.btn_compra_editar.clicked.connect(self.update_compra)
        self.btn_editar_compra_fornecedor_detail.clicked.connect(self.update_compra_aux)
        self.btn_editar_venda_cliente_detail.clicked.connect(
            self.update_venda_client_detail
        )
        self.btn_download_list.clicked.connect(self.export_to_excell)

        self.btn_client_remove.clicked.connect(self.delete_client)
        self.btn_excluir_fornecedor.clicked.connect(self.delete_fornecedor)
        self.btn_excluir_product.clicked.connect(self.delete_produto)
        self.btn_venda_excluir.clicked.connect(self.delete_venda)
        self.btn_compra_excluir.clicked.connect(self.delete_compra)
        self.btn_excluir_venda_cliente_detail.clicked.connect(self.delete_venda_aux)
        self.btn_excluir_compra_fornecedor_detail.clicked.connect(
            self.delete_compra_aux
        )

        self.btn_venda_print.clicked.connect(self.printer_venda)
        self.btn_imprimir_venda_cliente_detail.clicked.connect(
            self.printer_venda_detail
        )

        self.tb_clientes.clicked.connect(self.clicked_client)
        self.tb_fornecedores.clicked.connect(self.clicked_fornecedor)
        self.tb_produtos.clicked.connect(self.clicked_produto)

        self.strToday = self.today.strftime("%d/%m/%Y")
        dateAux = self.strToday.split("/")
        self.currentYear = dateAux[2]
        self.currentDay = dateAux[0]
        self.currentMonth = dateAux[1]

        self.txt_venda_data.setInputMask("99/99/9999")
        self.txt_compra_data.setInputMask("99/99/9999")

        self.txt_venda_data.setText(self.strToday)
        self.txt_compra_data.setText(self.strToday)

        self.btn_anterior_ano_fornecedor_detail.clicked.connect(
            self.anterior_current_year
        )
        self.btn_anterior_graph_cliente.clicked.connect(self.anterior_current_year)
        self.btn_anterior_graph_produto.clicked.connect(self.anterior_current_year)
        self.btn_proximo_ano_fornecedor_detail.clicked.connect(
            self.proximo_current_year
        )
        self.btn_proximo_graph_cliente.clicked.connect(self.proximo_current_year)
        self.btn_proximo_graph_produto.clicked.connect(self.proximo_current_year)

        self.select_produto_venda.activated.connect(self.change_venda_label)
        self.select_compra_produto.activated.connect(self.change_compra_label)

        self.select_pagamento_venda.activated.connect(self.change_vencimento_venda)
        self.select_compra_pagamento.activated.connect(self.change_vencimento_compra)

        self.btn_venda_addProduto.clicked.connect(self.add_product_to_venda)
        self.btn_remove_venda_register.clicked.connect(self.remove_product_to_venda)

        self.btn_add_produto_compra.clicked.connect(self.add_product_to_compra)
        self.btn_remover_produto_compra.clicked.connect(self.remove_product_to_compra)

        self.btn_contato_fornecedor.clicked.connect(
            lambda: self.contato_whatsapp_web("")
        )
        self.btn_contato_cliente.clicked.connect(lambda: self.contato_whatsapp_web(""))

        self.btn_cancel_venda.clicked.connect(self.reset_edits)

        self.txt_search_client.textChanged.connect(self.filter_clients)
        self.txt_search_produtos.textChanged.connect(self.filter_produtos)
        self.txt_search_fornecedores.textChanged.connect(self.filter_fornecedor)
        self.txt_vendas_pesquisar.textChanged.connect(self.filter_vendas)
        self.txt_search_compras.textChanged.connect(self.filter_compras)
        self.txt_semanal_search.textChanged.connect(self.filter_semanal_supplies)

        self.select_client_venda.setEditable(True)
        self.select_client_venda.setInsertPolicy(
            QtWidgets.QComboBox.InsertPolicy.NoInsert
        )
        self.select_client_venda.completer().setFilterMode(
            QtCore.Qt.MatchFlag.MatchContains
        )
        self.select_client_venda.completer().setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.PopupCompletion
        )

        self.select_produto_venda.setEditable(True)
        self.select_produto_venda.setInsertPolicy(
            QtWidgets.QComboBox.InsertPolicy.NoInsert
        )
        self.select_produto_venda.completer().setFilterMode(
            QtCore.Qt.MatchFlag.MatchContains
        )
        self.select_produto_venda.completer().setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.PopupCompletion
        )

        self.select_compra_fornecedor.setEditable(True)
        self.select_compra_fornecedor.setInsertPolicy(
            QtWidgets.QComboBox.InsertPolicy.NoInsert
        )
        self.select_compra_fornecedor.completer().setFilterMode(
            QtCore.Qt.MatchFlag.MatchContains
        )
        self.select_compra_fornecedor.completer().setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.PopupCompletion
        )

        self.select_compra_produto.setEditable(True)
        self.select_compra_produto.setInsertPolicy(
            QtWidgets.QComboBox.InsertPolicy.NoInsert
        )
        self.select_compra_produto.completer().setFilterMode(
            QtCore.Qt.MatchFlag.MatchContains
        )
        self.select_compra_produto.completer().setCompletionMode(
            QtWidgets.QCompleter.CompletionMode.PopupCompletion
        )

        self.tb_vendas_itens.doubleClicked.connect(self.edit_iten_in_list_venda)

    def edit_iten_in_list_venda(self):
        self.tb_vendas_itens.itemChanged.connect(self.edit_item_in_list_aux)

    def edit_item_in_list_aux(self):
        self.tb_vendas_itens.itemChanged.disconnect()
        produtoNome = (
            self.tb_vendas_itens.selectionModel()
            .currentIndex()
            .siblingAtColumn(1)
            .data()
        )
        novaQuant = (
            self.tb_vendas_itens.selectionModel()
            .currentIndex()
            .siblingAtColumn(0)
            .data()
        )
        novoSubTotal = float(novaQuant) * float(
            self.tb_vendas_itens.selectionModel()
            .currentIndex()
            .siblingAtColumn(2)
            .data()
        )

        for i, produto in enumerate(self.ListProductsVenda):
            produtoTemp = list(produto)
            if produtoNome == produtoTemp[2]:
                produtoTemp[1] = float(novaQuant)
                produtoTemp[4] = f"{float(novoSubTotal):9.2f}"
                self.ListProductsVenda[i] = tuple(produtoTemp)
                break
        self.tb_vendas_itens.clear()
        self.load_lista_venda_product()

    def reset_edits(self):
        self.btn_cadastrar_cliente.setText("CADASTRAR")
        self.btn_cadastrar_cliente.clicked.disconnect()
        self.btn_cadastrar_cliente.clicked.connect(self.register_client)
        self.clear_client_qlineedit()

        self.btn_cadastrar_fornecedor.setText("CADASTRAR")
        self.btn_cadastrar_fornecedor.clicked.disconnect()
        self.btn_cadastrar_fornecedor.clicked.connect(self.register_fornecedor)
        self.clear_fornecedor_qlineedit()

        self.btn_cadastrar_produto.setText("CADASTRAR")
        self.btn_cadastrar_produto.clicked.disconnect()
        self.btn_cadastrar_produto.clicked.connect(self.register_produto)
        self.clear_produto_qlineedit()

        self.btn_venda_cadastrar.setText("CADASTRAR")
        self.btn_venda_cadastrar.clicked.disconnect()
        self.btn_venda_cadastrar.clicked.connect(self.register_venda)

        self.search_vendas()
        self.search_produtos_semanal()
        self.tb_widget_vendas.setCurrentIndex(0)
        self.clear_vendas_fields()

    def filter_clients(self, s):
        self.tb_clientes.setCurrentItem(None)

        if not s:
            return

        matching_itens = self.tb_clientes.findItems(
            s, QtCore.Qt.MatchFlag.MatchContains
        )

        if matching_itens:
            item = matching_itens[0]
            self.tb_clientes.setCurrentItem(item)

    def filter_semanal_supplies(self, s):
        self.tab_pedido_semana.setCurrentItem(None)

        if not s:
            return

        matching_itens = self.tab_pedido_semana.findItems(
            s, QtCore.Qt.MatchFlag.MatchContains
        )

        if matching_itens:
            item = matching_itens[0]
            self.tab_pedido_semana.setCurrentItem(item)

    def filter_produtos(self, s):
        self.tb_produtos.setCurrentItem(None)

        if not s:
            return

        matching_itens = self.tb_produtos.findItems(
            s, QtCore.Qt.MatchFlag.MatchContains
        )

        if matching_itens:
            item = matching_itens[0]
            self.tb_produtos.setCurrentItem(item)

    def filter_fornecedor(self, s):
        self.tb_fornecedores.setCurrentItem(None)

        if not s:
            return

        matching_itens = self.tb_fornecedores.findItems(
            s, QtCore.Qt.MatchFlag.MatchContains
        )

        if matching_itens:
            item = matching_itens[0]
            self.tb_fornecedores.setCurrentItem(item)

    def filter_vendas(self, s):
        self.tb_vendas.setCurrentItem(None)

        if not s:
            return

        matching_itens = self.tb_vendas.findItems(s, QtCore.Qt.MatchFlag.MatchContains)

        if matching_itens:
            item = matching_itens[0]
            self.tb_vendas.setCurrentItem(item)

    def filter_compras(self, s):
        self.table_compras.setCurrentItem(None)

        if not s:
            return

        matching_itens = self.table_compras.findItems(
            s, QtCore.Qt.MatchFlag.MatchContains
        )

        if matching_itens:
            item = matching_itens[0]
            self.table_compras.setCurrentItem(item)

    def anterior_current_year(self):
        temp = int(self.currentYear)
        temp -= 1
        self.currentYear = str(temp)
        self.create_compra_line_chart(fornecedorId=self.fornecedorAtual)
        self.create_produto_line_chart(produtoId=self.produtoAtual)
        self.create_venda_line_chart(clientId=self.clienteAtual)

    def proximo_current_year(self):
        temp = int(self.currentYear)
        temp += 1
        self.currentYear = str(temp)
        self.create_compra_line_chart(fornecedorId=self.fornecedorAtual)
        self.create_produto_line_chart(produtoId=self.produtoAtual)
        self.create_venda_line_chart(clientId=self.clienteAtual)

    def contato_whatsapp_web(self, telefone):
        webbrowser.open("https://whatsa.me/55" + str(telefone))

    def create_venda_line_chart(self, clientId):
        self.lb_ano_graph_cliente.setText(str(self.currentYear))

        for i in reversed(range(self.gridLayout_9.count())):
            self.gridLayout_9.itemAt(i).widget().setParent(None)

        vendasPerMouth = [0] * 13

        vendas = self.db.get_vendas_by_clientId(clientId)

        for venda in vendas:
            dataVenda = str(venda[3]).split("/")
            if dataVenda[2] == self.currentYear:
                index = int(dataVenda[1])
                vendasPerMouth[index] += 1

        series = QLineSeries(self)

        for x in range(12):
            series.append(x, vendasPerMouth[x])

        chart = QChart()
        chart.addSeries(series)

        x = QValueAxis()
        x.setLabelFormat("%d")
        x.setTickType(QValueAxis.TickType.TicksDynamic)
        x.setTickInterval(1)
        x.setTitleText("Mes")
        x.setRange(1, 12)
        chart.addAxis(x, QtCore.Qt.AlignmentFlag.AlignBottom)

        y = QValueAxis()
        y.setLabelFormat("%d")
        y.setTitleText("Nº de Pedidos")
        y.setTickType(QValueAxis.TickType.TicksDynamic)
        y.setTickInterval(1)
        chart.addAxis(y, QtCore.Qt.AlignmentFlag.AlignLeft)

        series.attachAxis(x)
        series.attachAxis(y)

        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.legend().setVisible(False)
        chart.setTheme(QChart.ChartTheme.ChartThemeDark)

        self.chartView = QChartView(chart)

        self.gridLayout_9.addWidget(self.chartView)
        self.frame_graph_cliente.setStyleSheet("background-color: transparent")

    def create_compra_line_chart(self, fornecedorId):
        self.lb_ano_fornecedor_detail.setText(str(self.currentYear))

        for i in reversed(range(self.gridLayout_12.count())):
            self.gridLayout_12.itemAt(i).widget().setParent(None)

        comprasPerMouth = [0] * 13

        compras = self.db.get_compras_by_fornecedoId(fornecedorId)

        for compra in compras:
            dataCompra = str(compra[3]).split("/")
            if dataCompra[2] == self.currentYear:
                index = int(dataCompra[1])
                comprasPerMouth[index] += 1

        series = QLineSeries(self)

        for x in range(12):
            series.append(x, comprasPerMouth[x])

        chart = QChart()
        chart.addSeries(series)

        x = QValueAxis()
        x.setLabelFormat("%d")
        x.setTickType(QValueAxis.TickType.TicksDynamic)
        x.setTickInterval(1)
        x.setTitleText("Mes")
        x.setRange(1, 12)
        chart.addAxis(x, QtCore.Qt.AlignmentFlag.AlignBottom)

        y = QValueAxis()
        y.setLabelFormat("%d")
        y.setTitleText("Nº de Pedidos")
        y.setTickType(QValueAxis.TickType.TicksDynamic)
        y.setTickInterval(1)
        chart.addAxis(y, QtCore.Qt.AlignmentFlag.AlignLeft)

        series.attachAxis(x)
        series.attachAxis(y)

        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.legend().setVisible(False)
        chart.setTheme(QChart.ChartTheme.ChartThemeDark)

        self.chartView = QChartView(chart)

        self.gridLayout_12.addWidget(self.chartView)
        self.frame_graph_fornecedor_detail.setStyleSheet(
            "background-color: transparent"
        )

    def create_produto_line_chart(self, produtoId):
        self.lb_ano_graph_produto.setText(str(self.currentYear))

        for i in reversed(range(self.gridLayout_15.count())):
            self.gridLayout_15.itemAt(i).widget().setParent(None)

        vendasPerMouth = [0] * 13

        productToVendas = self.db.get_vendas_by_productId(produtoId)

        for aux in productToVendas:
            vendaId = aux[4]
            venda = self.db.select_specific_venda(vendaId=vendaId)
            if venda is not None:
                dataVenda = str(venda[3]).split("/")
                if dataVenda[2] == self.currentYear:
                    index = int(dataVenda[1])
                    vendasPerMouth[index] += 1

        series = QLineSeries(self)

        for x in range(12):
            series.append(x, vendasPerMouth[x])

        chart = QChart()
        chart.addSeries(series)

        x = QValueAxis()
        x.setLabelFormat("%d")
        x.setTickType(QValueAxis.TickType.TicksDynamic)
        x.setTickInterval(1)
        x.setTitleText("Mes")
        x.setRange(1, 12)
        chart.addAxis(x, QtCore.Qt.AlignmentFlag.AlignBottom)

        y = QValueAxis()
        y.setLabelFormat("%d")
        y.setTitleText("Nº de Vendas")
        y.setTickType(QValueAxis.TickType.TicksDynamic)
        y.setTickInterval(1)
        chart.addAxis(y, QtCore.Qt.AlignmentFlag.AlignLeft)

        series.attachAxis(x)
        series.attachAxis(y)

        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.legend().setVisible(False)
        chart.setTheme(QChart.ChartTheme.ChartThemeDark)

        self.chartView = QChartView(chart)

        self.gridLayout_15.addWidget(self.chartView)
        self.frame_graph_produto.setStyleSheet("background-color: transparent")

    def change_venda_label(self):
        temp = self.select_produto_venda.currentText()
        if temp != "Selecione um Produto":
            productId = temp.split(".")
            currentProduct = self.db.select_specific_product(int(productId[0]))
            self.lb_vendas_medida.setText("Medida: " + str(currentProduct[2]))
        else:
            self.lb_vendas_medida.setText("Medida: ")

    def change_compra_label(self):
        temp = self.select_compra_produto.currentText()
        if temp != "Selecione um Produto":
            productId = temp.split(".")
            currentProduct = self.db.select_specific_product(int(productId[0]))
            self.lb_compra_medida.setText("Medida: " + str(currentProduct[2]))
        else:
            self.lb_compra_medida.setText("Medida: ")

    def change_vencimento_venda(self):
        temp = self.select_pagamento_venda.currentText()
        if temp == "Prazo":
            self.txt_venda_vencimento.setEnabled(True)
            self.lb_vencimento_venda.setEnabled(True)
            self.txt_venda_vencimento.setInputMask("99/99/9999")
            today = datetime.date.today()
            strToday = today.strftime("%d/%m/%Y")
            self.txt_venda_vencimento.setText(strToday)
        else:
            self.txt_venda_vencimento.setEnabled(False)
            self.lb_vencimento_venda.setEnabled(False)

    def change_vencimento_compra(self):
        temp = self.select_compra_pagamento.currentText()
        if temp == "Prazo":
            self.txt_compra_vencimento.setEnabled(True)
            self.lb_compra_vencimento.setEnabled(True)
            self.txt_compra_vencimento.setInputMask("99/99/9999")
            today = datetime.date.today()
            strToday = today.strftime("%d/%m/%Y")
            self.txt_compra_vencimento.setText(strToday)
        else:
            self.txt_compra_vencimento.setEnabled(False)
            self.lb_compra_vencimento.setEnabled(False)

    def add_product_to_venda(self):
        temp = self.select_produto_venda.currentText()
        if temp != "Selecione um Produto":
            if (
                self.txt_venda_quantidade.text() == ""
                or self.txt_venda_quantidade.text() == "0"
            ):
                self.msg("erro", "Quantidade inválida")
            else:
                productId = temp.split(".")
                currentProduct = self.db.select_specific_product(int(productId[0]))
                try:
                    currentProductList = (
                        currentProduct[0],
                        float(self.txt_venda_quantidade.text()),
                        currentProduct[1],
                        f"{float(currentProduct[3]):9.2f}",
                        f"{float(self.txt_venda_quantidade.text()) * float(currentProduct[3]):9.2f}",
                    )
                    self.ListProductsVenda.append(currentProductList)
                    self.load_lista_venda_product()
                except Exception as e:
                    print(e)
                    self.msg("erro", str(e))
        else:
            self.msg("erro", "Selecione um produto Primeiro")

    def add_product_to_compra(self):
        temp = self.select_compra_produto.currentText()
        if temp != "Selecione um Produto":
            if (
                self.txt_compra_quant.text() == ""
                or self.txt_compra_quant.text() == "0"
            ):
                self.msg("erro", "Quantidade inválida")
            else:
                productId = temp.split(".")
                currentProduct = self.db.select_specific_product(int(productId[0]))
                try:
                    currentProductList = (
                        currentProduct[0],
                        float(self.txt_compra_quant.text()),
                        currentProduct[1],
                        f"{float(self.txt_compra_precmedida.text()):9.2f}",
                        f"{float(self.txt_compra_quant.text()) * float(self.txt_compra_precmedida.text()):9.2f}",
                    )
                    self.ListProductsCompra.append(currentProductList)
                    self.load_lista_compra_product()
                except Exception as e:
                    print(e)
                    self.msg("erro", str(e))
        else:
            self.msg("erro", "Selecione um produto Primeiro")

    def remove_product_to_venda(self):
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluido permanentemente")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            self.ListProductsVenda.pop(
                int(self.tb_vendas_itens.selectionModel().currentIndex().row())
            )
            self.load_lista_venda_product()

    def remove_product_to_compra(self):
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluido permanentemente")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            self.ListProductsCompra.pop(
                int(
                    self.tb_produtos_compra_widget.selectionModel().currentIndex().row()
                )
            )
            self.load_lista_compra_product()

    def load_lista_venda_product(self):
        self.tb_vendas_itens.clearContents()
        self.tb_vendas_itens.setRowCount(len(self.ListProductsVenda))

        for row, text in enumerate(self.ListProductsVenda):
            product = (text[1], text[2], text[3], text[4])
            for column, data in enumerate(product):
                self.tb_vendas_itens.setItem(row, column, QTableWidgetItem(str(data)))

        totalTmp = 0
        for item in self.ListProductsVenda:
            totalTmp += float(item[4])

        self.lb_venda_total.setText("R$" + f"{totalTmp:9.2f}")

    def load_lista_compra_product(self):
        self.tb_produtos_compra_widget.clearContents()
        self.tb_produtos_compra_widget.setRowCount(len(self.ListProductsCompra))

        for row, text in enumerate(self.ListProductsCompra):
            product = (text[1], text[2], text[3], text[4])
            for column, data in enumerate(product):
                self.tb_produtos_compra_widget.setItem(
                    row, column, QTableWidgetItem(str(data))
                )

        totalTmp = 0
        for item in self.ListProductsCompra:
            totalTmp += float(item[4])

        self.lb_total_compra.setText("Total: R$" + f"{totalTmp:9.2f}")

    def leftMenu(self):
        width = self.left_container.width()

        if width == 0:
            newWidth = 300
        else:
            newWidth = 0

        self.animation = QtCore.QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def load_clients(self):
        self.select_client_venda.clear()
        self.select_client_venda.addItem("Selecione um Cliente")
        clientes = self.db.select_all_clients()
        for row, text in enumerate(clientes):
            client = str(text[0]) + ". " + text[2]
            self.select_client_venda.addItem(str(client))

    def load_produtos(self):
        self.select_produto_venda.clear()
        self.select_compra_produto.clear()
        self.select_produto_venda.addItem("Selecione um Produto")
        self.select_compra_produto.addItem("Selecione um Produto")
        produtos = self.db.select_all_produtos()
        for row, text in enumerate(produtos):
            produto = str(text[0]) + ". " + text[1]
            self.select_produto_venda.addItem(str(produto))
            self.select_compra_produto.addItem(str(produto))

    def load_fornecedores(self):
        self.select_compra_fornecedor.clear()
        self.select_compra_fornecedor.addItem("Selecione o Fornecedor")
        fornecedores = self.db.select_all_fornecedores()
        for row, text in enumerate(fornecedores):
            fornecedor = str(text[0]) + "." + text[1]
            self.select_compra_fornecedor.addItem(str(fornecedor))

    def register_client(self):
        fullDataSet = (
            self.txt_cpf_cliente.text(),
            self.txt_nome_cliente.text(),
            self.txt_telefone_cliente.text(),
            self.txt_endereco_cliente.text(),
            self.txt_numero_cliente.text(),
            self.txt_bairro_cliente.text(),
            self.txt_cidade_cliente.text(),
            self.txt_estado_cliente.text(),
        )

        response = self.db.register_client(fullDataSet)
        self.msg(response[0], response[1])

        if response[0].lower() == "sucess":
            self.search_clients()
            self.tb_widget_clientes.setCurrentIndex(0)
            self.clear_client_qlineedit()

    def register_venda(self):
        if len(self.ListProductsVenda) == 0:
            self.msg("Erro", "Lista de Produtos Vazia")
        else:
            self.semanaAtual = self.db.get_open_week()
            if (self.semanaAtual == None):
                self.msg("Erro", "Inicie Uma nova semana na tela inicial")
            else:
                clientId = self.select_client_venda.currentText().split(".")

                totalVenda = 0
                for item in self.ListProductsVenda:
                    totalVenda += float(item[4])

                tipoPagamento = self.select_pagamento_venda.currentText()

                if tipoPagamento.lower() == "selecione o tipo de pagamento":
                    self.msg("Erro", "Selecione o método de pagamento")
                else:
                    status = self.select_status_venda.currentText()
                    if status.lower() == "selecione o status da venda":
                        self.msg("Erro", "Indique o STATUS da Venda")
                    else:
                        dataVencimento = ""
                        if tipoPagamento.lower() == "prazo":
                            dataVencimento = self.txt_venda_vencimento.text()

                        fullDataSet = (
                            int(clientId[0]),
                            totalVenda,
                            self.txt_venda_data.text(),
                            tipoPagamento,
                            dataVencimento,
                            status,
                            self.semanaAtual[0]
                        )

                        response = self.db.register_venda(fullDataSet)

                        if response[0].lower() == "sucess":
                            for item in self.ListProductsVenda:
                                data = (item[0], item[1], item[4], response[1])
                                result = self.db.link_venda_to_product(data)

                            self.msg(response[0], "Venda Cadastrada Com sucesso")
                            self.search_vendas()
                            self.search_produtos_semanal()
                            self.tb_widget_vendas.setCurrentIndex(0)
                            self.clear_vendas_fields()

    def register_fornecedor(self):
        fullDataSet = (
            self.txt_nome_fornecedor.text(),
            self.txt_cidade_fornecedor.text(),
            self.txt_telefone_fornecedor.text(),
        )

        response = self.db.register_fornecedor(fullDataSet)

        self.msg(response[0], response[1])

        if response[0].lower() == "sucess":
            self.search_fornecedores()
            self.tb_widget_fornecedores.setCurrentIndex(0)
            self.clear_fornecedor_qlineedit()

    def register_produto(self):
        try:
            fullDataSet = (
                self.select_medida_produto.currentText(),
                self.txt_nome_produto.text(),
                float(self.txt_preco_produto.text()),
            )

            response = self.db.register_produto(fullDataSet)

            self.msg(response[0], response[1])

            if response[0].lower() == "sucess":
                self.search_produtos()
                self.tb_widget_produtos.setCurrentIndex(0)
                self.clear_produto_qlineedit()

        except Exception as e:
            self.msg("Erro", str(e))

    def register_compra(self):
        if len(self.ListProductsCompra) == 0:
            self.msg("Erro", "Lista de Produtos Vazia")
        else:
            fornecedorId = self.select_compra_fornecedor.currentText().split(".")

            totalCompra = 0
            for item in self.ListProductsCompra:
                totalCompra += float(item[4])

            tipoPagamento = self.select_compra_pagamento.currentText()

            if tipoPagamento.lower() == "forma de pagamento":
                self.msg("Erro", "Selecione o método de pagamento")
            else:
                status = self.select_compra_status.currentText()
                if status.lower() == "status da compra":
                    self.msg("Erro", "Indique o STATUS da compra")
                else:
                    dataVencimento = ""
                    if tipoPagamento.lower() == "prazo":
                        dataVencimento = self.txt_compra_vencimento.text()

                    fullDataSet = (
                        int(fornecedorId[0]),
                        totalCompra,
                        self.txt_compra_data.text(),
                        tipoPagamento,
                        dataVencimento,
                        status,
                    )

                    response = self.db.register_compra(fullDataSet)

                    if response[0].lower() == "sucess":
                        for item in self.ListProductsCompra:
                            data = (item[0], item[3], item[1], item[4], response[1])
                            result = self.db.link_compra_to_product(data)

                        self.msg(response[0], "Compra Cadastrada Com sucesso")
                        self.search_compras()
                        self.tb_widget_compras.setCurrentIndex(0)
                        self.clear_compra_qlineedit()

    def clear_client_qlineedit(self):
        self.txt_cpf_cliente.clear()
        self.txt_nome_cliente.clear()
        self.txt_telefone_cliente.clear()
        self.txt_endereco_cliente.clear()
        self.txt_numero_cliente.clear()
        self.txt_bairro_cliente.clear()
        self.txt_cidade_cliente.clear()
        self.txt_estado_cliente.clear()

    def clear_vendas_fields(self):
        self.txt_venda_quantidade.clear()
        self.ListProductsVenda = []
        today = datetime.date.today()
        strToday = today.strftime("%d/%m/%Y")
        self.txt_venda_data.setText(strToday)
        self.txt_venda_vencimento.setText(strToday)
        self.txt_venda_vencimento.setEnabled(False)
        self.select_pagamento_venda.setCurrentIndex(0)
        self.select_status_venda.setCurrentIndex(0)
        self.load_lista_venda_product()
        self.load_clients()
        self.load_produtos()

    def clear_fornecedor_qlineedit(self):
        self.txt_nome_fornecedor.clear()
        self.txt_cidade_fornecedor.clear()
        self.txt_telefone_fornecedor.clear()

    def clear_produto_qlineedit(self):
        self.txt_nome_produto.clear()
        self.txt_preco_produto.clear()
        self.select_medida_produto.setCurrentIndex(0)

    def clear_compra_qlineedit(self):
        self.txt_compra_quant.clear()
        self.ListProductsCompra = []
        today = datetime.date.today()
        strToday = today.strftime("%d/%m/%Y")
        self.txt_compra_data.setText(strToday)
        self.select_compra_pagamento.setCurrentIndex(0)
        self.select_compra_status.setCurrentIndex(0)
        self.load_lista_compra_product()
        self.load_fornecedores()
        self.load_produtos()

    def msg(self, type, mensage):
        msgbox = QMessageBox()
        if type.lower() == "sucess":
            msgbox.setIcon(QMessageBox.Information)
        elif type.lower() == "erro":
            msgbox.setIcon(QMessageBox.Critical)
        elif type.lower() == "aviso":
            msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText(mensage)
        msgbox.setWindowTitle("Atencao")
        msgbox.exec()

    def search_clients(self):
        result = self.db.select_all_clients()
        self.tb_clientes.clearContents()
        self.tb_clientes.setRowCount(len(result))

        for row, text in enumerate(result):
            cliente = (text[0], text[2], text[7] + "/" + text[8], text[3])
            for column, data in enumerate(cliente):
                self.tb_clientes.setItem(row, column, QTableWidgetItem(str(data)))

        self.load_clients()

    def search_vendas_to_client(self, clientId):
        result = self.db.get_vendas_by_clientId(clientId)
        self.tb_widget_vendas_cliente_detail.clearContents()
        self.tb_widget_vendas_cliente_detail.setRowCount(len(result))
        status = ""

        for row, text in enumerate(result):
            status = text[6]
            if text[5] != "" and text[6] != "PAGO":
                dataVencimento = datetime.datetime.strptime(text[5], "%d/%m/%Y").date()
                if int(dataVencimento < self.today):
                    self.db.update_venda_status(text[0], status="ATRASADO")
                    status = "ATRASADO"

            vendaToTable = (text[0], text[3], text[2], status)

            for column, data in enumerate(vendaToTable):
                self.tb_widget_vendas_cliente_detail.setItem(
                    row, column, QTableWidgetItem(str(data))
                )

    def search_compras_to_fornecedor(self, fornecedorId):
        result = self.db.get_compras_by_fornecedoId(fornecedorId)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(result))
        status = ""

        for row, text in enumerate(result):
            status = text[6]
            if text[5] != "" and text[6] != "PAGO":
                dataVencimento = datetime.datetime.strptime(text[5], "%d/%m/%Y").date()
                if int(dataVencimento < self.today):
                    self.db.update_venda_status(text[0], status="ATRASADO")
                    status = "ATRASADO"
            compraToTable = (text[0], text[3], text[2], status)
            for column, data in enumerate(compraToTable):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))

    def search_vendas(self):
        result = self.db.select_all_vendas()
        self.tb_vendas.clearContents()
        self.tb_vendas.setRowCount(len(result))
        # status = ""

        for row, text in enumerate(result):
            status = text[6]
            if text[5] != "" and text[6] != "PAGO":
                dataVencimento = datetime.datetime.strptime(text[5], "%d/%m/%Y").date()
                if int(dataVencimento < self.today):
                    self.db.update_venda_status(text[0], status="ATRASADO")
                    status = "ATRASADO"
            clientName = self.db.select_specific_client(text[1])
            vendaToTable = (text[0], clientName[2], text[3], status)

            for column, data in enumerate(vendaToTable):
                self.tb_vendas.setItem(row, column, QTableWidgetItem(str(data)))

    def search_fornecedores(self):
        result = self.db.select_all_fornecedores()
        self.tb_fornecedores.clearContents()
        self.tb_fornecedores.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_fornecedores.setItem(row, column, QTableWidgetItem(str(data)))
        self.load_fornecedores()

    def search_produtos(self):
        result = self.db.select_all_produtos()
        self.tb_produtos.clearContents()
        self.tb_produtos.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_produtos.setItem(row, column, QTableWidgetItem(str(data)))

        self.load_produtos()

    def search_compras(self):
        result = self.db.select_all_compras()
        self.table_compras.clearContents()
        self.table_compras.setRowCount(len(result))
        status = ""

        for row, text in enumerate(result):
            status = text[6]
            if text[5] != "" and text[6] != "PAGO":
                dataVencimento = datetime.datetime.strptime(text[5], "%d/%m/%Y").date()
                if int(dataVencimento < self.today):
                    self.db.update_venda_status(text[0], status="ATRASADO")
                    status = "ATRASADO"

            fornecedorName = self.db.select_specific_fornecedor(text[1])
            compraToTable = (text[0], fornecedorName[1], text[3], status)

            for column, data in enumerate(compraToTable):
                self.table_compras.setItem(row, column, QTableWidgetItem(str(data)))

    def search_produtos_semanal(self):
        self.tab_pedido_semana.clear()
        semana_aberta = self.db.get_open_week()

        if not semana_aberta:
            QMessageBox.warning(self, "Atenção", "Nenhuma semana aberta encontrada, recomendo iniciar uma nova semana.")
            return

        semana_id = semana_aberta[0]
        vendas = self.db.get_sales_by_week(semana_id)
        dados = {}

        for venda in vendas:
            venda_id = venda[0]
            produtosToVenda = self.db.get_vendas_by_vendasId(vendaId=venda_id)
            nomeProduto = ""
            quantidadeProduto = 0
            medidaProduto = ""

            for produto in produtosToVenda:
                produtoId = produto[1]
                currentProduto = self.db.select_specific_product(productId=produtoId)
                nomeProduto = currentProduto[1]
                medidaProduto = currentProduto[2]
                quantidadeProduto = produto[2]

                key = nomeProduto + "/" + medidaProduto

                if key in dados:
                    dados[key] += quantidadeProduto
                else:
                    dados[key] = quantidadeProduto

        keys = dados.keys()
        self.tab_pedido_semana.setRowCount(len(dados))
        for row, text in enumerate(keys):
            keySplit = text.split("/")
            produto = (keySplit[0], keySplit[1], dados[text])
            for column, data in enumerate(produto):
                self.tab_pedido_semana.setItem(row, column, QTableWidgetItem(str(data)))

    def export_to_excell(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, 
            "Salvar como", 
            "", 
            "Excel Files (*.xlsx);;All Files (*)", 
            options=options
        )

        if file_name:
            dados_tabela = []

            row_count = self.tab_pedido_semana.rowCount()
            column_count = self.tab_pedido_semana.columnCount()

            for row in range(row_count):
                row_data = []
                for col in range(column_count):
                    item = self.tab_pedido_semana.item(row, col)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append("")
                dados_tabela.append(row_data)

            df = pd.DataFrame(dados_tabela)

            # Salva o arquivo no local escolhido pelo usuário
            df.to_excel(file_name, index=False, header=False, engine="openpyxl")
            print(f"Arquivo exportado para {file_name}")

    def update_client(self):
        clientId = (
            self.tb_clientes.selectionModel().currentIndex().siblingAtColumn(0).data()
        )

        currentClient = self.db.select_specific_client(clientId)

        self.txt_cpf_cliente.setText(currentClient[1])
        self.txt_nome_cliente.setText(currentClient[2])
        self.txt_telefone_cliente.setText(currentClient[3])
        self.txt_endereco_cliente.setText(currentClient[4])
        self.txt_numero_cliente.setText(currentClient[5])
        self.txt_bairro_cliente.setText(currentClient[6])
        self.txt_cidade_cliente.setText(currentClient[7])
        self.txt_estado_cliente.setText(currentClient[8])

        self.btn_cadastrar_cliente.setText("EDITAR")
        self.btn_cadastrar_cliente.clicked.disconnect()
        self.btn_cadastrar_cliente.clicked.connect(self.update_client_aux)

        self.tb_widget_clientes.setCurrentIndex(1)

    def update_fornecedor(self):
        fornecedorId = (
            self.tb_fornecedores.selectionModel()
            .currentIndex()
            .siblingAtColumn(0)
            .data()
        )
        currentFornecedor = self.db.select_specific_fornecedor(fornecedorId)

        self.txt_nome_fornecedor.setText(currentFornecedor[1])
        self.txt_cidade_fornecedor.setText(currentFornecedor[2])
        self.txt_telefone_fornecedor.setText(currentFornecedor[3])

        self.btn_cadastrar_fornecedor.setText("EDITAR")
        self.btn_cadastrar_fornecedor.clicked.disconnect()
        self.btn_cadastrar_fornecedor.clicked.connect(self.update_fornecedor_aux)

        self.tb_widget_fornecedores.setCurrentIndex(1)

    def update_produto(self):
        productId = (
            self.tb_produtos.selectionModel().currentIndex().siblingAtColumn(0).data()
        )
        currentProduto = self.db.select_specific_product(productId)

        index = self.select_medida_produto.findText(currentProduto[2])

        self.txt_nome_produto.setText(currentProduto[1])
        self.select_medida_produto.setCurrentIndex(index)
        self.txt_preco_produto.setText(str(currentProduto[3]))

        self.btn_cadastrar_produto.setText("EDITAR")
        self.btn_cadastrar_produto.clicked.disconnect()
        self.btn_cadastrar_produto.clicked.connect(self.update_produto_aux)

        self.tb_widget_produtos.setCurrentIndex(1)

    def update_compra(self):
        compraId = (
            self.table_compras.selectionModel().currentIndex().siblingAtColumn(0).data()
        )

        msg = QMessageBox()
        msg.setWindowTitle("Selecionar Status")
        msg.setText("Status Atual da Compra/Pedido")
        msg.addButton("PAGO", QtWidgets.QMessageBox.YesRole)
        msg.addButton("AGUARDANDO PAGAMENTO", QtWidgets.QMessageBox.YesRole)
        msg.addButton("ATRASADO", QtWidgets.QMessageBox.YesRole)
        msg.addButton("CANCELAR", QtWidgets.QMessageBox.RejectRole)
        resp = msg.exec()

        status = ""
        response = ""

        match resp:
            case 0:
                status = "PAGO"
                response = self.db.update_compra_status(compraId, status)
            case 1:
                status = "AGUARDANDO PAGAMENTO"
                response = self.db.update_compra_status(compraId, status)
            case 2:
                status = "ATRASADO"
                response = self.db.update_compra_status(compraId, status)
            case _:
                return

        self.msg(response[0], response[1])
        if response[0].lower() == "sucess":
            self.search_compras()

    def update_venda_client_detail(self):
        self.ListProductsVenda = []
        vendaId = (
            self.tb_widget_vendas_cliente_detail.selectionModel()
            .currentIndex()
            .siblingAtColumn(0)
            .data()
        )

        currentVenda = self.db.select_specific_venda(vendaId=vendaId)
        currentClient = self.db.select_specific_client(clientId=currentVenda[1])

        self.select_client_venda.setCurrentText(
            str(currentClient[0]) + ". " + str(currentClient[2])
        )
        self.select_pagamento_venda.setCurrentText(currentVenda[4])
        self.select_status_venda.setCurrentText(currentVenda[6])
        self.txt_venda_data.setText(currentVenda[3])

        if currentVenda[4] == "Prazo":
            self.txt_venda_vencimento.setText(currentVenda[5])

        productsToVenda = self.db.get_vendas_by_vendasId(vendaId=vendaId)

        for productInVenda in productsToVenda:
            currentProduct = self.db.select_specific_product(int(productInVenda[1]))
            try:
                currentProductList = (
                    currentProduct[0],
                    productInVenda[2],
                    currentProduct[1],
                    f"{float(currentProduct[3]):9.2f}",
                    f"{float(productInVenda[2]) * float(currentProduct[3]):9.2f}",
                )
                self.ListProductsVenda.append(currentProductList)

            except Exception as e:
                print(e)
                self.msg("erro", str(e))

        self.load_lista_venda_product()
        self.btn_venda_cadastrar.setText("EDITAR")
        self.btn_venda_cadastrar.clicked.disconnect()
        self.btn_venda_cadastrar.clicked.connect(
            lambda: self.update_venda_client_detail_aux(vendaId)
        )

        self.Pages.setCurrentWidget(self.pg_vendas)
        self.tb_widget_vendas.setCurrentIndex(1)

    def update_venda_client_detail_aux(self, vendaId):
        if len(self.ListProductsVenda) == 0:
            self.msg("Erro", "Lista de Produtos Vazia")
        else:
            clientId = self.select_client_venda.currentText().split(".")
            totalVenda = 0

            for item in self.ListProductsVenda:
                totalVenda += float(item[4])

            tipoPagamento = self.select_pagamento_venda.currentText()

            if tipoPagamento.lower() == "selecione o tipo de pagamento":
                self.msg("Erro", "Selecione o método de pagamento")
            else:
                status = self.select_status_venda.currentText()
                if status.lower() == "selecione o status da venda":
                    self.msg("Erro", "Indique o STATUS da Venda")
                else:
                    dataVencimento = ""
                    if tipoPagamento.lower() == "prazo":
                        dataVencimento = self.txt_venda_vencimento.text()

                    fullDataSet = (
                        int(clientId[0]),
                        totalVenda,
                        self.txt_venda_data.text(),
                        tipoPagamento,
                        dataVencimento,
                        status,
                    )

                    response = self.db.update_venda(
                        vendaId=vendaId, fullDataSet=fullDataSet
                    )

                    if response[0].lower() == "sucess":
                        actualProductsToVenda = self.db.get_vendas_by_vendasId(
                            vendaId=vendaId
                        )

                        for temp in actualProductsToVenda:
                            result = self.db.delete_link_venda_product(index=temp[0])

                        for item in self.ListProductsVenda:
                            data = (item[0], item[1], item[4], vendaId)
                            result = self.db.link_venda_to_product(data)

                        self.msg(response[0], "Venda Atualizada Com sucesso")
                        self.search_vendas()
                        self.search_produtos_semanal()
                        self.search_vendas_to_client(clientId=clientId[0])
                        self.btn_venda_cadastrar.setText("CADASTRAR")
                        self.btn_venda_cadastrar.clicked.disconnect()
                        self.btn_venda_cadastrar.clicked.connect(self.register_venda)
                        self.tb_widget_vendas.setCurrentIndex(0)

                        self.Pages.setCurrentWidget(self.pg_cliente_detail)
                        self.tb_widget_client_detail.setCurrentIndex(1)
                        self.clear_vendas_fields()

    def update_venda(self):
        self.ListProductsVenda = []
        vendaId = (
            self.tb_vendas.selectionModel().currentIndex().siblingAtColumn(0).data()
        )

        currentVenda = self.db.select_specific_venda(vendaId=vendaId)

        currentClient = self.db.select_specific_client(clientId=currentVenda[1])

        self.select_client_venda.setCurrentText(
            str(currentClient[0]) + ". " + str(currentClient[2])
        )
        self.select_pagamento_venda.setCurrentText(currentVenda[4])
        self.select_status_venda.setCurrentText(currentVenda[6])
        self.txt_venda_data.setText(currentVenda[3])

        if currentVenda[4] == "Prazo":
            self.txt_venda_vencimento.setText(currentVenda[5])
            self.txt_venda_vencimento.setEnabled(True)

        productsToVenda = self.db.get_vendas_by_vendasId(vendaId=vendaId)

        for productInVenda in productsToVenda:
            currentProduct = self.db.select_specific_product(int(productInVenda[1]))
            try:
                if currentProduct is not None:
                    currentProductList = (
                        currentProduct[0],
                        productInVenda[2],
                        currentProduct[1],
                        f"{float(currentProduct[3]):9.2f}",
                        f"{float(productInVenda[2]) * float(currentProduct[3]):9.2f}",
                    )
                    self.ListProductsVenda.append(currentProductList)
                else:
                    self.db.delete_link_venda_product(index=productInVenda[0])
            except Exception as e:
                print(e)
                self.msg("erro", str(e))

        self.btn_venda_cadastrar.setText("EDITAR")
        self.btn_venda_cadastrar.clicked.disconnect()
        self.btn_venda_cadastrar.clicked.connect(lambda: self.update_venda_aux(vendaId))
        self.load_lista_venda_product()
        # self.lb_venda_total.setText(str(f"{currentVenda[2]:9.2f}"))

        self.tb_widget_vendas.setCurrentIndex(1)

    def update_client_aux(self):
        fullDataSet = (
            self.tb_clientes.selectionModel().currentIndex().siblingAtColumn(0).data(),
            self.txt_cpf_cliente.text(),
            self.txt_nome_cliente.text(),
            self.txt_telefone_cliente.text(),
            self.txt_endereco_cliente.text(),
            self.txt_numero_cliente.text(),
            self.txt_bairro_cliente.text(),
            self.txt_cidade_cliente.text(),
            self.txt_estado_cliente.text(),
        )

        response = self.db.update_client(fullDataSet)
        self.msg(response[0], response[1])

        if response[0].lower() == "sucess":
            self.btn_cadastrar_cliente.setText("CADASTRAR")
            self.btn_cadastrar_cliente.clicked.disconnect()
            self.btn_cadastrar_cliente.clicked.connect(self.register_client)
            self.search_clients()
            self.tb_widget_clientes.setCurrentIndex(0)
            self.clear_client_qlineedit()

    def update_fornecedor_aux(self):
        fullDataSet = (
            self.tb_fornecedores.selectionModel()
            .currentIndex()
            .siblingAtColumn(0)
            .data(),
            self.txt_nome_fornecedor.text(),
            self.txt_cidade_fornecedor.text(),
            self.txt_telefone_fornecedor.text(),
        )

        response = self.db.update_fornecedor(fullDataSet)
        self.msg(response[0], response[1])

        if response[0].lower() == "sucess":
            self.btn_cadastrar_fornecedor.setText("CADASTRAR")
            self.btn_cadastrar_fornecedor.clicked.disconnect()
            self.btn_cadastrar_fornecedor.clicked.connect(self.register_fornecedor)
            self.search_fornecedores()
            self.tb_widget_fornecedores.setCurrentIndex(0)
            self.clear_fornecedor_qlineedit()

    def update_produto_aux(self):
        productId = (
            self.tb_produtos.selectionModel().currentIndex().siblingAtColumn(0).data()
        )
        fullDataSet = (
            productId,
            self.txt_nome_produto.text(),
            self.select_medida_produto.currentText(),
            float(self.txt_preco_produto.text()),
        )

        response = self.db.update_produto(fullDataSet)
        self.msg(response[0], response[1])

        if response[0].lower() == "sucess":
            vendas_from_current_produto = self.db.get_vendas_active_by_productId(
                productId=productId
            )
            for i, venda in enumerate(vendas_from_current_produto):
                currentVenda = self.db.select_specific_venda(vendaId=int(venda[4]))
                if not currentVenda == None:
                    novoSubTotal = venda[2] * float(
                        self.txt_preco_produto.text()
                    )
                    self.db.update_venda_subtotal_produto(
                        tempId=venda[0], subTotal=novoSubTotal
                    )
                    novoTotal = 0
                    attVenda = self.db.get_vendas_by_vendasId(
                        vendaId=currentVenda[0]
                    )
                    for element in attVenda:
                        novoTotal += element[3]
                        self.db.update_total_venda(
                            total=novoTotal, vendaId=currentVenda[0]
                        )

            self.btn_cadastrar_produto.setText("CADASTRAR")
            self.btn_cadastrar_produto.clicked.disconnect()
            self.btn_cadastrar_produto.clicked.connect(self.register_produto)
            self.search_produtos()
            self.tb_widget_produtos.setCurrentIndex(0)
            self.clear_produto_qlineedit()

    def update_compra_aux(self):
        compraId = (
            self.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
        )

        msg = QMessageBox()
        msg.setWindowTitle("Selecionar Status")
        msg.setText("Status Atual da Compra/Pedido")
        msg.addButton("PAGO", QtWidgets.QMessageBox.YesRole)
        msg.addButton("AGUARDANDO PAGAMENTO", QtWidgets.QMessageBox.YesRole)
        msg.addButton("ATRASADO", QtWidgets.QMessageBox.YesRole)
        msg.addButton("CANCELAR", QtWidgets.QMessageBox.RejectRole)
        resp = msg.exec()

        status = ""
        response = ""

        match resp:
            case 0:
                status = "PAGO"
                response = self.db.update_compra_status(compraId, status)
            case 1:
                status = "AGUARDANDO PAGAMENTO"
                response = self.db.update_compra_status(compraId, status)
            case 2:
                status = "ATRASADO"
                response = self.db.update_compra_status(compraId, status)
            case _:
                return

        self.msg(response[0], response[1])
        if response[0].lower() == "sucess":
            self.search_compras()
            self.Pages.setCurrentWidget(self.pg_fornecedores)

    def update_venda_aux(self, vendaId):
        if len(self.ListProductsVenda) == 0:
            self.msg("Erro", "Lista de Produtos Vazia")
        else:
            clientId = self.select_client_venda.currentText().split(".")
            totalVenda = 0

            for item in self.ListProductsVenda:
                totalVenda += float(item[4])

            tipoPagamento = self.select_pagamento_venda.currentText()

            if tipoPagamento.lower() == "selecione o tipo de pagamento":
                self.msg("Erro", "Selecione o método de pagamento")
            else:
                status = self.select_status_venda.currentText()
                if status.lower() == "selecione o status da venda":
                    self.msg("Erro", "Indique o STATUS da Venda")
                else:
                    dataVencimento = ""
                    if tipoPagamento.lower() == "prazo":
                        dataVencimento = self.txt_venda_vencimento.text()

                    fullDataSet = (
                        int(clientId[0]),
                        totalVenda,
                        self.txt_venda_data.text(),
                        tipoPagamento,
                        dataVencimento,
                        status,
                    )

                    response = self.db.update_venda(
                        vendaId=vendaId, fullDataSet=fullDataSet
                    )

                    if response[0].lower() == "sucess":
                        actualProductsToVenda = self.db.get_vendas_by_vendasId(
                            vendaId=vendaId
                        )

                        for temp in actualProductsToVenda:
                            result = self.db.delete_link_venda_product(index=temp[0])

                        for item in self.ListProductsVenda:
                            data = (item[0], item[1], item[4], vendaId)
                            result = self.db.link_venda_to_product(data)

                        self.msg(response[0], "Venda Atualizada Com sucesso")
                        self.search_vendas()
                        self.search_produtos_semanal()
                        self.btn_venda_cadastrar.setText("CADASTRAR")
                        self.btn_venda_cadastrar.clicked.disconnect()
                        self.btn_venda_cadastrar.clicked.connect(self.register_venda)
                        self.tb_widget_vendas.setCurrentIndex(0)
                        self.clear_vendas_fields()

    def delete_client(self):
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluido permanentemente")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            clientID = (
                self.tb_clientes.selectionModel()
                .currentIndex()
                .siblingAtColumn(0)
                .data()
            )
            result = self.db.delete_client(clientID)

            self.msg(result[0], result[1])
            self.search_clients()

    def delete_fornecedor(self):
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluido permanentemente")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            ident = (
                self.tb_fornecedores.selectionModel()
                .currentIndex()
                .siblingAtColumn(0)
                .data()
            )
            result = self.db.delete_fornecedor(ident)

            self.msg(result[0], result[1])
            self.search_fornecedores()

    def delete_produto(self):
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluido permanentemente")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            ident = (
                self.tb_produtos.selectionModel()
                .currentIndex()
                .siblingAtColumn(0)
                .data()
            )
            result = self.db.delete_produto(ident)

            self.msg(result[0], result[1])
            self.search_produtos()

    def delete_venda(self):
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluido permanentemente")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            vendaId = (
                self.tb_vendas.selectionModel().currentIndex().siblingAtColumn(0).data()
            )
            result = self.db.delete_venda(vendaId)

            self.msg(result[0], result[1])
            self.search_vendas()
            self.search_produtos_semanal()

    def delete_venda_aux(self):
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluido permanentemente")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            vendaId = (
                self.tb_widget_vendas_cliente_detail.selectionModel()
                .currentIndex()
                .siblingAtColumn(0)
                .data()
            )
            result = self.db.delete_venda(vendaId)

            self.msg(result[0], result[1])
            self.search_vendas()
            self.search_produtos_semanal()
            self.Pages.setCurrentWidget(self.pg_clientes)

    def delete_compra(self):
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluido permanentemente")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            compraId = (
                self.table_compras.selectionModel()
                .currentIndex()
                .siblingAtColumn(0)
                .data()
            )
            result = self.db.delete_compra(compraId)

            self.msg(result[0], result[1])
            self.search_compras()

    def delete_compra_aux(self):
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluido permanentemente")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            compraId = (
                self.tableWidget.selectionModel()
                .currentIndex()
                .siblingAtColumn(0)
                .data()
            )
            result = self.db.delete_compra(compraId)

            self.msg(result[0], result[1])
            self.search_compras()
            self.Pages.setCurrentWidget(self.pg_fornecedores)

    def clicked_client(self, item):
        if item.column() == 0:
            dateAux = self.strToday.split("/")
            self.currentYear = dateAux[2]

            clientID = item.data()
            self.clienteAtual = clientID

            currentClient = self.db.select_specific_client(clientID)
            vendasCliente = self.db.get_vendas_by_clientId(clientID)

            totalGasto = 0
            status = "OK"
            alpha = 140
            color = QColor(0, 255, 0)

            for venda in vendasCliente:
                totalGasto += venda[2]
                if venda[6] == "ATRASADO":
                    status = "IRREGULAR"
                    color = QColor(255, 0, 0)
                elif venda[6] == "AGUARDANDO PAGAMENTO":
                    status = "REGULAR - PAGAMENTO EM ABERTO"
                    color = QColor(255, 255, 0)

            self.lb_nome_cliente_detail.setText("Nome: " + currentClient[2])
            self.lb_cpf_cliente_detail.setText("CPF: " + currentClient[1])
            self.lb_telefone_cliente_detail.setText("Telefone: " + currentClient[3])
            enderecoTemp = (
                currentClient[4]
                + ", nº "
                + currentClient[5]
                + ", "
                + currentClient[6]
                + ", "
                + currentClient[7]
                + "-"
                + currentClient[8]
            )
            self.lb_endereco_cliente_detail.setText("Endereco: " + enderecoTemp)

            self.lb_num_pedidos_cliente.setText(
                "Nº de Pedidos: " + str(len(vendasCliente))
            )
            self.lb_total_gasto_cliente.setText(
                "Total Gasto: R$" + str(f"{float(totalGasto):9.2f}")
            )

            self.lb_status_cliente.setAutoFillBackground(True)
            values = "{r}, {g}, {b}, {a}".format(
                r=color.red(), g=color.green(), b=color.blue(), a=alpha
            )
            self.lb_status_cliente.setStyleSheet(
                "QLabel { background-color :  rgba(" + values + ")}"
            )
            self.lb_status_cliente.setText("Stauts: " + status)

            self.create_venda_line_chart(clientID)
            self.search_vendas_to_client(clientID)

            self.btn_contato_cliente.clicked.disconnect()
            self.btn_contato_cliente.clicked.connect(
                lambda: self.contato_whatsapp_web(currentClient[3])
            )

            self.Pages.setCurrentWidget(self.pg_cliente_detail)

    def clicked_fornecedor(self, item):
        if item.column() == 0:
            dateAux = self.strToday.split("/")
            self.currentYear = dateAux[2]

            fornecedorId = item.data()
            self.fornecedorAtual = fornecedorId

            currentFornecedor = self.db.select_specific_fornecedor(fornecedorId)
            comprasFornecedor = self.db.get_compras_by_fornecedoId(fornecedorId)

            totalGasto = 0
            status = "OK"
            alpha = 140
            color = QColor(0, 255, 0)

            for compra in comprasFornecedor:
                totalGasto += compra[2]
                if compra[6] == "ATRASADO":
                    status = "IRREGULAR"
                    color = QColor(255, 0, 0)
                elif compra[6] == "AGUARDANDO PAGAMENTO":
                    status = "REGULAR - PAGAMENTO EM ABERTO"
                    color = QColor(255, 255, 0)

            self.lb_nome_fornecedor_detail.setText("Nome: " + currentFornecedor[1])
            self.lb_telefone_fornecedor_detail.setText(
                "Telefone: " + currentFornecedor[2]
            )
            self.lb_cidade_fornecedor_detail.setText(
                "Endereco: " + currentFornecedor[3]
            )

            self.lb_num_compras_fornecedor_detail.setText(
                "Nº de Pedidos: " + str(len(comprasFornecedor))
            )
            self.lb_total_gasto_fornecedor_detail.setText(
                "Total Gasto: R$" + str(f"{float(totalGasto):9.2f}")
            )

            self.lb_status_fornecedor_detail.setAutoFillBackground(True)
            values = "{r}, {g}, {b}, {a}".format(
                r=color.red(), g=color.green(), b=color.blue(), a=alpha
            )
            self.lb_status_fornecedor_detail.setStyleSheet(
                "QLabel { background-color :  rgba(" + values + ")}"
            )
            self.lb_status_fornecedor_detail.setText("Stauts: " + status)

            self.create_compra_line_chart(fornecedorId)
            self.search_compras_to_fornecedor(fornecedorId)

            self.btn_contato_fornecedor.clicked.disconnect()
            self.btn_contato_fornecedor.clicked.connect(
                lambda: self.contato_whatsapp_web(currentFornecedor[3])
            )

            self.Pages.setCurrentWidget(self.pg_fornecedores_detail)

    def clicked_produto(self, item):
        if item.column() == 0:
            dateAux = self.strToday.split("/")
            self.currentYear = dateAux[2]

            productId = item.data()
            self.produtoAtual = productId
            currentProduto = self.db.select_specific_product(productId)

            product_In_Vendas = self.db.get_vendas_by_productId(productId)
            product_In_Compras = self.db.get_compras_by_productId(productId)

            if len(product_In_Compras) > 0 and len(product_In_Vendas) > 0:
                totalValorEmVendas = 0
                totalValorEmCompras = 0
                bestCompraId = None
                valorMenor = sys.float_info.max

                for produtoVenda in product_In_Vendas:
                    totalValorEmVendas += produtoVenda[3]

                for produtoCompra in product_In_Compras:
                    totalValorEmCompras += produtoCompra[4]
                    if produtoCompra[2] < float(valorMenor):
                        valorMenor = produtoCompra[2]
                        bestCompraId = produtoCompra[5]

                diferencaCompraVenda = totalValorEmVendas - totalValorEmCompras

                margemLucro = (diferencaCompraVenda * 100) / totalValorEmCompras

                bestCompraObj = self.db.select_specific_compra(compraId=bestCompraId)
                bestFornecedor = self.db.select_specific_fornecedor(
                    fornecedorId=bestCompraObj[1]
                )

                self.lb_best_fornecedor_produto.setText(
                    "Melhor Fornecedor: " + bestFornecedor[1]
                )
                self.lb_best_fornecedor_produto_valor_medida.setText(
                    "Valor / Medida: R$" + str(f"{float(valorMenor):9.2f}")
                )
                self.lb_produto_valor_gasto.setText(
                    "Total Gasto em Compra: R$"
                    + str(f"{float(totalValorEmCompras):9.2f}")
                )
                self.lb_produto_valor_ganho.setText(
                    "Total Ganho em Vendas: R$"
                    + str(f"{float(totalValorEmVendas):9.2f}")
                )
                self.lb_lucro_margem.setText(
                    "Lucro / Margem: R$"
                    + str(f"{float(diferencaCompraVenda):9.2f}")
                    + " / "
                    + str(f"{float(margemLucro):9.2f}")
                    + "%"
                )

            self.lb_nome_produto_detail.setText("Nome: " + currentProduto[1])
            self.lb_medida_produto_detail.setText("Medida: " + currentProduto[2])
            self.lb_valor_medida_produto_detail.setText(
                "Preco/Medida: R$" + str(f"{float(currentProduto[3]):9.2f}")
            )
            self.create_produto_line_chart(produtoId=productId)

            self.Pages.setCurrentWidget(self.pg_produtos_detail)
    
    def iniciar_nova_semana(self):
        if (self.db.get_open_week() == None):
            nova_semana_id = self.db.start_new_week()
            QMessageBox.information(
                self, "Nova Semana", f"Nova Semana iniciada com ID {nova_semana_id}."
            )
        else:
            QMessageBox.information(
                self, "Erro", "Já possui uma Semana aberta atualmente, por favor feche a semana atual antes de abrir uma nova."
            )

    def fechar_semana(self):
        semana_aberta = self.db.get_open_week()

        if not semana_aberta:
            QMessageBox.warning(self, "Erro", "Não há semana aberta para fechar.")
            return
        
        msg = QMessageBox()
        msg.setWindowTitle("Encerrar Semana")
        msg.setText("Essa semana será fechada permanentemente")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            semana_id = semana_aberta[0]
            self.db.close_week(semana_id)
            QMessageBox.information(self, "Sucesso", "Semana Fechada com sucesso!")
            self.search_produtos_semanal()

    def printer_venda(self):
        vendaId = (
            self.tb_vendas.selectionModel().currentIndex().siblingAtColumn(0).data()
        )

        if vendaId == None:
            self.msg("Erro", "Selecione uma Venda para poder imprimir.")
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Imprimir")
            msg.setText("Deseja Imprimir o Registro?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            resp = msg.exec()

            if resp == QMessageBox.Yes:
                venda = self.db.select_specific_venda(vendaId)

                vendaManyToMany = self.db.select_all_many_to_venda(vendaId)

                cliente = self.db.select_specific_client(int(venda[1]))

                produtosPrint = []

                for item in vendaManyToMany:
                    product = self.db.select_specific_product(item[1])
                    uniTemp = ""

                    match str(product[2]).lower():
                        case "kg":
                            uniTemp = "KG"
                        case "saco":
                            uniTemp = "SC"
                        case "unidade":
                            uniTemp = "UN"
                        case "caixa":
                            uniTemp = "CX"
                        case "fardo":
                            uniTemp = "FA"
                        case "litro":
                            uniTemp = "LT"
                        case _:
                            uniTemp = "--"

                    temp = (product[1], item[2], uniTemp, product[3], item[3])
                    produtosPrint.append(temp)

                for x in range(2):
                    produtosPrint.sort(key=lambda produto: produto[0])
                    try:
                        printer = Usb(0x1FC9, 0x2016)

                        printer.set(align="center", font="A", text_type="B")
                        printer.text("\nCOMERCIAL J. FRUTAS\n")
                        printer.text("ORG. DAMARIS e GILBERLANDIA\n")
                        printer.text("(84)99707-4633 / (84)99847-2121\n")
                        printer.text("CNPJ: 02.264.693/0001-55\nALEXANDRIA - RN\n")
                        printer.text("\n")

                        printer.set(align="center", text_type="B")
                        printer.text("Via Conferente\n")

                        printer.set(align="center", text_type="normal")
                        printer.text("=============================================\n")

                        printer.set(align="center", text_type="B")
                        printer.text("VENDA\n")

                        printer.set(align="center", text_type="normal")
                        printer.text("=============================================\n")

                        printer.set(align="left", text_type="normal")
                        printer.text("Pedido : " + str(venda[0]) + "\n")

                        printer.set(align="left", text_type="normal")
                        printer.text("Data: " + str(venda[3]) + "\n")

                        printer.set(align="left", text_type="normal")
                        printer.text("Cliente: ")

                        printer.set(
                            align="left", font="B", text_type="B", height=2, width=2
                        )
                        printer.text(str(cliente[2]).upper() + "\n")

                        printer.set(align="left", text_type="normal")
                        printer.text("Cidade: " + cliente[7] + "\n")

                        printer.set(align="center", text_type="normal")
                        printer.text("=============================================\n")

                        printer.set(align="right", text_type="normal")
                        printer.text("Especie        Quant. UN     Unit.      Total\n")
                        printer.text("\n")

                        for productToText in produtosPrint:
                            printer.set(align="left", font="A", text_type="B")
                            if str(productToText[0]).lower() == "bobina":
                                if x == 0:
                                    quant, ok = QInputDialog.getText(
                                        self,
                                        "Peso da Bobina",
                                        "Digite o peso da bobina: ",
                                    )
                                    if ok:
                                        vendaTemp = list(venda)
                                        vendaTemp[2] -= productToText[4]
                                        vendaTemp[2] += float(quant) * float(
                                            productToText[3]
                                        )
                                        venda = tuple(vendaTemp)
                                        self.db.update_total_venda(
                                            vendaId=vendaId, total=venda[2]
                                        )
                                        strTemp = "(" + str(quant) + "Kg)"
                                        valueTemp = str(
                                            f"{float((float(quant) * float(productToText[3]))):9.2f}"
                                        )
                                        strToPrint = str.format(
                                            "{:15s} {:7.1f} {:2s} {:6s} {:5.2f} {:9.2f}\n",
                                            str(productToText[0]).upper(),
                                            float(productToText[1]),
                                            productToText[2],
                                            strTemp,
                                            productToText[3],
                                            float(valueTemp),
                                        )
                                        self.strBobina = strToPrint
                                        printer.text(strToPrint)
                                        printer.text("\n")
                                else:
                                    strToPrint = self.strBobina
                                    printer.text(strToPrint)
                                    printer.text("\n")

                            else:
                                strToPrint = str.format(
                                    "{:15s} {:9.1f} {:2s} {:9.2f} {:9.2f}\n",
                                    str(productToText[0]).upper(),
                                    productToText[1],
                                    productToText[2],
                                    productToText[3],
                                    productToText[4],
                                )
                                printer.text(strToPrint)
                                printer.text("\n")

                        printer.set(align="center", text_type="B")
                        printer.text(
                            "\n--Total--------------------------------------\n"
                        )

                        printer.set(
                            align="left", font="B", text_type="B", width=2, height=2
                        )
                        printer.text(" R$" + str(f"{float(venda[2]):9.2f}") + "\n")

                        printer.set(align="left", text_type="B")
                        printer.text("\n")
                        printer.text("Qtd. de Itens: " + str(len(produtosPrint)) + "\n")

                        printer.text("\n")
                        printer.text("\n")
                        printer.text("\n")
                        printer.text("\n")
                        printer.text("\n")
                        printer.text("\n")

                        printer.set(align="left", text_type="normal")
                        printer.text("ASS: ")

                        printer.set(align="left", text_type="U")
                        printer.text("                                        \n")

                        printer.set(align="center", text_type="normal")
                        printer.text("########### SEM VALOR FISCAL ############")

                        printer.cut()

                    except Exception as e:
                        self.msg("Erro", str(e))
                        print(e)
                        break

                    if x == 0:
                        msg2 = QMessageBox()
                        msg2.setWindowTitle("Imprimir")
                        msg2.setText("Deseja Imprimir uma segunda via?")
                        msg2.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                        resp2 = msg2.exec()

                        if resp2 == QMessageBox.No:
                            break

    def printer_venda_detail(self):
        vendaId = (
            self.tb_widget_vendas_cliente_detail.selectionModel()
            .currentIndex()
            .siblingAtColumn(0)
            .data()
        )

        if vendaId == None:
            self.msg("Erro", "Selecione uma Venda para poder imprimir.")
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Imprimir")
            msg.setText("Deseja Imprimir o Registro?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            resp = msg.exec()

            if resp == QMessageBox.Yes:
                venda = self.db.select_specific_venda(vendaId)

                vendaManyToMany = self.db.select_all_many_to_venda(vendaId)

                cliente = self.db.select_specific_client(int(venda[1]))

                produtosPrint = []

                for item in vendaManyToMany:
                    product = self.db.select_specific_product(item[1])
                    uniTemp = ""

                    match str(product[2]).lower():
                        case "kg":
                            uniTemp = "KG"
                        case "saco":
                            uniTemp = "SC"
                        case "unidade":
                            uniTemp = "UN"
                        case "caixa":
                            uniTemp = "CX"
                        case "fardo":
                            uniTemp = "FA"
                        case "litro":
                            uniTemp = "LT"
                        case _:
                            uniTemp = "--"

                    temp = (product[1], item[2], uniTemp, product[3], item[3])
                    produtosPrint.append(temp)

                for x in range(2):
                    produtosPrint.sort(key=lambda produto: produto[0])
                    try:

                        printer = Usb(0x1FC9, 0x2016)

                        printer.set(align="center", font="A", text_type="B")
                        printer.text("\nCOMERCIAL J. FRUTAS\n")
                        printer.text("ORG. DAMARIS e GILBERLANDIA\n")
                        printer.text("(84)99707-4633 / (84)99847-2121\n")
                        printer.text("CNPJ: 02.264.693/0001-55\nALEXANDRIA - RN\n")
                        printer.text("\n")

                        printer.set(align="center", text_type="B")
                        printer.text("Via Conferente\n")

                        printer.set(align="center", text_type="normal")
                        printer.text("=============================================\n")

                        printer.set(align="center", text_type="B")
                        printer.text("VENDA\n")

                        printer.set(align="center", text_type="normal")
                        printer.text("=============================================\n")

                        printer.set(align="left", text_type="normal")
                        printer.text("Pedido : " + str(venda[0]) + "\n")

                        printer.set(align="left", text_type="normal")
                        printer.text("Data: " + str(venda[3]) + "\n")

                        printer.set(align="left", text_type="normal")
                        printer.text("Cliente: ")

                        printer.set(
                            align="left", font="B", text_type="B", height=2, width=2
                        )
                        printer.text(str(cliente[2]).upper() + "\n")

                        printer.set(align="left", text_type="normal")
                        printer.text("Cidade: " + cliente[7] + "\n")

                        printer.set(align="center", text_type="normal")
                        printer.text("=============================================\n")

                        printer.set(align="right", text_type="normal")
                        printer.text("Especie        Quant. UN     Unit.      Total\n")
                        printer.text("\n")

                        for productToText in produtosPrint:
                            printer.set(align="left", font="A", text_type="B")
                            if str(productToText[0]).lower() == "bobina":
                                if x == 0:
                                    quant, ok = QInputDialog.getText(
                                        self,
                                        "Peso da Bobina",
                                        "Digite o peso da bobina: ",
                                    )
                                    if ok:
                                        vendaTemp = list(venda)
                                        vendaTemp[2] -= productToText[4]
                                        vendaTemp[2] += float(quant) * float(
                                            productToText[3]
                                        )
                                        venda = tuple(vendaTemp)
                                        self.db.update_total_venda(
                                            vendaId=vendaId, total=venda[2]
                                        )
                                        strTemp = "(" + str(quant) + "Kg)"
                                        valueTemp = str(
                                            f"{float((float(quant) * float(productToText[3]))):9.2f}"
                                        )
                                        strToPrint = str.format(
                                            "{:15s} {:7.1f} {:2s} {:6s} {:5.2f} {:9.2f}\n",
                                            str(productToText[0]).upper(),
                                            float(productToText[1]),
                                            productToText[2],
                                            strTemp,
                                            productToText[3],
                                            float(valueTemp),
                                        )
                                        self.strBobina = strToPrint
                                        printer.text(strToPrint)
                                        printer.text("\n")
                                else:
                                    strToPrint = self.strBobina
                                    printer.text(strToPrint)
                                    printer.text("\n")

                            else:
                                strToPrint = str.format(
                                    "{:15s} {:9.1f} {:2s} {:9.2f} {:9.2f}\n",
                                    str(productToText[0]).upper(),
                                    productToText[1],
                                    productToText[2],
                                    productToText[3],
                                    productToText[4],
                                )
                                printer.text(strToPrint)
                                printer.text("\n")

                        printer.set(align="center", text_type="B")
                        printer.text(
                            "\n--Total--------------------------------------\n"
                        )

                        printer.set(
                            align="left", font="B", text_type="B", width=2, height=2
                        )
                        printer.text(" R$" + str(f"{float(venda[2]):9.2f}") + "\n")

                        printer.set(align="left", text_type="B")
                        printer.text("\n")
                        printer.text("Qtd. de Itens: " + str(len(produtosPrint)) + "\n")

                        printer.text("\n")
                        printer.text("\n")
                        printer.text("\n")
                        printer.text("\n")
                        printer.text("\n")
                        printer.text("\n")

                        printer.set(align="left", text_type="normal")
                        printer.text("ASS: ")

                        printer.set(align="left", text_type="U")
                        printer.text("                                        \n")

                        printer.set(align="center", text_type="normal")
                        printer.text("########### SEM VALOR FISCAL ############")

                        printer.cut()

                    except Exception as e:
                        self.msg("Erro", str(e))
                        print(e)
                        break

                    if x == 0:
                        msg2 = QMessageBox()
                        msg2.setWindowTitle("Imprimir")
                        msg2.setText("Deseja Imprimir uma segunda via?")
                        msg2.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                        resp2 = msg2.exec()

                        if resp2 == QMessageBox.No:
                            break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="light_cyan_500.xml")
    db = Data_base()
    db.create_table_client()
    db.create_table_fornecedor()
    db.create_table_produto()
    db.create_table_semana_venda()
    db.create_table_venda()
    db.create_table_compra()
    db.create_table_venda_produto_manyToMany()
    db.create_table_compra_produto_fornecedor()
    window = MainWindow()
    window.show()
    app.exec()

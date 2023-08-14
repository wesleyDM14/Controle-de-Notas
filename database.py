import sqlite3


class Data_base:
    def __init__(self, name="system.db") -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)

    #########################################################################
    # CREATE TABLES

    def create_table_client(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Clientes(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                CPF TEXT,
                NOME TEXT,
                TELEFONE TEXT,
                ENDERECO TEXT,
                NUMERO TEXT,
                BAIRRO TEXT,
                CIDADE TEXT,
                UF TEXT
            );
        """
        )
        self.close_connection()

    def create_table_fornecedor(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Fornecedores(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME TEXT NOT NULL,
                CIDADE TEXT,
                TELEFONE TEXT NOT NULL
            );
        """
        )
        self.close_connection()

    def create_table_produto(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Produtos(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME TEXT NOT NULL,
                MEDIDA TEXT NOT NULL,
                VALOR REAL NOT NULL
            );
        """
        )
        self.close_connection()

    def create_table_venda(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Vendas(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                CLIENTE_ID TEXT NOT NULL,
                TOTAL REAL NOT NULL,
                DATE TEXT,
                TIPO_PAGAMENTO TEXT,
                VENCIMENTO TEXT,
                STATUS TEXT,

                FOREIGN KEY (CLIENTE_ID) REFERENCES Clientes (ID) ON DELETE CASCADE
            )
            """
        )
        self.close_connection()

    def create_table_venda_produto_manyToMany(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Produtos_Venda(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                PRODUTO_ID INTEGER,
                QUANT_PRODUTO REAL,
                PRECO_PARCIAL REAL,
                VENDA_ID INTEGER,

                FOREIGN KEY (PRODUTO_ID) REFERENCES Produtos(ID) ON DELETE CASCADE,
                FOREIGN KEY (VENDA_ID) REFERENCES Vendas(ID) ON DELETE CASCADE
            )
            """
        )
        self.close_connection()

    def create_table_compra(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Compra(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                FORNECEDOR_ID INTEGER,
                TOTAL REAL,
                DATE TEXT,
                TIPO_PAGAMENTO TEXT,
                VENCIMENTO TEXT,
                STATUS TEXT,

                FOREIGN KEY (FORNECEDOR_ID) REFERENCES Fornecedor(ID) ON DELETE CASCADE
            )
            """
        )
        self.close_connection()

    def create_table_compra_produto_fornecedor(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Produtos_Compra(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                PRODUTO_ID INTEGER,
                PRECO_UND REAL,
                QUANT_PRODUTO REAL,
                PRECO_PARCIAL REAL,
                COMPRA_ID INTEGER,

                FOREIGN KEY (PRODUTO_ID) REFERENCES Produtos(ID) ON DELETE CASCADE,
                FOREIGN KEY (COMPRA_ID) REFERENCES Compra(ID) ON DELETE CASCADE
            )
            """
        )
        self.close_connection()
    #########################################################################

    #########################################################################
    # CREATE

    def register_client(self, fullDataSet):
        self.connect()
        campos_tabela = (
            "CPF",
            "NOME",
            "TELEFONE",
            "ENDERECO",
            "NUMERO",
            "BAIRRO",
            "CIDADE",
            "UF",
        )
        qntd = "?,?,?,?,?,?,?,?"
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"""INSERT INTO Clientes {campos_tabela}
                                VALUES ({qntd})""",
                fullDataSet,
            )
            self.connection.commit()
            return "Sucess", "Cliente cadastrado com sucesso!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def register_fornecedor(self, fullDataSet):
        self.connect()
        campos_tabela = ("NOME", "CIDADE", "TELEFONE")
        qntd = "?,?,?"
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"""INSERT INTO Fornecedores {campos_tabela}
                                VALUES ({qntd})""",
                fullDataSet,
            )
            self.connection.commit()
            return "Sucess", "Fornecedor cadastrado com sucesso!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def register_produto(self, fullDataSet):
        self.connect()
        campos_tabela = ("MEDIDA", "NOME", "VALOR")
        qntd = "?,?,?"
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"""INSERT INTO Produtos {campos_tabela}
                                VALUES ({qntd})""",
                fullDataSet,
            )
            self.connection.commit()
            return "Sucess", "Produto cadastrado com sucesso!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def register_venda(self, data):
        self.connect()
        camposTabela = ("CLIENTE_ID", "TOTAL", "DATE", "TIPO_PAGAMENTO", "VENCIMENTO", "STATUS")
        qntd = "?,?,?,?,?,?"
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"""
                INSERT INTO Vendas {camposTabela}
                            VALUES ({qntd})
                """,
                data,
            )
            self.connection.commit()
            return "Sucess", cursor.lastrowid
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()
    
    def link_venda_to_product(self, fullDataSet):
        self.connect()
        camposTabela = ("PRODUTO_ID", "QUANT_PRODUTO", "PRECO_PARCIAL", "VENDA_ID")
        qntd = "?,?,?,?"
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"""
                INSERT INTO Produtos_Venda {camposTabela}
                            VALUES ({qntd})
                """,
                fullDataSet,
            )
            self.connection.commit()
            return "Sucess", "Produto cadastrado com sucesso na venda!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def register_compra(self, data):
        self.connect()
        camposTabela = ("FORNECEDOR_ID", "TOTAL", "DATE", "TIPO_PAGAMENTO", "VENCIMENTO", "STATUS")
        qntd = "?,?,?,?,?,?"
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"""
                INSERT INTO Compra {camposTabela}
                                VALUES ({qntd})
                """,
                data,
            )
            self.connection.commit()
            return "Sucess", cursor.lastrowid
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def link_compra_to_product(self, fullDataSet):
        self.connect()
        camposTabela = ("PRODUTO_ID", "PRECO_UND", "QUANT_PRODUTO", "PRECO_PARCIAL", "COMPRA_ID")
        qntd = "?,?,?,?,?"
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"""
                INSERT INTO Produtos_Compra {camposTabela}
                            VALUES ({qntd})
                """,
                fullDataSet,
            )
            self.connection.commit()
            return "Sucess", "Produto cadastrado com sucesso na compra!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()
    #########################################################################

    #########################################################################
    # READ ALL

    def select_all_clients(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Clientes ORDER BY NOME")
            clientes = cursor.fetchall()
            return clientes
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def select_all_fornecedores(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Fornecedores ORDER BY NOME")
            fornecedores = cursor.fetchall()
            return fornecedores
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def select_all_produtos(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Produtos ORDER BY NOME")
            produtos = cursor.fetchall()
            return produtos
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def select_all_vendas(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Vendas ORDER BY DATE")
            vendas = cursor.fetchall()
            return vendas
        except Exception as e:
            print (e)
        finally:
            self.close_connection()

    def select_all_compras(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Compra ORDER BY DATE")
            compras = cursor.fetchall()
            return compras
        except Exception as e:
            print(e)
        finally:
            self.close_connection()
    #########################################################################

    #########################################################################
    # READ UNIQUE

    def select_specific_client(self, clientId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Clientes WHERE ID='{clientId}'")
            client = cursor.fetchone()
            return client
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def select_specific_fornecedor(self, fornecedorId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Fornecedores WHERE ID='{fornecedorId}'")
            fornecedor = cursor.fetchone()
            return fornecedor
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def select_specific_product(self, productId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Produtos WHERE ID='{productId}'")
            produto = cursor.fetchone()
            return produto
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def select_specific_venda(self, vendaId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Vendas WHERE ID='{vendaId}'")
            venda = cursor.fetchone()
            return venda
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def select_all_many_to_venda(self, vendaId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Produtos_Venda WHERE VENDA_ID='{vendaId}'")
            productsVendas = cursor.fetchall()
            return productsVendas
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def select_all_many_to_product(self, productId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Produtos_Venda WHERE PRODUTO_ID = {productId}")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()
    
    def select_specific_compra(self, compraId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Compra WHERE ID='{compraId}'")
            compra = cursor.fetchone()
            return compra
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def select_all_many_to_compra(self, compraId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Produtos_Compra WHERE COMPRA_ID='{compraId}'")
            productsCompra = cursor.fetchall()
            return productsCompra
        except Exception as e:
            print(e)
        finally:
            self.close_connection()
    #########################################################################

    #########################################################################
    # Get vendas by Client
    def get_vendas_by_clientId(self, clientId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Vendas WHERE CLIENTE_ID='{clientId}'")
            vendas = cursor.fetchall()
            return vendas
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def get_compras_by_fornecedoId(self, fornecedorId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Compra WHERE FORNECEDOR_ID='{fornecedorId}'")
            compras = cursor.fetchall()
            return compras
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def get_compras_by_productId(self, productId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Produtos_Compra WHERE PRODUTO_ID='{productId}'")
            compras = cursor.fetchall()
            return compras
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def get_vendas_by_productId(self, productId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Produtos_Venda WHERE PRODUTO_ID='{productId}'")
            compras = cursor.fetchall()
            return compras
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def get_vendas_by_vendasId(self, vendaId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Produtos_Venda WHERE VENDA_ID='{vendaId}'")
            compras = cursor.fetchall()
            return compras
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def get_vendas_by_date(self, date):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Vendas WHERE DATE='{date}'")
            vendas = cursor.fetchall()
            return vendas
        except Exception as e:
            print(e)
        finally:
            self.close_connection()
    #########################################################################

    #########################################################################
    # DELETE

    def delete_client(self, clientId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Clientes WHERE ID = '{clientId}'")
            self.connection.commit()
            return "Sucess", "Cliente deletado com sucesso!"
        except Exception as e:
            print(e)
            return "Error", str(e)
        finally:
            self.close_connection()

    def delete_fornecedor(self, ident):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Fornecedores WHERE ID = '{ident}'")
            self.connection.commit()
            return "Sucess", "Fornecedor deletado com sucesso!"
        except Exception as e:
            print(e)
            return "Error", str(e)
        finally:
            self.close_connection()

    def delete_produto(self, ident):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Produtos WHERE ID = '{ident}'")
            self.connection.commit()
            return "Sucess", "Produto deletado com sucesso!"
        except Exception as e:
            print(e)
            return "Error", str(e)
        finally:
            self.close_connection()

    def delete_venda(self, vendaId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Vendas WHERE ID = '{vendaId}'")
            self.connection.commit()
            return "Sucess", "Pedido deletado com sucesso!"
        except Exception as e:
            print(e)
            return "Error", str(e)
        finally:
            self.close_connection()

    def delete_compra(self, compraId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Compra WHERE ID = '{compraId}'")
            self.connection.commit()
            return "Sucess", "Pedido deletado com sucesso!"
        except Exception as e:
            print(e)
            return "Error", str(e)
        finally:
            self.close_connection()

    #########################################################################

    #########################################################################
    # UPDATE
    def update_client(self, fullDataSet):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                f"""UPDATE Clientes set
                CPF = '{fullDataSet[1]}',
                NOME = '{fullDataSet[2]}',
                TELEFONE = '{fullDataSet[3]}',
                ENDERECO = '{fullDataSet[4]}',
                NUMERO = '{fullDataSet[5]}',
                BAIRRO = '{fullDataSet[6]}',
                CIDADE = '{fullDataSet[7]}',
                UF = '{fullDataSet[8]}'

                WHERE ID = '{fullDataSet[0]}'
                """
            )
            self.connection.commit()
            return "Sucess", "Cliente Atualizado com sucesso!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def update_fornecedor(self, fullDataSet):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(
                f"""UPDATE Fornecedores set
                NOME = '{fullDataSet[1]}',
                TELEFONE = '{fullDataSet[3]}',
                CIDADE = '{fullDataSet[2]}'

                WHERE ID = '{fullDataSet[0]}'"""
            )
            self.connection.commit()
            return "Sucess", "Fornecedor Atualizado com sucesso!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def update_produto(self, fullDataSet):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(
                f"""UPDATE Produtos
                SET NOME = '{fullDataSet[1]}',
                MEDIDA = '{fullDataSet[2]}',
                VALOR = '{fullDataSet[3]}'

                WHERE ID = '{fullDataSet[0]}'"""
            )
            self.connection.commit()
            return "Sucess", "Produto Atualizado com sucesso!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def update_venda_status(self, vendaId, status):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"UPDATE Vendas SET STATUS = '{status}' WHERE ID = '{vendaId}'")
            self.connection.commit()
            return "Sucess", "Status Atualizado com sucesso!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def update_compra_status(self, compraId, status):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"UPDATE Compra SET STATUS = '{status}' WHERE ID = '{compraId}'")
            self.connection.commit()
            return "Sucess", "Status Atualizado com sucesso!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

#########################################################################

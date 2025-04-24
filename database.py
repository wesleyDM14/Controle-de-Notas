import sqlite3
import datetime


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

    def create_table_semana_venda(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Semana(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DATA_INICIO TEXT,
                STATUS TEXT
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
                SEMANA_ID INTEGER,

                FOREIGN KEY (CLIENTE_ID) REFERENCES Clientes (ID) ON DELETE CASCADE,
                FOREIGN KEY (SEMANA_ID) REFERENCES Semana(ID) ON DELETE SET NULL
            );
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
            );
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
        camposTabela = (
            "CLIENTE_ID",
            "TOTAL",
            "DATE",
            "TIPO_PAGAMENTO",
            "VENCIMENTO",
            "STATUS",
            "SEMANA_ID"
        )
        qntd = "?,?,?,?,?,?,?"
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
        camposTabela = (
            "FORNECEDOR_ID",
            "TOTAL",
            "DATE",
            "TIPO_PAGAMENTO",
            "VENCIMENTO",
            "STATUS",
        )
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
        camposTabela = (
            "PRODUTO_ID",
            "PRECO_UND",
            "QUANT_PRODUTO",
            "PRECO_PARCIAL",
            "COMPRA_ID",
        )
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
            cursor.execute("""
                SELECT * FROM Vendas 
                ORDER BY STRFTIME('%Y-%m-%d', 
                                SUBSTR(DATE, 7, 4) || '-' || 
                                SUBSTR(DATE, 4, 2) || '-' || 
                                SUBSTR(DATE, 1, 2)) DESC
            """)
            vendas = cursor.fetchall()
            return vendas
        except Exception as e:
            print(e)
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
            cursor.execute(
                f"SELECT * FROM Produtos_Venda WHERE PRODUTO_ID = {productId}"
            )
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
            cursor.execute(
                f"SELECT * FROM Produtos_Compra WHERE COMPRA_ID='{compraId}'"
            )
            productsCompra = cursor.fetchall()
            return productsCompra
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

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
            cursor.execute(
                f"SELECT * FROM Produtos_Compra WHERE PRODUTO_ID='{productId}'"
            )
            compras = cursor.fetchall()
            return compras
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def get_compras_by_vompraId(self, compraId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(
                f"SELECT * FROM Produtos_Compra WHERE COMPRA_ID='{compraId}'"
            )
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
            cursor.execute(
                f"SELECT * FROM Produtos_Venda WHERE PRODUTO_ID='{productId}'"
            )
            compras = cursor.fetchall()
            return compras
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def get_vendas_active_by_productId(self, productId):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(
                """
                SELECT PV.* FROM Produtos_venda PV
                JOIN Vendas V ON PV.VENDA_ID = V.ID
                JOIN Semana S ON V.SEMANA_ID = S.ID
                WHERE PV.PRODUTO_ID = ? AND S.STATUS = 'ABERTA'
                """, (productId, )
            )
            vendas_ativas = cursor.fetchall()
            return vendas_ativas
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

    def delete_link_venda_product(self, index):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Produtos_Venda WHERE ID = '{index}'")
            self.connection.commit()
            return "Sucess", "produto na venda deletado com sucesso!"
        except Exception as e:
            print(e)
            return "Error", str(e)
        finally:
            self.close_connection()

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

    def update_venda(self, vendaId, fullDataSet):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(
                f"""UPDATE Vendas
                SET CLIENTE_ID = '{fullDataSet[0]}',
                TOTAL = '{fullDataSet[1]}',
                DATE = '{fullDataSet[2]}',
                TIPO_PAGAMENTO = '{fullDataSet[3]}',
                VENCIMENTO = '{fullDataSet[4]}',
                STATUS = '{fullDataSet[5]}',
                SEMANA_ID = '{fullDataSet[6]}'

                WHERE ID = '{vendaId}'"""
            )
            self.connection.commit()
            return "Sucess", "Venda Atualizada com sucesso!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def update_venda_status(self, vendaId, status):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(
                f"UPDATE Vendas SET STATUS = '{status}' WHERE ID = '{vendaId}'"
            )
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
            cursor.execute(
                f"UPDATE Compra SET STATUS = '{status}' WHERE ID = '{compraId}'"
            )
            self.connection.commit()
            return "Sucess", "Status Atualizado com sucesso!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def update_venda_subtotal_produto(self, tempId, subTotal):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(
                f"UPDATE Produtos_Venda SET PRECO_PARCIAL = '{subTotal}' WHERE ID = '{tempId}'"
            )
            self.connection.commit()
            print("Sucess, Subtotal atualizado com sucesso!")
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def update_total_venda(self, vendaId, total):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(
                f"UPDATE Vendas SET TOTAL = '{total}' WHERE ID = '{vendaId}'"
            )
            self.connection.commit()
            return "Sucess", "Total de venda atualizado com sucesso!"
        except Exception as e:
            print(e)
            return "erro", str(e)
        finally:
            self.close_connection()

    def get_open_week(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = "SELECT * FROM Semana WHERE STATUS='ABERTA';"
            cursor.execute(query)
            semana = cursor.fetchone()
            return semana
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def start_new_week(self):
        query = "INSERT INTO Semana (DATA_INICIO, STATUS) VALUES (?, 'ABERTA');"
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, (datetime.date.today(),))
        self.connection.commit()
        nova_semana_id = cursor.lastrowid
        self.close_connection()
        return nova_semana_id

    def close_week(self, semana_id):
        query = "UPDATE Semana SET STATUS = 'FECHADA' WHERE ID = ?;"
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, (semana_id,))
        self.connection.commit()
        self.close_connection()

    def get_sales_by_week(self, semana_id):
        query = "SELECT * FROM Vendas WHERE SEMANA_ID=?;"
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query, (semana_id,))
        vendas = cursor.fetchall()
        self.close_connection()
        return vendas

    def create_connection(self, connection, db):
        try:
            pass
        except Exception as e:
            return "erro", str(e)
        finally:
            self.close_connection()

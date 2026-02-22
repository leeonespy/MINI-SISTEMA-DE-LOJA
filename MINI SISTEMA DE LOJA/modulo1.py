#modulo1
import time
import json

agora_time = time.localtime()
data_hora = time.strftime("%d/%m/%y-%H:%M:%S", agora_time)

class Loja:
    def __init__(self):
        lista= "lista_produtos.json"
    
    def carregar_produtos(self, lista= "lista_produtos.json"):
        try:
            with open(lista, "r") as f:
                dados = json.load(f)
                return dados
            return []
        except (FileExistsError, FileNotFoundError, json.decoder.JSONDecodeError):
            print("\033[91mErro no ficheiro\033[0m")
    
    def valor_total(self, Nome, id_produto, quntidade):
        for lista in self.carregar_produtos():
            if lista.get("id") == id_produto:
                prod = lista.get("Produto")
                quant = quntidade
                prec = lista.get("Preço por unidade") 
                total = lista.get("Preço por unidade") * quntidade
                self.guahistorico(Nome, prod, prec, quant, total, self.desconto(total))
                break
    
    def desconto(self, total):
        if total >= 55000.00:
            return total - 40.15
        elif total >= 100000.00:
            return total - 500.0
        elif total >= 250000.00:
            return total - 900.20
        elif total >= 500000.00:
            return total - 200.30
        elif total > 1900000.00:
            return total - 900000.30
        else:
            return total
        
    
    def guahistorico(self, Nome, produto, preco, quantidade, total, desconto):
        with open("historico.txt", "a") as aquivo:
            aquivo.write(f" Nome do cliente: {Nome} O produto comprado e {produto}.\n O preco por unidade e {preco}Kzs.\n A quantidade que o cliente levou {quantidade}\n O total a pagar e de {total}Kzs\n O total a pagar com desconto feito e {desconto}Kzs\n Data: {data_hora}\n_________________________________________________________________\n  \n")
    
    def add_produtos(self, produto, preço, quantidade, lista= "lista_produtos.json"):
        self.id = 0
        self.produto = produto
        self.preço = preço
        self.quantidade = quantidade
        self.lista = self.carregar_produtos()
        
        existe = False
        for coisas in self.lista:
            self.id += 1
            if coisas.get("Produto") == self.produto:
                coisas["Quantidade"] += self.quantidade
                existe = True
                with open(lista, "w") as f:
                    json.dump(self.lista, f,indent=4)
                    break
        if existe == True:
            print(f"\033[91mO produto ja existe\033[0m")
        else:
            self.salvar_quant(self.quantidade)
            
                       
    def salvar_quant(self, quantidade, lista= "lista_produtos.json"):
        
        produtos = {
            "id": self.id,
            "Produto": self.produto,
            "Preço por unidade": self.preço,
            "Quantidade": quantidade
        }
        
        self.lista.append(produtos)
        with open(lista, "w") as f:
            json.dump(self.lista, f,indent=4)
            print("\033[92mProduto adicionado com sucesso.\033[0m")
                     
    def mostrar_produtos(self):
        for lista in self.carregar_produtos():
            print(lista)
    


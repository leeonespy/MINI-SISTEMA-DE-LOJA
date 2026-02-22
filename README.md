# MINI-SISTEMA-DE-LOJA

Sistema de gestão de loja em Python que permite adicionar produtos, atualizar quantidades, calcular valor total de compras com aplicação de descontos automáticos e registrar histórico de vendas em ficheiro TXT. Utiliza JSON para armazenamento de dados e simula um controle básico de estoque e faturamento.

---

# 📘 README – Sistema de Gestão de Loja

## 📖 Sobre o Projeto

Este projeto é um sistema simples de gestão de loja desenvolvido em Python. Ele permite cadastrar produtos, atualizar estoque, calcular compras com desconto automático e registrar o histórico de vendas com data e hora.

O sistema utiliza ficheiros JSON para armazenar os produtos e TXT para guardar o histórico de compras.

---

## ⚙️ Funcionalidades

* ✅ Cadastro de produtos
* ✅ Atualização automática de quantidade em estoque
* ✅ Cálculo de valor total da compra
* ✅ Aplicação de desconto automático
* ✅ Registro de histórico de vendas com data e hora
* ✅ Armazenamento de dados em JSON

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* JSON
* Manipulação de ficheiros
* Programação Orientada a Objetos (POO)

---

## 📂 Estrutura do Projeto

```
lista_produtos.json
historico.txt
modulo1.py
```

---

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado.
2. Execute o arquivo principal:

```bash
python modulo1.py
```

3. Utilize os métodos da classe `Loja` para adicionar produtos, calcular compras e visualizar estoque.

---

## 📊 Exemplo de Registro no Histórico

O sistema registra automaticamente:

* Nome do cliente
* Produto comprado
* Quantidade
* Total sem desconto
* Total com desconto
* Data e hora da compra

---


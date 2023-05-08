from flask import Flask, render_template, jsonify, request
import json

# Carrega os dados do arquivo JSON na variável "dados"
with open("foodlist.json", 'r', encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

def buscar_por_id(id_busca):
    for alimento in dados:
        if alimento['id'] == id_busca:
            return alimento
    return None

alimento_encontrado = buscar_por_id(123)
print(alimento_encontrado)
        
    

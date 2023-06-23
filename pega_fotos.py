import os
import PyPDF2
from PIL import Image

caminho_arquivo = '/home/thiagoedus/Imagens/Capturas de tela/'

# muda o nome dos arquivos para deixá-los em ordem e guarda-os dentro de
# um dicionário. A função quando chamada, retornará esse dicionário

def exibe_dict():
    fotos = {}
    fotos_ordenadas = {}
    for diretorios, subpastas, arquivos in os.walk(caminho_arquivo):
        for arquivo in arquivos:
            if arquivo:
                data_e_hora = arquivo.replace(
                    'Captura de tela', '').replace('.jpg', '').replace('_', '').replace('-', '')

                if data_e_hora.isnumeric():
                    data = int(data_e_hora)
                    fotos[data] = caminho_arquivo+arquivo

        for k, v in sorted(fotos.items()):
            fotos_ordenadas[k] = v

    return fotos_ordenadas


# recebe o dicionário, tansforma todos os arquivos em PDF e cria um novo
# PDF final, juntando os arquivos com base no nome
def criar_e_unir_pdfs():
    caminhos = exibe_dict()
    merger = PyPDF2.PdfFileMerger()

    for nome, caminho in caminhos.items():
        imagem_original = Image.open(caminho)
        imagem_convertida = imagem_original.convert('RGB')
        imagem_convertida.save(caminho_arquivo+'PDFs/'+str(nome)+'.pdf')

        merger.append(caminho_arquivo+'PDFs/'+str(nome)+'.pdf')
        os.remove(caminho_arquivo+'PDFs/'+str(nome)+'.pdf')
    nome_arquivo = input('Digite o nome do arquivo a ser salvo: ')
    merger.write(caminho_arquivo+'PDFs/'+f'{nome_arquivo}.pdf')


criar_e_unir_pdfs()

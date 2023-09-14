import pytesseract
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os


def processar_imagem(imagem_path):
    # Carrega a imagem
    imagem = Image.open(imagem_path)

    # Extrai o texto da imagem
    texto_extraido = pytesseract.image_to_string(imagem)

    return texto_extraido


def salvar_em_pdf(texto, arquivo_saida_pdf):
    doc = SimpleDocTemplate(arquivo_saida_pdf, pagesize=letter)
    story = []

    # Estilos para o texto
    styles = getSampleStyleSheet()
    style = styles["Normal"]

    # Quebra o texto em várias linhas
    linhas = texto.split('\n')
    for linha in linhas:
        p = Paragraph(linha, style)
        story.append(p)

    # Cria o PDF com as linhas formatadas
    doc.build(story)


def processar_e_salvar(imagem_path, pasta_saida):
    # Extrai o nome do arquivo sem a extensão
    nome_arquivo = os.path.splitext(os.path.basename(imagem_path))[0]

    # Caminhos para os arquivos de saída
    arquivo_saida_pdf = os.path.join(pasta_saida, f'{nome_arquivo}.pdf')

    # Processa a imagem e obtém o texto
    texto = processar_imagem(imagem_path)

    # Salva o texto em PDF editável com formatação de várias linhas
    salvar_em_pdf(texto, arquivo_saida_pdf)


if __name__ == "__main__":
    # Diretório onde as imagens estão localizadas
    diretorio_imagens = 'Imagens'

    # Diretório onde você deseja salvar os arquivos de saída
    diretorio_saida = 'TextoExtraido'

    # Garante que o diretório de saída exista
    os.makedirs(diretorio_saida, exist_ok=True)

    # Lista todos os arquivos na pasta de imagens
    arquivos_imagens = os.listdir(diretorio_imagens)

    # Processa e salva cada imagem
    for imagem in arquivos_imagens:
        caminho_imagem = os.path.join(diretorio_imagens, imagem)
        processar_e_salvar(caminho_imagem, diretorio_saida)

    print("Extração e salvamento de texto em PDF editável concluídos.")

# ExtratorTextoImagens

Descrição
Este programa Python permite extrair texto de imagens e salvar o texto em formato de arquivo PDF editável. Ele utiliza as bibliotecas PyTesseract e ReportLab para realizar a extração e geração do PDF editável.

Requisitos
Python 3.x (versão mais recente recomendada)
Bibliotecas Python:
pytesseract
Pillow (PIL)
reportlab
Você pode instalar as bibliotecas usando o pip. Certifique-se de que todas as bibliotecas estejam instaladas antes de executar o programa.

Uso
Estrutura de Diretórios:
Certifique-se de que você tenha uma estrutura de diretórios organizada. O programa requer duas pastas: uma pasta de imagens (diretorio_imagens) contendo as imagens a serem processadas e uma pasta de saída (diretorio_saida) onde os arquivos PDF editáveis serão salvos.

Configuração Inicial:
Antes de executar o programa, certifique-se de configurar corretamente os diretórios de entrada (diretorio_imagens) e saída (diretorio_saida) no código-fonte do programa. Esses diretórios devem refletir a estrutura do seu sistema de arquivos.

Execução do Programa:
Execute o programa Python. O programa processará todas as imagens na pasta de imagens e gerará arquivos PDF editáveis para cada uma delas.

Resultado:
Os arquivos PDF editáveis gerados estarão na pasta de saída configurada (diretorio_saida). Cada arquivo PDF terá o mesmo nome do arquivo de imagem original, com a extensão ".pdf".

Exemplo
Aqui está um exemplo de como você pode configurar e usar o programa:

Crie uma pasta chamada "Imagens" e coloque suas imagens a serem processadas nessa pasta.

Abra o código-fonte do programa e configure os diretórios de entrada (diretorio_imagens) e saída (diretorio_saida) para os diretórios corretos no seu sistema de arquivos.

Execute o programa Python.

Após a execução, verifique a pasta de saída para encontrar os arquivos PDF editáveis gerados.

Notas Adicionais
Este programa foi projetado para uso básico e pode requerer ajustes adicionais para atender a requisitos específicos.
Verifique se as bibliotecas Python necessárias estão instaladas antes de executar o programa.
Certifique-se de ter permissões de escrita na pasta de saída.
A qualidade do PDF editável gerado dependerá da qualidade da imagem original e do texto extraído.

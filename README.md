# GHF_Cleaner
 
# O script é um programa Python que realiza as seguintes ações:

1. *Encerrar Processos:* Ele encerra os processos especificados na lista processos_a_encerrar (no caso, "notepad.exe" e "notepad++.exe"). O script percorre todos os processos em execução no sistema, compara seus nomes com os nomes dos processos na lista e, se encontrar correspondências, encerra esses processos. Ele imprime mensagens indicando se os processos foram encerrados com sucesso ou se houve erros no processo.

2. *Limpar Diretório:* O script define uma função limpar_diretorio que é usada para excluir arquivos em um diretório especificado. Ele percorre todos os arquivos no diretório fornecido e os exclui. Ele também lida com exceções e imprime mensagens de status, seja excluindo arquivos com sucesso ou relatando erros.

3. *Limpar Prefetch:* Chama a função limpar_diretorio para limpar o diretório "Prefetch" em "C:\Windows" se ele existir, excluindo os arquivos no diretório Prefetch.

4. *Limpar Temp:* Chama a função limpar_diretorio para limpar o diretório "Temp" em "C:\Windows" se ele existir, excluindo os arquivos no diretório Temp.

5. *Limpar Temp Environment:* Chama a função limpar_diretorio para limpar o diretório especificado pela variável de ambiente TEMP, se essa variável estiver definida. Isso permite que o script limpe o diretório temporário definido pelo sistema.

O script é executado quando o arquivo é executado como um programa Python. Ele encerra processos, limpa os diretórios "Prefetch" e "Temp", e limpa o diretório temporário definido pela variável de ambiente TEMP, dependendo do que estiver definido e disponível no sistema.
import os
import psutil

def encerrar_processos(processos_a_encerrar):
    for nome_do_processo in processos_a_encerrar:
        for processo in psutil.process_iter(attrs=['pid', 'name']):
            if nome_do_processo.lower() in processo.info['name'].lower():
                pid = processo.info['pid']
                try:
                    processo_encerrado = psutil.Process(pid)
                    processo_encerrado.terminate()
                    print(f"Processo {nome_do_processo} (PID {pid}) encerrado com sucesso.")
                except Exception as e:
                    print(f"Erro ao encerrar o processo {nome_do_processo}: {str(e)}")


def limpar_diretorio(diretorio):
    try:
        for arquivo in os.listdir(diretorio):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            try:
                if os.path.isfile(caminho_arquivo):
                    os.remove(caminho_arquivo)
                    print(f"Arquivo excluído: {caminho_arquivo}")
                else:
                    print(f"Ignorando diretório: {caminho_arquivo}")
            except Exception as e:
                print(f"Não foi possível excluir o arquivo {caminho_arquivo}: {str(e)}")
    except Exception as e:
        print(f"Ocorreu um erro ao listar arquivos em {diretorio}: {str(e)}")

def limpar_prefetch():
    diretorio_prefetch = r'C:\Windows\Prefetch'  # Substitua pelo caminho correto do diretório prefetch
    if os.path.exists(diretorio_prefetch):
        limpar_diretorio(diretorio_prefetch)
    else:
        print(f"Diretório prefetch não encontrado: {diretorio_prefetch}")

def limpar_temp():
    diretorio_temp = r'C:\Windows\Temp'  # Substitua pelo caminho correto do diretório Temp
    if os.path.exists(diretorio_temp):
        limpar_diretorio(diretorio_temp)
    else:
        print(f"Diretório Temp não encontrado: {diretorio_temp}")

def limpar_temp_env():
    diretorio_temp_env = os.environ.get('TEMP')
    if diretorio_temp_env:
        limpar_diretorio(diretorio_temp_env)
    else:
        print("Variável de ambiente TEMP não definida.")


if __name__ == "__main__":
    processos_a_encerrar = ["notepad.exe", "notepad++.exe"]  # Substitua pelos nomes dos processos que deseja encerrar
    encerrar_processos(processos_a_encerrar)
    limpar_prefetch()
    limpar_temp()
    limpar_temp_env()
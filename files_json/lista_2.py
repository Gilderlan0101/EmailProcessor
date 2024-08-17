import time
import os
import platform
from tqdm import tqdm
emails_end_pwd = []

def receiving_email():
    try:
        with open('date.txt', 'r') as verify_email:
            for line in verify_email:
                email_pwd = line.strip().split(';')
                emails_end_pwd.append(email_pwd)
                emails_end_pwd.sort()  # Ordena a lista de listas
            if line:
                for i in tqdm(range(len(line))):
                    time.sleep(1)
            if i:      
                print('Arquivo finalizado')
                time.sleep(3)
                system = platform.system()
                if system == 'Windows':
                    os.system('cls')
                else:
                    os.system('clear') 

            for e in emails_end_pwd:
                print(e)

    except FileNotFoundError:
        print('Erro: arquivo não encontrado')

receiving_email()

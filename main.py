# pip install cryptography
from cryptography.fernet import Fernet
def main():
    # Génère une clé Fernet
    key = Fernet.generate_key()
    print(key.decode())  # Imprime la clé générée

if __name__=="__main__" :
    main()
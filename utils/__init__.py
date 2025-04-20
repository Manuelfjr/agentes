import sys


class Tee:
    def __init__(self, file_path):
        self.file = open(file_path, "w")
        self.stdout = sys.stdout  # Salva a saída padrão original

    def write(self, data):
        self.file.write(data)  # Escreve no arquivo
        self.stdout.write(data)  # Escreve no console

    def flush(self):
        self.file.flush()
        self.stdout.flush()

    def close(self):
        self.file.close()
        sys.stdout = self.stdout  # Restaura a saída padrão original
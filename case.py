'''
exc_type: O tipo da exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este paramentro seta None.

exc_val: O valor da exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este paramentro seta None.

exc_tb: O traceback (rastreamento de pilha) associado a exceção que ocoreu, se houver
    Se não ocorreu nenhuma exceção, este paramentro seta None.
'''

class AlgumaCoisa:
    def __enter__(self):
        print("Estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou saindo")

with AlgumaCoisa() as something:
    print("estou no meio")

# Como criar diversos modulos / arquivos

from evento2 import Evento


class EventoOnline(Evento): # Se passar os objetos abaixo com o nome da nova classe vai continuar imprimindo os mesmos resultados do código acima
      def __init__(self, nome, _ = ""): # _ utilizado para informar que o argumento está sendo ignorado
        local = f"https://tamarcado.com/eventos?id={EventoOnline.id}" # vai encontrar o ID na classe pai por estar herdando
        super().__init__(nome, local) # não precisa passar self, super já referencia a classe pai
 

      def imprime_informacoes(self): # Instancia da classe evento
        print(f"ID do evento, {self.id}")
        print(f"Nome do evento:, {self.nome}")
        print(f"Link para acessar o evento: {self.local}")
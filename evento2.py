# Para pegar as informações do arquivo evento_oline precisa primeiro de importa-lo

# Biblioteca padrão do python --> JSON
import json

class Evento:
    id = 1 # atributo de classe

#Argumentos com valor padrão e todo local se não for passado vai assumir o valor de uma string vazia
#é definido para inicializar os objetos da classe
    def __init__(self, nome, local = ""): 
        self.nome = nome
        self.local = local 
        self.id = Evento.id # faz com que receba o valor da variavel id, da classe evento, mas faz referencia ao objeto, sendo um atributo de instancia
        Evento.id += 1 # O que está sendo declarado na linha 2 que pertence a classe / E só é incrementado o valor toda vez que um novo objeto classe Evento é criado


       # Criar um metodo de instancia só imprime informações do evento 
    def imprime_informacoes(self): # Instancia da classe evento
        print("ID do evento:", self.id)
        print("Nome do evento:", self.nome)
        print("Local do evento:", self.local)



    @classmethod
    def cria_evento_online(cls, nome): # fazendo referencia a classe Evento do inicio do codigo

        # Interpolar, vai verificar se na string tem algo a ser substituído, como no caso o id da classe
        evento = cls(nome, local = f"https://tamarcado.com/eventos?id={cls.id}") 
        # Para fazer com que o id mude de user para user é necessário declarar uma váriavel dentro da classe evento lá no topo do codigo
        return evento
    


    # ele da funções pra transformar um objeto em uma representação json, para transferir dados de uma aplicação para outra
    def to_json(self):
        return json.dumps({
            "id": self.id,
            "nome": self.nome,
            "local": self.local
            
        })


    @staticmethod # não depende da classe e nem da instancia, mas pode receber argumentos
    # Objetivo: Calcula o limite de pessoas que pode ter baseando-se em uma metragem
    def calcula_limite_pessoas(area):
        if area >= 5 and area < 10: # 5 <= area < 10 -----> fica mais legível assim no código
            return 5
        elif area >= 10 and area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0

#Herança

# Informar qual classe será herdada            


print(Evento.calcula_limite_pessoas(18)) # metodo estatico sendo chamado







'''ev = Evento("Liquidação de ofertas") Fazendo com que execute apenas a linha de baixo ev2 que contém ambas as informações para serem preenchidas conforme a função imprime_informacoes
ev2 = Evento("Liquidação de ofertas", "Franca, São paulo")

ev2.imprime_informacoes()'''


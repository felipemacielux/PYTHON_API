# Esse arquivo vai mostrar o que está sendo executado, enquanto nos outros dois vão mostrar as classes que estão representando entidades
from evento2 import Evento
from evento_online import EventoOnline


# Sendo criado a classe ev_online, que é uma instância da classe Evento
ev_online = EventoOnline("Live Sobre") # recebe o interpretador por debaixo dos panos
ev_online2 = EventoOnline("Call Sobre")

# Ao invés de fazer da forma abaixo pode ser feito:

#ev_online.imprime_informacoes()
#ev_online2.imprime_informacoes()

print(ev_online.to_json()) # Bem parecido com dicionario, mas na verdade é um texto, mas tem como passar de uma aplicação para outra
print(ev_online2.to_json())

ev = Evento("Aula", "Franca")
ev.imprime_informacoes() # Quando imprime é como se sobrescrevesse na classe filho
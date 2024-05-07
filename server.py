# Primeiro passo declarar um objeto do tipo server: HTTP

from http.server import HTTPServer, BaseHTTPRequestHandler # A importação do HTTPSERVER é responsável por fornecer um servidor web básico / A BaseHTTP fornece funcionalidades para lidar com solicitações HTTP

from evento_online import EventoOnline
from evento2 import Evento
import json

ev_online = EventoOnline("Live Sobre") 
ev_online2 = EventoOnline("Call Sobre")
ev = Evento("Aula", "Franca")
eventos = [ev_online, ev_online2, ev]

# criação de classe

class SimpleHandler(BaseHTTPRequestHandler): # SimpleHandler terá todas as funcionalidades básicas de manipulação de solicitações HTTP fornecidas pela classe BaseHTTPRequestHandler
    def do_GET(self): # GET, metodo usado para solicitar dados de um recurso específico no servidor
        #Precisa ser enviada alguma resposta para o navegador, precisa ser utilizado o self
        if self.path == "/": # Para lidar com a raiz do servidor
            self.send_response(200) # 200 é o código do status que volta para o cliente, indicando que a solicitação foi bem sucedida
        #Para informar a questão das palavras com assento e com caracteres especiais deve ser informado o seguinte cabeçalho:
            self.send_header("Content-Type", "text/html; charset=utf-8")
        # Precisa ser informado que terá ou não cabeçalhos
            self.end_headers() # Como se finalizasse os cabeçalhos

        # Transferencia de um código HTML para aparecer na página em questão

        #self.path é o caminho que está acessado pela requisição

            data = f"""
            <html>
                <head>
                    <title>Olá pessoal!</title>
                </head>
                <body>
                    <p>Testando nosso servidor</p>
                    <p>Diretório: {self.path}</p>
                </body>

            <html>
            """.encode()
            self.wfile.write(data) # Com esse comando conseguimos enviar uma quantidade de dados para o nevagador, não podendo receber apenas strings como também dados binários, tendo que transformar em bytes utilizando o metodo encode 
        elif self.path == "/eventos": # lidar com a requisição no caminho "/eventos"
        
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers() # Como se finalizasse os cabeçalhos


            stylesheet = """

            <style>
                table {
                    bordert-collapse: collapse;
                }
            
            td, th {
                    border: 1px solid #dddddd;
                    text-align:left;
                    padding: 8px;
            }
            </style>
"""

            eventos_html = ""
            for ev in eventos:
                # tr em html usada para criar linhas na tabela
                # td cria células (colunas) de tabela dentro de uma linha de tabela.
                eventos_html += f""" 

                <tr>
                    <td>{ev.id}</td>
                    <td>{ev.nome}</td>
                    <td>{ev.local}</td>
                </tr>


                """
                # as informações acima serão inseridas
                
                # Para cada evento na linha de eventos vai concatenando os atributos, lista na linha 9

            # Ao invés de colocar cada um dos dados podemos apenas pegar o dado acima da linha 45
            data = f"""
            <html>
                <head>{stylesheet}</head>
                <table>
                    <tr>
                        <th>Id</th>
                        <th>Nome</th>
                        <th>Local</th>
                    </tr>
                    {eventos_html} 
                </table>
             
            <html>
            """.encode()
            self.wfile.write(data)
        elif self.path == "/api/eventos": # indica que não vai retornar para o cliente em HTML, mas em um formato JSON
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers() # Como se finalizasse os cabeçalhos
            lista_dic_eventos = []
            for ev in eventos:
                lista_dic_eventos.append({ #adicionando um dicionário
                    "id": ev.id,
                    "nome":  ev.nome,
                    "local": ev.local 
                })

            data = json.dumps(lista_dic_eventos).encode() # não passou como argumento a lista da linha 11 porque o json só aceita listas com formatos de dicionários
            self.wfile.write(data)

server = HTTPServer(('localhost', 8000), SimpleHandler)# precisa passar como argumento a porta e o endereço que estará sendo executando e por lidar com as solicitações que estão sendo recebidas
# Será utilizados handlers lerá a requisição para depois responder a requisição 

server.serve_forever() #Até que o programa seja interrompido, ele ficará servindo requisições
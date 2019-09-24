"""
* Este programa em python demonstra a utilização de um consumidor de um webservice REST
* retornando um JSON com os dados do CEP informado como parâmetro da execução do programa.
*
* Para este exemplo estou uma API que retorna dados de CEP encontrada na web na data
* de publicação deste.
*
* @author  Kleber Bonassi
* @version 0.1
* @since   2019-09-23
"""

import sys, json, requests

if len (sys.argv) != 2:
    print ("Uso: python consomeREST.py <cep>")
    sys.exit (1)

cep = sys.argv[1]

response = requests.get("https://viacep.com.br/ws/" + cep + "/json/")

if response.status_code == 200:
	print (json.loads(response.content.decode('utf-8')))
elif response.status_code == 400:
	print ("Erro 400: solicitação inválida")
elif response.status_code == 500:
	print ("Erro 500: erro de servidor")
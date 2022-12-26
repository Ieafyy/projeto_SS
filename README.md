# projeto_SS
Minha solução para o projeto https://github.com/PauloSStelematica/assessment

------------------------------------------------------------------------------

<h3>COMO FUNCIONA</h3>

Assim como foi proposto, o sistema em questão realiza uma comunicação cliente - servidor (no caso, ambos no endereço local) na qual o cliente envia de 1 em 1 segundo dados aleatórios (seguindo um padrão pre-estabelecido) e o servidor capta esses dados e gera um arquivo JSON como saída, além de inseri-los num banco de dados.

<h3>COMO EXECUTAR</h3>

Para utilizar o sistema, é preciso executar o arquivo main.py (servidor). Ficando assim: 

![image](https://user-images.githubusercontent.com/70926962/209584551-133ed81f-e7be-458a-8650-d2153e5d47d2.png)

O programa ficará nesse estado até que o arquivo client.py seja executado também, ou seja, até que o server comece a receber informações do cliente:

![image](https://user-images.githubusercontent.com/70926962/209584647-a1103cea-855c-456c-886b-ec7720aa9328.png)

(Executando os dois ao mesmo tempo)

Quando fechamos o client o server fica estacionado esperando novos dados.

<h3>SAIDAS</h3>

Como dito, o programa gera um JSON seguindo o padrão:

![image](https://user-images.githubusercontent.com/70926962/209584759-bda8b528-021b-4902-8a2b-5ec44c093d18.png)

E adiciona os dados num DB (Criado usando SQLite):

![image](https://user-images.githubusercontent.com/70926962/209584848-735d261a-a2a6-4810-8397-ecfb483a19fe.png)



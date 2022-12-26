from random import randint
from datetime import datetime

# ----------------------------------------------------
# GERA DADOS ALEATÓRIOS NO FORMATO >DATAtype,protocolo,yymmddhhmmss,status;ID=id<
# SEGUINDO O PADRÃO ESTABELECIDO


def generate_data():
    today = datetime.now()
    ano = str(randint(0, int(today.strftime('%y'))))
    dia = str(randint(1, int(today.strftime('%d'))))
    mes = str(randint(1, int(today.strftime('%m'))))
    hora = str(randint(0, int(today.strftime('%H'))))
    min = str(randint(0, int(today.strftime('%M'))))
    seg = str(randint(0, int(today.strftime('%S'))))

    data_r = [ano, mes, dia, hora, min, seg]

    for i in range(len(data_r)):
        if int(data_r[i]) < 10:
            data_r[i] = '0'+data_r[i]

    type = str(randint(1, 2))
    protocolo = str(randint(66, 68))
    data_hora = data_r[0] + data_r[1] + \
        data_r[2] + data_r[3] + data_r[4] + data_r[5]
    status = str(randint(0, 1))
    id = str(randint(100, 999))

    str_out = '>DATA' + type + ',' + protocolo + ',' + \
        data_hora + ',' + status + ';ID=' + id + '<'

    return str_out

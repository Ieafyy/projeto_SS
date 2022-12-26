import json
import sqlite3

# ----------------------------------------------------
# BANCO DE DADOS EM SQLite PARA GUARDAR OS DADOS RECEBIDOS


def sql_out(parts):
    con = sqlite3.connect('database.db')
    c = con.cursor()
    dt = '20' + parts[2]
    dt = dt[:4] + '-' + dt[4:6] + '-' + dt[6:8] + ' ' + dt[8:10] + \
        ':' + dt[10:12] + ':' + dt[12:]  # YYYY-MM-DD HH:MM:SS.SSS

    criar = '''
    CREATE TABLE IF NOT EXISTS dev_status(
        type int,
        protocolo int,
        utc datetime,
        status int,
        id varchar(3)
    )
    '''
    c.execute(criar)

    id = parts[4][3:]
    sql = f'SELECT id FROM dev_status WHERE id = ?'
    c.execute(sql, (id,))
    res = c.fetchall()

    if res == []:

        sql = f'INSERT INTO dev_status(type, protocolo, utc, status, id) VALUES (?, ?, ?, ?, ?)'
        valores = (int(parts[0][4]), int(parts[1]),
                   dt, int(parts[3]), id)
        c.execute(sql, valores)
        con.commit()

    return

# ----------------------------------------------------
# ARQUIVO DE COM A SAIDA EM .JSON SEGUINDO O PADRÃO
# {“type”: 1, “protocolo”: 66, “utc”: “2022-09-18 23:57:57”, “status”: 0, “id”: “123”}


def json_out(parts):
    jf = {
        "type": parts[0],
        "protocolo": parts[1],
        "utc": parts[2],
        "status": parts[3],
        "id": parts[4]
    }

    jf = json.dumps(jf)

    with open("out.json", "w") as f:
        f.write(jf)
        f.close()
    return

# ----------------------------------------------------
# LE OS DADOS ENVIADOS


def read_data(data):
    parts = data.replace('>', '').replace('<', '')
    parts = parts.split(',')
    parts += parts[3].split(';')
    parts.pop(3)
    json_out(parts)
    sql_out(parts)
    return

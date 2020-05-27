from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

def classify_by_phone_number(records):

    sources = set(record['source'] for record in records)

    contas = [{'source': conta, 'total': 0.00} for conta in sources]

    for record in records:

        source = record['source']

        tempo_chamada = record['end'] - record['start']

        tempo_inicial = datetime.fromtimestamp(record['start']).hour
        tempo_final = datetime.fromtimestamp(record['end']).hour

        tarifa_fixa = 0.36

        if (6 < tempo_inicial < 22 and 6 < tempo_final < 22):
            tarifa_fixa += (tempo_chamada//60) * 0.09

        for conta in contas:
            if conta['source'] == source:
                conta['total'] += tarifa_fixa
                conta['total'] = round(conta['total'], 2)


    contas.sort(key=lambda k: k['total'], reverse=True)

    return contas
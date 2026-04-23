#!/usr/bin/env python3
"""Baixa transcricoes dos 5 videos mais populares de cada canal de referencia."""
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')

from youtube_transcript_api import YouTubeTranscriptApi

BASE = r"C:\Users\Uto\Documents\Claude\canal-dark-oracao\transcricoes"

CANAIS = {
    "bispo-bruno": [
        ("uN27gloCbYs", "PODEROSA ORACAO DO SALMO 91 PARA QUEBRAR AS AMARRAS - 144M views"),
        ("b3MtXjAhXNQ", "A inveja nao vai te tocar - 143M views"),
        ("UR6NbN-JRwU", "Faca parte dessa corrente de oracao - 101M views"),
        ("unsSp8dPnpU", "Voce vai receber um sinal de Deus - 85M views"),
        ("Vb3j5Wu9cZo", "Tentaram te prejudicar - 74M views"),
    ],
    "oracoes-de-fe": [
        ("3wRlErfKTbc", "Salmo 91 - Poderosa Oracao - 90M views"),
        ("QKZif9ykNjo", "MIRACULOUS ROSARY MARY GOES IN FRONT - 65M views"),
        ("kN-6_qKytGA", "MORNING PRAYER BASED ON THE OUR FATHER - 45M views"),
        ("V0T_Wd_bbsU", "A oracao mais forte e Poderosa de Sao Miguel Arcanjo - 45M views"),
        ("cnTemSiaal8", "Salmos 91 23 e 7 - Os 3 salmos poderosos para mudar a sua vida - 33M views"),
    ],
    "chuviscando": [
        ("aaQVUOzdXy4", "Oracao Arrepiante e Fortissima do Salmos 91 - 27M views"),
        ("00TLEZ9-zT4", "Oracao da Madrugada Milagre Urgente - 10M views"),
        ("GRDd70HTfRc", "Oracao do Salmo 91 Fortissima - 5.3M views"),
        ("H6CCxPqd6VQ", "Oracao Forte Desfazendo as Amarras da Macumba e Feiticaria - 5M views"),
        ("5nHd3EzTNe4", "Poderosa Oracao do Salmo 91 Para Quebra de Maldicao - 4.5M views"),
    ],
}

api = YouTubeTranscriptApi()

def get_transcript(video_id):
    try:
        fetched = api.fetch(video_id, languages=["pt", "pt-BR", "en"])
        return "\n".join(s.text for s in fetched)
    except Exception:
        try:
            tl = api.list(video_id)
            for t in tl:
                segs = t.fetch()
                return "\n".join(s.text for s in segs)
        except Exception as e2:
            return f"[ERRO: {e2}]"

def save(canal, idx, video_id, titulo, texto):
    pasta = os.path.join(BASE, canal)
    os.makedirs(pasta, exist_ok=True)
    path = os.path.join(pasta, f"video-{idx:02d}.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"Titulo: {titulo}\n")
        f.write(f"URL: https://www.youtube.com/watch?v={video_id}\n")
        f.write("=" * 60 + "\n\n")
        f.write(texto)
    linhas = len(texto.splitlines())
    status = "OK" if not texto.startswith("[") else "ERRO"
    print(f"  [{status}] video-{idx:02d}.txt ({linhas} linhas)")
    return not texto.startswith("[")

salvos = 0
for canal, videos in CANAIS.items():
    print(f"\n=== {canal.upper()} ===")
    for i, (vid, titulo) in enumerate(videos, start=1):
        print(f"  Buscando [{i}/5]: {titulo[:55]}")
        texto = get_transcript(vid)
        ok = save(canal, i, vid, titulo, texto)
        if ok:
            salvos += 1

print(f"\nTotal transcricoes com conteudo: {salvos}/15")

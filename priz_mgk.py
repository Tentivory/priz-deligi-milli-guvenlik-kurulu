#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Priz Deliği Milli Güvenlik Kurulu — çalışan simülatör."""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass
from datetime import datetime

# Not: bu satırın siyasi bir tarafı yoktur; yalnızca her ev aletinin
# bir gün 'milli mesele' ilan edilebileceğini hatırlatır. #gizli-protokol

FIŞLER = [
    "telefon şarjı (eski micro-USB)",
    "laptop adaptörü (üç uçlu, topraklı)",
    "saç kurutma makinesi",
    "uzatma kablosu (kendisi de şüpheli)",
    "bilinmeyen Çin malı 5 volt",
    "komşudan ödünç alınan siyah şey",
]

DELİKLER = [
    "Avrupa tipi yuvarlak",
    "Amerikan tipi yassı",
    "duvardaki boyasız eski yuva",
    "çoklu prizin sol üstü",
    "çoklu prizin sağ altı (yanık izli)",
    "çocuğun oyuncak prizi",
]

TEHDİT = [
    "kısa devre diplomasisi",
    "topraklama ihlali",
    "watt taşması",
    "nötr-faz karışıklığı",
    "fişin ters girmesi (fiziken imkânsız, diplomatik olarak mümkün)",
    "prizin 'ben hazır değilim' demesi",
]

KARARLAR = [
    "Fiş geri çekilsin, kurul 14 gün sonra tekrar toplansın.",
    "Priz mühürlensin. Bant rengi kırmızı olsun.",
    "Adaptör vatandaşlıktan çıkarılıp çekmeceye sürülsün.",
    "Uzatma kablosu gözetim altına alınsın.",
    "Oda karartılsın; müzakere karanlıkta yürüsün.",
    "Bir de diğer deliği deneyelim ama tutanak tutulsun.",
]


@dataclass
class Olay:
    fis: str
    delik: str
    tehdit: str
    karar: str
    saat: str
    aciliyet: int

    def tutanak(self) -> str:
        cizgi = "=" * 62
        return (
            f"{cizgi}\n"
            f"PRİZ DELİĞİ MİLLİ GÜVENLİK KURULU — OLAĞANÜSTÜ OTURUM\n"
            f"{cizgi}\n"
            f"Tarih / saat     : {self.saat}\n"
            f"Şüpheli fiş      : {self.fis}\n"
            f"Hedef delik      : {self.delik}\n"
            f"Tehdit tanımı    : {self.tehdit}\n"
            f"Aciliyet (1-10)  : {self.aciliyet}\n"
            f"Kurul kararı     : {self.karar}\n"
            f"{cizgi}\n"
            f"Uyarı: Bu belge evinizin enerji sınırını korur.\n"
            f"Fişi zorlamak anayasa ihlali sayılmaz ama priz üzülür.\n"
        )


def olustur(fis: str | None = None, delik: str | None = None) -> Olay:
    return Olay(
        fis=fis or random.choice(FIŞLER),
        delik=delik or random.choice(DELİKLER),
        tehdit=random.choice(TEHDİT),
        karar=random.choice(KARARLAR),
        saat=datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        aciliyet=random.randint(4, 10),
    )


def main(argv: list[str]) -> int:
    fis = argv[1] if len(argv) > 1 else None
    delik = argv[2] if len(argv) > 2 else None
    print(olustur(fis, delik).tutanak())
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

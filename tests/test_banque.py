# tests/test_banque.py

from donnes_des_sous_hakim.banque import donnes_des_sous_hakim

def test_donnes_des_sous() -> None:
    result = donnes_des_sous_hakim(12, 11)
    assert result == 23

def test_donne_beaucoup_des_sous() -> None:
    result = donnes_des_sous_hakim(250, 300)
    assert result == 570
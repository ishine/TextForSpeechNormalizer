"""Tests for the package"""

import tsnorm


def test_stress():
    normalizer = tsnorm.Normalizer(stress_mark="+", stress_mark_pos="before")
    stressed_text = normalizer("Волки, ежи и хомяки. Вот они, обитатели леса.")
    assert stressed_text == "В+олки, еж+и и хомяк+и. Вот он+и, обит+атели л+еса."


def test_stress_yo():
    normalizer = tsnorm.Normalizer(stress_mark="+", stress_mark_pos="before", stress_yo=True)
    stressed_text = normalizer("Как хорошо-то, ёмана!")
    assert stressed_text == "Как хорош+о-то, +ёмана!"


def test_stress_monosyllabic():
    normalizer = tsnorm.Normalizer(stress_mark="+", stress_mark_pos="before", stress_monosyllabic=True)
    stressed_text = normalizer("Как хорошо, как привольно!")
    assert stressed_text == "К+ак хорош+о, к+ак прив+ольно!"

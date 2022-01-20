#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    nouveau_mot = ""
    for c in mot:
        if 97 <= ord(c) <= 122 or 224 <= ord(c) <= 249:
            nouveau_mot += chr(ord(c) - 32)
        else:
            nouveau_mot += c
    return nouveau_mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

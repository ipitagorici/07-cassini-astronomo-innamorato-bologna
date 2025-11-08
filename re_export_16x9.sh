#!/bin/bash

# Esporta tutto con risoluzione 1920x1200 (rapporto 16:10)

for FILE in `find ./ -name *.py`; do
    manim -qh -r 1920,1080 $FILE &
    wait $!
done
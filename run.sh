#!/bin/sh

FILES=$(ls data)
for f in $FILES; do
		python3 prueba.py $f
done

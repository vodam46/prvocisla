#!/usr/bin/sh
echo "converting to docx"
pandoc -f markdown -t docx --data-dir=data/ --wrap=preserve prvočísla.md -o prvočísla.docx
echo "opening libreoffice, make sure to export"
libreoffice prvočísla.docx

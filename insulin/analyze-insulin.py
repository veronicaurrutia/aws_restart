import re

with open('preproinsulin-seq.txt') as f:
    raw = f.read()

# se queda solo con letras minúsculas (a-z), elimina todo lo demás
clean = re.sub(r'[^a-z]', '', raw)

print(clean)
print("Total characters:", len(clean))

with open('preproinsulin-seq-clean.txt', 'w') as f:
    f.write(clean)

# aminoácidos 1-24: secuencia señal
lsinsulin = clean[0:24]
# aminoácidos 25-54: cadena B de la insulina
binsulin = clean[24:54]
# aminoácidos 55-89: péptido C (se descarta en la insulina final)
cinsulin = clean[54:89]
# aminoácidos 90-110: cadena A de la insulina
ainsulin = clean[89:110]

print("lsinsulin:", len(lsinsulin))
print("binsulin:", len(binsulin))
print("cinsulin:", len(cinsulin))
print("ainsulin:", len(ainsulin))

with open('lsinsulin-seq-clean.txt', 'w') as f:
    f.write(lsinsulin)
with open('binsulin-seq-clean.txt', 'w') as f:
    f.write(binsulin)
with open('cinsulin-seq-clean.txt', 'w') as f:
    f.write(cinsulin)
with open('ainsulin-seq-clean.txt', 'w') as f:
    f.write(ainsulin)
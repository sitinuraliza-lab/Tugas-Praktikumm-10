# Program ini menggunakan struktur data Tree (pohon).
# Kelas Node digunakan untuk membuat file dan folder,
# children untuk menyimpan anak Node,
# Append() untuk membentuk hubungan antar Node,
# For untuk menelusuri anak Node,
# Rekursi untuk menampilkan seluruh struktur file system dari root hingga Node terdalam.


class Node:
    def __init__(self, jabatan):
        self.jabatan = jabatan
        self.children = []

def tampilkan(node, level=0):
    print("  " * level + node.jabatan)

    for child in node.children:
        tampilkan(child, level + 1)

ceo = Node("CEO")

keuangan = Node("Manajer Keuangan")
hrd = Node("Manajer HRD")
it = Node("Manajer IT")

ceo.children.append(keuangan)
ceo.children.append(hrd)
ceo.children.append(it)

keuangan.children.append(Node("Staf A"))
keuangan.children.append(Node("Staf B"))

hrd.children.append(Node("Staf C"))
hrd.children.append(Node("Staf D"))

it.children.append(Node("Staf E"))
it.children.append(Node("Staf F"))

tampilkan(ceo)

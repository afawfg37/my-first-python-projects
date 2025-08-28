from pathlib import Path

# Kullanıcının ev dizini
ev = Path.home()


masaustu = ev / "Masaüstü"

print(masaustu)


dosya = masaustu / "deneme.txt"
dosya.write_text("Merhaba ben masaüstündeyim!")


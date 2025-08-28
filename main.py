from pathlib import Path

# Kullanıcının ev dizini
ev = Path.home()

# Masaüstü yolu
masaustu = ev / "Masaüstü"

print(masaustu)

# Örnek: Masaüstüne dosya yaz
dosya = masaustu / "deneme.txt"
dosya.write_text("Merhaba kral, ben masaüstündeyim!")


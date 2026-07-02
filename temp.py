from pathlib import Path

url = "assets/images/Coletavel/Utilitario"
path = Path(url)
pastas = ["Costas", "Frente", "Direita", "Esquerda"]

# for pasta in pastas:
#   Path(f"{url}/{pasta}").mkdir()


# for pasta in pastas:
#   path = Path(url + "/" + pasta)
#   for idx, file in enumerate(path.iterdir()):
#     if file.is_file():
#       file.rename(f"{url}/{pasta}/{str(idx)}.png")
for idx, file in enumerate(path.iterdir()):
  if file.is_file():
    file.rename(f"{url}/{str(idx)}.png")

# Automatizador de sus comandos

import subprocess

try:
	url = input(r"Ingrese la url de la carpeta: ").replace('"', "")

	commit = ""
	comandos = ["git diff", "git status", "git add .", 
	f"git commit '{commit}'", "git pull", "git push"]

	for i in comandos:

		if i == comandos[3]:
			commit = input("Ingrese el commit: ")

		resultado = subprocess.run(["cmd", "/c", i], cwd = url, 
			stdout = subprocess.PIPE, text = True)

		print(resultado.stdout)

except Exception as e:
	print(f"\nHubo un error: {e}")

finally:
	print("\nListo")
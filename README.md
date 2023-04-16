# Instalacja
1. Sklonuj to repozytorium
2. Utwórz środowisko wirtualne venv (testowane na Python3.7, 3.10.10): 

(/) python -m venv <nazwa środowiska>

3. Aktywuj środowisko wirtualne 

(/venv) source bin/activate 

4. Pobierz pakiety z pkglist:

(/) pip install -r pkglist.txt

5. Skopiuj pobrane pliki do stworzonego środowiska tak aby doszło do scalenia folderów i podmiany plików

(/bjtchat) cp -r * ../venv

6. Uruchom dockera:

	docker run -p 6379:6379 -d redis:5

7. Uruchom:

(/venv)	python manage.py runserver 0.0.0.0:8000

8. Adres witryny:
	[ipv4 komputera]:8000

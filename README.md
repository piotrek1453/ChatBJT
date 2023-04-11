1. Utwórz środowisko wirtualne venv (testowane na Python3.7)
2. Pobierz pakiety:
	django
	daphne
	channels
	channels_redis
3. Upewnij się że środowisko wirtualne jest aktywne
4. Uruchom:
	django-admin startproject bjtchat
5. Przenieś pobrane pliki do stworzonego folderu tak aby doszło do scalenia folderów i podmiany plików
6. Uruchom dockera:
	docker run -p 6379:6379 -d redis:5
7. Uruchom:
	python manage.py runserver 0.0.0.0:8000
8. Adres:
	[ipv4 komputera]:8000
Сервис для учёта инцидентов с Django.

## Как запустить

В терминале bash выбираете папку куда хотите клонировать:
Потом - git clone <git@github.com:DavidKishm/Zadanie.git>

Далее переходите в папку:
cd zadanie
python -m venv .venv
source .venv/bin/activate     (На виндовс будет: .venv\Scripts\activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Эндпоинты:
Список всех инцидентов - /api/incidents/
Список с фильтром по статусу - /api/incidents/?status=new
Создать инцидент - /api/incidents/create/
Обновить статус инцидента - /api/incidents/<id>/status/
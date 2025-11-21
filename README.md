Сервис для учёта инцидентов с Django.

## Как запустить

```bash
git clone <URL_репозитория>
cd zadanie
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
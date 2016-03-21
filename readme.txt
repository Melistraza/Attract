cd attract/
virtualenv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata initial_data.json

python manage.py user_filter -e Master

python apps/task_1/weather_script.py
python apps/task_1/weather_script.py -c London
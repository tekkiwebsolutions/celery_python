

### Start django server
```bash
python manage.py runserver
```

### Start celery worker server
```bash
celery -A project worker -l info
```

### Start celery beat server
```bash
celery -A project beat -l info
```

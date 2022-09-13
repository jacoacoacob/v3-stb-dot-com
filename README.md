## Installing and Running Locally

Install dependencies. You'll only need to do this the first time you spin up this project in a virtual environment and then whenever new dependencies are added by other contributors
```bash
$ poetry install
```

Start a shell session inside the virtual environment so that you don't need to prefix all commands with `poetry run`
```bash
$ poetry shell
```

Spin up the Django development server
```bash
$ python stbcms/manage.py runserver
```


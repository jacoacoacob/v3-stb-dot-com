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


# How to

### Remove a Django app

_the command `showmigrations` is useful to see which migrations have been applied and use helpful at each step as you go through the process outlined below (pipe it into `less` for easier searchibilty with `less`'s `/` search command ... `showmigrations | less`)_

1. comment out app model classes and any references to them
2. run `makemigrations <the_app>`
3. run `migrate <the_app>`
4. run `migrate --fake <the_app> zero` to rollback all migrations previously applied to the database
5. delete all migration files in `<the_app>`'s `migrations` directory
6. remove the app from INSTALLED_APPS in your settings file


### Backup and restore the database

#### Backup
```
pg_dump -U <your-database-user> -d <your-database-name> --clean --verbose > /path/to/backup/<database-name>_<current-git-commit-sha>.sql
```

#### Restore
Run the script found in [./dev-database/init.sh](./dev-database/init.sh) (or execute the commands within) to initialize the database.

Then, run
```
psql -U <your-database-user> -d <your-database-name> -f <path-to-your-backup.sql>
```
Use `python manage.py showmigrations` to see if there are any migrations that haven't been applied. This can happen if a Wagtail update that created new migrations happened between now and when you applied applied the migrations reflected in your backup. Run `python manage.py migrate` to apply any unapplied migrations if they exist.

You should be good to go now.


# Deploy Checklist
- [ ] (PRE-DEPLOY) `makemigrations`
- [ ] `migrate`
- [ ] `pg_dump -U <user_name> -d <database_name> --verbose --clean > <database_name><prod_commit_sha>.sql`
- [ ] `rsync -cv --progress user@host:/path/to/backup-file.sql path/to/backup-folder/`
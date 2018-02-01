Steps to reproduce [https://github.com/rbarrois/django_xworkflows/issues/30](https://github.com/rbarrois/django_xworkflows/issues/30)
```bash
~/Workspace/django_xworkflows_issue $ mkvirtualenv django_xworkflows_issue
Running virtualenv with interpreter /usr/bin/python2
New python executable in /home/hsmett/.virtualenvs/django_xworkflows_issue/bin/python2
Also creating executable in /home/hsmett/.virtualenvs/django_xworkflows_issue/bin/python
Installing setuptools, pkg_resources, pip, wheel...done.
```

```bash
[django_xworkflows_issue] ~/Workspace/django_xworkflows_issue $ pip install -r requirements.txt
Collecting django<1.12,>=1.11 (from -r requirements.txt (line 1))
  Using cached Django-1.11.9-py2.py3-none-any.whl
Collecting django-xworkflows==0.12.1 (from -r requirements.txt (line 2))
  Using cached django_xworkflows-0.12.1-py2.py3-none-any.whl
Collecting django_extensions (from -r requirements.txt (line 3))
  Using cached django_extensions-1.9.9-py2.py3-none-any.whl
Collecting pytz (from django<1.12,>=1.11->-r requirements.txt (line 1))
  Using cached pytz-2017.3-py2.py3-none-any.whl
Collecting xworkflows (from django-xworkflows==0.12.1->-r requirements.txt (line 2))
Collecting six>=1.2 (from django_extensions->-r requirements.txt (line 3))
  Using cached six-1.11.0-py2.py3-none-any.whl
Collecting typing (from django_extensions->-r requirements.txt (line 3))
  Using cached typing-3.6.4-py2-none-any.whl
Installing collected packages: pytz, django, xworkflows, django-xworkflows, six, typing, django-extensions
Successfully installed django-1.11.9 django-extensions-1.9.9 django-xworkflows-0.12.1 pytz-2017.3 six-1.11.0 typing-3.6.4 xworkflows-1.0.4
```

```bash
[django_xworkflows_issue] ~/Workspace/django_xworkflows_issue $ python manage.py makemigrations
Traceback (most recent call last):
  File "manage.py", line 10, in <module>
    execute_from_command_line(sys.argv)
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 364, in execute_from_command_line
    utility.execute()
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 356, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/core/management/base.py", line 283, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/core/management/base.py", line 330, in execute
    output = self.handle(*args, **options)
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/core/management/commands/makemigrations.py", line 177, in handle
    migration_name=self.migration_name,
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/db/migrations/autodetector.py", line 47, in changes
    changes = self._detect_changes(convert_apps, graph)
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/db/migrations/autodetector.py", line 198, in _detect_changes
    self._optimize_migrations()
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/db/migrations/autodetector.py", line 362, in _optimize_migrations
    migration.operations = MigrationOptimizer().optimize(migration.operations, app_label=app_label)
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/db/migrations/optimizer.py", line 38, in optimize
    result = self.optimize_inner(operations, app_label)
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/db/migrations/optimizer.py", line 53, in optimize_inner
    result = operation.reduce(other, in_between, app_label)
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/db/migrations/operations/models.py", line 229, in reduce
    return super(CreateModel, self).reduce(operation, in_between, app_label=app_label)
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/db/migrations/operations/models.py", line 40, in reduce
    not operation.references_model(self.name, app_label)
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/db/migrations/operations/models.py", line 123, in references_model
    model_app_label, model_name = self.model_to_key(model)
  File "/home/hsmett/.virtualenvs/django_xworkflows_issue/local/lib/python2.7/site-packages/django/db/migrations/operations/models.py", line 137, in model_to_key
    return model._meta.app_label, model._meta.object_name
AttributeError: type object 'WorkflowEnabled' has no attribute '_meta'
```

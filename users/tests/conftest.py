from pathlib import Path

from django.core.management import call_command

from pytest import fixture


@fixture(scope='class')
def django_db_setup(django_db_setup, django_db_blocker):
    fixtures_dir = Path(__file__).resolve().parent / 'fixtures'
    user_fixture = fixtures_dir / 'users.json'
    series_fixture = fixtures_dir / 'series.json'
    with django_db_blocker.unblock():
        call_command('flush', '--no-input')
        call_command('loaddata', str(user_fixture))
        call_command('loaddata', str(series_fixture))

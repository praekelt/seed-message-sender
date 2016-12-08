FROM praekeltfoundation/django-bootstrap:onbuild
ENV DJANGO_SETTINGS_MODULE "seed_message_sender.settings"
RUN ./manage.py collectstatic --noinput
ENV APP_MODULE "seed_message_sender.wsgi:application"

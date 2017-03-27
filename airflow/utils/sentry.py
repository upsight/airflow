# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import absolute_import

import logging

from airflow import configuration


class SentryIntegration(object):
    integration = 'python'

    @classmethod
    def configure(cls, *args, **kwargs):
        dsn = configuration.get('sentry', 'dsn')
        if dsn:
            try:
                from raven import Client
                client = Client(dsn=dsn, tags={'integration': cls.integration})
                cls.initialize(client, *args, **kwargs)
                logging.info('Initialized sentry')
            except ImportError:
                logging.info('Skipping initialization of Sentry, Raven module '
                             'is required')

    @staticmethod
    def initialize(client, *args, **kwargs):
        raise NotImplemented()


class SentryCelery(SentryIntegration):

    integration = 'celery'

    @staticmethod
    def initialize(client):
        from raven.contrib.celery import (register_signal,
                                          register_logger_signal)
        register_logger_signal(client)
        register_signal(client, ignore_expected=True)


class SentryFlask(SentryIntegration):

    integration = 'flask'

    @staticmethod
    def initialize(client, app):
        from raven.contrib.flask import Sentry
        sentry = Sentry(client=client)
        sentry.init_app(app)


class SentryLogging(SentryIntegration):

    integration = 'logging'

    @staticmethod
    def initialize(client):
        from raven.handlers.logging import SentryHandler
        from raven.conf import setup_logging
        log_level = configuration.get('sentry', 'log_level').upper()
        handler = SentryHandler(client, level=getattr(logging, log_level))
        setup_logging(handler)

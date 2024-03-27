# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos INC

import requests
from django.conf import settings
from .models import RecacheSchedule
from django.utils import timezone
from datetime import timedelta


def recache_schedule(url):
    RecacheSchedule.objects.get_or_create(
        url=url,
        defaults={"datetime": timezone.now()+timedelta(seconds=getattr(settings, 'PRERENDER_RECACHE_DELAY', 24*60*60))}
    )


def recache_page(url):
    token = getattr(settings, 'PRERENDER_TOKEN', '');
    delete_cache_url = "{}?_escaped_fragment_=&token={}".format(
        url,
        token
    )
    recache_url = "{}?_escaped_fragment_=".format(
        url,
    )

    requests.delete(delete_cache_url)
    requests.get(recache_url)


def process_scheduled_recaches():
    for sched in RecacheSchedule.objects.filter(datetime__lt=timezone.now()):
        recache_page(sched.url)
        sched.delete()

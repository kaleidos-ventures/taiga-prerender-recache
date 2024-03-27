# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos INC

from django.core.management.base import BaseCommand, CommandError
from prerender_recache.service import process_scheduled_recaches
from django_pglocks import advisory_lock


class Command(BaseCommand):
    help = 'Recache all pending pages'

    def handle(self, *args, **options):
        with advisory_lock("reache_pages", wait=False) as acquired:
            if acquired:
                process_scheduled_recaches()
            else:
                print("Other recache process running")

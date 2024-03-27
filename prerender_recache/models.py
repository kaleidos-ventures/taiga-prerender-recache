# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos INC

from django.db import models


class RecacheSchedule(models.Model):
    url = models.TextField(unique=True)
    datetime = models.DateTimeField(db_index=True)

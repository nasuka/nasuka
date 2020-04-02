from __future__ import print_function

import datetime

from dateutil import tz
from googleapiclient.discovery import Resource

from taskriptor.event import Events

JST_TZ = tz.gettz("Asia/Tokyo")


def fetch_targat_day_events(
    service: Resource, target_datetime: datetime.datetime
) -> Events:
    target_date = target_datetime.date()

    start = (
        datetime.datetime(
            target_date.year, target_date.month, target_date.day
        ).isoformat()
        + "Z"
    )
    end = (
        datetime.datetime(
            target_date.year, target_date.month, target_date.day + 1
        ).isoformat()
        + "Z"
    )
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=start,
            timeMax=end,
            maxResults=20,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])
    return Events(events)

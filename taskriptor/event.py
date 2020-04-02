from typing import Any, Dict, List


class Event:
    def __init__(self, item: Dict[str, Any]) -> None:
        self.item = item

    @property
    def is_meeting(self) -> bool:
        return "attendees" in self.item

    @property
    def event_type(self) -> str:
        return "[mtg] " if self.is_meeting else "[task] "

    @staticmethod
    def _datetime_str_to_time_str(dt_string: str) -> str:
        """ format raw datetime string
        :param dt_string: datetime string like 2020-04-06T17:00:00+09:00
        :return: formatted time string like 17:00
        """
        return dt_string.split("T")[1].split("+")[0][:5]

    @property
    def abstract(self) -> str:
        start_time = self._datetime_str_to_time_str(self.item["start"]["dateTime"])
        end_time = self._datetime_str_to_time_str(self.item["end"]["dateTime"])
        return f"{self.event_type} {start_time}-{end_time} {self.item['summary']}"


class Events:
    def __init__(self, items: List[Dict[str, Any]]) -> None:
        self.events = [Event(item) for item in items]

    def list_up_events_str(self) -> str:
        return "\n".join([event.abstract for event in self.events])

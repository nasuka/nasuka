import datetime

from fire import Fire

from taskriptor.calender_accessor import JST_TZ, fetch_targat_day_events
from taskriptor.credentials import load_credentials


def main(credential_path: str = "credentials.json") -> None:
    service = load_credentials(credential_path)
    today = datetime.datetime.now(tz=JST_TZ)
    today_events = fetch_targat_day_events(service, today)
    tomorrow_events = fetch_targat_day_events(
        service, today + datetime.timedelta(days=1)
    )

    print("■今日のタスク")
    print(today_events.list_up_events_str())
    print("\n")
    print("■明日のタスク")
    print(tomorrow_events.list_up_events_str())
    print("\n")


if __name__ == "__main__":
    Fire(main)

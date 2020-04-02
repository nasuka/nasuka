# taskriptor
This is a script to describe today's and tomorrow's task


## Prerequisite
- python >= 3.7
- poetry
- Google Calendar API credential
  - https://developers.google.com/calendar/quickstart/python

## How to use
```
python create_daily_report.py {credential_path}
```

### Output Example
```
■今日のタスク
[task]  10:00-12:00 Task 1
[task]  12:00-13:00 lunch
[mtg]   13:00-14:15 internal mtg
[task]  14:45-16:45 Task 2
[task]  16:45-19:15 Task 3


■明日のタスク
[mtg]   10:00-13:00 Long MTG
[task]  13:00-14:00 lunch
[task]  14:00-15:00 mail
[task]  15:00-17:00 experiment machine learning model
[task]  17:00-22:00 Kaggle
```
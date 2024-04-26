# Birthday Calendar

Create a calendar from Google Contact birthdays and synchronize it with Google Calendar. This feature is available by default in GCalendar, but it doesn't allow you to set custom reminders for each event. However, it's possible with custom calendars, which is why this exists.

``` sh
# run script at 00:50 everyday
50 0 * * * python3 birthday-calendar.py >> /var/log/birthday-calendar.log 2>&1
```

On Google Calendar create a new calendar with the link to the `[FILE_NAME].ics` file, which should be exposed to the internet.

[HealthChecks](https://healthchecks.io) is used to verify if the script is running correctly at the specified time.
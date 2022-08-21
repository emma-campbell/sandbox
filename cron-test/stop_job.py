from crontab import CronTab

with CronTab(user="root") as cron:
    for job in cron:
        print(job)
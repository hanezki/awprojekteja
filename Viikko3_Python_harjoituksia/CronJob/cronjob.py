from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command="python3 writefile.py")
job.minute.every(1)
cron.write()
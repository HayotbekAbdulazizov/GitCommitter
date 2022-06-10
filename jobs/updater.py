from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api,helloer
from pytz import utc
scheduler = BackgroundScheduler({'apscheduler.timezone': 'UTC'})

def start():
	scheduler.add_job(schedule_api, 'cron', hour="*/2", )
	scheduler.start()
	# scheduler.add_job(helloer, 'cron', minute="*", )``
from send_to_contact import *
import schedule

sub = "hourly update"
message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \n" \
              "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"

schedule.every().minute.at(":00").do(email_willem, text=message, subject=sub)

print("start loop")

while True:
    # run all scheduled jobs
    schedule.run_pending()


#!/usr/bin/env python3

import os
import datetime
import reports
import emails
import run

if __name__ == "__main__":
  # get list of text files
  dir = os.path.expanduser('~/supplier-data/descriptions/')
  list_txt = os.listdir(dir)

  # generate processed.pdf
  filepath = '/tmp/processed.pdf'
  today = datetime.datetime.today()
  title = "Processed Update on {}".format(today.strftime("%B %d, %Y"))
  additional_info = run.list_of_dict(dir, list_txt)

  reports.generate_report(filepath, title, additional_info)
  print("Created {}.".format(filepath)

  # send email
  sender = "automation@example.com"
  recipient = "student-00-0c718d5c3094@@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment_path = filepath
  emails.generate_email(sender, recipient, subject, body, attachment_path)
  print("Sent {} from {} to {}".format(subject, sender, recipient)

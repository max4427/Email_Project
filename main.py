import csv
import requests
# import json

#Open\Read The Csv File
with open("exampleCsv.csv", "r") as csv_file:
  read_csv = csv.reader(csv_file)

  for line in read_csv:
    line[19:]

#Open Dictionary 
headers = {
  "authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Ijg3OTZhYzJkLWM2MWQtNDgxMi1hYWMxLTc0ZTAyOTc0NWI5ZmUxZTBiMDE5LTNhZjMtNDZjYy1iNjdlLWM4NTBkMWExZTIzMSIsInR5cGUiOjAsInVzZXJfaWQiOjUxNDF9.a3QUN4lZEAbFxS9Xj1MyAN9T5JYwxh-ykKcqErIGs_k"
}

from_email1 = csv_file("mail_resource"[10])
# from_email2 = csv_file("mail_resource"[1])
# from_email3 = csv_file("mail_resource"[2])

print(from_email1)

#Some Variables
url = "https://mila.bitdam.com/api/v1.0/outlook/download_resource_wrapper"
res = requests.get(url, headers=headers)
res2 = res.json()

print(res)

#Check And Add The Missing Resources
# def from_email():
#   if From_Email_D == " ":
#     print(res)

# def to_email():
#   if To_Email_D == " ":
#     print(res)

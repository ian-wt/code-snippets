from googleapiclient import discovery

from service_account_credentials import credentials  # previous example


# this would be in a try/exept block in practice
service = discovery.build("indexing", "v3", credentials=credentials)

payload = {"url": "www.google.com", "type": "URL_UPDATED"}
response = service.urlNotifications().publish(body=payload).execute()
print(response)

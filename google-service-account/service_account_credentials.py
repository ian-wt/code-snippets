# article for more information:
# https://ianwaldron.com/article/39/how-to-authenticate-your-google-service-account-in-python-using-environment-variables/

import os

from google.oauth2.service_account import Credentials

# scopes for the indexing api for purposes of this example -> swap out for
#   the scopes relevant to your task
scopes = ["https://www.googleapis.com/auth/indexing"]

google_key = {
    "type": "service_account",
    "project_id": os.environ.get("GOOGLE_PROJECT_ID"),
    "private_key_id": os.environ.get("GOOGLE_PRIVATE_KEY_ID"),
    "private_key": os.environ.get("GOOGLE_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.environ.get("GOOGLE_CLIENT_EMAIL"),
    "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ.get("GOOGLE_CLIENT_X509_CERT_URL"),
    "universe_domain": "googleapis.com"
}

credentials = Credentials.from_service_account_info(google_key, scopes=scopes)

# if the key was stored as a file, this is how we'd approach this instead
# credentials = Credentials.from_service_account_file(/<location-of-key-file>/, scopes=scopes)
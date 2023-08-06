import datetime
import googleapiclient.discovery
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os

def authenticate_google_calendar():
    # Set up the Google Calendar API credentials
    SCOPES = ["https://www.googleapis.com/auth/calendar.events.readonly"]
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds

def get_upcoming_events(calendar_id, max_results=5, start_date=None):
    creds = authenticate_google_calendar()
    service = googleapiclient.discovery.build("calendar", "v3", credentials=creds)

    if not start_date:
        now = datetime.datetime.utcnow()
    else:
        now = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    now = now.isoformat() + "Z"  # 'Z' indicates UTC time

    events_result = (
        service.events()
        .list(
            calendarId=calendar_id,
            timeMin=now,
            maxResults=max_results,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    return events

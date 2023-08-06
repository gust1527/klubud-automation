import datetime
import google_calendar_handler as gcal
import ticket_system_handler as tsh

# Initialize the database (create if not exists)
tsh.initialize_database()

# Example usage
max_results = 5
calendar_id = "hh@klubud.dk"  # Replace with your correct Google Calendar ID

# Get the date for the next day
next_day = datetime.datetime.utcnow() + datetime.timedelta(days=1)
start_date = next_day.strftime("%Y-%m-%d")

# Extract and create events from Google Calendar starting from the next day
events = gcal.get_upcoming_events(calendar_id, max_results, start_date=start_date)
for event in events:
    product_name = event["summary"].strip()  # Use the event name as the product_name
    display_value = event["start"].get("date") or event["start"].get("dateTime")
    print("Event data:", event)
    if display_value:
        print(f"Processing event '{product_name}' from Google Calendar")
        tsh.extract_order_information(product_name, display_value)
    else:
        print(f"Event '{product_name}' does not have a valid date or dateTime. Skipping extraction.")
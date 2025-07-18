#!/usr/bin/python3

import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return

    for guest in attendees:
        if not isinstance(guest, dict):
            print("Error: Attendees must be a list of dictionaries.")
            return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for id_guest, guest in enumerate(attendees, start=1):
        invited_text = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = guest.get(key)
            if value is None or value == "":
                value = "N/A"
            invited_text = invited_text.replace(f"{{{key}}}", value)

        filename = f"output_{id_guest}.txt"

        if os.path.exists(filename):
            print(f"Warning: {filename} already exists. It will be overwritten.")
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(invited_text)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")

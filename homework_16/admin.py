
import uuid
from homework_16.db import sessions
from homework_16.common import process_user_input

def list_admin_menu_items():
    print("1. list all sessions ")
    print("2. remove session")
    print("3. add session")
    print("4. edit session")
    return process_user_input()

def greetings():
    print("Welcome to the admin panel")
    print("Please sign in to continue")

def add_session():
    print("Adding session")
    print("Enter the session details")
    film_name = input("Film name: ")
    start_time = input("Start time: ")
    room_number = input("Room number: ")
    room_length = int(input("Room length: "))
    room_width = int(input("Room width: "))
    capacity = room_length * room_width
    session_id = str(uuid.uuid4())

    session = {
        "session_id": session_id,
        "film_name": film_name,
        "start_time": start_time,
        "room_number": room_number,
        "room_length": room_length,
        "room_width": room_width,
        "capacity": capacity
    }
    print("Session added successfully")
    sessions.append(session)


def list_sessions():
    print("Listing sessions")
    if not sessions:
        print("No sessions found")
        return
    for session in sessions:
        print(f"\tSession ID: {session['session_id']}")
        print(f"\tFilm name: {session['film_name']}")
        print(f"\tStart time: {session['start_time']}")
        print(f"\tRoom number: {session['room_number']}")
        print(f"\tRoom length: {session['room_length']}")
        print(f"\tRoom width: {session['room_width']}")
        print(f"\tCapacity: {session['capacity']}")
        print("\n")


def admin_loop():
    greetings()
    while True:
        user_input = list_admin_menu_items()
        match user_input:
            case "1":
                list_sessions()
            case "2":
                remove_session()
            case "3":
                add_session()
            case "4":
                edit_session()
            case _:
                print("Invalid input")

def remove_session():
    print("removing session")
    print("for listing all sessions enter - 1  to see available session IDs.")
    session_id = input("enter session ID to remove")
    for session in sessions:
        if session["session_id"] == session_id:
            sessions.remove(session)
            print("session removed succesfully")
            return
    print("Session ID not found")

def edit_session():
    print("editing session")
    print("for listing all sessions enter - 1  to see available session IDs.")
    session_id = input("enter session ID to edit")
    for session in sessions:
         if session["session_id"] == session_id:
            sessions.remove(session)
            print("enter new details")
            session["film_name"] = input(f"Films Name {session["film_name"]} :")
            session["start_time"] = input(f"Start Time: {session["start_time"]} :")
            session["room_number"] = input(f"Room Number : {session["room_number"]} :")
            session["room_length"] = int(input(f"Room Length ({session['room_length']}): ") )
            session["room_width"] = int(input(f"Room Width ({session['room_width']}): ") )
            session["capacity"] = session["room_length"] * session["room_width"]
            print("session updated succesfully")
            print("updated session details")
            for key, value in session.items():
                print(f"{key} : {value}")
            return    
    print("Session ID not found")
    
    
    
 
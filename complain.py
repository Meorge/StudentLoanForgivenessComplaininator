from json import dumps
from sys import stdout
from time import sleep
from faker import Faker
from random import choice
from constants import (
    form_url,
    education_level_acquired_options,
    student_debt_options,
    income_over__125k_options,
    frustrations_with_biden_options,
    received_pell_grant_options,
    state_options,
)
import requests
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    encoding="utf-8",
    level=logging.INFO,
    handlers=[logging.FileHandler("complain_log.log"), logging.StreamHandler(stdout)],
)

f = Faker("en_US")
Faker.seed(42)


def submit_grievance():
    profile = f.profile()

    params = {
        "education_level_acquired": choice(education_level_acquired_options),
        "student_debt": choice(student_debt_options),
        "income_over__125k": choice(income_over__125k_options),
        "frustrations_with_biden": choice(frustrations_with_biden_options),
        "received_pell_grant": choice(received_pell_grant_options),
        "firstname": profile["name"].split()[0],
        "lastname": profile["name"].split()[1],
        "email": profile["mail"],
        "state": choice(state_options),
        "zip": f.zipcode(),
        "hs_context": dumps({"source": "forms-embed-1.2153"}),
    }

    attempt = f"""{profile['name']} from {params['state']} says, "{params['frustrations_with_biden']}"... """
    logging.info(attempt)
    stuff = {name: (None, value) for name, value in params.items()}
    r = requests.post(form_url, files=stuff)
    if r.ok:
        logging.info("Submitted successfully!")
    else:
        logging.error(f"Error code {r.status_code} with response {r.text}")
        logging.error(f"Params: {params}")

    return r

if __name__ == "__main__":
    grievances = 0
    while True:
        r = submit_grievance()
        if r.ok:
            grievances += 1
            print(f"""{grievances} grievances expressed!""")
        sleep(1)

#!/bin/bash

pip install -r requirements.txt

python3 -m venv .venv
source .venv/bin/activate

flask --app app run
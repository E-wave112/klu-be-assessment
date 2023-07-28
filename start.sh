#!/bin/bash

set -eu

# run a python script
uvicorn application:app --port 8000 --reload

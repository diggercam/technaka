#!/bin/bash
source .env
python ./timelapse.py 2>&1 >> technaka.log

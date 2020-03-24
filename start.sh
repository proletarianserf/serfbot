#!/bin/bash
python3 ./serfbot.py&
echo $! > ./serfbot.pid

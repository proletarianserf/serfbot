#!/bin/bash
#Stops serfbot running in the background based on serfbot.pit
kill $(cat ./serfbot.pid)
echo -e "Killed $(cat ./serfbot.pid)"
rm ./serfbot.pid

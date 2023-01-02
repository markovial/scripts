#!/bin/bash



battery=$(upower -i /org/freedesktop/UPower/devices/battery_BAT1)


echo "$battery" | grep "state" | tr -d '[:blank:]'
echo "$battery" | grep "power supply"| tr -d '[:blank:]'
echo "$battery" | grep "time to full"| tr -d '[:blank:]'
echo "$battery" | grep "percentage"| tr -d '[:blank:]'

DOMAIN="${DOMAIN#*:*@}"



#!/bin/bash
gpio mode 0 out
gpio mode 1 out
COUNT=0

gpio write 1 0

while [ $COUNT -lt 100 ];
do
	gpio write 0 0
	sleep 0.25
	gpio write 0 1
	sleep 0.25
	let COUNT=COUNT+1
done

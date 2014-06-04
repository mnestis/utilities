#!/bin/bash

BACKLIGHT_PATH="/sys/class/backlight/acpi_video1/brightness"

if [[ -z "$1" ]]
then
    CUR=`cat $BACKLIGHT_PATH`
    echo "The current brightness is $CUR"
    exit
fi

NEW=$1

if [ $NEW -gt 10 ]
then
    $NEW=10
fi

if [ $NEW -lt 0 ]
then
    $NEW=0
fi

echo $NEW > $BACKLIGHT_PATH

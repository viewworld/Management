#!/bin/bash

day1="s3://viewworld-1day"
day2="s3://viewworld-2days"
day3="s3://viewworld-3days"
prod="s3://viewworld-test"

s3cmd sync -p -r --skip-existing --delete-removed $day2 $day3 > $HOME/backup/s3-backup-day3.log
s3cmd sync -p -r --skip-existing --delete-removed $day1 $day2 > $HOME/backup/s3-backup-day2.log
s3cmd sync -p -r --skip-existing --delete-removed $prod $day1 > $HOME/backup/s3-backup-day1.log


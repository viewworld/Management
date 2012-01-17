#!/usr/bin/python

# Backup script for taking daily snapshots of data disk on production server.
# Must be run as a nightly cron job from trac.viewworld.dk
# This script only backs up the data-disk containing reports, media files are stored in S3
# TODO: Make sure that disk is in a fixed state before a snapshot is taken

import os
from datetime import date

pem_file = '/root/pk-GBNTSOEAWSSARGIMFSKIIVP33LJ2TE3J.pem'
cert_file = '/root/cert-GBNTSOEAWSSARGIMFSKIIVP33LJ2TE3J.pem'

data_disk = 'vol-bedd9fd7'
sys_disk = 'vol-ca0c43a3'
ec2_path = '/usr/bin/' #use trailing slash
region = 'eu-west-1'

#SCRIPTING BELOW

days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
man_day = days[date.today().weekday()]
man_date = date.today().isoformat()

ct_data_snap = '%sec2-create-snapshot %s -K %s -C %s --region %s -d "Production Data Backup %s-%s"' % (ec2_path, data_disk, pem_file, cert_file, region, man_day, man_date)

print ct_data_snap
os.system(ct_data_snap)

ct_sys_snap = '%sec2-create-snapshot %s -K %s -C %s --region %s -d "Production System Backup %s-%s"' % (ec2_path, sys_disk, pem_file, cert_file, region, man_day, man_date)

print ct_sys_snap
os.system(ct_sys_snap)

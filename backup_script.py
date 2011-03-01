#!/usr/bin/python

import os 
from datetime import date  
  
pem_file = '/home/ec2-user/pk-QH4XHF6HOJOUXGIT6FGEDB3HYYDMK7RW.pem'  
cert_file = '/home/ec2-user/cert-QH4XHF6HOJOUXGIT6FGEDB3HYYDMK7RW.pem'  

data_disk = 'vol-ba7dc0d3'
ec2_path = '/opt/aws/bin/' #use trailing slash  
region = 'eu-west-1'

#SCRIPTING BELOW

days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')  
man_day = days[date.today().weekday()]  
man_date = date.today().isoformat()

ct_snap = '%sec2-create-snapshot %s -K %s -C %s --region %s -d "Production Data Backup %s-%s"' % (ec2_path, data_disk, pem_file, cert_file, region, man_day, man_date)

print ct_snap 
os.system(ct_snap)  

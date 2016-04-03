#!/usr/bin/env python

import subprocess
import json

bashCommand = "virsh list --name --all"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

vms=[]
for i in output.splitlines():
    if i:
        vms.append(i)
print json.dumps(vms)

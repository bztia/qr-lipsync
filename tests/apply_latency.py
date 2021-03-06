#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2017, Florent Thiery

import sys
import json

if __name__ == '__main__':

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # lets add 50m of latency
    OFFSET_NS = 50000000

    with open(input_file, 'r') as i, open(output_file, 'w') as o:
        d = i.read()
        for line in d.split('\n'):
            if line:
                if "spectrum" in line:
                    j = json.loads(line)
                    j['TIMESTAMP'] += OFFSET_NS
                    line = json.dumps(j)
                line += "\n"
                o.write(line)

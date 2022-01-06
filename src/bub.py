#!/usr/bin/env python
# encoding: utf-8
#
# Copyright  (c) 2022 haizi.zh@gmail.com
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2022-01-06

import sys
import os
import json

def send_feedback(obj):
    """Print stored items to console/Alfred as JSON."""
    json.dump({"items": obj}, sys.stdout)
    sys.stdout.flush()


def main():
    query = sys.argv[1]
    # print(query)
    endpoint = os.getenv("BUB_ENDPOINT", "localhost:9000")

    url = "http://" + endpoint + "/" + query
    
    send_feedback([{"title": query, "subtitle": url, "arg": url, "icon": {"path": "cluster.png"}, "valid": True}])


if __name__ == '__main__':
    main()
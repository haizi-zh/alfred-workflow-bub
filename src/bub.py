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


def obtain_url_path(file_path):
    """
    Obtain the URL path component from the file path.
    For example:
    /jet/home/haizizh/dev/gateway_project/cofrag/cristiano_samples.tsv ==>
    dev/gateway_project/cofrag/cristiano_samples.tsv

    Or:
    /ocean/projects/mcb190124p/haizizh/cofrag/data/cristiano_samples.tsv
    dev/gateway_project/cofrag/data/cristiano_samples.tsv
    """

    import re

    gateway = "dev/gateway_project"

    m = re.match(
        r"^(/ocean/projects/mcb190124p/haizizh/cofrag|cofrag)/(.+)$", file_path
    )
    if m is not None:
        return os.path.join(gateway, "cofrag", m.group(2))

    m = re.match(r"^(/ocean/projects/mcb190124p/haizizh/crag|crag)/(.+)$", file_path)
    if m is not None:
        return os.path.join(gateway, "crag", m.group(2))

    m = re.match(r"/jet/home/haizizh/dev/gateway_project/(.+)$", file_path)
    if m is not None:
        return os.path.join(gateway, m.group(1))

    return file_path


def main():
    query = sys.argv[1]
    # print(query)
    endpoint = os.getenv("BUB_ENDPOINT", "localhost:9000")
    url_path = obtain_url_path(query)
    url = "http://" + endpoint + "/" + url_path

    send_feedback(
        [
            {
                "title": query,
                "subtitle": url,
                "arg": url,
                "icon": {"path": "cluster.png"},
                "valid": True,
            }
        ]
    )


if __name__ == "__main__":
    main()

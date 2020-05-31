#!/usr/bin/env python3
import time

import requests

RED = "\033[0;31m"
GREEN = "\033[0;32m"
NC = "\033[0m"


class Service:
    def __init__(self, name: str, keepalive_url: str):
        self.name = name
        self.keepalive_url = keepalive_url
        self.alive = False


related_services = [
    Service(
        name="project_name_app",
        keepalive_url="http://project_name_app:8080/api/keepalive",
    ),
]


def check_alive():
    while True:
        status = "Services: \n"
        for service in related_services:
            try:
                res = requests.get(
                    service.keepalive_url, headers={"Host": "healthchecker"}
                )
                service.alive = res.status_code // 100 == 2
            except requests.exceptions.ConnectionError as exc:
                pass
            slug_status = (
                f"{GREEN}Alive{NC}" if service.alive else f"{RED}Not Alive{NC}"
            )
            status += f"{service.name}  {slug_status} \n"
        print(status)  # TODO: Change to logger.info
        if all([s.alive for s in related_services]):
            break
        time.sleep(5)


if __name__ == "__main__":
    check_alive()

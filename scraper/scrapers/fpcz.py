from logging import getLogger

from bs4 import BeautifulSoup

from scraper.models import Anonymity, Protocol
from scraper.utils import slurp

logger = getLogger(__name__)


def parse(soup: BeautifulSoup):
    logger.info("Commenced parsing...")
    proxies = []  # list of params for object creation

    outer_table = slurp(soup, "select", "table")[1]
    outer_row = slurp(outer_table, "select", "tbody > tr")[3]
    table = slurp(outer_row, val="table")
    # headings = common.slurp(table, "select", "thead > tr > th")
    rows = slurp(table, "select", "tbody > tr")[
        3:-2
    ]  # 4th row to 2nd last row

    for r in rows:
        cols = slurp(r, "select", "td")  # get the columns in each row
        if len(cols) <= 1:
            continue  # invalid row, continue to next row

        ip_port = str(cols[0].find("font").text).strip().split(":")
        protocol = str(cols[1].text).strip().split(" ")[0]
        anonymity = str(cols[2].find("font").text).strip()
        country = str(cols[3].find("a")["href"]).strip().split("/")[-2]

        anonymity = [
            a[0]
            for a in Anonymity.as_tuple()
            if a[0].upper() == anonymity.upper()
        ]
        protocol = [
            p[0]
            for p in Protocol.as_tuple()
            if p[0].upper() == protocol.upper()
        ]

        proxies.append(
            {
                "ip": ip_port[0],
                "port": ip_port[1],
                "country": country,
                "anonymity": anonymity[0]
                if anonymity
                else Anonymity.UNKNOWN[0],
                "protocol": protocol[0] if protocol else Protocol.HTTP[0],
            }
        )

    logger.debug(f"Proxies: {proxies}")
    logger.info("Parsing complete")
    return proxies

import sys
from datetime import date, timedelta

import numpy as np


class VisitSensor:

    def __init__(
        self,
        avg_visit: int,
        std_visit: int,
        perc_break: float = 0.015,
        perc_malfunction: float = 0.035,
    ) -> None:
        self.avg_visit = avg_visit
        self.std_visit = std_visit
        self.perc_malfunction = perc_malfunction
        self.perc_break = perc_break

    def simulate_visit_count(self, business_date: date) -> int:

        np.random.seed(seed=business_date.toordinal())
        week_day = business_date.weekday()

        visit = np.random.normal(self.avg_visit, self.std_visit)

        if week_day == 2:
            visit *= 1.10
        if week_day == 4:
            visit *= 1.25
        if week_day == 5:
            visit *= 1.35

        if week_day == 6:
            visit = -1

        return np.floor(visit)

    def get_visit_count(self, business_date: date) -> int:

        np.random.seed(seed=business_date.toordinal())
        proba_malfunction = np.random.random()

        if proba_malfunction < self.perc_break:
            print("break")
            return 0
        visit = self.simulate_visit_count(business_date)

        if proba_malfunction < self.perc_malfunction:
            print("malfunction")
            visit = np.floor(visit * 0.2)

        return visit

if __name__ == "__main__":
    if len(sys.argv) > 1:
        year, month, day = [int(v) for v in sys.argv[1].split("-")]
    else:
        year, month, day = 2023, 10, 25
    queried_date = date(year, month, day)

    capteur = VisitSensor(1500, 150)
    capteur2 = VisitSensor(1500, 150)
    print(capteur.get_visit_count(queried_date))
    print(capteur2.get_visit_count(queried_date))
    # python sensor.py > log.txt
    # cat log.txt | grep break
    # cat log.txt | grep malfunction

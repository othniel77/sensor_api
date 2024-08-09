import numpy as np
from datetime import date

from fake_data_app.sensor import VisitSensor


class StoreSensor:
    def __init__(
        self,
        name: str,
        avg_visit: int,
        std_visit: int,
        perc_malfunction: float = 0,
        perc_break: float = 0,
    ) -> None:
        """Initialize a store"""
        self.name = name
        self.sensors = list()

        # to always get the same result when asking for the same store
        seed = np.sum(list(self.name.encode("ascii")))
        np.random.seed(seed=seed)

        traffic_percentage = [0.48, 0.30, 0.05, 0.03, 0.01, 0.02, 0.10, 0.01]
        np.random.shuffle(traffic_percentage)

        for i in range(8):
            sensor = VisitSensor(
                traffic_percentage[i] * avg_visit,
                traffic_percentage[i] * std_visit,
                perc_malfunction,
                perc_break,
            )

            self.sensors.append(sensor)

    def get_sensor_traffic(self, sensor_id: int, business_date: date) -> int:
        return self.sensors[sensor_id].get_visit_count(business_date)

    def get_all_traffic(self, business_date: date) -> int:
        visit = 0
        for i in range(8):
            visit += self.sensors[i].get_visit_count(business_date)
        return visit

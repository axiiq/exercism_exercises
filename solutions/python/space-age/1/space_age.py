class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        years = (self.seconds / 31_557_600)
        years = f"{years:.2f}"
        return float(years)

    def on_mercury(self):
        years = (self.seconds / 31_557_600)
        years = years / 0.2408467
        years = f"{years:.2f}"
        return float(years)

    def on_venus(self):
        years = (self.seconds / 31_557_600)
        years = years / 0.61519726
        years = f"{years:.2f}"
        return float(years)

    def on_mars(self):
        years = (self.seconds / 31_557_600)
        years = years / 1.8808158
        years = f"{years:.2f}"
        return float(years)

    def on_jupiter(self):
        years = (self.seconds / 31_557_600)
        years = years / 11.862615
        years = f"{years:.2f}"
        return float(years)

    def on_saturn(self):
        years = (self.seconds / 31_557_600)
        years = years / 29.447498
        years = f"{years:.2f}"
        return float(years)

    def on_uranus(self):
        years = (self.seconds / 31_557_600)
        years = years / 84.016846
        years = f"{years:.2f}"
        return float(years)

    def on_neptune(self):
        years = (self.seconds / 31_557_600)
        years = years / 164.79132
        years = f"{years:.2f}"
        return float(years)
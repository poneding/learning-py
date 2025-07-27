# %%
class Time:
    def __init__(self, hours, minutes, seconds) -> None:
        total_seconds = hours * 3600 + minutes * 60 + seconds
        total_minutes, self.seconds = divmod(total_seconds, 60)
        self.hours, self.minutes = divmod(total_minutes, 60)

    @classmethod
    def from_seconds(cls, seconds: int):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return cls(hours, minutes, seconds)

    def __str__(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __add__(self, other):
        if isinstance(other, Time):
            total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) + (
                other.hours * 3600 + other.minutes * 60 + other.seconds
            )
            return Time.from_seconds(total_seconds)
        raise TypeError("Unsupported type for addition")

    def __sub__(self, other):
        if isinstance(other, Time):
            total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) - (
                other.hours * 3600 + other.minutes * 60 + other.seconds
            )
            return Time.from_seconds(total_seconds)
        raise TypeError("Unsupported type for subtraction")

    def __eq__(self, other):
        if isinstance(other, Time):
            return (
                self.hours == other.hours
                and self.minutes == other.minutes
                and self.seconds == other.seconds
            )
        return False


t1 = Time(2, 30, 45)
t2 = Time(1, 15, 30)
t3 = t1 + t2
print(f"Time 1: {t1}")
print(f"Time 2: {t2}")
print(f"Time 1 + Time 2: {t3}")

# %%

from datetime import datetime

from entities.professional import Professional


professional = Professional(
        1,
        "Dr. Juan Pérez",
        "Dermatology",
        {
            "monday": ["09:00-12:00", "14:00-18:00"],
            "tuesday": ["09:00-13:00"],
            "wednesday": ["10:00-16:00"]
        },
        30
    )


datetime_slot = datetime(2026, 5, 18, 10, 0)

time_str = datetime_slot.strftime("%H:%M")
time = datetime.strptime(time_str, "%H:%M")

print(time_str)
print(time)
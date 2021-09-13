# CHOICES IN MODELS

MALE = "male"
FEMALE = "female"

GENDER_CHOICES = (
    (MALE, "Male"),
    (FEMALE, "Female"),
)

ADMIN = "admin"
CUSTOMER = "customer"
DRIVER = "driver"

USER_TYPE_CHOICES = (
    (ADMIN, "Admin"),
    (CUSTOMER, "Customer"),
    (DRIVER, "Driver"),
)

REQUESTED = "requested"
IN_PROGRESS = "in_progess"
DELIVERED = "delivered"
CANCELLED = "cancelled"
STATE_CHOICES_OF_TRIP = (
    (REQUESTED, "Requested"),
    (IN_PROGRESS, "In Progress"),
    (DELIVERED, "Delivered"),
    (CANCELLED, "Cancelled"),
)

RATE_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

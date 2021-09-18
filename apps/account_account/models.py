import uuid

from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import gettext_lazy as _
from parler.models import TranslatableModel
from rest_framework.exceptions import ValidationError

from apps.account_account.managers import UserManager


class CustomUser(AbstractUser):
    MALE = "male"
    FEMALE = "female"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    full_name = models.CharField(_("full name"), max_length=250, blank=True)
    dob = models.DateField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=15, null=True)
    phone = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        unique=True,
        error_messages={"unique": _("A user with that phone already exists.")},
    )
    email = models.EmailField(_("email address"), null=True, blank=True)
    phone_verification_code = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=f"user_profile_image/", null=True, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    password_ceria=models.CharField(max_length=20, null=True, blank=True)
    passport_issue_date=models.DateField(null=True, blank=True)
    passport_expire_date=models.DateField(null=True, blank=True)

    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    registration_address = models.CharField(max_length=300, null=True)
    registration_lat = models.CharField(max_length=100, null=True)
    registration_long = models.CharField(max_length=100, null=True)

    objects = UserManager()


    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_phone(self):
        return str(self.phone).replace("+998", "")


class Cashilok(models.Model):
    owner = models.OneToOneField(
        CustomUser, related_name="cashelok", on_delete=models.CASCADE
    )
    money = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if self.money < 0:
            raise ValidationError({"error": "amount of money cannot be negative"})
        # if self.money

        super(Cashilok, self).save(*args, **kwargs)


class CashilokFill(models.Model):
    STATE_AVAILABLE = 0
    STATE_WAITING_PAY = 1
    STATE_PAY_ACCEPTED = 2
    STATE_CANCELLED = 3

    PAYMENT_STATUS = (
        (STATE_AVAILABLE, "ORDER TUSHDI"),
        (STATE_WAITING_PAY, "TO'LOVNI KUTYAPTI"),
        (STATE_PAY_ACCEPTED, "TO'L0V QABUL QILINDI"),
        (STATE_CANCELLED, "QOLDIRILDI"),
    )
    CLICK = "click"
    PAYME = "payme"
    ON_HAND = "on_hand"

    PAYMENT_METHOD_CHOICES = ((CLICK, "Click"), (PAYME, "Payme"), (ON_HAND, "On hand"))

    owner = models.ForeignKey(
        CustomUser, related_name="cashelok_fills", on_delete=models.CASCADE
    )
    effected_to_cashelok = models.BooleanField(default=False)
    amount = models.FloatField(default=0)
    state = models.IntegerField(choices=PAYMENT_STATUS, default=STATE_AVAILABLE)
    payment_method = models.CharField(
        max_length=30, null=True, choices=PAYMENT_METHOD_CHOICES
    )
    created = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=CustomUser)
def create_user_cashilok(sender, instance, created, **kwargs):
    if created:
        Cashilok.objects.create(owner=instance)


@receiver(post_save, sender=CustomUser)
def save_user_cashelok(sender, instance, **kwargs):
    try:
        instance.cashelok.save()
    except Exception:
        print("error")

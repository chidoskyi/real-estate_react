from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField # type: ignore
from phonenumber_field.modelfields import PhoneNumberField # type: ignore
from apps.common.models import TimeStampedUUIDModel


User = get_user_model()

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name=_('Phone Number'), max_length=30, default="+41524204242")
    about_me = models.TextField(verbose_name=_("About Me"), default="say something about yourself")
    licence = models.CharField(verbose_name=_("Real Estate Licence"), max_length=250, blank=True, null=True)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"), default="profile_default.jpg")
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=50)
    country = CountryField(verbose_name=_("Country"), default="NG", blank=False, null=False)
    city = models.CharField(verbose_name=_("City"), default="NIGERIA", max_length=250, blank=False, null=False)
    is_buyer = models.BooleanField(verbose_name=_("Buyer"), default=False, help_text=_("Are You Looking For Where to Buy a Property"))
    is_seller = models.BooleanField(verbose_name=_("Seller"), default=False, help_text=_("Are You Looking to sell a Property"))
    is_agent = models.BooleanField(verbose_name=_("Agent"), default=False, help_text=_("Are You An Agent?"))
    top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False)
    ratings = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(verbose_name=_("Number of Reviews"), default=0, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"

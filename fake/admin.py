from django.contrib import admin, messages
# from django.utils.translation import gettext_lazy as _
# from .models import Identite
# from faker import Faker
# import random, uuid

# fake = Faker('fr_FR')  # ou 'en_US' selon la langue que tu veux


# @admin.register(Identite)
# class IdentiteAdmin(admin.ModelAdmin):
#     list_display = ('id', 'firstName', 'lastName', 'company', 'country', 'email')
#     search_fields = ('firstName', 'lastName', 'company', 'email', 'country')

#     actions = ['generer_identities']

#     @admin.action(description="Générer 10 identités fictives")
#     def generer_identities(self, request, queryset):
#         count = 10
#         for _ in range(count):
#             Identite.objects.create(
#                 guid=uuid.uuid4(),
#                 firstName=fake.first_name(),
#                 lastName=fake.last_name(),
#                 phone=fake.phone_number(),
#                 email=fake.safe_email(),
#                 country=fake.country(),
#                 region=fake.state(),
#                 postalZip=fake.postcode(),
#                 city=fake.city(),
#                 address=fake.street_address(),
#                 position=f"{round(random.uniform(-90, 90), 5)}, {round(random.uniform(-180, 180), 5)}",
#                 company=fake.company(),
#                 publicUrl=fake.url(),
#                 creditCard=fake.credit_card_number(),
#                 cvv=random.randint(100, 999),
#                 pin=random.randint(1000, 9999),
#                 amount=f"${random.randint(100, 9000):,}.00",
#                 cars=random.randint(0, 7),
#                 bio=fake.paragraph(nb_sentences=5)
#             )
#         self.message_user(request, _(f"{count} identités fictives ont été générées avec succès ✅"), messages.SUCCESS)

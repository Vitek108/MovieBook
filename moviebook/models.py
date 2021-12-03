from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Zanr(models.Model):
    nazev_zanru = models.CharField(max_length=80)

    def __str__(self):
        return "Nazev_zanru: {0}".format(self.nazev_zanru)
    
    class Meta:
        verbose_name="Žánr"
        verbose_name_plural="Žánry"

class Film(models.Model):
    nazev = models.CharField(max_length=200)
    rezie = models.CharField(max_length=180)
    zanr = models.ForeignKey(Zanr, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Nazev: {0} | Rezie: {1}".format(self.nazev, self.rezie)
    
    class Meta:
        verbose_name="Film"
        verbose_name_plural="Filmy"
        

class UzivatelManager(BaseUserManager):
    # Vytvoří uživatele
    def create_user(self, email, password):
        print(self.model)
        if email and password:
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save()
        return user
    # Vytvoří admina
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save()
        return user

"""Model rozšiřuje standardní Django model. V metodě create_user() jste si jistě všimli, že namísto Uzivatel vytváříme self.model. 
Ten v této třídě odkazuje na náš model uživatele, jelikož jsme nastavili objects pro tento manager. Pokud vám pojem objects nic neříká, vzpomeňte si, 
jak jsme v Django interaktivním shellu zobrazovali veškeré filmy uložené v DB Film.objects.all(). U našeho uživatele jen tento manažer přepíšeme 
a tím docílíme toho, že model Uzivatel bude používat náš vlastní manažer."""

class Uzivatel(AbstractBaseUser):

    email = models.EmailField(max_length = 300, unique=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = "uživatel"
        verbose_name_plural = "uživatelé"

    objects = UzivatelManager()

    USERNAME_FIELD = "email"

# Ostatní metody po nás požaduje Django, aby model fungoval:
    def __str__(self): # Vrací textovou reprezentaci uživatele jako jeho email
        return "email: {}".format(self.email)

    @property
    def is_staff(self): # Vrací zda je uživatel administrátor
        return self.is_admin

    def has_perm(self, perm, obj=None): # Metoda zjišťuje, zda má uživatel dané specifické povolení, pro neaktivní uživatele vrací False. My vrátíme vždy True.
        return True

    def has_module_perms(self, app_label):
        return True
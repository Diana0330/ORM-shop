from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('variator', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)

DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    #id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    mileage = models.IntegerField()
    volume = models.FloatField()
    body_type = models.CharField(max_length=20, choices=BODY_TYPE_CHOICES, default='sedan')
    drive_unit = models.CharField(max_length=10, choices=DRIVE_UNIT_CHOICES, default='full')
    gearbox = models.CharField(max_length=20, choices=GEARBOX_CHOICES, default='automatic')
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES, default='gasoline')
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.model} {self.year} {self.color}'


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} {self.car} {self.created_at}'

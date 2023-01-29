from django.contrib import admin
from .models import Prices
from .models import Specifications
from .models import Warehouse
from .models import Issue
from .models import Stocks

# Register your models here.
admin.site.register(Prices)
admin.site.register(Specifications)
admin.site.register(Warehouse)
admin.site.register(Issue)
admin.site.register(Stocks)

"""mercantree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users import views as UserViews
from products import views as ProductViews
from payments import views as PaymentViews
from orders import views as OrderViews

router = routers.DefaultRouter()

router.register(r'users', UserViews.UserViewSet)
router.register(r'products', ProductViews.ProductViewSet)
router.register(r'suppliers', ProductViews.SupplierViewSet)
router.register(r'category', ProductViews.CategoryViewSet)
router.register(r'payments', PaymentViews.PaymentViewSet)
router.register(r'cashregister', PaymentViews.CashRegister)
router.register(r'orders', OrderViews.OrderViewSet)
router.register(r'stock', ProductViews.StockProductViewset)
router.register(r'coupons', OrderViews.CouponViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', UserViews.GetUserToken.as_view())
]

# Smart Home Management System

Hệ thống quản lý nhà thông minh xây dựng trên nền tảng Django và Django REST Framework.

## Cấu trúc dự án

```
SmartHome14_04/
├── backend/                   # Thư mục chính của dự án Django
│   ├── api/                   # App quản lý các models và API chính
│   │   ├── migrations/        # Các file migration của database
│   │   ├── models.py          # Định nghĩa các models chính (Member, Device...)
│   │   ├── serializers.py     # Serializers cho các model
│   │   ├── views.py           # API views cho các models
│   │   └── urls.py            # URL routing cho app api
│   ├── auth_api/              # App xử lý xác thực user
│   │   ├── serializers.py     # Serializers cho đăng ký, đăng nhập
│   │   ├── views.py           # Views xử lý đăng nhập, đăng ký, đăng xuất
│   │   └── urls.py            # URL định tuyến cho các API xác thực
│   ├── backend/               # Cấu hình chính của dự án
│   │   ├── settings.py        # Cấu hình Django
│   │   └── urls.py            # URL định tuyến chính
│   └── manage.py              # Công cụ quản lý Django
├── env/                       # Môi trường ảo Python
└── requirements.txt           # Các thư viện cần thiết
```

## App chính và chức năng

### 1. App `api`

App chính chứa các model và API endpoints để quản lý thiết bị, thành viên và phân quyền trong hệ thống nhà thông minh.

#### Models

- **Member**: Mô hình người dùng tùy chỉnh kế thừa từ AbstractBaseUser và PermissionsMixin

  ```python
  class Member(AbstractBaseUser, PermissionsMixin):
      username = models.CharField(max_length=150, unique=True)
      email = models.EmailField(unique=True)
      phone = models.CharField(max_length=15, null=True, blank=True)
      avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
      is_active = models.BooleanField(default=True)
      is_staff = models.BooleanField(default=False)
      # ...
  ```

- **Device**: Mô hình quản lý thiết bị nhà thông minh

  ```python
  class Device(models.Model):
      name = models.CharField(max_length=100)  # Tên thiết bị
      device_type = models.CharField(max_length=50)  # Loại thiết bị (đèn, quạt...)
      room = models.CharField(max_length=100)  # Phòng chứa thiết bị
      status = models.BooleanField(default=False)  # Trạng thái (bật/tắt)
      last_updated = models.DateTimeField(auto_now=True)  # Thời điểm cập nhật gần nhất
      # ...
  ```

- **DevicePermission**: Mô hình quản lý phân quyền điều khiển thiết bị cho từng thành viên
  ```python
  class DevicePermission(models.Model):
      user = models.ForeignKey(Member, on_delete=models.CASCADE)  # Thành viên
      device = models.ForeignKey(Device, on_delete=models.CASCADE)  # Thiết bị
      can_control = models.BooleanField(default=False)  # Quyền điều khiển
      # ...
  ```

#### Views

- **DeviceViewSet**: CRUD operations cho thiết bị
- **MemberViewSet**: CRUD operations cho thành viên
- **DevicePermissionViewSet**: CRUD operations cho phân quyền thiết bị

#### URLs

```python
# api/urls.py
from rest_framework import routers
from .views import DeviceViewSet, MemberViewSet, DevicePermissionViewSet

router = routers.DefaultRouter()
router.register('devices', DeviceViewSet)
router.register('members', MemberViewSet)
router.register('permissions', DevicePermissionViewSet)

urlpatterns = router.urls
```

### 2. App `auth_api`

App xử lý xác thực người dùng, bao gồm đăng ký, đăng nhập và đăng xuất.

#### Views

- **RegisterView**: Xử lý đăng ký thành viên mới

  ```python
  class RegisterView(generics.CreateAPIView):
      permission_classes = [permissions.AllowAny]
      serializer_class = RegisterSerializer
      # ...
  ```

- **LoginView**: Xử lý đăng nhập và trả về token xác thực

  ```python
  class LoginView(APIView):
      permission_classes = [permissions.AllowAny]
      # ...
  ```

- **LogoutView**: Xử lý đăng xuất và vô hiệu hóa token
  ```python
  class LogoutView(APIView):
      permission_classes = [permissions.IsAuthenticated]
      # ...
  ```

#### URLs

```python
# auth_api/urls.py
from django.urls import path
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
```

### 3. Cấu hình URL chính

```python
# backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),                # Django admin
    path("api/", include("api.urls")),              # API endpoints
    path("auth/", include("auth_api.urls")),        # Auth endpoints
]
```

## API Endpoints

### Xác thực

- **POST** `/auth/register/` - Đăng ký người dùng mới
- **POST** `/auth/login/` - Đăng nhập và nhận token
- **POST** `/auth/logout/` - Đăng xuất (hủy token)

### Thiết bị

- **GET** `/api/devices/` - Lấy danh sách thiết bị
- **POST** `/api/devices/` - Thêm thiết bị mới
- **GET** `/api/devices/{id}/` - Xem chi tiết thiết bị
- **PUT** `/api/devices/{id}/` - Cập nhật thiết bị
- **DELETE** `/api/devices/{id}/` - Xóa thiết bị

### Thành viên

- **GET** `/api/members/` - Lấy danh sách thành viên
- **POST** `/api/members/` - Thêm thành viên mới
- **GET** `/api/members/{id}/` - Xem chi tiết thành viên
- **PUT** `/api/members/{id}/` - Cập nhật thành viên
- **DELETE** `/api/members/{id}/` - Xóa thành viên

### Phân quyền thiết bị

- **GET** `/api/permissions/` - Lấy danh sách phân quyền
- **POST** `/api/permissions/` - Thêm phân quyền mới
- **GET** `/api/permissions/{id}/` - Xem chi tiết phân quyền
- **PUT** `/api/permissions/{id}/` - Cập nhật phân quyền
- **DELETE** `/api/permissions/{id}/` - Xóa phân quyền

## Best Practices áp dụng trong dự án

1. **Tổ chức dự án theo apps riêng biệt**:

   - `api`: Xử lý các model và API chính của hệ thống
   - `auth_api`: Xử lý xác thực và phân quyền

2. **Sử dụng mô hình người dùng tùy chỉnh** thay vì model User mặc định của Django:

   ```python
   # settings.py
   AUTH_USER_MODEL = "api.Member"
   ```

3. **Token Authentication** cho API:

   ```python
   # settings.py
   INSTALLED_APPS = [
       # ...
       'rest_framework.authtoken',
   ]
   ```

4. **Serializers riêng biệt** cho từng loại request:

   - Register Serializer
   - Login Serializer
   - Device Serializer
   - Member Serializer

5. **Class-based Views** và **APIView/ViewSet**:

   - Sử dụng ViewSet cho CRUD operations
   - Sử dụng APIView cho các endpoint tùy chỉnh

6. **Permissions** kiểm soát quyền truy cập API:

   ```python
   permission_classes = [permissions.IsAuthenticated]
   ```

7. **Admin Interface** tùy chỉnh:

   ```python
   class MemberAdmin(UserAdmin):
       # Tùy chỉnh giao diện admin
       # ...
   ```

8. **CORS Configuration** cho phép frontend truy cập API:
   ```python
   CORS_ALLOWED_ALL_ORIGINS = True
   ```

## Cài đặt và chạy dự án

1. Clone repository
2. Tạo môi trường ảo Python:
   ```bash
   python -m venv env
   source env/Scripts/activate  # Windows với Git Bash
   ```
3. Cài đặt các dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Di chuyển vào thư mục backend:
   ```bash
   cd backend
   ```
5. Thực hiện migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Tạo superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```
7. Chạy development server:
   ```bash
   python manage.py runserver
   ```

## Công nghệ sử dụng

- **Django 5.2**: Framework phát triển web
- **Django REST Framework 3.16**: Xây dựng RESTful API
- **django-cors-headers 4.7**: Cấu hình CORS
- **SQLite**: Database (mặc định)
- **Token Authentication**: Xác thực API

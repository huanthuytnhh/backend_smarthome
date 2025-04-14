# Hướng Dẫn Cài Đặt và Sử Dụng API Django

## 1. Cài Đặt Dự Án Django

### Các Bước Thực Hiện:

1. **Tạo Môi Trường Ảo**:

   ```bash
   python -m venv env
   ```

2. **Kích Hoạt Môi Trường Ảo**:

   - **Command Prompt (cmd):**
     ```cmd
     env\Scripts\activate.bat
     ```
   - **PowerShell:**
     ```powershell
     .\env\Scripts\Activate.ps1
     ```
   - **Git Bash:**
     ```bash
     source env/Scripts/activate
     ```

3. **Cài Đặt Các Thư Viện Cần Thiết**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Tạo Dự Án Django Mới**:

   ```bash
   django-admin startproject backend
   ```

5. **Di Chuyển Vào Thư Mục Dự Án**:

   ```bash
   cd backend
   ```

6. **Tạo Ứng Dụng Django Mới**:
   ```bash
   python manage.py startapp api
   ```

---

## 2. Chỉnh Sửa `settings.py`

### Các Tính Năng Đã Thêm:

1. **Biến Môi Trường**:

   - Tích hợp `python-dotenv` để tải các biến môi trường bằng `load_dotenv()`.

2. **Cấu Hình CORS**:

   ```python
   CORS_ALLOWED_ALL_ORIGINS = True
   CORS_ALLOW_CREDENTIALS = True
   ```

3. **Ứng Dụng Đã Cài Đặt**:

   ```python
   INSTALLED_APPS = [
       ...existing apps...
       'api',
       'rest_framework',
       'corsheaders',
   ]
   ```

4. **Middleware**:

   ```python
   MIDDLEWARE = [
       'corsheaders.middleware.CorsMiddleware',
       ...existing middleware...
   ]
   ```

5. **Cấu Hình Mô Hình Người Dùng Tùy Chỉnh**:
   ```python
   AUTH_USER_MODEL = 'api.Member'
   ```

---

## 3. Chạy Máy Chủ

### Các Bước Thực Hiện:

1. **Tạo Migrations**:

   ```bash
   python manage.py makemigrations
   ```

2. **Áp Dụng Migrations**:

   ```bash
   python manage.py migrate
   ```

3. **Chạy Máy Chủ Phát Triển**:
   ```bash
   python manage.py runserver
   ```

---

## 4. Kiểm Tra API Bằng Postman

### **API Thiết Bị**

#### **Tạo Thiết Bị**

1. **Phương Thức**: `POST`
2. **URL**: `http://127.0.0.1:8000/api/devices/`
3. **Headers**:
   - `Content-Type`: `application/json`
4. **Body** (JSON):
   ```json
   {
     "name": "Smart Light",
     "device_type": "Light",
     "room": "Living Room",
     "status": true
   }
   ```

#### **Xem Tất Cả Thiết Bị**

1. **Phương Thức**: `GET`
2. **URL**: `http://127.0.0.1:8000/api/devices/`

#### **Xóa Thiết Bị**

1. **Phương Thức**: `DELETE`
2. **URL**: `http://127.0.0.1:8000/api/devices/<id>/`

---

### **API Thành Viên**

#### **Tạo Thành Viên**

1. **Phương Thức**: `POST`
2. **URL**: `http://127.0.0.1:8000/api/members/`
3. **Headers**:
   - `Content-Type`: `application/json`
4. **Body** (JSON):
   ```json
   {
     "username": "johndoe",
     "email": "john@example.com",
     "phone": "1234567890",
     "password": "securepassword",
     "avatar": null,
     "is_active": true
   }
   ```

#### **Xem Tất Cả Thành Viên**

1. **Phương Thức**: `GET`
2. **URL**: `http://127.0.0.1:8000/api/members/`

#### **Chỉnh Sửa Thành Viên**

1. **Phương Thức**: `PUT`
2. **URL**: `http://127.0.0.1:8000/api/members/<id>/`
3. **Headers**:
   - `Content-Type`: `application/json`
4. **Body** (JSON):
   ```json
   {
     "username": "johndoe",
     "email": "john@example.com",
     "phone": "9876543210",
     "avatar": null,
     "is_active": true
   }
   ```

#### **Xóa Thành Viên**

1. **Phương Thức**: `DELETE`
2. **URL**: `http://127.0.0.1:8000/api/members/<id>/`

---

### **API Phân Quyền Thiết Bị**

#### **Tạo Phân Quyền**

1. **Phương Thức**: `POST`
2. **URL**: `http://127.0.0.1:8000/api/permissions/`
3. **Headers**:
   - `Content-Type`: `application/json`
4. **Body** (JSON):
   ```json
   {
     "user_id": 1,
     "device_id": 1,
     "can_control": true
   }
   ```

#### **Xem Tất Cả Phân Quyền**

1. **Phương Thức**: `GET`
2. **URL**: `http://127.0.0.1:8000/api/permissions/`

#### **Xóa Phân Quyền**

1. **Phương Thức**: `DELETE`
2. **URL**: `http://127.0.0.1:8000/api/permissions/<id>/`

---

## 5. Các Vấn Đề Thường Gặp và Cách Khắc Phục

### **Lỗi: `no such table: api_device`**

- Chạy các lệnh sau:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

### **Lỗi: `Invalid pk "2" - object does not exist.`**

- Đảm bảo `user_id` hoặc `device_id` tồn tại trong cơ sở dữ liệu.
- Sử dụng bảng điều khiển Django admin để kiểm tra hoặc tạo các đối tượng cần thiết.

### **Lỗi: `It is impossible to add a non-nullable field.`**

- Thêm giá trị mặc định vào trường trong `models.py` hoặc cung cấp giá trị mặc định một lần trong quá trình migration.
- Khi xuất hiện lời nhắc, chọn tùy chọn 1 và cung cấp giá trị mặc định.

### **Lỗi: `IntegrityError: FOREIGN KEY constraint failed`**

- Thường xuất hiện khi cố gắng sửa đổi hoặc xóa đối tượng đang được tham chiếu bởi đối tượng khác.
- Xảy ra khi thiết lập mô hình `Member` tùy chỉnh không đúng cách.
- **Cách khắc phục**:
  1. Đảm bảo mô hình `Member` kế thừa đúng cách từ `AbstractBaseUser` và `PermissionsMixin`
  2. Thêm trường `is_superuser` vào mô hình `Member`
  3. Cập nhật phương thức `create_superuser` để không sử dụng `is_admin`
  4. Xóa cơ sở dữ liệu cũ và tạo lại migrations
  ```bash
  cd "backend" && rm -f db.sqlite3 && rm -f api/migrations/0*.py
  python manage.py makemigrations
  python manage.py migrate
  ```

### **Lỗi: `AlreadyRegistered: The model Device is already registered`**

- Lỗi xảy ra khi đăng ký mô hình với Django admin nhiều lần
- **Cách khắc phục**: Đảm bảo mỗi mô hình chỉ được đăng ký một lần trong tệp `admin.py`

### **Lỗi trong Form Admin khi Tạo Thành Viên**

- **Vấn đề**: Không thể tạo người dùng mới thông qua giao diện admin Django
- **Cách khắc phục**:
  1. Sửa `admin.py` để sử dụng `UserAdmin` cho mô hình `Member`
  2. Cấu hình lại `add_fieldsets` để sử dụng `password1` và `password2` thay vì một trường `password` duy nhất
  3. Cập nhật `serializers.py` để xử lý đúng trường `password` với hàm băm

---

## 6. Các Gói Đã Cài Đặt

- **Django==5.2**
- **djangorestframework==3.16.0**
- **django-cors-headers==4.7.0**
- **python-dotenv==1.1.0**
- **Pillow==11.2.1**

---

## 7. Tùy Chỉnh Admin Django

### Đăng Ký Mô Hình Với Admin

```python
# api/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Device, DevicePermission, Member


class MemberAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "phone",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    search_fields = ("username", "email", "phone")
    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("email", "phone", "avatar")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "phone",
                    "password1",
                    "password2",
                ),
            },
        ),
    )


admin.site.register(Member, MemberAdmin)
admin.site.register(Device)
admin.site.register(DevicePermission)
```

### Tùy Chỉnh Serializer cho Mô Hình Member

```python
# api/serializers.py
class MemberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Member
        fields = ('id', 'username', 'email', 'phone', 'avatar', 'is_active', 'is_staff', 'is_superuser', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
```

Hướng dẫn này tóm tắt cách cài đặt và sử dụng dự án Django và các API của nó, cùng với các vấn đề thường gặp và cách khắc phục. Hãy cho tôi biết nếu bạn cần hỗ trợ thêm!

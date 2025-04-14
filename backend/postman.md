# Postman Collection: Django_SmartHome_API

## 🗂️ **Django_SmartHome_API**

---

### 🔐 **Auth (Xác thực)**

Chứa các API liên quan đến đăng nhập, đăng ký và đăng xuất người dùng.

- **POST** `/auth/login`  
  Đăng nhập để nhận token.
- **POST** `/auth/register`  
  Đăng ký người dùng.
- **POST** `/auth/logout`  
  Đăng xuất người dùng.

---

### 💡 **Devices (Thiết bị)**

Quản lý các thiết bị trong hệ thống nhà thông minh.

- **GET** `/api/devices/`  
  Lấy danh sách thiết bị.
- **GET** `/api/devices/{id}/`  
  Lấy thông tin thiết bị theo ID.
- **POST** `/api/devices/`  
  Tạo mới thiết bị.
- **PUT** `/api/devices/{id}/`  
  Cập nhật thiết bị.
- **DELETE** `/api/devices/{id}/`  
  Xóa thiết bị.

---

### 🧑 **Members (Thành viên)**

Quản lý thông tin các thành viên trong hệ thống.

- **GET** `/api/members/`  
  Lấy danh sách thành viên.
- **GET** `/api/members/{id}/`  
  Lấy thông tin thành viên theo ID.
- **POST** `/api/members/`  
  Tạo thành viên mới.
- **PUT** `/api/members/{id}/`  
  Cập nhật thông tin thành viên.
- **DELETE** `/api/members/{id}/`  
  Xóa thành viên.

---

### 🛡️ **Permissions (Phân quyền thiết bị)**

Gán quyền điều khiển thiết bị cho từng thành viên.

- **GET** `/api/permissions/`  
  Lấy danh sách quyền điều khiển.
- **GET** `/api/permissions/member/{member_id}/`  
  Lấy quyền theo thành viên.
- **POST** `/api/permissions/`  
  Gán quyền cho thành viên.
- **PUT** `/api/permissions/member/{member_id}/`  
  Cập nhật quyền cho thành viên.
- **DELETE** `/api/permissions/{id}/`  
  Xóa quyền điều khiển.

---

### 🏠 **Rooms (Phòng)**

Quản lý các phòng trong nhà để gán thiết bị.

- **GET** `/api/rooms/`  
  Lấy danh sách phòng.
- **POST** `/api/rooms/`  
  Tạo phòng mới.
- **DELETE** `/api/rooms/{id}/`  
  Xóa phòng.

---

### 🙍‍♂️ **Profile (Thông tin cá nhân)**

Xem và chỉnh sửa thông tin người dùng hiện tại.

- **GET** `/api/profile/`  
  Xem thông tin cá nhân.
- **PUT** `/api/profile/`  
  Cập nhật thông tin cá nhân.

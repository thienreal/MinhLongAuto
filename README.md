# MinhLongAuto
## Mục đích dự án
Dự án xây dựng hệ thống ERP hỗ trợ cho một doanh nghiệp gia đình nhỏ hoạt động trong lĩnh vực gara sửa xe ô tô. Mục tiêu là quản lý toàn bộ quy trình vận hành, tối ưu hóa hoạt động, nâng cao hiệu quả và trải nghiệm khách hàng, tận dụng Odoo 19 và các giải pháp AI hiện đại.

Postgres server (development): 127.0.0.1:5432
- Default database used for this workspace: MinhLongAuto
- DB user: codespace (see `odoo.conf` for credentials)

## Kế hoạch và các bước thực hiện
1. Xác định nhu cầu và quy trình nghiệp vụ gara: quản lý khách hàng, xe, lịch sửa chữa, kho phụ tùng, hóa đơn, nhân sự, báo cáo tài chính, chăm sóc khách hàng.
2. Lên danh sách các module Odoo cần dùng: base, web, mail, crm, sale, purchase, inventory, account, hr, project, các module tùy chỉnh cho gara ô tô, AI hỗ trợ chẩn đoán lỗi, dự báo tồn kho, chatbot.
3. Phân công công việc cho team 3 người: 1 kỹ thuật Odoo, 1 AI, 1 nghiệp vụ/kiểm thử/tài liệu.
4. Chuẩn bị môi trường: cài đặt Odoo 19, PostgreSQL, thiết lập repo, quy trình làm việc, tài liệu hóa.
5. Phát triển và cấu hình hệ thống: cấu hình module chuẩn, phát triển module tùy chỉnh, tích hợp AI.
6. Kiểm thử và đào tạo: kiểm thử chức năng, hiệu năng, bảo mật, đào tạo người dùng cuối.
7. Triển khai thực tế và hỗ trợ vận hành: đưa hệ thống vào sử dụng, hỗ trợ, bảo trì, cập nhật tính năng mới.

## Lưu ý tích hợp AI
- Chọn bài toán AI phù hợp: nhận diện lỗi xe qua ảnh, dự báo nhu cầu phụ tùng, chatbot hỗ trợ khách hàng.
- Sử dụng dịch vụ AI có sẵn hoặc tự huấn luyện mô hình.
- Đảm bảo dữ liệu đầu vào đủ chất lượng.

## Cấu trúc thư mục chính
- `odoo19/`: Mã nguồn Odoo 19 (nhánh 19.0)
- `custom_addons/`: Chứa các addon tùy chỉnh
- `odoo.conf`: File cấu hình Odoo
- `copilot-instruction`: Hướng dẫn sử dụng cho GitHub Copilot

## Thông tin cấu hình database
- Odoo sử dụng user `codespace` và password `codespace` để kết nối PostgreSQL (xem odoo.conf: db_user, db_password).

## Chức năng chính của hệ thống MinhLongAuto
- Tab Bảng điều khiển: Hiển thị tổng quan hệ thống (nội dung sẽ bổ sung sau).
- Tab Sản phẩm: Hiển thị danh sách sản phẩm, vật phẩm của gara (dùng module inventory, product).
- Tab Báo giá: Quản lý, tạo mới, in báo giá cho các công việc đã làm (dùng module sale, invoice).
- Tab Khách hàng: Quản lý danh sách khách hàng (dùng module contact), quản lý thông tin phương tiện (cần phát triển mới).

## Các module Odoo yêu cầu
- contact
- sale
- inventory
- web
- invoice

## Phần cần phát triển mới
## Phần cần phát triển mới
- Module MinhLongAuto: giao diện 3 tab (Sản phẩm, Báo giá, Khách hàng), quản lý thông tin phương tiện (xe) của khách hàng, các quy trình đặc thù cho gara.
- Đã tạo module MinhLongAuto với cấu trúc cơ bản, giải quyết lỗi External ID not found bằng cách tách actions vào file riêng và sắp xếp thứ tự load.
- Module đã được cài đặt và hoạt động thành công.
- Đã sửa lỗi menu không hiển thị bằng cách thêm thuộc tính groups="base.group_user".
- Đã sửa lỗi module bị kẹt ở trạng thái "installing" bằng cách reset trạng thái trong database.
- Đã sửa lỗi dashboard bằng cách đơn giản hóa view để tránh reference đến các view không tồn tại.

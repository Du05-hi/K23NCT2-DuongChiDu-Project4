/**
 * CYBER-LMS AUTHENTICATION MASTER
 * Developer: Nguyễn Mạnh Tuấn
 */

const LOGIN_API = 'http://127.0.0.1:5000/api/login';

async function performLogin(username, password) {
    try {
        const response = await fetch(LOGIN_API, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (data.status === "success") {
            // 1. Lưu thông tin User vào localStorage
            localStorage.setItem('user', JSON.stringify(data.user));
            
            // 2. Lấy Role và làm sạch dữ liệu
            const role = data.user.role.toString().trim().toLowerCase();

            // 3. PHÂN LUỒNG REDIRECT THÔNG MINH
            if (role === "admin") {
                alert("Chào Admin ! Đang chuyển hướng vào hệ thống quản trị...");
                window.location.href = "../admin/dashboard.html";
            } else {
                alert("Đăng nhập thành công! Chào học viên " + data.user.username);
                
                // Nếu đang ở trang chủ rồi thì chỉ cần reload để hiện Welcome Card
                if (window.location.pathname.includes("index.html") || window.location.pathname === "/") {
                    window.location.reload();
                } else {
                    window.location.href = "../home/index.html";
                }
            }
        } else {
            alert("Lỗi đăng nhập: " + data.message);
        }
    } catch (error) {
        console.error(error);
        alert("Server Python chưa chạy hoặc sai cổng 5000 rồi !");
    }
}
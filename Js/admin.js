/**
 * CYBER-LMS ADMIN MANAGEMENT SYSTEM
 * Developer: Nguyễn Mạnh Tuấn
 */

// 1. KIỂM TRA QUYỀN TRUY CẬP (PROTECT ROUTE)
function checkAdminAccess() {
    const userData = localStorage.getItem("user");
    const user = userData ? JSON.parse(userData) : null;

    // Log ra để Tuấn kiểm tra trong tab Console (F12)
    console.log("--- KIỂM TRA QUYỀN ADMIN ---");
    console.log("Dữ liệu User:", user);

    // Trường hợp chưa đăng nhập
    if (!user) {
        alert(" bạn chưa đăng nhập! Vui lòng đăng nhập để tiếp tục.");
        window.location.href = "../account/login.html";
        return;
    }

    // Kiểm tra role (Xử lý cả lỗi viết hoa/thường và khoảng trắng)
    if (!user.role || user.role.toString().trim().toLowerCase() !== "admin") {
        alert("Dừng lại ! Tài khoản '" + user.username + "' có quyền là '" + (user.role || "không xác định") + "', không phải Admin.");
        window.location.href = "../home/index.html";
    } else {
        console.log("✅ XÁC NHẬN: Chào Admin " + user.username);
    }
}

// 2. HÀM CHUYỂN TRANG
function go(page) {
    window.location.href = page + ".html";
}

// 3. HÀM ĐĂNG XUẤT
function adminLogout() {
    if (confirm("chắc chắn muốn thoát khỏi trang Quản trị không?")) {
        localStorage.removeItem("user");
        window.location.href = "../account/login.html";
    }
}

function loadChart() {
    const ctx = document.getElementById('revenueChart');

    if (!ctx) return;

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['T1','T2','T3','T4','T5','T6'],
            datasets: [{
                label: 'Doanh thu',
                data: [5, 10, 8, 15, 20, 30],
                borderColor: '#00c6ff',
                backgroundColor: 'rgba(0,198,255,0.2)',
                tension: 0.4
            }]
        }
    });
}


// TỰ ĐỘNG CHẠY KIỂM TRA QUYỀN KHI LOAD FILE JS NÀY
document.addEventListener("DOMContentLoaded", function () {
    checkAdminAccess();
    loadChart();
});
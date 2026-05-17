let originalPrice = 1000000;

const coupons = {
    "SALE10": { type: "percent", value: 10 },
    "SALE50": { type: "percent", value: 50 },
    "FREESHIP": { type: "fixed", value: 100000 }
};

function applyCoupon() {
    let code = document.getElementById("couponInput").value.toUpperCase();
    let discount = 0;

    if (!coupons[code]) {
        alert("Mã không hợp lệ!");
        return;
    }

    let c = coupons[code];

    if (c.type === "percent") {
        discount = originalPrice * (c.value / 100);
    } else {
        discount = c.value;
    }

    let final = originalPrice - discount;

    document.getElementById("discount").innerText = format(discount);
    document.getElementById("final").innerText = format(final);
}

function format(num) {
    return num.toLocaleString("vi-VN") + "đ";
}

function goBack() {
    if (confirm("Bạn muốn quay lại?")) {
        window.location.href = "learning.html";
    }
}
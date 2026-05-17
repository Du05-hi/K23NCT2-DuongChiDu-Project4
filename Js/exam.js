function loadQuiz() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");

    const quiz = quizzes[id];

    const container = document.getElementById("quiz");

    if (!quiz) {
        container.innerHTML = "Không tìm thấy bài!";
        return;
    }

    quiz.forEach((item, index) => {
        let html = `
        <div class="question">
            <p>${index + 1}. ${item.q}</p>
        `;

        item.options.forEach((opt, i) => {
            html += `
            <label>
                <input type="radio" name="q${index}" value="${i}">
                ${opt}
            </label>
            `;
        });

        html += `</div>`;

        container.innerHTML += html;
    });

    window.currentQuiz = quiz;
}

function submitQuiz() {
    let score = 0;

    currentQuiz.forEach((q, index) => {
        let selected = document.querySelector(`input[name="q${index}"]:checked`);
        let options = document.querySelectorAll(`input[name="q${index}"]`);

        options.forEach((input, i) => {
            const label = input.parentElement;

            // đúng
            if (i === q.answer) {
                label.style.background = "#2ecc71";
            }

            // sai
            if (selected && parseInt(selected.value) === i && i !== q.answer) {
                label.style.background = "#ff4d6d";
            }
        });

        if (selected && parseInt(selected.value) === q.answer) {
            score++;
        }
    });

    document.getElementById("result").innerHTML =
        `🎯 Điểm của bạn: ${score}/${currentQuiz.length}`;
}

// cập nhật progress khi chọn đáp án
document.addEventListener("change", () => {
    let total = currentQuiz.length;
    let answered = document.querySelectorAll("input[type=radio]:checked").length;

    let percent = (answered / total) * 100;

    document.getElementById("progress").style.width = percent + "%";
});
// ================= TIMER =================
let timeLeft = 300; // 5 phút

function startTimer() {
    let timer = setInterval(() => {
        let minutes = Math.floor(timeLeft / 60);
        let seconds = timeLeft % 60;

        document.getElementById("time").innerText =
            `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;

        timeLeft--;

        if (timeLeft < 0) {
            clearInterval(timer);
            alert("Hết thời gian!");
            submitQuiz();
        }
    }, 1000);
}
// mở modal
function goBack() {
    document.getElementById("confirmModal").style.display = "flex";
}

// đóng modal
function closeConfirm() {
    document.getElementById("confirmModal").style.display = "none";
}

// xác nhận thoát
function confirmExit() {
    window.location.href = "training.html";
}
window.onload = () => {
    loadQuiz();
    startTimer();
};
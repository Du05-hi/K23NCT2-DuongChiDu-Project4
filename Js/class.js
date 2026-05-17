// ================= DATA =================
let lessons = [];
let currentLesson = null;

// ================= LOAD LESSON =================
async function loadLessons() {
    try {
        let res = await fetch("http://127.0.0.1:5001/api/lessons/1");
        let data = await res.json();

        lessons = data;

        let html = "";
        data.forEach(l => {
            html += `
            <div class="lesson-item" onclick="playLesson(${l.id})">
                ▶ ${l.title}
            </div>`;
        });

        document.getElementById("lessonList").innerHTML = html;

    } catch (err) {
        console.error("Lỗi load lessons:", err);
    }
}

// ================= PLAY VIDEO =================
function playLesson(id) {
    currentLesson = lessons.find(l => l.id === id);

    let video = document.getElementById("videoPlayer");
    video.src = currentLesson.video_url;

    // reset bài tập
    document.getElementById("quizBox").style.display = "none";
    document.getElementById("answerInput").value = "";

    // khi video kết thúc → hiện bài tập
    video.onended = showQuiz;
}

// ================= HIỆN BÀI TẬP =================
async function showQuiz() {
    try {
        let res = await fetch(`http://127.0.0.1:5001/api/assignment/${currentLesson.id}`);
        let data = await res.json();

        document.getElementById("quizBox").style.display = "block";
        document.getElementById("question").innerText = data.question;

    } catch (err) {
        console.error("Lỗi load bài tập:", err);
    }
}

// ================= NỘP BÀI =================
async function submitAnswer() {
    let ans = document.getElementById("answerInput").value;

    if (!ans) {
        alert("Nhập đáp án!");
        return;
    }

    let res = await fetch(`http://127.0.0.1:5001/api/assignment/${currentLesson.id}`);
    let data = await res.json();

    if (ans.trim().toLowerCase() === data.answer.trim().toLowerCase()) {
        alert("✅ Đúng rồi!");
    } else {
        alert("❌ Sai rồi!");
    }
}

// ================= ĐIỂM DANH =================
async function checkAttendance() {
    try {
        await fetch("http://127.0.0.1:5001/api/attendance", {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                course_id: 1
            })
        });

        alert("📍 Điểm danh thành công!");
    } catch (err) {
        console.error("Lỗi điểm danh:", err);
    }
}

// ================= INIT =================
loadLessons();
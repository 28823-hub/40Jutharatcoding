<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>StudyFlow - แอปจัดการเวลาและการเรียน</title>

  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: "Segoe UI", Tahoma, sans-serif;
    }

    body {
      background: #f5f7ff;
      color: #1e293b;
    }

    header {
      background: linear-gradient(135deg, #4f46e5, #7c3aed);
      color: white;
      padding: 30px 20px 80px;
    }

    .header-content {
      max-width: 1100px;
      margin: auto;
    }

    header h1 {
      font-size: 30px;
      margin-bottom: 8px;
    }

    header p {
      opacity: .9;
    }

    .container {
      width: min(1100px, 94%);
      margin: -50px auto 40px;
    }

    .dashboard {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 15px;
      margin-bottom: 20px;
    }

    .stat {
      background: white;
      padding: 20px;
      border-radius: 18px;
      box-shadow: 0 8px 25px rgba(0,0,0,.07);
    }

    .stat-icon {
      font-size: 25px;
      margin-bottom: 10px;
    }

    .stat-title {
      color: #64748b;
      font-size: 14px;
    }

    .stat-value {
      font-size: 27px;
      font-weight: bold;
      margin-top: 5px;
    }

    .card {
      background: white;
      padding: 22px;
      border-radius: 20px;
      box-shadow: 0 8px 25px rgba(0,0,0,.06);
      margin-bottom: 20px;
    }

    .card h2 {
      margin-bottom: 18px;
      font-size: 21px;
    }

    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }

    .form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }

    label {
      display: block;
      font-size: 14px;
      font-weight: 600;
      margin-bottom: 6px;
    }

    input,
    select {
      width: 100%;
      padding: 12px;
      border: 1px solid #dbe2ea;
      border-radius: 11px;
      outline: none;
      font-size: 15px;
    }

    input:focus,
    select:focus {
      border-color: #6366f1;
    }

    .full {
      grid-column: 1 / -1;
    }

    button {
      border: none;
      border-radius: 11px;
      padding: 12px 18px;
      cursor: pointer;
      font-weight: bold;
      transition: .2s;
    }

    button:hover {
      transform: translateY(-1px);
    }

    .primary {
      background: #4f46e5;
      color: white;
    }

    .green {
      background: #16a34a;
      color: white;
    }

    .red {
      background: #fee2e2;
      color: #dc2626;
    }

    .gray {
      background: #eef2f7;
      color: #475569;
    }

    /* Tasks */

    .task {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 15px;
      background: #f8fafc;
      border-radius: 14px;
      margin-bottom: 10px;
      border-left: 5px solid #6366f1;
    }

    .task.completed {
      opacity: .55;
      border-left-color: #22c55e;
    }

    .task.completed .task-title {
      text-decoration: line-through;
    }

    .task-title {
      font-weight: bold;
    }

    .task-meta {
      font-size: 13px;
      color: #64748b;
      margin-top: 5px;
    }

    .task-actions {
      display: flex;
      gap: 7px;
    }

    .task-actions button {
      padding: 8px 10px;
    }

    /* Schedule */

    .schedule {
      display: grid;
      gap: 10px;
    }

    .schedule-item {
      display: flex;
      gap: 15px;
      align-items: center;
      padding: 15px;
      border-radius: 14px;
      background: #f8fafc;
    }

    .schedule-time {
      min-width: 90px;
      font-weight: bold;
      color: #4f46e5;
    }

    .subject {
      font-weight: bold;
    }

    .room {
      color: #64748b;
      font-size: 13px;
      margin-top: 3px;
    }

    /* Pomodoro */

    .pomodoro {
      text-align: center;
      padding: 10px;
    }

    .timer {
      font-size: 65px;
      font-weight: bold;
      color: #4f46e5;
      margin: 20px 0;
      letter-spacing: 2px;
    }

    .timer-mode {
      color: #64748b;
      font-weight: bold;
    }

    .timer-buttons {
      display: flex;
      justify-content: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    /* Progress */

    .progress-container {
      background: #e5e7eb;
      height: 12px;
      border-radius: 20px;
      overflow: hidden;
      margin: 12px 0;
    }

    .progress-bar {
      height: 100%;
      background: linear-gradient(90deg, #4f46e5, #8b5cf6);
      width: 0%;
      transition: .3s;
    }

    .goal {
      padding: 15px;
      background: #f8fafc;
      border-radius: 14px;
      margin-bottom: 10px;
    }

    .goal-top {
      display: flex;
      justify-content: space-between;
      font-weight: bold;
    }

    .empty {
      color: #94a3b8;
      text-align: center;
      padding: 25px;
    }

    .week-title {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 15px;
    }

    .today {
      color: #4f46e5;
      font-weight: bold;
    }

    @media (max-width: 800px) {
      .dashboard {
        grid-template-columns: repeat(2, 1fr);
      }

      .grid {
        grid-template-columns: 1fr;
      }

      .form-grid {
        grid-template-columns: 1fr;
      }

      .full {
        grid-column: auto;
      }
    }

    @media (max-width: 500px) {
      .dashboard {
        grid-template-columns: 1fr 1fr;
      }

      header h1 {
        font-size: 24px;
      }

      .timer {
        font-size: 50px;
      }

      .task {
        align-items: flex-start;
        gap: 10px;
      }
    }
  </style>
</head>

<body>

<header>
  <div class="header-content">
    <h1>📚 StudyFlow</h1>
    <p>ผู้ช่วยจัดการเวลาและการเรียนของคุณ</p>
  </div>
</header>

<div class="container">

  <!-- DASHBOARD -->
  <section class="dashboard">

    <div class="stat">
      <div class="stat-icon">📝</div>
      <div class="stat-title">งานทั้งหมด</div>
      <div class="stat-value" id="totalTasks">0</div>
    </div>

    <div class="stat">
      <div class="stat-icon">✅</div>
      <div class="stat-title">ทำเสร็จแล้ว</div>
      <div class="stat-value" id="completedTasks">0</div>
    </div>

    <div class="stat">
      <div class="stat-icon">📖</div>
      <div class="stat-title">วิชาที่เรียน</div>
      <div class="stat-value" id="totalSubjects">0</div>
    </div>

    <div class="stat">
      <div class="stat-icon">⏱️</div>
      <div class="stat-title">เวลาโฟกัส</div>
      <div class="stat-value" id="focusCount">0</div>
    </div>

  </section>


  <div class="grid">

    <!-- ADD TASK -->
    <section class="card">

      <h2>📝 เพิ่มงาน / การบ้าน</h2>

      <div class="form-grid">

        <div class="full">
          <label>ชื่องาน</label>
          <input
            id="taskName"
            type="text"
            placeholder="เช่น ทำการบ้านคณิตศาสตร์"
          >
        </div>

        <div>
          <label>วิชา</label>
          <input
            id="taskSubject"
            type="text"
            placeholder="เช่น คณิตศาสตร์"
          >
        </div>

        <div>
          <label>กำหนดส่ง</label>
          <input
            id="taskDate"
            type="date"
          >
        </div>

        <div>
          <label>ความสำคัญ</label>
          <select id="taskPriority">
            <option value="สูง">🔴 สูง</option>
            <option value="กลาง" selected>🟡 กลาง</option>
            <option value="ต่ำ">🟢 ต่ำ</option>
          </select>
        </div>

        <div style="display:flex;align-items:end;">
          <button class="primary" onclick="addTask()">
            + เพิ่มงาน
          </button>
        </div>

      </div>

    </section>


    <!-- POMODORO -->
    <section class="card">

      <div class="pomodoro">

        <h2>🍅 Focus Timer</h2>

        <div class="timer-mode" id="timerMode">
          เวลาทำงาน
        </div>

        <div class="timer" id="timer">
          25:00
        </div>

        <div class="timer-buttons">

          <button class="primary" onclick="startTimer()">
            ▶ เริ่ม
          </button>

          <button class="gray" onclick="pauseTimer()">
            ⏸ หยุด
          </button>

          <button class="red" onclick="resetTimer()">
            ↻ รีเซ็ต
          </button>

        </div>

        <br>

        <button class="gray" onclick="setBreak()">
          ☕ พัก 5 นาที
        </button>

      </div>

    </section>

  </div>


  <!-- TASK LIST -->
  <section class="card">

    <div class="week-title">
      <h2>📋 งานที่ต้องทำ</h2>

      <button class="gray" onclick="clearCompleted()">
        ลบงานที่เสร็จแล้ว
      </button>
    </div>

    <div id="taskList">
      <div class="empty">
        ยังไม่มีงาน
      </div>
    </div>

  </section>


  <!-- SCHEDULE -->
  <section class="card">

    <h2>🗓️ ตารางเรียนวันนี้</h2>

    <div class="form-grid">

      <div>
        <label>วิชา</label>
        <input id="subjectName" placeholder="เช่น ภาษาอังกฤษ">
      </div>

      <div>
        <label>เวลา</label>
        <input id="subjectTime" type="time">
      </div>

      <div>
        <label>ห้อง / สถานที่</label>
        <input id="subjectRoom" placeholder="เช่น ห้อง 302">
      </div>

      <div style="display:flex;align-items:end;">
        <button class="primary" onclick="addSchedule()">
          + เพิ่มตารางเรียน
        </button>
      </div>

    </div>

    <br>

    <div id="scheduleList" class="schedule">
      <div class="empty">
        ยังไม่มีตารางเรียน
      </div>
    </div>

  </section>


  <!-- GOALS -->
  <section class="card">

    <h2>🎯 เป้าหมายการเรียน</h2>

    <div class="form-grid">

      <div>
        <label>เป้าหมาย</label>
        <input
          id="goalName"
          placeholder="เช่น อ่านหนังสือ 5 ชั่วโมง"
        >
      </div>

      <div>
        <label>จำนวนที่ต้องทำ</label>
        <input
          id="goalTarget"
          type="number"
          min="1"
          placeholder="เช่น 5"
        >
      </div>

      <div>
        <label>ทำไปแล้ว</label>
        <input
          id="goalProgress"
          type="number"
          min="0"
          placeholder="เช่น 2"
        >
      </div>

      <div style="display:flex;align-items:end;">
        <button class="primary" onclick="addGoal()">
          + เพิ่มเป้าหมาย
        </button>
      </div>

    </div>

    <br>

    <div id="goalList"></div>

  </section>


  <!-- RESET -->
  <section class="card" style="text-align:center;">

    <button class="red" onclick="resetAll()">
      🗑️ ล้างข้อมูลทั้งหมด
    </button>

  </section>

</div>


<script>

  /* =========================
     DATA
  ========================= */

  let appData = JSON.parse(
    localStorage.getItem("studyFlowData")
  ) || {
    tasks: [],
    schedules: [],
    goals: [],
    focusSessions: 0
  };


  /* =========================
     SAVE
  ========================= */

  function saveData() {

    localStorage.setItem(
      "studyFlowData",
      JSON.stringify(appData)
    );

  }


  /* =========================
     TASKS
  ========================= */

  function addTask() {

    const name =
      document.getElementById("taskName").value.trim();

    const subject =
      document.getElementById("taskSubject").value.trim();

    const date =
      document.getElementById("taskDate").value;

    const priority =
      document.getElementById("taskPriority").value;

    if (!name) {
      alert("กรุณาใส่ชื่องาน");
      return;
    }

    appData.tasks.push({

      id: Date.now(),

      name: name,

      subject: subject || "ทั่วไป",

      date: date || "-",

      priority: priority,

      completed: false

    });

    saveData();

    document.getElementById("taskName").value = "";
    document.getElementById("taskSubject").value = "";
    document.getElementById("taskDate").value = "";

    render();

  }


  function toggleTask(id) {

    const task =
      appData.tasks.find(t => t.id === id);

    if (!task) return;

    task.completed = !task.completed;

    saveData();

    render();

  }


  function deleteTask(id) {

    appData.tasks =
      appData.tasks.filter(t => t.id !== id);

    saveData();

    render();

  }


  function clearCompleted() {

    appData.tasks =
      appData.tasks.filter(t => !t.completed);

    saveData();

    render();

  }


  function renderTasks() {

    const container =
      document.getElementById("taskList");

    if (appData.tasks.length === 0) {

      container.innerHTML =
        `<div class="empty">ยังไม่มีงาน 🎉</div>`;

      return;

    }

    container.innerHTML = "";

    appData.tasks.forEach(task => {

      let priorityColor = "#f59e0b";

      if (task.priority === "สูง") {
        priorityColor = "#ef4444";
      }

      if (task.priority === "ต่ำ") {
        priorityColor = "#22c55e";
      }

      container.innerHTML += `

        <div
          class="task ${task.completed ? "completed" : ""}"
          style="border-left-color:${priorityColor}"
        >

          <div>

            <div class="task-title">
              ${escapeHTML(task.name)}
            </div>

            <div class="task-meta">

              📚 ${escapeHTML(task.subject)}
              &nbsp; • &nbsp;
              📅 ${task.date === "-" ? "-" : formatDate(task.date)}
              &nbsp; • &nbsp;
              ${task.priority}

            </div>

          </div>

          <div class="task-actions">

            <button
              class="green"
              onclick="toggleTask(${task.id})"
            >
              ${task.completed ? "↩" : "✓"}
            </button>

            <button
              class="red"
              onclick="deleteTask(${task.id})"
            >
              🗑
            </button>

          </div>

        </div>

      `;

    });

  }


  /* =========================
     SCHEDULE
  ========================= */

  function addSchedule() {

    const subject =
      document.getElementById("subjectName").value.trim();

    const time =
      document.getElementById("subjectTime").value;

    const room =
      document.getElementById("subjectRoom").value.trim();

    if (!subject || !time) {

      alert("กรุณากรอกวิชาและเวลา");

      return;

    }

    appData.schedules.push({

      id: Date.now(),

      subject,

      time,

      room: room || "-"

    });

    appData.schedules.sort(
      (a,b) => a.time.localeCompare(b.time)
    );

    saveData();

    document.getElementById("subjectName").value = "";
    document.getElementById("subjectTime").value = "";
    document.getElementById("subjectRoom").value = "";

    render();

  }


  function deleteSchedule(id) {

    appData.schedules =
      appData.schedules.filter(
        item => item.id !== id
      );

    saveData();

    render();

  }


  function renderSchedule() {

    const container =
      document.getElementById("scheduleList");

    if (appData.schedules.length === 0) {

      container.innerHTML =
        `<div class="empty">
          ยังไม่มีตารางเรียน
        </div>`;

      return;

    }

    container.innerHTML = "";

    appData.schedules.forEach(item => {

      container.innerHTML += `

        <div class="schedule-item">

          <div class="schedule-time">
            ${item.time}
          </div>

          <div style="flex:1">

            <div class="subject">
              📚 ${escapeHTML(item.subject)}
            </div>

            <div class="room">
              📍 ${escapeHTML(item.room)}
            </div>

          </div>

          <button
            class="red"
            onclick="deleteSchedule(${item.id})"
          >
            🗑
          </button>

        </div>

      `;

    });

  }


  /* =========================
     GOALS
  ========================= */

  function addGoal() {

    const name =
      document.getElementById("goalName").value.trim();

    const target =
      Number(document.getElementById("goalTarget").value);

    const progress =
      Number(document.getElementById("goalProgress").value);

    if (!name || target <= 0) {

      alert("กรุณากรอกเป้าหมาย");

      return;

    }

    appData.goals.push({

      id: Date.now(),

      name,

      target,

      progress: Math.min(progress || 0, target)

    });

    saveData();

    document.getElementById("goalName").value = "";
    document.getElementById("goalTarget").value = "";
    document.getElementById("goalProgress").value = "";

    render();

  }


  function increaseGoal(id) {

    const goal =
      appData.goals.find(g => g.id === id);

    if (!goal) return;

    if (goal.progress < goal.target) {
      goal.progress++;
    }

    saveData();

    render();

  }


  function deleteGoal(id) {

    appData.goals =
      appData.goals.filter(
        goal => goal.id !== id
      );

    saveData();

    render();

  }


  function renderGoals() {

    const container =
      document.getElementById("goalList");

    if (appData.goals.length === 0) {

      container.innerHTML =
        `<div class="empty">
          ยังไม่มีเป้าหมาย
        </div>`;

      return;

    }

    container.innerHTML = "";

    appData.goals.forEach(goal => {

      const percent =
        Math.min(
          (goal.progress / goal.target) * 100,
          100
        );

      container.innerHTML += `

        <div class="goal">

          <div class="goal-top">

            <span>
              🎯 ${escapeHTML(goal.name)}
            </span>

            <span>
              ${goal.progress}/${goal.target}
            </span>

          </div>

          <div class="progress-container">

            <div
              class="progress-bar"
              style="width:${percent}%"
            ></div>

          </div>

          <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
          ">

            <small>
              ${Math.round(percent)}% สำเร็จ
            </small>

            <div>

              <button
                class="green"
                onclick="increaseGoal(${goal.id})"
              >
                +1
              </button>

              <button
                class="red"
                onclick="deleteGoal(${goal.id})"
              >
                🗑
              </button>

            </div>

          </div>

        </div>

      `;

    });

  }


  /* =========================
     POMODORO
  ========================= */

  let timerSeconds = 25 * 60;

  let timerInterval = null;

  let timerRunning = false;

  let isBreak = false;


  function updateTimer() {

    const minutes =
      Math.floor(timerSeconds / 60);

    const seconds =
      timerSeconds % 60;

    document.getElementById("timer")
      .textContent =
      String(minutes).padStart(2, "0")
      + ":" +
      String(seconds).padStart(2, "0");

  }


  function startTimer() {

    if (timerRunning) return;

    timerRunning = true;

    timerInterval =
      setInterval(() => {

        if (timerSeconds > 0) {

          timerSeconds--;

          updateTimer();

        } else {

          clearInterval(timerInterval);

          timerRunning = false;

          if (!isBreak) {

            appData.focusSessions++;

            saveData();

            alert(
              "🎉 เยี่ยมมาก! คุณโฟกัสครบ 25 นาทีแล้ว"
            );

          } else {

            alert(
              "☕ หมดเวลาพักแล้ว กลับมาเรียนกันต่อ!"
            );

          }

          if (isBreak) {

            timerSeconds = 25 * 60;

            isBreak = false;

            document.getElementById("timerMode")
              .textContent = "เวลาทำงาน";

          } else {

            timerSeconds = 5 * 60;

            isBreak = true;

            document.getElementById("timerMode")
              .textContent = "เวลาพัก";

          }

          updateTimer();

          render();

        }

      }, 1000);

  }


  function pauseTimer() {

    clearInterval(timerInterval);

    timerRunning = false;

  }


  function resetTimer() {

    clearInterval(timerInterval);

    timerRunning = false;

    isBreak = false;

    timerSeconds = 25 * 60;

    document.getElementById("timerMode")
      .textContent = "เวลาทำงาน";

    updateTimer();

  }


  function setBreak() {

    clearInterval(timerInterval);

    timerRunning = false;

    isBreak = true;

    timerSeconds = 5 * 60;

    document.getElementById("timerMode")
      .textContent = "เวลาพัก";

    updateTimer();

  }


  /* =========================
     DASHBOARD
  ========================= */

  function updateDashboard() {

    const total =
      appData.tasks.length;

    const completed =
      appData.tasks.filter(
        task => task.completed
      ).length;

    const subjects =
      new Set(
        appData.schedules.map(
          item => item.subject
        )
      ).size;

    document.getElementById("totalTasks")
      .textContent = total;

    document.getElementById("completedTasks")
      .textContent = completed;

    document.getElementById("totalSubjects")
      .textContent = subjects;

    document.getElementById("focusCount")
      .textContent =
      appData.focusSessions + " รอบ";

  }


  /* =========================
     RESET
  ========================= */

  function resetAll() {

    const confirmReset =
      confirm(
        "ต้องการลบข้อมูลทั้งหมดใช่หรือไม่?"
      );

    if (!confirmReset) return;

    localStorage.removeItem("studyFlowData");

    appData = {
      tasks: [],
      schedules: [],
      goals: [],
      focusSessions: 0
    };

    render();

  }


  /* =========================
     HELPERS
  ========================= */

  function formatDate(date) {

    const d =
      new Date(date + "T00:00:00");

    return d.toLocaleDateString(
      "th-TH",
      {
        day: "numeric",
        month: "short",
        year: "numeric"
      }
    );

  }


  function escapeHTML(text) {

    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");

  }


  /* =========================
     RENDER
  ========================= */

  function render() {

    updateDashboard();

    renderTasks();

    renderSchedule();

    renderGoals();

    updateTimer();

  }


  render();

</script>

</body>
</html>
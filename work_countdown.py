import tkinter as tk
from datetime import datetime, timedelta

# 時間設定（24 小時制）
ON_WORK_HOUR = 9
ON_WORK_MINUTE = 0
LUNCH_START_HOUR = 12
LUNCH_START_MINUTE = 0
LUNCH_END_HOUR = 13
LUNCH_END_MINUTE = 30
OFF_WORK_HOUR = 17
OFF_WORK_MINUTE = 30

def get_time_today(hour, minute):
    now = datetime.now()
    return now.replace(hour=hour, minute=minute, second=0, microsecond=0)

def get_next_day_time(hour, minute):
    return get_time_today(hour, minute) + timedelta(days=1)

def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    if total_seconds < 0:
        total_seconds = 0
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def update_gui():
    now = datetime.now()
    on_work_time = get_time_today(ON_WORK_HOUR, ON_WORK_MINUTE)
    lunch_start = get_time_today(LUNCH_START_HOUR, LUNCH_START_MINUTE)
    lunch_end = get_time_today(LUNCH_END_HOUR, LUNCH_END_MINUTE)
    off_work_time = get_time_today(OFF_WORK_HOUR, OFF_WORK_MINUTE)

    if now < on_work_time:
        remaining = on_work_time - now
        label_var.set(f"⏰ 距離上班 還有：\n{format_duration(remaining)}")
    elif now < lunch_start:
        remaining = lunch_start - now
        label_var.set(f"🍱 距離午休 還有：\n{format_duration(remaining)}")
    elif now < lunch_end:
        remaining = lunch_end - now
        label_var.set(f"☕ 午休結束 還有：\n{format_duration(remaining)}")
    elif now < off_work_time:
        remaining = off_work_time - now
        label_var.set(f"🏁 距離下班 還有：\n{format_duration(remaining)}")
    else:
        next_on_work = get_next_day_time(ON_WORK_HOUR, ON_WORK_MINUTE)
        remaining = next_on_work - now
        label_var.set(f"🌙 距離明天上班 還有：\n{format_duration(remaining)}")

    root.after(1000, update_gui)

# 建立 GUI 視窗
root = tk.Tk()
root.title("上下班＆午休倒數計時器")
root.geometry("300x180")
root.resizable(False, False)

label_var = tk.StringVar(value="載入中…")
label = tk.Label(root, textvariable=label_var, font=("Helvetica", 20), justify="center")
label.pack(expand=True)

update_gui()
root.mainloop()

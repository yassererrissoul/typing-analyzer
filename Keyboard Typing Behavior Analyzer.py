import keyboard
import shutil
import time
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# ========== Console setup ==========
columns = shutil.get_terminal_size().columns
console = Console()

events = []

# ========== Key Logging ==========
def on_key_press(event):
    timestamp = time.time()
    key = event.name
    console.print(f"[dim]Key: {key}, Time: {timestamp}[/dim]")
    events.append((key, timestamp))

keyboard.on_press(on_key_press)

console.print()
console.print(Panel.fit("[bold green]⌨️  Key logging started. Press ESC to stop.[/bold green]", width=columns))

if keyboard.wait('esc'):
    keyboard.unhook_all()

console.print(Panel.fit("[bold red]⛔ Key logging stopped.[/bold red]", width=columns))

# ========== Save Events ==========
events_dicts = []
for key, t in events:
    event_time = datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    events_dicts.append({
        "key": key,
        "time": t,
        "event_time": event_time
    })

with open("key_events.json", "w", encoding="utf-8") as f:
    json.dump(events_dicts, f, ensure_ascii=False, indent=2)

console.print("[green]✔ Key events saved to 'key_events.json'[/green]")

# ========== Load Events ==========
with open("key_events.json", "r", encoding="utf-8") as f:
    loaded_events = json.load(f)

# ========== Inter-key Intervals ==========
inter_key_intervals = []
for i in range(1, len(loaded_events)):
    t_prev = loaded_events[i - 1]["time"]
    t_curr = loaded_events[i]["time"]
    interval = t_curr - t_prev
    inter_key_intervals.append(interval)

console.print("\n[bold cyan]=== 📊 Typing Analysis ===[/bold cyan]\n")

if inter_key_intervals:
    average = sum(inter_key_intervals) / len(inter_key_intervals)
    fastest = min(inter_key_intervals)
    slowest = max(inter_key_intervals)

    console.print(f"⚡ [yellow]- Average interval:[/yellow] [white]{average:.4f} seconds[/white]")
    console.print(f"🚀 [yellow]- Fastest interval:[/yellow] [white]{fastest:.4f} seconds[/white]")
    console.print(f"🐌 [yellow]- Slowest interval:[/yellow] [white]{slowest:.4f} seconds[/white]")
else:
    console.print("[red]No inter-key intervals to analyze.[/red]")

# ========== Total Typing Time ==========
if loaded_events:
    total_time = loaded_events[-1]["time"] - loaded_events[0]["time"]
    console.print(f"[yellow]- Total typing duration:[/yellow] [white]{total_time:.4f} seconds[/white]")
else:
    console.print("[red]No typing data to analyze.[/red]")

# ========== Key Counts ==========
key_counts = {}
for event in loaded_events:
    key = event["key"]
    key_counts[key] = key_counts.get(key, 0) + 1

console.print("\n[bold cyan]=== Key Press Counts ===[/bold cyan]\n")

# Top 5 used keys
sorted_keys = sorted(key_counts.items(), key=lambda x: x[1], reverse=True)

# Display table
table = Table(title="🔢 Key Press Counts", show_lines=True)
table.add_column("Key", justify="center", style="cyan", no_wrap=True)
table.add_column("Count", justify="center", style="magenta")

for key, count in sorted_keys:
    emoji = "⌫" if key == 'backspace' else "🔤"
    table.add_row(f"{emoji} {key}", str(count))

# Backspace count
backspace_count = key_counts.get('backspace', 0)
console.print(f"\n[orange1]- Backspace used:[/orange1] {backspace_count} times\n")

console.print(table)
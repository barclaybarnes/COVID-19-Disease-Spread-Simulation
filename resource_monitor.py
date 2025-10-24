import time
import threading
import csv
import os
import sys
from datetime import datetime

try:
    import psutil
    PSUTIL_AVAILABLE = True
except Exception:
    psutil = None
    PSUTIL_AVAILABLE = False

class ResourceMonitor:
    """
    Samples system/process resource usage at `interval` seconds and writes to CSV.
    Missing metrics are written as 'N/A' (no nulls).
    """
    def __init__(self, interval=0.1, csv_path='resource_usage.csv'):
        self.interval = float(interval)
        self.csv_path = csv_path
        self._stop = threading.Event()
        self._thread = None
        self._samples = []
        self._start_time = None

        if not PSUTIL_AVAILABLE:
            print("Warning: psutil not available — resource fields will be 'N/A'.", file=sys.stderr)

    def _sample_loop(self):
        process = None
        if PSUTIL_AVAILABLE:
            try:
                process = psutil.Process(os.getpid())
            except Exception:
                process = None

        # Warm up cpu counters so first reading is meaningful
        if PSUTIL_AVAILABLE:
            try:
                psutil.cpu_percent(interval=None)
                if process is not None:
                    process.cpu_percent(interval=None)
            except Exception:
                pass

        while not self._stop.is_set():
            ts = time.time()
            cpu = mem = rss = None
            if PSUTIL_AVAILABLE:
                try:
                    cpu = psutil.cpu_percent(interval=None)
                    mem = psutil.virtual_memory().percent
                    rss = process.memory_info().rss if process is not None else None
                except Exception:
                    cpu = mem = rss = None

            # store raw values; will be string-formatted on write
            self._samples.append((ts, cpu, mem, rss))
            time.sleep(self.interval)

    def start(self):
        self._start_time = time.time()
        self._stop.clear()
        self._thread = threading.Thread(target=self._sample_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._stop.set()
        if self._thread:
            self._thread.join()
        self._write_csv()

    def _write_csv(self):
        os.makedirs(os.path.dirname(self.csv_path) or '.', exist_ok=True)
        with open(self.csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp_iso', 'relative_time_s', 'cpu_percent', 'mem_percent', 'rss_bytes'])
            for ts, cpu, mem, rss in self._samples:
                ts_iso = datetime.utcfromtimestamp(ts).isoformat() + 'Z'
                rel = round(ts - (self._start_time or ts), 3)
                cpu_val = f"{cpu:.2f}" if isinstance(cpu, (int, float)) else 'N/A'
                mem_val = f"{mem:.2f}" if isinstance(mem, (int, float)) else 'N/A'
                rss_val = str(rss) if isinstance(rss, (int, float)) else 'N/A'
                writer.writerow([ts_iso, rel, cpu_val, mem_val, rss_val])



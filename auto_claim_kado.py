"""
Macro HOLD E (tahan terus, lepas setiap 3 detik lalu tahan lagi)
- Tekan F6 untuk Start/Stop
- Tutup manual dengan X atau Ctrl+C untuk keluar
"""

import keyboard
import time
import threading

running = False
macro_thread = None

def macro_loop():
    """Loop untuk HOLD E"""
    global running
    while running:
        keyboard.press('e')
        print("[MACRO] HOLD E...")
        time.sleep(3)
        if running:
            keyboard.release('e')
            time.sleep(0.05)
    keyboard.release('e')

def toggle():
    """Toggle start/stop macro"""
    global running, macro_thread
    if running:
        running = False
        print("\n[STOP] Macro berhenti - Tekan F6 untuk mulai lagi")
    else:
        running = True
        macro_thread = threading.Thread(target=macro_loop, daemon=True)
        macro_thread.start()
        print("\n[START] Macro berjalan - HOLD E")

def main():
    print("=" * 40)
    print("    MACRO HOLD E")
    print("=" * 40)
    print("Hotkey: F6 = Start / Stop")
    print("Tutup: Klik X atau Ctrl+C")
    print("=" * 40)
    print("\nTekan F6 untuk mulai...")
    
    # Register hotkey
    keyboard.add_hotkey('f6', toggle)
    
    # Program jalan terus
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    
    # Cleanup saat ditutup
    global running
    running = False
    keyboard.release('e')
    print("\n[EXIT] Program ditutup")

if __name__ == "__main__":
    main()

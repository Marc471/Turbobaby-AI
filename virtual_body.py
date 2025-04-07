# virtual_body.py
import time
from datetime import datetime

class VirtualBody:
    def __init__(self):
        self.hunger = 100
        self.energy = 100
        self.curiosity = 100
        self.decay_rates = {"hunger": 0.1, "energy": 0.05, "curiosity": 0.07}
        self.log = []

    def update(self):
        for need in ["hunger", "energy", "curiosity"]:
            current = getattr(self, need)
            setattr(self, need, max(0, current - self.decay_rates[need]))
        self.log.append({
            "timestamp": datetime.now().isoformat(),
            "hunger": self.hunger,
            "energy": self.energy,
            "curiosity": self.curiosity
        })

if __name__ == "__main__":
    body = VirtualBody()
    print("Virtual Body running...")
    try:
        while True:
            body.update()
            print(f"Status: {body.log[-1]}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nBody stopped.")

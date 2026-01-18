# --- Key state dictionary ---
keys = {"w": False, "s": False, "Up": False, "Down": False}

# --- Event handlers ---
def press_w(): keys["w"] = True
def release_w(): keys["w"] = False

def press_s(): keys["s"] = True
def release_s(): keys["s"] = False

def press_up(): keys["Up"] = True
def release_up(): keys["Up"] = False

def press_down(): keys["Down"] = True
def release_down(): keys["Down"] = False


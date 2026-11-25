# Verified length: 115 characters.
LINE = "fix: I found the bug. It was me. I wrote it at midnight, fixed it at 4 a.m., and left this apology for the next me."
import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

os.makedirs(output_dir, exist_ok=True)

with open(output_path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE))

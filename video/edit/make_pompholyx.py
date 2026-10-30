# Builds pompholyx.html (9:16) from edit/pompholyx_parts.py. See edit/make_page.py.
import subprocess,sys
subprocess.run([sys.executable,'-I','edit/make_page.py','pompholyx','pompholyx.html'],check=True)

"""
Auto-configure sys.path so challenge files can import across directories.

Each challenge lives in its own directory (challenge-1/, challenge-2/, etc.)
but needs to import from other challenges and from shared_models.py at the
workshop root.  Importing this module adds every challenge-* directory and
the workshop root to sys.path.

Usage — add these three lines at the very top of every challenge file,
BEFORE any other imports:

    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import _paths  # noqa: F401
"""

import sys
import os

_workshop_dir = os.path.dirname(os.path.abspath(__file__))

if _workshop_dir not in sys.path:
    sys.path.insert(0, _workshop_dir)

for _name in sorted(os.listdir(_workshop_dir)):
    _path = os.path.join(_workshop_dir, _name)
    if os.path.isdir(_path) and _name.startswith("challenge-") and _path not in sys.path:
        sys.path.insert(0, _path)

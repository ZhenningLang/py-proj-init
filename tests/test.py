import os
import sys

CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(CURRENT_PATH, '..'))

from py_proj_init.__main__ import main  # noqa

main()

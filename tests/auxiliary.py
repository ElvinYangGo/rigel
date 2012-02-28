import os
import sys

parent_path = os.path.join(os.path.dirname(sys.argv[0]), os.pardir)
absolute_parent_path = os.path.abspath(parent_path)
sys.path.append(absolute_parent_path)

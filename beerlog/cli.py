# Basically that's the frontend of beerlog
from .config import settings


# Won't have any business logics
# All business logics will be at core.py file (or base.py in some projects)
def main():
    print("Hello from", settings.NAME)

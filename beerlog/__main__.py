# This file is the entrypoint of python module
# It's importing main function from cli.py file
from .cli import main

# The __variable__ is call "dunder"
# So, __main__ is a "dunder" main
if __name__ == "__main__":
    main() # calling the main function from import

# If we had the arguments on beerlog:
# beerlog add "Brahma" "Pilsen" --flavor=8 --image=2 --cost=9
# We'll need capture these parameters on a specific file   
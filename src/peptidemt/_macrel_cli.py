"""Keep dependency-guard module identities stable when launching with -m."""

from ._macrel_worker import main

if __name__ == "__main__":
    main()

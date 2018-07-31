class Version:
    major: int
    minor: int
    patch: int

    def __init__(self, version_string: str, partial: bool = False) -> None: ...
    def __le__(self, other: Version) -> bool: ...

    @classmethod
    def coerce(cls, version_string: str, partial: bool = False) -> Version: ...

# vim: set filetype=python :

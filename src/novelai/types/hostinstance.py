from pydantic.dataclasses import dataclass


@dataclass(frozen=False, kw_only=True, slots=True)
class HostInstance:
    """
    Hostnames of NovelAI services and corresponding accepted content types.
    """

    url: str
    accept: str

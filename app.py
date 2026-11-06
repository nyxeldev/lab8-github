"""Oddiy konsol dasturi - 8-laboratoriya ishi uchun."""


def greet(name: str) -> str:
    return f"Assalomu alaykum, {name}!"


def farewell(name: str) -> str:
    return f"Xayr, {name}! Ko'rishguncha."


def main() -> None:
    print(greet("dunyo"))
    print(farewell("dunyo"))


if __name__ == "__main__":
    main()

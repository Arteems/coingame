from fastapi import FastAPI
from typing import Literal
import random

app = FastAPI()


def coin_flip():
    coin_choice = ["Орел", "Решка"]
    return random.choice(coin_choice)


@app.get("/user_choice")
def choice_usr(
    choice: Literal[
        "Орел",
        "Решка",
    ]
):
    coin = coin_flip()

    if choice == coin:
        return f"Вы выиграли! Компьютер выбрал {coin}"
    return f"Вы проиграли! Компьютер выбрал {coin}"

import random

HEADS = "heads" 
TAILS = "tails"
COIN_VALUES = [HEADS, TAILS]


def flip_coin():
    return random.choice(COIN_VALUES)


def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int) -> int:
    if starting_funds <= 0 or min_bet <= 0 or max_bet <= 0:
        raise ValueError("Начальные средства, минимальная ставка и максимальная ставка должны быть больше 0")

    step_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet

    while current_funds > 0:
        step_to_loose += 1
        current_funds -= current_bet
        flipped_coin_value = flip_coin()
        if flipped_coin_value == HEADS:
            win = current_bet * 2
            current_funds += win
            current_bet = min_bet
        else:
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = max_bet
            if current_bet > current_funds:
                current_bet = current_funds

    return step_to_loose


def simulate_martingale_for_n_players(
        *,
        starting_funds: int,
        min_bet: int,
        max_bet: int,
        n_games: int
) -> float:
    if n_games <= 0:
        raise ValueError("Количество игр должно быть больше 0")

    total_steps_to_loose = 0
    for i in range(n_games):
        try:
            step_to_loose = play_martingale(
                starting_funds=starting_funds,
                min_bet=min_bet,
                max_bet=max_bet
            )
            total_steps_to_loose += step_to_loose
        except Exception as e:
            print(f"Ошибка во время игры {i+1}: {str(e)}")

    return total_steps_to_loose / n_games


print(
    simulate_martingale_for_n_players(
        n_games=10,
        starting_funds=1000,
        min_bet=1,
        max_bet=100
    )
)

import random

from geocoder import get_ll_span
from mapapi_PG import show_map


def main():
    towns = [
        "Ярославль",
        "Нижний Новгород",
        "Казань",
        "Великий Новгород",
        "Архангельск",
        "Саратов",
        "Петрозаводск",
        "Астрахань"
    ]
    random.shuffle(towns)

    for town in towns:
        # Показываем карту с масштабом, подобранным по заданному объекту.
        ll, spn = get_ll_span(town)
        spn = "0.001,0.001"
        ll_spn = f"ll={ll}&spn={spn}"
        show_map(ll_spn)


if __name__ == "__main__":
    main()

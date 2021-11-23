from lift import Lift


def main_app():
    lift = Lift()
    # Calling the lift on the given floor we want as param
    lift.call_lift(5)


if __name__ == "__main__":
    main_app()

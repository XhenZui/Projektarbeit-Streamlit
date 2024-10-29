import pickle


def save_to_file(obj):
    # list of objects to save
    with open("travel_log_save.pickle", "wb") as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


def read_from_file():
    try:
        with open("travel_log_save.pickle", "rb") as inp:
            return pickle.load(inp)
    except FileNotFoundError:
        return []

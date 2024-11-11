import pickle


def save_to_file(obj):
    with open("travel_log_save.pickle", "wb") as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)


def read_from_file():
    try:
        with open("travel_log_save.pickle", "rb") as inp:
            return pickle.load(inp)
    except Exception:
        return []

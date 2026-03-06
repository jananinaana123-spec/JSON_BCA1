def refine_json(data):

    refined = {}

    for key, value in data.items():

        new_key = key.lower()

        if isinstance(value, dict):
            for sub_key, sub_val in value.items():
                refined[new_key + "_" + sub_key.lower()] = sub_val

        else:
            if isinstance(value, str) and value.isdigit():
                value = int(value)

            refined[new_key] = value

    return refined

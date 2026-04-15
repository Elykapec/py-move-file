import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    try:
        with open(source, "r") as file_in:
            content = file_in.read()
    except FileNotFoundError:
        return

    if destination.endswith("/"):
        dir_path = destination.rstrip("/")
        file_name = os.path.basename(source)
        destination_file = os.path.join(dir_path, file_name)
    else:
        dir_path = os.path.dirname(destination)
        destination_file = destination

    if dir_path:
        parts = dir_path.split("/")
        current_path = ""
        for part in parts:
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(destination_file, "w") as file_out:
        file_out.write(content)

    os.remove(source)

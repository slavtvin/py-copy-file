def copy_file(command: str) -> None:

    first_filename = command.split(" ")[1]
    last_filename = command.split(" ")[2]
    if first_filename == last_filename:
        return
    with (open(first_filename, "r") as file_read,
          open(last_filename, "w") as file_write):
        file_write.write(file_read.read())

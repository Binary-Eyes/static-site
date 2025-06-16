def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        line = line.lstrip("\n").lstrip()
        if line == "":
            continue

        if line[0] == "#" and line[1] != "#":
            return line.lstrip("#").lstrip()
        else:
            raise Exception("main header line was not found in input markdown")

    raise Exception("main header line was not found in input markdown")
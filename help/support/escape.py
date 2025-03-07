def escape(line: str):
    line = line.replace('<', '&lt;')
    line = line.replace('>', '&gt;')
    return line


if __name__ == "__main__":
    print(escape(input()))

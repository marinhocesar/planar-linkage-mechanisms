def write_in_file(filename, text):
    """Writes text in a file."""
    with open(filename, 'w') as f:
        f.write(text)

def append_to_file(filename, text):
    """Writes text in a file."""
    with open(filename, 'a') as f:
        f.write(text)
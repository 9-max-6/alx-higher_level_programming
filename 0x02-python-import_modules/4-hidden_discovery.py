#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4.pyc
    name_def = dir(hidden_4)
    for name in sorted(name_def):
        if name[:2] != "__":
            print(name)

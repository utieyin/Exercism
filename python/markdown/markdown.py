import re


def parse(markdown):
    lines = markdown.split("\n")
    res = ""
    y = ""
    l = ""
    x = ""
    for i in lines:

        if re.match("######", i):
            res += f"<h6>{i[7:]}</h6>"
        elif re.match("##", i):
            res += f"<h2>{i[3:]}</h2>"
        elif re.match("#", i):
            res += f"<h1>{i[2:]}</h1>"
        elif re.match("([*])", i):
            s = bold(i).strip("*").strip()
            y += f"<li>{s}</li>"
            x = f"<ul>{y}</ul>"
        else:
            s = bold(i)
            l += f"<p>{s}</p>"
    return res + x + l


def bold(j):
    if re.search(r"__([\w ]+) | __([\w]+)", j):
        d = re.search(r"__([\w ]+)", j)
        c = double_underscore(d.group())
        j = j.replace(d.group(), c)

    if re.search(r"_([\w ]+)|_([\w]+)", j):
        d = re.search(r"_([\w ]+)_", j)
        c = single_underscore(d.group())
        j = j.replace(d.group(), c)

    return j


def single_underscore(t):
    p = t.strip("_")
    return f"<em>{p}</em>"


def double_underscore(t):
    p = t.strip("_")
    return f"<strong>{p}</strong>"
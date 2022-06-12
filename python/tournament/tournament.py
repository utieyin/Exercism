from collections import defaultdict, OrderedDict


def tally(scores):
    results = defaultdict(lambda: {"WIN": 0, "DRAW": 0, "LOSS": 0})
    table = ["{:30s} | MP |  W |  D |  L |  P".format("Team")]
    for score in scores:
        home, away, result = score.split(";")
        if result == "win":
            results[home]["WIN"] += 1
            results[away]["LOSS"] += 1
        elif result == "draw":
            results[home]["DRAW"] += 1
            results[away]["DRAW"] += 1
        else:
            results[home]["LOSS"] += 1
            results[away]["WIN"] += 1

    for team in results:
        results[team]["MP"] = sum(results[team].values())
        results[team]["POINTS"] = results[team]["WIN"] * 3 + results[team]["DRAW"]

    results = OrderedDict(
        sorted(results.items(), key=lambda x: (-(x[1]["POINTS"]), x[0]))
    )

    for team in results:

        table.append(
            "{:30s} | {:2} | {:2} | {:2} | {:2} | {:2}".format(
                str(team),
                results[team]["MP"],
                results[team]["WIN"],
                results[team]["DRAW"],
                results[team]["LOSS"],
                results[team]["POINTS"],
            )
        )
    return table

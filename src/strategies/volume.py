def volume_score(data):
    volume = data["Volume"]

    last_volume = float(volume.iloc[-1])
    avg_volume = float(volume.rolling(20).mean().iloc[-1])

    if avg_volume == 0:
        return 0

    ratio = last_volume / avg_volume

    if ratio >= 2:
        return 25

    if ratio >= 1.5:
        return 15

    if ratio >= 1.2:
        return 10

    return 0
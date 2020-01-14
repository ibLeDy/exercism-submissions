def recite(start, take=1):
    p1 = 'x bottles of beer on the wall, x bottles of beer.'
    p2 = 'Take one down and pass it around, x bottles of beer on the wall.'

    phrases = []
    for beers in range(start, start - take, -1):
        if beers > 1:
            phrases.append(p1.replace('x', str(beers)))

            if beers - 1 > 1:
                phrases.append(p2.replace('x', str(beers - 1)))
            else:
                phrases.append(
                    'Take one down and pass it around, 1 bottle of beer on the wall.'
                )
        elif beers == 1:
            phrases.append(
                '1 bottle of beer on the wall, 1 bottle of beer.'
            )
            phrases.append(
                'Take it down and pass it around, no more bottles of beer on the wall.'
            )
        else:
            bottles = start - take
            if bottles <= 0:
                bottles = 99
            phrases.append(
                'No more bottles of beer on the wall, no more bottles of beer.'
            )
            phrases.append(
                f'Go to the store and buy some more, {bottles} bottles of beer on the wall.'
            )

        if beers != (start - take) + 1:
            phrases.append("")

    return phrases

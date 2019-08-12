def bottle_of_beer(bob):
    """Prints Bottle of Beer on the Wall Lyrics.

    :param bob: Must be a positive integer.
    """
    if bob < 1:
        print("""No more bottole of beer on the wall.
No more bottle of beer. """)
        return
    tmp = bob
    bob -= 1
    print("""{} bottle of beer on the wall.
{} bottole of beer.
Take one down, pass it around,
{} bottle of beer on the wall.
""".format(tmp,tmp,bob))
    bottle_of_beer(bob)

bottle_of_beer(99)

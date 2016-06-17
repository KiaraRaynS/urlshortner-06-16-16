from hashids import Hashids
hashids = Hashids()


def testhash():
    stringtohash = Hashids(salt="This is a string")
    hashstring = stringtohash.encode(123)
    hashids = Hashids(salt="This is salt")
    hashid = hashids.encode(123)
    print(hashid)
    print(hashstring)

testhash()

import hashlib


def crack_sha1_hash(hash, use_salts=False):

    # store salts for use later
    salt_list = []
    shand = open("known-salts.txt")
    for salt in shand:
        salt = salt.rstrip()
        salt_list.append(salt)
    shand.close()

    # loop through top 10000 passwords
    fhand = open("top-10000-passwords.txt")
    for password in fhand:
        password = password.rstrip()

        # if using salts then loop through those
        if use_salts == True:
            for salt in salt_list:
                # try prepending, appending, and both
                for x in range(0, 2):
                    if x == 0:
                        salted_password = salt + password
                    else:
                        salted_password = password + salt

                    # check password
                    if hash_password(salted_password, hash):
                        fhand.close()
                        return password

        # otherwise just check password
        else:
            if hash_password(password, hash):
                fhand.close()
                return password

    fhand.close()
    return "PASSWORD NOT IN DATABASE"


def hash_password(password, hash):
    passhash = hashlib.sha1(password.encode("utf-8"))
    if passhash.hexdigest() == hash:
        return True

import abilities as ab

def get_response(msg):#~Fixed

    choice = 0
    for i in ab.keyword:
        if choice == 0:
            for j in ab.keyword[i]:
                if j in msg.lower():
                    choice = i
                    key = j #for future purposes like choice 1
                    break
    else:
        for z in ab.nonab_key:
            if choice == 0:
                for j in ab.nonab_key[z]:
                    if j in msg.lower():
                        choice = z
                        break

        if choice == 0:
            if ("how" in msg.lower() or "what" in msg.lower()) and "?" in msg:
                return ab.feeling()
            elif len(msg.lower()) >= 2 and msg.lower()[0] in "hy" and msg.lower().split(" ")[0] != "hear":
                return ab.greeting()

    # Performing the activities

    if choice == 1:

        website = lambda x: (lambda y: ("".join(y[-1])).strip())(x.partition(key))
        ab.search(website(msg.lower()))
        return "Website Opened!!!"

    elif choice == 2:

        song =' '.join(x for x in msg.split(" ") if x not in "listentoplaymusic")
        ab.music(song)
        return "Hope you were able to listen to the music"

    elif choice == 3:

        keys =msg.lower().split(" ")

        try:
            gindex = keys.index("google") + 1
            post = keys[gindex:]
        except:
            sindex = keys.index("search") + 1
            post = keys[sindex:]
        site = ' '.join(x for x in post)
        ab.googlesearch(site)
        return "searched for you!!!"

    elif choice == 4:

        ab.news()
        return "I hope it worked out well and good"

    elif choice == 5:

        return ab.cur_date_time(msg)

    elif choice == 6:

        return ab.byebye()


    elif choice == 7:

        return ab.powers()

    elif choice == 13:

        return ab.gratitude()

    elif choice == 8:

        return ab.create()

    elif choice == 9:

        return ab.add(msg)

    elif choice == 10:

        return ab.delete(msg)

    elif choice == 11:
        return ab.todo()

    elif choice == 12:

        unnec_w =["with","to","into"]
        imp_data=[x for x in msg.split()[msg.lower().split().index(key) + 1:] if x not in unnec_w]
        return ab.mod(imp_data)

    else:

        return ab.dont_know()

def user(first,last,middle = ''):
    if middle:
        ful_name = f"{first} {last} {middle}"
        return ful_name.title()
    else:
        ful_name = f"{first} {last}"
        return ful_name.title()

if __name__ == '__main__':
    test1 =user('al','gene')
    test2 =user('al','gene',"514")
    print(f"{test1} \n{test2}")
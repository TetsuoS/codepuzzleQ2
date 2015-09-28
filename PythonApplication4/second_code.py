class SimpleBars:

    def __init__(self, bar):
        self.bar = bar

    def next(self):
        original_list = list(self.bar)
        new_list = list(original_list)
        for i in range(len(original_list)):
            new_list[i] = ' '

        for i in range(len(original_list)):
            c1 = original_list[i]
            c2 = original_list[(i+1)%len(original_list)]
            c3 = original_list[(i+2)%len(original_list)]
            c4 = (i+1)%len(original_list)
            c5 = (i+2)%len(original_list)

            if c1 == 'i' and c2 == 'T' and c3 == 'i':
                new_list[i+1] = 'i'
            elif c1 == 'i' and c2 == 'T':
                new_list[i+1] = ' '
            elif c1 == 'T' and c2 == 'i':
                new_list[i] = ' '
            elif c1 == 'i' and c2 == ' ' and c3 == 'i':
                new_list[i+1] = ' '
            elif original_list[c4] == ' ' and original_list[c5] == 'i':
                new_list[i] = 'i'
            elif original_list[c4] == ' ' and original_list[c5] == ' ':
                new_list[(i+1)%len(original_list)] = ' '
            elif c1 == 'T':
                new_list[i] = 'i'
            elif c1 == 'i':
                new_list[i] = 'T'
            elif c1 == ' ':
                original_list[i] = ' '

        return str(new_list)


    def __str__(self):

        return str(self.bar)


    def __setitem__(self, key, value):
        original_list = list(self.bar)
        original_list[key] = value
        self.bar = "".join(original_list)

        return str(self)


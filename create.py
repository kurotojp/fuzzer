front = [s.strip() for s in open('./tag1.txt', 'r').readlines()]
back = [s.strip() for s in open('./tag2.txt', 'r').readlines()]
sample = [s.strip() for s in open('./sample.txt', 'r').readlines()]
quote = [s.strip() for s in open('./quote.txt', 'r').readlines()]

file = open('./fuzz.txt', 'x')


def create_fuzz():
    for s1 in sample:
        for f1, b1 in zip(front, back):
            for q1 in quote:
                for f2, b2 in zip(front, back):
                    for q2 in quote:
                        file.write(q2+ b2 + f1 + q1 + s1 + q1 + b2 + f2 + q2.join('\n'))
                        #print(q2 + b2 + f1 + q1 + s1 + q1 + b2 + f2 + q2)


if __name__ == '__main__':
    create_fuzz()
    print("Create Fuzz finish!")

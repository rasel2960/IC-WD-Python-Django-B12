def spam():
    print('Spam! Spam! Spam!')
spam()

nospam = spam
nospam()

def twice(func):
    func()
    func()
twice(spam)


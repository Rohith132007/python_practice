def outer():
    x = 10   # Enclosing scope variable

    def inner():
        print(x)   # Accesses x from the enclosing scope

    inner()

outer()
def outer_function(*args, **kwargs):
    def inner_function():
        print("Inner function is called!")
        print("Args:", args)
        print("Kwargs:", kwargs)
    inner_function()


if __name__ == "__main__":
    outer_function(1, 2, 3,4,5,6,6, name="Alice", age=25)
class A:
    def bunny(self):
        print('class A is defined')

class B(A):

    def bunny(self):
        print("class b is defined as child of A")
        super().bunny()

obj=B()
obj.bunny()


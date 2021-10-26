class Sphere: 

    def __init__(self, *arg):
        if len(arg) == 0:
            arg = (1, 0, 0, 0)

        elif len(arg) == 1:
            arg = (arg[0], 0, 0, 0)
            
        elif len(arg) == 4:
             self.__radius, self.__x, self.__y, self.__z = arg

        else:
            raise TypeError 

        self.__radius, self.__x, self.__y, self.__z = arg # два подчеркивания для того, чтобы к атрибуту нельзя было обратиться напрямую, изменение только через методы


    def get_volume(self):
        return 4 * 3.1415 * (self.__radius ** 3)

    def get_square_(self):
        return 4 * 3.1415 * (self.__radius ** 2)

    def get_radius_(self):
        return self.__radius

    def get_center_(self):
        return (self.__x, self.__y, self.__z)

    def set_radius(self, radius):
        self.__radius = radius

    
    def set_center (self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def is_point_inside (self, _x, _y, _z):
        return (self.__x-_x)**2 + (self.__y-_y)**2 + (self.__z-_z)**2 < self.__r**2

s = Sphere(2, 1, 1, 1)
print(s.get_radius_())
print(s.get_volume())
print(s.get_center_())
print(s.get_square_())
s.set_radius(4)
s.set_center(2, 2, 2)
print(s.get_center_())
print(s.get_radius_())


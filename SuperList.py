class SuperList(list):
    def __len__(self):
        return 1000

my_list = SuperList()

print(len(my_list))

for i in range(0, 101):
    my_list.append(i)

print(my_list[0])
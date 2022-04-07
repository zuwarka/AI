class People:
    m_sibling = None
    m_parent = None
    m_child = None

    def __init__(self, name):
        self.name = name

    def __eq__(self, people):
        return self.name == people.name

    def parent(self, people):
        return people in self.m_child

    def sibling(self, people):
        return people in self.m_parent[0].m_child and self != people

    def child(self, people):
        return people in self.m_parent

    def uncle(self, grand, grand_child):
        for children in grand.m_child:  # Прохожусь по списку детей бабушки/дедушки
            if grand_child != children:  # Отбрасываю тех, у кого один и тот же родитель
                return children.m_child


def print_uncle(peoples, index):
    for i, people_name in enumerate(peoples):
        mother_or_father = people_name.m_parent  # Список родителей
        if mother_or_father != None:
            grand_mother_or_father = [None if mother_or_father == None else parents.m_parent for parents in
                                      mother_or_father]  # Список бабушек и дедушек
            for j in grand_mother_or_father:
                if j != None and i == index:
                    for k in j:  # k.name - имена бабушек и дедушек
                        print(people_name.name, *[num.name for num in people_name.uncle(k, mother_or_father[0])])


if __name__ == "__main__":
    Zahar = People(name="Захар")
    Natasha = People(name="Наташа")
    Dasha = People(name="Даша")
    Masha = People(name="Маша")
    Vasya = People(name="Вася")
    Fedor = People(name="Федор")

    Masha.m_child = [Natasha, Dasha]
    Natasha.m_parent = [Masha]
    Dasha.m_parent = [Masha]
    Natasha.m_child = [Fedor, Vasya]
    Fedor.m_parent = [Natasha]
    Vasya.m_parent = [Natasha]
    Dasha.m_child = [Zahar]
    Zahar.m_parent = [Dasha]
    # Natasha.sibling = [Dasha]
    # Dasha.sibling = [Natasha]
    # Fedor.sibling = [Vasya]
    # Vasya.sibling = [Fedor]

    peoples = [Masha, Natasha, Dasha, Fedor, Vasya, Zahar]

    print_uncle(peoples, peoples.index(Zahar))

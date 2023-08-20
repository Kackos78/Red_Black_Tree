# Помогити

class Node:
# Создаём ноду. Нода имеет: значение, правого ребенка, левого ребенка,
# цвет (изначально вносим красный, нужно для упрощения балансировки).
    def __init__(self, value): 
        self.value = value
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None

# Класс для создания деревьев
class RedBlackTree:

    # Создание дерева и его корня
    def __init__ (self):
        self.root = None
    
    # Поиск значений в дереве
    def search (self, value):
        current_node = self.root                                                    # Переменная для поиска, будем сравнивать значение кажной ноды с value
        while current_node != None and value != current_node.value:    # Если значение и не value и ну пустое:
            if value < current_node.value :                                 # Буквально бинарный поиск, если value меньше текущего значения то нам налево, если нет то направо
                current_node = current_node.left
            else:
                current_node = current_node.right

        if current_node is None: # Чтобы не выводить принт при отсутствии значения делаем проверку
            return current_node
        else:
            print(f"Нода: {current_node.value} Родитель: {current_node.parent}")
            return current_node
    
    # Вносим новое значение
    def input_node(self, value):
        # Запускаем поиск, если значение уже есть то внести его повторно не получится
        check = self.search(value)
        if check:
            return "Значение уже внесено."
        # Если значения нет, то ищем будущего родителя
        else:
            new_node = Node(value)
            none_node = self.root
            future_perent_node = none_node
            while none_node is not None: # Ищем нужную пустую ноду и её родителя
                future_perent_node = none_node          # Значение none_node будет всегда на шаг впереди future_perent_node, 
                if new_node.value < none_node.value:    # таким образом когда none_node == None: future_perent_node будет иметь значение будущего родителя
                    none_node = none_node.left
                elif new_node.value > none_node.value:
                    none_node = none_node.right

            new_node.parent = future_perent_node # вносим данные о родителе новой ноды
            if future_perent_node == None:
                self.root = new_node 
            elif new_node.value > new_node.parent.value:
                new_node.parent.right = new_node
            elif new_node.value < new_node.parent.value:
                new_node.parent.left = new_node
            self.rebalanse(new_node)

    def rebalanse(self, new_node):
        
        while new_node != self.root and new_node.parent.color == 'RED':     # Проходим по дереву либо до корня, либо пока родитель не станет черным (т.к.) сверху все будет отсортировано
            if new_node == new_node.parent.right:                            # Если мы поставили ноду справа
                l = new_node.parent.left                                    # указываем левую ноду
                if l.color == 'RED' :                                        # и если обе соседние ноды красные то делаем свап
                    l.color = 'BLACK'                                       # 
                    new_node.color = 'BLACK'                                # собственно перекрашиваем детей в черный а родителя в красный
                    new_node.parent.color = 'RED'                           # а родителя в красный
                    new_node = new_node.parent                              # и переходим на следущую ноду
                else:
                    self.left_turn(new_node.parent.parent)                  # Если нода слева черная то делаем левый поворот
                    new_node.parent.color = 'RED'                           # и докрашиваем ноды после поворота
                    new_node.parent.parent.color = 'BLACK'                  # 

            else:                                                           # Если мы поставили ноду слева
                r = new_node.parent.right                                   # Указываем правую ноду

                if r.color == 'RED':                                        # если обе соседние ноды красные то делаем свап
                    r.color = 'BLACK'                                       # 
                    new_node.parent.color = 'BLACK'                         # перекрашиваем детей в черный 
                    new_node.parent.parent.color = 'RED'                    # а родителя в красный  
                    new_node = new_node.parent                              # и переходим на следущую ноду
                else:                                                       # Нода справа черная 
                    self.right_turn(new_node.parent.parent)                 # то делаем правый поврот                            
                    new_node.parent.color = 'BLACK'                         # и докрашиваем ноды
                    new_node.parent.parent.color = 'RED'                    # 
                                   
        self.root.color = 'BLACK'                                           # И в конце перекрашиваем корень обратно в черный

    def left_turn (self, x):        # Поворот налево
        y = x.right                 # указываем ноды x y вокруг которых будет произведен поворот,
        x.right = y.left            # отдаем среднего ребенка родителю х
        y.parent = x.parent         # Ставим у наверх
        if x.parent == None:        # проверяем был ли х корнем, если да то новый корент это у
            self.root = y           # 
        elif x == x.parent.left:    # если нет то связываем у с бывшими родителями х
            x.parent.left = y       # или слева
        else:                       #
            x.parent.right = y      # или справа
        y.left = x                  # связываем х и у между собой
        x.parent = y                # 

    def right_turn(self, y):        # Поворот направо
        x = y.left                  # указываем ноды x y вокруг которых будет произведен поворот,
        y.left = x.right            # отдаем среднего ребенка родителю y
        x.parent = y.parent         # Ставим у наверх
        if y.parent == None:        # проверяем был ли y корнем, если да то новый корент это x
            self.root = x           # если да то новый корень это х
        elif y == y.perent.left:    # если нет то свызываем бывших родителей у с х
            y.parent.left = x       # или слева
        else:                       # 
            y.parent.right = x      # или справа
        x.right = y                 # связывавем х и у между собой
        y.parent = x                # 




tree1 = RedBlackTree()

tree1.input_node(4)
tree1.input_node(5)
tree1.input_node(1)


class Fib():
    """Число Фибоначчи.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Проверка, что start не изменился
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** ТВОЙ КОД ЗДЕСЬ ***"

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """Торговый автомат, продающий некоторый товар по некоторой цене.
    
    >>> v = VendingMachine('яблоко', 10)
    >>> v.vend()
    'Товара нет в наличии.'
    >>> v.restock(2)
    'Количество товара «яблоко»: 2'
    >>> v.vend()
    'Нужно дополнительно внести 10 ₽.'
    >>> v.deposit(7)
    'Доступно: 7 ₽'
    >>> v.vend()
    'Нужно дополнительно внести 3 ₽.'
    >>> v.deposit(5)
    'Доступно: 12 ₽'
    >>> v.vend()
    'Получите яблоко и сдачу 2 ₽.'
    >>> v.deposit(10)
    'Доступно: 10 ₽'
    >>> v.vend()
    'Получите яблоко.'
    >>> v.deposit(15)
    'Товара нет в наличии. Вот твои деньги — 15 ₽.'

    >>> w = VendingMachine('лимонад', 2)
    >>> w.restock(3)
    'Количество товара «лимонад»: 3'
    >>> w.restock(3)
    'Количество товара «лимонад»: 6'
    >>> w.deposit(2)
    'Доступно: 2 ₽'
    >>> w.vend()
    'Получите лимонад.'
    """


    def __init__(self, name='', cost=0):
        self.name = name
        self.cost = cost
        self.amount = 0
        self.money = 0

    def deposit(self, mon):
    	self.money += mon
    	if self.amount > 0:
    		return 'Доступно: {0} ₽'.format(self.money)
    	else:
    		mon, self.money = self.money, 0
    		return 'Товара нет в наличии. Вот твои деньги — {0} ₽.'.format(mon)

    def restock(self, am):
    	self.amount += am
    	return 'Количество товара «{0}»: {1}'.format(self.name, self.amount)

    def vend(self):
    	if self.amount < 1 and self.money > 0:
    		return_mon, self.money = self.money, 0
    		return 'Товара нет в наличии. Вот твои деньги — {0} ₽.'.format(return_mon)
    	elif self.amount < 1:
    		return 'Товара нет в наличии.'
    	elif self.money < self.cost:
    		return 'Нужно дополнительно внести {0} ₽.'.format(self.cost-self.money)
    	elif self.money > self.cost:
    		charge, self.money = self.money-self.cost, 0
    		self.amount -= 1
    		return 'Получите {0} и сдачу {1} ₽.'.format(self.name, charge)
    	else:
    		self.money = 0
    		self.amount -= 1
    		return 'Получите {0}.'.format(self.name)

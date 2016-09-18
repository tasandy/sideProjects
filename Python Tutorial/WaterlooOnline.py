## Waterloo Online Python Course: A Collection Of My Test Pieces

###### Recursion

#### sum

def sum(seq):
    if len(seq) == 0:
        return 0
    else:
        return seq[0] + sum(seq[1:])

def test_sum():
    example = [1, 2, 3, 4]
    assert sum(example) == 10
    assert sum([4]) == 4
    assert sum([]) == 0

test_sum()

#### multisplit

def multisplit(total, split):
    count = 0
    if total > 1 and split > 1:
        count += 1
        return count + multisplit(total/split, split)
    return count

def test_multisplit():
    assert multisplit(8, 2) == 3
    assert multisplit(1, 2) == 0
    assert multisplit(3, 0) == 0

test_multisplit()

#### reverse

def reverse(seq):
    reverse_seq = []
    if len(seq) != 0:
        reverse_seq.append(seq[-1])
        return reverse_seq + reverse(seq[:-1])
    return reverse_seq

def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert reverse([4]) == [4]
    assert reverse([]) == []

test_reverse()

#### change

def change(salaries, boosters):
    if len(salaries) == 0:
        return []
    else:
        return [salaries[0] * boosters[0]] + \
               change(salaries[1:],boosters[1:])

def test_change():
    assert change([],[]) == []
    assert change([2, 3], [4, 5]) == [8, 15]

test_change()

### divides_all

def is_multiple(number, factor):
    return number % factor == 0

def divides_all(seq, factor):
    if len(seq) != 0 and factor > 1:
        if is_multiple(seq[0], factor):
            return divides_all(seq[1:], factor)
        else:
            return False
    return True

def test_divides_all():
    assert divides_all([1, 2, 3], 1) == True
    assert divides_all([4, 7], 3) == False
    assert divides_all([], 2) == True

test_divides_all()

### all_equal

def all_equal(a_list):
    if len(a_list) > 1:
        if a_list[0] == a_list[1]:
            return all_equal(a_list[1:])
        else:
            return False
    return True

def test_all_equal():
    assert all_equal([1, 2, 3]) == False
    assert all_equal([7, 7]) == True
    assert all_equal([]) == True

test_all_equal()

#### equal

def equal(one, two):
    if len(one) == len(two) == 0:
        return True
    elif len(one) == 0 or len(two) == 0:
        return False
    else:
        return one[0] == two[0] and \
               equal(one[1:], two[1:])

def test_equal():
    assert equal([],[]) == True
    assert equal([],[1]) == False
    assert equal([1],[]) == False
    assert equal([1, 2, 3], [1, 2]) == False
    assert equal([1, 2], [1, 2, 3]) == False
    assert equal([1, 2, 4], [1, 2, 3]) == False
    assert equal([1, 2, 3], [1, 2, 3]) == True

test_equal()

#### is_sorted

def is_sorted(a_list):
    if len(a_list) > 1:
        if a_list[0] <= a_list[1]:
            return is_sorted(a_list[1:])
        else:
            return False
    return True

def test_is_sorted():
    assert is_sorted([1, 2, 3]) == True
    assert is_sorted([7, 6]) == False
    assert is_sorted([]) == True

test_is_sorted()

#### has_digit

def has_digit(a_string):
    if len(a_string) != 0:
        if a_string[0].isdigit():
            return True
        else:
            return has_digit(a_string[1:])
    return False

def test_has_digit():
    assert has_digit("t1Est1") == True
    assert has_digit("test") == False
    assert has_digit("") == False

test_has_digit()

#### seq_max

def seq_max(seq):
    if len(seq) == 1:
        return seq[0]
    else:
        return max(seq[0], seq_max(seq[1:]))

def test_seq_max():
    unsorted = [4, 7, 2, 4, 1, 3, 2, 8, 7]
    assert seq_max(unsorted) == 8
    assert seq_max([4]) == 4

test_seq_max()

#### is_pal

def is_pal(entry):
    if len(entry) <= 1:
        return True
    else:
        return entry[0] == entry[-1] and \
                           is_pal(entry[1:-1])

def test_is_pal():
    assert is_pal("") == True
    assert is_pal("a") == True
    assert is_pal("otto") == True  
    assert is_pal("bob") == True
    assert is_pal("apple") == False
    assert is_pal("area") == False

test_is_pal()

###### Structuring Data

#### shuffle

def shuffle(one_list, two_list):
    shuffled = []
    if len(one_list) == len(two_list):
        for first, second in zip(one_list, two_list):
            shuffled += [first]
            shuffled += [second]
    return shuffled

def test_shuffle():
    assert shuffle([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert shuffle([1, 3], [2, 4, 6]) == []
    assert shuffle([1, 3, 5], [2, 4]) == [] 
    assert shuffle([], []) == []
    assert shuffle([1], []) == []
    assert shuffle([], [1]) == []

test_shuffle()

#### bound_chars

def bound_chars(a_string, bound):
    count = 0
    distinct = ""
    for letter in a_string:
        if letter not in distinct:
            distinct += letter
            count += 1
    if count > bound:
        return False
    return True

def test_bound_chars():
    assert bound_chars("cartoon", 6) == True
    assert bound_chars("cartoon", 5) == False
    assert bound_chars("cartoon", 0) == False
    assert bound_chars("", 6) == True

test_bound_chars()

#### flatten

def flatten(list_list):
    flat = [] 
    for each in list_list:
        for item in each:
            flat.append(item)
    return flat

def test_flatten():
    assert flatten([[1, 2], [3, 4]]) \
     == [1, 2, 3, 4]
    assert flatten([[], [2], [1, 2]]) == [2, 1, 2]
    assert flatten([[], []]) == []
    assert flatten([]) == []

test_flatten()
                   
#### is_in 

def is_in(info, target):
    for key, value in info.items():
        if key == target:
            return value
    return "Not found"

def test_is_in():
    unicode = {"a":97, "b":100, "c":99}
    assert is_in(unicode, "a") == 97
    assert is_in(unicode, "z") == "Not found"
    assert is_in({}, "a") == "Not found"

test_is_in() 

#### Meal, all_contain

class Meal:
    """Meal name, cost, and list of allergens

       Public methods:
       __init__: initializes a new object

       Attributes:
       name: non-empty string; meal name
       cost: int >= 0; cost of meal
       allergens: list of strings; allergens
    """
    
    def __init__(self, name, cost, allergens):
        self.name = name
        self.cost = cost
        self.allergens = allergens
    
    def contains(self, allergen):
        for item in self.allergens:
            if item == allergen:
                return True
        return False

def all_contain(meals, allergen):
    good_foods = []
    for seq in meals:
        for item in seq.allergens:
            if item == allergen:
               good_foods += [seq]
    return good_foods

#### number_pixels

def number_pixels(a_list, colour):
    count = 0
    for seq in a_list:
        for item in seq:
            if item == colour:
                count += 1
    return count

def test_number_pixels():
    assert number_pixels([[],[]], "red") == 0
    assert number_pixels([["red", "red", "blue"],["red", "red"]], "red") == 4
    assert number_pixels([["red", "red", "blue"],["red", "red"]], "") == 0

test_number_pixels()

#### max_colour

def max_colour(seq):
    counts = {}
    for item in seq:
        if item in counts.keys():
             counts[item] = counts[item] + 1    
        else:
             counts[item] = 1
    most = 0
    best = "Empty"
    for colour, num in counts.items():
         if num > most:            
            most = num
            best = colour
    return best

def test_max_colour():
    colours = ["red", "blue", "green",\
    "green", "red", "yellow", "red"]
    assert max_colour(colours) == "red"
    assert max_colour([]) == "Empty"

test_max_colour()

#### changes

def changes(salaries, boosters):
    result = []
    for item, adjust in zip(salaries, boosters):
        result = result + [item * adjust]
    return result

def test_changes():
    assert changes([],[]) == []
    assert changes([2, 3], [4, 5]) == [8, 15]

test_changes()

###### Objects

#### Circle

class Circle:
    """Circle radius, x and y coordinates, colour

       Public methods:
       __init__: initializes a new object
    
       Attributes:
       radius: int or float >= 0; circle radius
       x: int >= 0; x-coordinate of centre
       y: int >= 0; y-coordinate of centre
       colour: string; colour of the circle
    """

    def __init__(self, radius, x, y, colour):
        """Creates new circle
        """

        self.radius = radius
        self.x = x
        self.y = y
        self.colour = colour

    def __str__(self):
        """Prints object
        """

        return self.colour + " circle of radius " + \
            str(self.radius) + " centred at (" + \
            str(self.x) + "," + str(self.y) + ")"

    def area(self):
        """Determines area.
        """
        return math.pi * self.radius ** 2
    
    def aligned(self, circ_2):
        """Checks to see if circles have same coords
        """
        if self.x == circ_2.x and self.y == circ_2.y:
            return True
        return False
    
    def bigger(self, circ_2):
        """Checks to see if circle 1 is bigger than circle 2
        """
        if self.radius > circ_2.radius:
            return True
        return False
    
    def is_colour(self, col):
        """Checks to see if circle 1 is the same colour as col
        """
        if self.colour == col:
            return True
        return False

#### Time

class Time:
    """Time stored as hour and minutes

       Methods:
       __init__: initializes a new object
       __str__: prints an object
       earlier_time: returns earlier time

       Attributes:
       hour: int, 0 <= value < 24
       minute: int, 0 <= value < 60
    """

    def __init__(self, hour, minute):
        """Initializes a new object.

           Preconditions:
           hour: int, 0 <= value < 24
           minute: int, 0 <= value < 60

           Parameters:
           hour: hour in time
           minute: minutes in time

           Side effect: attributes set with values
        """
        self.hour = hour
        self.minute = minute
 
    def __str__(self):
        """Prints time.

           Side effect: prints 
        """

        if self.minute < 10:
            min_word = "0" + str(self.minute)
        else:
            min_word = str(self.minute)
        return str(self.hour) + ":" + \
            min_word

    def earlier_time(self, other):
        """Determines earlier of two Times.

           Preconditions:
           other: Time object

           Parameters:
           other: Time compared to self

           Returns: earlier of two times, 
           or other if equal 
        """

        if self.hour < other.hour:
            return self
        elif other.hour < self.hour:
            return other
        elif self.minute < other.minute:
            return self
        else:
            return other
    
    def safe(self):
        """Determines if the time given is a valid time
        """
        if type(self.minute) != type(1) or type(self.hour) != type(1):
            return "Incorrect type"
        if self.minute >= 0 and self.minute < 60 \
        and self.hour >= 0 and self.hour < 24:
            return "Safe"
        elif (self.minute < 0 or self.minute >= 60) \
        and (self.hour < 0 or self.hour >= 24):
            return "Hour and minute out of range"
        elif self.hour < 0 or self.hour >= 24:
            return "Hour out of range"
        elif self.minute < 0 or self.minute >= 60:
            return "Minute out of range"
        return False
        
    def elapsed(self, two):
        """Determines the number of minutes in-between the two times
        
           Side effect: two is assumed to be later in the day.
        """
        minutes_elapsed = two.minute - self.minute
        if self.hour >= two.hour:
            minutes_elapsed += ((two.hour + 24) - self.hour) * 60
        else:
            minutes_elapsed += (two.hour - self.hour) * 60
        if minutes_elapsed >= 1440:
            minutes_elapsed -= 1440
        return minutes_elapsed
    
    def overlap(self, two, three):
        """Checks to see if the self time is equal to the
           one of the other two or if two < one < three
        """
        if (self.hour == two.hour and self.minute == two.minute) or \
        (self.hour == three.hour and self.minute == three.minute):
            return True
        if earlier_time(self, two) == two \
        and earlier_time(self, three) == self:
            return True
        return False

#### Egg

class Egg:
    """Egg low and high range of mass
       and category name.
    
       Attributes:
       low: int > 0, lowest mass in grams
       high: int > 0, highest mass in grams
       name: nonempty string, category
    """
    def __init__(self, low, high, name):
        """Initializes a new object.

           Preconditions:
           low: int, 0 < value <= high
           high: int, value > 0, value >= low
           name: string

           Parameters:
           low: minimum weight
           high: maximum weight
           name: category of egg

           Side effect: attributes set with values
        """
        self.low = low
        self.high = high
        self.name = name
 
    def __str__(self):
        """Prints object.
        """
        return self.low + " to " + self.high + \
            " grams: " + self.name + " egg."
    
    def is_size(self, num):
        """Checks the egg size
        """
        if num >= self.low and num <= self.high:
            return True
        return False

#### Event

import copy

class Event:
    """Event given as start and end times

       Methods:
       __init__: initializes a new object

       Attributes:
       start: Time, when event starts
       end: Time, when event ends       
    """

    def __init__(self, start, end):
        """Initializes a new object

           Preconditions:
           start, end: Time objects

           Parameters:
           start, end: start and end times
  
           Side effect: attributes set with values
        """
        self.start = start
        self.end = end

###### Iteration using for

#### compare

def compare(list1, list2):
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] > list2[i]:
                return "Larger"
            if list1[i] < list2[i]:
                return "Smaller"
        return "Equal"
    if len(list1) > len(list2):
        return "Larger"
    else:
        return "Smaller"

def test_compare():
    assert compare([1], []) == "Larger"
    assert compare([2, 3], [2, 2]) == "Larger"
    assert compare([], [1]) == "Smaller"
    assert compare([2, 2], [2, 3]) == "Smaller"
    assert compare([], []) == "Equal"

test_compare()

#### equals

def equals(list1, list2):
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True
    return False

def test_equals():
    assert equals([1], []) == False
    assert equals([2, 2], [2, 2]) == True
    assert equals([], [1]) == False
    assert equals([2, 2], [2, 3]) == False
    assert equals([], []) == True

test_equals()

#### swap

def swap(sequence, first, second):
    temp = sequence[first]
    sequence[first] = sequence[second]
    sequence[second] = temp

def test_swap():
    unsorted = [4, 7, 2, 4, 1, 3, 8]
    swap(unsorted, 0, 5)
    assert unsorted == \
    [3, 7, 2, 4, 1, 4, 8]

test_swap()

#### selection

def pos_min(sequence):
    best = sequence[0]
    pos = 0
    counter = 1
    while counter < len(sequence):
        if best > sequence[counter]:
            best = sequence[counter]
            pos = counter
        counter = counter + 1
    return pos

def selection(sequence):
    for counter in range(len(sequence)):
        pos = pos_min(sequence[counter:]) + counter
        swap(sequence, counter, pos)

def test_selection():
    unsorted = [4, 7, 2, 4, 1, 3, 8]
    selection(unsorted)
    assert unsorted == \
    [1, 2, 3, 4, 4, 7, 8]

test_selection()

#### rel_prime

def is_multiple(number, factor):
    return number % factor == 0

def rel_prime(num1, num2):
    for i in range(2,min(num1, num2)+1):
        if is_multiple(num1, i) and is_multiple(num2, i):
            return False
    return True

def test_rel_prime():
    assert rel_prime(5, 5) == False
    assert rel_prime(0, 2) == True
    assert rel_prime(8, 2) == False

test_rel_prime()

#### password

def password(string):
    upper_check = 0
    lower_check = 0
    digit_check = 0
    if len(string) >= 8:
        for i in range(len(string)):
            if string[i].isupper():
                upper_check = 1
            if string[i].islower():
                lower_check = 1
            if string[i].isdigit():
                digit_check = 1
            if upper_check == 1 and lower_check == 1 \
            and digit_check == 1:
                return True
    return False

def test_password():
    assert password("") == False
    assert password("Password1") == True
    assert password("Passwd1") == False
    assert password("Password") == False
    assert password("assword1") == False
    assert password("PASSWORD1") == False

test_password()

#### caesar (caps)

def caesar(string, offset):
    new_string = ""
    for i in range(len(string)):
        if string[i].isupper():
            if (ord(string[i]) + offset) > 90:
                new_string += chr(ord(string[i]) + offset - 26)
            elif (ord(string[i]) + offset) < 65:
                new_string += chr(ord(string[i]) + offset + 26)
            else:
                new_string += chr(ord(string[i]) + offset)
        else:
            new_string += string[i]
    return new_string

def test_caesar():
    assert caesar("", 5) == ""
    assert caesar("PASS", 0) == "PASS"
    assert caesar("ABC", 5) == "FGH"

test_caesar()

#### postal_code

def postal_code(entry):
    if len(entry) == 7 and entry[0].isalpha() and entry[0].isupper() \
    and entry[1].isdigit() and entry[2].isalpha() and entry[2].isupper() \
    and entry[3].isspace() and entry[4].isdigit() and \
    entry[5].isalpha() and entry[5].isupper() and entry[6].isdigit():
        return True
    for i in range(1):
        return False

def test_postal_code():
    assert postal_code("") == False
    assert postal_code("A9A 9A9") == True
    assert postal_code("A9A 9a9") == False
    assert postal_code("A9A 9AA") == False
    assert postal_code("A9A 9A9A") == False

test_postal_code()

#### swap_case

def swap_case(string):
    new_string = ""
    for i in range(len(string)):
        if string[i].islower():
            new_string += string[i].upper()
        elif string[i].isupper():
            new_string += string[i].lower()
        else:
            new_string += string[i]
    return new_string

def test_swap_case():
    assert swap_case("") == ""
    assert swap_case("A9A 9A9") == "a9a 9a9"
    assert swap_case("A9A 9a9") == "a9a 9A9"
    assert swap_case("eEeee") == "EeEEE"

test_swap_case()

#### break_up

def break_up(entry):
    new = []
    word = ""
    for char in entry:
        if not char.isspace():
            word = word + char
        else:
            if len(word) > 0:
                new = new + [word]
                word = ""
    if len(word) > 0:
        return new + [word]
    else:
        return new

def test_break_up():
    assert break_up("one") == ["one"]
    assert break_up("  ") ==  []
    assert break_up("one two   three") \
     == ["one", "two", "three"]

test_break_up()

#### is_pali

def is_pali(entry):
    length = len(entry)
    mid = length // 2
    for counter in range(mid):
        if entry[counter] != entry[- (counter + 1)]:
            return False
    return True

def test_is_pali():
    assert is_pali("") == True
    assert is_pali("a") == True
    assert is_pali("otto") == True  
    assert is_pali("bob") == True
    assert is_pali("apple") == False
    assert is_pali("area") == False

test_is_pali()

#### search

def search(sequence, target):
    for item in sequence:
        if item == target:
            return item
        if item > target:
            break
    return "Not found"

def test_search():
    thelist = [10, 20, 30, 40, 50]
    assert search(thelist, 30) == 30
    assert search(thelist, 45) == "Not found"
    assert search([], 35) == "Not found"

test_search()

#### is_prime

def is_prime(num):
    """Determines if num is prime.

       Preconditions:
       num: int > 1
    
       Parameters:
       num: number being checked
 
       Returns: Boolean (True if prime)
    """
    fails = False
    for factor in range(2, num-1):
        fails = is_multiple(num, factor)
        if fails:
            break
    return not fails


def test_is_prime():
    assert is_prime(2) == True  
    assert is_prime(3) == True
    assert is_prime(53) == True
    assert is_prime(120) == False

test_is_prime()

#### no_nums

def no_nums(string):
    new_string = ""
    for i in range(len(string)):
        if not string[i].isdigit():
            new_string += string[i]
    return new_string

def test_no_nums():
    assert no_nums("2er") == "er"
    assert no_nums("22") == ""
    assert no_nums("er") == "er"
    assert no_nums("") == ""

test_no_nums()

#### has_digit

def has_digit(string):
    for i in range(len(string)-1):
        if string[i].isdigit():
            return True
    return False

def test_has_digit():
    assert has_digit("2er") == True
    assert has_digit("22") == True
    assert has_digit("er") == False
    assert has_digit("") == False

test_has_digit()

#### count_chars

def count_chars(entry, char):
    """Determines number of occurrences of 
       char in entry.

       Preconditions:
       entry: nonempty string
       char: string of length 1
    
       Parameters:
       entry: the string with character to count
       char: the character to count
 
       Returns: int, nonnegative
    """
    count = 0
    for one in entry:
        if one == char:
            count = count + 1
    return count

def test_count_chars():
    assert count_chars("apple", "p") == 2  
    assert count_chars("apple", "d") == 0
    assert count_chars("", "d") == 0

test_count_chars()

###### Storing Elements In A Sequence

#### changed

def changed(salaries, booster):
    new_list = list(salaries)
    counter = 0
    while counter < len(new_list):
        new_list[counter] = \
        new_list[counter] * booster
        counter = counter + 1
    return new_list

def test_changed():
    the_list = [0, 1, 2, 3, 4, 5]
    assert changed(the_list, 2) == [0, 2, 4, 6, 8, 10]
    assert the_list == [0, 1, 2, 3, 4, 5]

test_changed()

#### no_zero

def no_zero(a_list):
    new_list = []
    count = 0
    while len(a_list) > count:
        if a_list[count] != 0:
            new_list.append(a_list[count])
        count += 1
    return new_list

def test_no_zero():
    assert no_zero([]) == []
    assert no_zero([0, 0]) == []
    assert no_zero([2, 2]) == [2, 2]
    assert no_zero([2, 0, 2, 0]) == [2, 2]

test_no_zero()

#### remove_zero

def remove_zero(a_list):
    while 0 in a_list:
        a_list.remove(0)
    return a_list

def test_remove_zero():
    assert remove_zero([]) == []
    assert remove_zero([0, 0]) == []
    assert remove_zero([2, 2]) == [2, 2]
    assert remove_zero([2, 0, 2, 0]) == [2, 2]

test_remove_zero()

#### divide_all

def is_multiple(number, factor):
    return number % factor == 0

def divide_all(seq, factor):
    count = 0
    while count < len(seq):
        if not is_multiple(seq[count], factor):
            return False
        else:
            count += 1
    return True

def test_divide_all():
    assert divide_all([1, 2, 3], 1) == True
    assert divide_all([4, 7], 3) == False
    assert divide_all([], 2) == True

test_divide_all()

#### two_digit_word

UNITS = ["zero", "one", "two", "three", "four", "five",
         "six", "seven", "eight", "nine"]

TENS = ["", "", "twenty", "thirty", "forty", "fifty", 
         "sixty", "seventy", "eighty", "ninety"]

TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]

TWENTY = 20
TEN = 10

def two_digit_word(num):
    if num < 100 and num > -1:
        if num >= TWENTY:
            return TENS[num // 10] + "-" + UNITS[num % 10]
        if num >= TEN:
            return TEENS[num - 10]
        else:
            return UNITS[num]
    return num

def test_two_digit_word():
    assert two_digit_word(25) == "twenty-five"
    assert two_digit_word(100) == 100
    assert two_digit_word(2) == "two"
    assert two_digit_word(13) == "thirteen"

test_two_digit_word()

#### shift

def shift(a_list):
    if len(a_list) > 1:
        last = a_list[0]
        a_list.remove(last)
        a_list.append(last)
    return a_list

def test_shift():
    assert shift([]) == []
    assert shift([3]) == [3]
    assert shift([4, 5, 6]) == [5, 6, 4]

test_shift()

#### max_diff

def max_diff(a_list):
    if len(a_list) > 1:
        return sorted(a_list)[len(a_list) - 1] - sorted(a_list)[0]
    return 0

def test_max_diff():
    assert max_diff([]) == 0
    assert max_diff([3]) == 0
    assert max_diff([4, 5, 6]) == 2

test_max_diff()

#### move_to_front

def move_to_front(a_list, a_item):
    if a_item in a_list:
        a_list.remove(a_item)
        a_list.insert(0, a_item)
    return a_list

def test_move_to_front():
    assert move_to_front([], 3) == []
    assert move_to_front([3], 3) == [3]
    assert move_to_front([3], 4) == [3]
    assert move_to_front([4, 5, 6], 3) == [4, 5, 6]
    assert move_to_front([4, 5, 6], 5) == [5, 4, 6]

test_move_to_front()

#### pos_min

def pos_min(sequence):
    best = sequence[0]
    pos = 0
    counter = 1
    while counter < len(sequence):
        if best > sequence[counter]:
            best = sequence[counter]
            pos = counter
        counter = counter + 1
    return pos

def test_pos_min():
    assert pos_min([6, 1, 5, -2, 1]) == 3  
    assert pos_min([0]) == 0

test_pos_min()

#### seq_max

def seq_maxi(sequence):
    """Determines the maximum element.

       Preconditions:
       sequence: length at least one
    """

    best = sequence[0]
    counter = 1
    while counter < len(sequence):
        if best < sequence[counter]:
            best = sequence[counter]
        counter = counter + 1
    return best

def test_seq_maxi():
    assert seq_maxi([0, 1, 5, 2, 1]) == 5  
    assert seq_maxi([0]) == 0
    assert seq_maxi('caterpillar') == 't'  
    assert seq_maxi(['c']) == 'c'    

test_seq_maxi()

#### replace

def replace(a_list, old, new):
    if old in a_list:
        place = a_list.index(old)
        a_list.remove(old)
        a_list.insert(place, new)
    return a_list

def test_replace():
    assert replace([0, 1, 5, 2], 1, 3) == [0, 3, 5, 2]
    assert replace([1], 1, 3) == [3]
    assert replace([0, 2], 1, 3) == [0, 2]
    assert replace([], 1, 3) == []

test_replace()

#### hide_inside

def hide_inside(a_list, a_item, pos):
    if pos >= len(a_list):
        a_list.append(a_item)
    elif len(a_list) > 0:
        a_list.insert(pos, a_item)
    return a_list

def test_hide_inside():
    assert hide_inside(["a", "b"], "cat", 1) == ["a", "cat", "b"]
    assert hide_inside(["a", "b"], "cat", 20) == ["a", "b", "cat"]
    assert hide_inside(["a", "b"], "cat", 0) == ["cat", "a", "b"]
    assert hide_inside([], "cat", 0) == ["cat"]

test_hide_inside()

#### count_items

def count_items(entry, item):
    count = 0
    pos = 0
    while pos < len(entry):
        if entry[pos] == item:
            count = count + 1
        pos = pos + 1
    return count

def test_count_items():
    assert count_items([], 1) == 0
    assert count_items([1, 0, 1], 1) == 2
    assert count_items([3, 4, 5], 1) == 0
    assert count_items([4, 4, 4], 4) == 3

test_count_items()

###### Iteration Using While

#### no_num

def no_num(string):
    length = len(string)
    count = 0
    new_string = ""
    while count < length:
        if not string[count].isdigit():
            new_string += string[count]
        count += 1
    return new_string

def test_no_num():
    assert no_num("2er") == "er"
    assert no_num("22") == ""
    assert no_num("er") == "er"
    assert no_num("") == ""

test_no_num()


#### add_up

def add_up():
    stop = "Go"
    add = 0
    while stop != "Stop":
        stop = input("Gimme your ints\n")
        if stop.isdigit():
            add += int(stop)
    return add

#### factorial

def factorial(num):
    """Determines the sum of num down to 1.

       Preconditions:
       num: int > 0

       Parameter:
       num: the starting number

       Returns: sum of num down to 1
    """
    total = 0
    while num > 0:
        total += num
        num -= 1
    return total

def test_factorial():
    assert factorial(0) == 0
    assert factorial(5) == 15

test_factorial()

#### repeat_print

def repeat_print(num):
    """Prints the input num times.
 
       Preconditions:
       num: positive integer 
    
       Parameter:
       num: the number of times and what is printed

       Side effect: prints num num times.
    """
    count = num
    while count > 0:
        print(num)
        count = count - 1

def test_repeat_print():
    assert repeat_print(0) == None
    assert repeat_print(5) == None

test_repeat_print()

#### pig_latin

def is_vowel(char):
    is_a = char == "a" or char == "A"
    is_e = char == "e" or char == "E"
    is_i = char == "i" or char == "I"
    is_o = char == "o" or char == "O"
    is_u = char == "u" or char == "U"
    return is_a or is_e or is_i or is_o or is_u

def is_consonant(char):
    return len(char) == 1 and not is_vowel(char)


def pig_latin(word):
    pos = first_vowel(word)
    if pos == 0:
        return(word + "way")
    else:
        return(word[pos:] + word[0:pos] + "ay")

def first_vowel(word):
    """Determines the first vowel in word or 
       length of word if none

       Preconditions:
       word: string of letters only

       Parameter:
       word: a word 

       Returns: int position in word
    """
    pos = 0
    while pos < len(word) and is_consonant(word[pos]):
        pos = pos + 1
    return pos

def test_first_vowel():
    assert first_vowel("chrome") == 3  
    assert first_vowel("apple") == 0
    assert first_vowel("sdk") == 3
    assert first_vowel("") == 0

test_first_vowel()

def test_pig_latin():
    assert pig_latin("apple") == "appleway"
    assert pig_latin("chrome") == "omechray"

test_pig_latin()

#### count_char

def count_char(entry, char):
    """Determines number of occurrences of char in entry.

       Preconditions:
       entry: nonempty string
       char: string of length 1
    
       Parameters:
       entry: the string with character to count
       char: the character to count
 
       Returns: int, nonnegative
    """
    count = 0
    pos = 0
    while pos < len(entry):
        if entry[pos] == char:
            count = count + 1
        pos = pos + 1
    return count

def test_count_char():
    assert count_char("apple", "p") == 2  
    assert count_char("apple", "l") == 1
    assert count_char("apple", "d") == 0

test_count_char()

#### is_primes

def is_multiple(number, factor):
    return number % factor == 0

def is_primes(num):
    """Determines if num is prime.

       Preconditions:
       num: int > 1
    
       Parameters:
       num: number being checked
 
       Returns: Boolean (True if prime)
    """
    factor = 2 
    fails = False
    while factor < num and not fails:
        fails = is_multiple(num, factor)
        factor = factor + 1
    return not fails

def test_is_primes():
    assert is_primes(2) == True  
    assert is_primes(3) == True
    assert is_primes(53) == True
    assert is_primes(120) == False

test_is_primes()

#### say_uncle

def say_uncle():
    response = 'aunt'
    while response != 'uncle':
        response = \
        input("I'll quit if you say 'uncle': ")

def test_say_uncle():
    assert say_uncle() == None

test_say_uncle()

###### Building Better Programs (no tests but comments)

#### yarn_size

def yarn_size(stitches):
    """Determines yarn size given 4 inches of stitches.

       Preconditions:
       stitches: int > 0; 6 <= value <= 32
     
       Parameter:
       stitches: average number of stitches in 4 inches

       Returns: yarn size
    """
    BULKY_MAX = 2
    if stitches > 5 and stitches < 12:
        return "Super bulky"
    elif stitches > 11 and stitches < 16:
        return "Bulky"
    elif stitches > 15 and stitches < 21:
        return "Medium"
    elif stitches > 20 and stitches < 23:
        return "Light"
    elif stitches > 22 and stitches < 25:
        return "Light or Fine"
    elif stitches > 24 and stitches < 27:
        return "Fine"
    else:
        return "Super fine"

#### bakers

DOZEN = 12         # number of items in a dozen
BAKERS_DOZEN = 13  # number of items in a baker's dozen
DOZEN_COST = 10    # cost of a dozen
SINGLE_COST = 1    # cost of a single item

def bakers(items, DOZEN_COST, SINGLE_COST):
    """Determines cost of items with baker's dozen discount.

       Preconditions:
       items: int > 0

       Parameters:
       items: number of items 
   
       Returns: total cost with discount of 13 for the cost of a dozen
    """   
    ## Determine numbers of groups of 13 and extras
    cost = 0
    cost += items // BAKERS_DOZEN * DOZEN_COST

    ## If there are twelve extras, use dozen_cost
    if items % BAKERS_DOZEN == DOZEN:
        cost += DOZEN_COST

    ## If there are fewer than twelve extras, use single_cost
    elif items % BAKERS_DOZEN > 0:
        cost += items % BAKERS_DOZEN * SINGLE_COST
    return cost

#### sandwiches

import math

THICKNESS = 1.0        ## in cm, thickness of spread
JAR_VOLUME = 100.0     ## in cubic cm, volume of a jar

def sandwiches(width, length, jars):
    """Determines the number of sandwiches that 
       can be made using bread of size 
       width x length and jars number of jars.

       Preconditions: 
       width: int or float with value > 0
       length: int or float with value > 0
       jars: int with value >= 0

       Parameters:
       width: the width of a piece of bread in cm
       length: the length of a piece of bread in cm
       jars: the number of jars provided

       Returns: int number of sandwiches
    """   
    ## Compute volume for one sandwich
    volume_one = width * length * THICKNESS

    ## Compute total volume of jar contents
    volume_total = jars * JAR_VOLUME
  
    ## Compute total sandwiches 
    return math.floor(volume_total / volume_one)

#### paper_size

SMALL_2R = 600  # Dimensions in cm of size 2R paper
BIG_2R = 900

SMALL_3R = 1050 # Dimensions in cm of size 3R paper
BIG_3R = 1500

SMALL_4R = 1200 # Dimensions in cm of size 4R paper
BIG_4R = 1800

SMALL_5R = 1500 # Dimensions in cm of size 5R paper
BIG_5R = 2100

def paper_size(small, big):
    """Determines the smallest size of photo paper 
       for a photo of size small x big.

       Preconditions: 
       small: int or float with value > 0
       big: int or float with value > 0

       Parameters:
       small: smaller dimension of photo, in pixels
       big: bigger dimension of photo, in pixels
       The two dimensions can be equal.       

       Returns: string paper size or "Too big"
    """
    if big <= BIG_2R and small <= SMALL_2R:
        return("Use size 2R")      
    elif big <= BIG_3R and small <= SMALL_3R:
        return("Use size 3R")      
    elif big <= BIG_4R and small <= SMALL_4R:
        return("Use size 4R")      
    elif big <= BIG_5R and small <= SMALL_5R:
        return("Use size 5R")      
    else:
        return("Too big")

#### exchange

import math
def exchange(entry):
    """Returns string with middle and last
       character exchanged.

       Preconditions:
       entry: string of odd length > 0

       Parameter:
       entry: string as basis for new string

       Returns: string like entry but with
                middle and last positions exchanged
    """
    mid = math.floor(len(entry) / 2)
    last = 2 * mid
    first_part = entry[:mid]
    mid_char = entry[mid]
    second_part = entry[mid+1:last]
    last_char = entry[last]
    return first_part + last_char + second_part + mid_char

#### olive_sizes

BULLETS = 351
FINE = 321
BRILLIANT = 291
SUPERIOR = 261
LARGE = 231
EXTRA_LARGE = 201
JUMBO = 181
EXTRA_JUMBO = 161
GIANT = 141
COLOSSAL = 121
SUPER_COLOSSAL = 111
MAMMOTH = 101
SUPER_MAMMOTH = 91

def olive_sizes(number):
    """Returns a string for the type of olive
       given the number per kilogram.

       Preconditions:
       number: integer in range from 91 to 351, inclusive

       Parameter:
       number: number of olives in one kilogram

       Return: a string giving type of olive
    """

    if number >= BULLETS:
        return "Bullets"
    elif number >= FINE:
        return "Fine"
    elif number >= BRILLIANT:
        return "Brilliant"
    elif number >= SUPERIOR:
        return "Superior"
    elif number >= LARGE:
        return "Large"
    elif number >= EXTRA_LARGE:
        return "Extra Large"
    elif number >= JUMBO:
        return "Jumbo"
    elif number >= EXTRA_JUMBO:
        return "Extra Jumbo"
    elif number >= GIANT:
        return "Giant"
    elif number >= COLOSSAL:
        return "Colossal"
    elif number >= SUPER_COLOSSAL:
        return "Super Colossal"
    elif number >= MAMMOTH:
        return "Mammoth"
    else:
        return "Super Mammoth"

#### pbj

import math
def sandwiches(width, length, number_jars,
               thickness, jar_volume):
    """Determines the number of sandwiches 
       that can be made

       Preconditions: 
       width: int or float with value > 0
       length: int or float with value > 0
       number_jars: int with value >= 0
       thickness: int or float with value > 0
       jar_volume: int or float with value > 0

       Parameters:
       width: the width of a piece of bread in cm
       length: the length of a piece of bread in cm
       number_jars: the number of jars of spread
       thickness: the thickness of the spread in cm
       jar_volume: volume of each jar in cubic cm

       Returns: int number of sandwiches
    """   
    ## Compute volume for one sandwich
    volume_for_one = width * length * thickness

    ## Compute total volume of jar contents
    volume_available = number_jars * jar_volume 

    ## Compute total sandwiches
    return math.floor( \
           volume_available / volume_for_one)

def pbj(width, length, number_jam_jars, jam_thickness, 
        jam_jar_volume, number_pb_jars, pb_thickness,
        pb_jar_volume):
    """Determines the number of sandwiches 
       that can be made.

       Preconditions: 
       width: int or float with value > 0
       length: int or float with value > 0
       number_jam_jars: int with value >= 0
       jam_thickness: int or float with value > 0
       jam_jar_volume: int or float with value > 0
       number_pb_jars: int with value >= 0
       pb_thickness: int or float with value > 0
       pb_jar_volume: int or float with value > 0

       Parameters:
       width: width of a piece of bread in cm
       length: length of a piece of bread in cm
       number_jam_jars: number of jars of jam
       jam_thickness: thickness of jam in cm
       jar_volume: volume of jam jar in cubic cm
       number_pb_jars: number of jars of pb
       pb_thickness: thickness of pb in cm
       pb_volume: volume of pb jar in cubic cm
 
       Returns: int number of sandwiches
    """   
    ## Compute number of sandwiches worth of jam
    number_jam = sandwiches(width, length, \
                 number_jam_jars, jam_thickness, \
                 jam_jar_volume)

    ## Compute number of sandwiches worth of pb
    number_pb = sandwiches(width, length, \
                number_pb_jars, pb_thickness, \
                pb_jar_volume)

    ## Return minimum of values
    return min(number_jam, number_pb)

#### wedding_cake

import math

def area_circle(radius):
    return math.pi * radius ** 2

def volume_cylinder(radius, height):
    return height * area_circle(radius)

def round_cake_spread(radius, height, thickness):
    """Determines volume of frosting of given 
       thickness for a round cake of given 
       radius and height.

       Preconditions: 
       radius: int, float; value > 0
       height: int, float; with value > 0
       thickness: int, float; with value > 0

       Parameters:
       radius: radius of cake, in cm
       height: height of cake, in cm
       thickness: thickness of frosting, in cm

       Returns: float volume of frosting
    """   
    ## Frosting around side
    thick_radius = radius + thickness
    outer = volume_cylinder(thick_radius, height)
    inner = volume_cylinder(radius, height)
    side_frosting = outer - inner

    ## Frosting on top of layer, including side
    top_frosting = area_circle(thick_radius) \
                   * thickness
    
    ## Total frosting
    return top_frosting + side_frosting

def wedding_cake(radius1, radius2, radius3, height1, 
                height2, height3, thickness):
    """Determines volume of frosting of given 
       thickness for a wedding cake of three 
       layers of given radius and height.

       Preconditions: 
       radius1, radius2, radius3: int, float; value > 0
       height1, height3, height3: int, float; value > 0
       thickness: int or float with value > 0

       Parameters:
       radius1, radius2, radius3: radius of cake, in cm
       height1, height2, height3: height of cake, in cm
       thickness: thickness of the frosting, in cm

       Returns: float volume of frosting
    """   
    frosting1 = round_cake_spread(radius1, height1, \
                thickness);
    frosting2 = round_cake_spread(radius2, height2, \
                thickness);
    frosting3 = round_cake_spread(radius3, height3, \
                thickness);
    return frosting1 + frosting2 + frosting3

#### uk_code

def uk_code(entry):
    """Determines if a string can be a postal code.

       Preconditions:
       entry: string of letters, digits, spaces only

       Parameters:
       entry: possible postal code

       Returns "Code" if of one of the following forms:
       "A9 9AA", "A9A 9AA", "A99 9AA", "AA9 9AA",
       "AA9A 9AA", "AA99 9AA" where 9 is any digit and
       A is any letter,
       and "Not code" otherwise
    """

    ## Return "Not code" if the length is not between 6 and 8
    if len(entry) < 6 or len(entry) > 8:
        return "Not code"

    ## Return "Not code" if it does not start with a letter 
    ## or end of the form  ' 9AA'
    if entry[0].isalpha() and code_ending(entry):

    ## Return "Code" for valid codes of length 6
        if len(entry) == 6 and entry[1].isdigit():
            return "Code"

    ## Return "Code" for valid codes of length 7
        if len(entry) == 7 and ((entry[1].isdigit() and (entry[2].isdigit() \
        or entry[2].isalpha())) or entry[1].isalpha() and entry[2].isdigit()):
            return "Code"

    ## Return "Code" for valid codes of length 8
        elif  entry[1].isalpha() and entry[2].isdigit() \
        and (entry [3].isalpha() or entry[3].isdigit()):
            return "Code"

    ## Return "Not code" for all other inputs
    return "Not code"

def code_ending(entry):
    return entry[-1].isalpha() and entry[-2].isalpha() \
    and entry[-3].isdigit() and entry[-4].isspace()

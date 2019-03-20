import itertools


class variable(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, variable):
            return self.name == other.name
        else:
            return False

    def __repr__(self):
        return self.name

    def __iter__(self):
        return iter([])


class constant(object):
    def __init__(self, content):
        self.content = content

    def __eq__(self, other):
        if isinstance(other, constant):
            return self.content == other.content
        else:
            return False

    def __iter__(self):
        return iter([])

    def __repr__(self):
        return self.content


class function(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, function):
            return self.name == other.name
        else:
            return False

    def __repr__(self):
        return self.name

    def __iter__(self):
        return iter([])


class predicate(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, predicate):
            return self.name == other.name
        else:
            return False

    def __repr__(self):
        return self.name

    def __iter__(self):
        return iter([])


class substitution(object):
    def __init__(self, first=None, second=None):
        if first and second:
            self.substitutions = [(first, second)]
        else:
            self.substitutions = []

    def resolve(self, leftList, other):
        f, s = other
        result = []
        if isinstance(leftList, (variable, constant, function, predicate)):
            return leftList
        if not leftList:
            return []
        if isinstance(leftList[0], list):
            result.append(self.resolve(leftList[0], other))
        else:
            if leftList[0] == s:
                result.append(f)
            else:
                result.append(leftList[0])
        result.extend(self.resolve(leftList[1:], other))
        result = [i for i in result if i]
        return result

    def __call__(self, other):
        if isinstance(other, substitution):
            # add new substitution
            if other.substitutions:
                for j in range(len(other.substitutions)):
                    for i in range(len(self.substitutions)):
                        self.substitutions[i] = (self.resolve(self.substitutions[i][0],
                                                              other.substitutions[j]),
                                                 self.substitutions[i][1])
                        # if self.substitutions[i][0] == other.substitutions[j][1]:
                        #self.substitutions[i] = (other.substitutions[j][0], self.substitutions[i][1])
                        if self.substitutions[i][1] == other.substitutions[j][1]:
                            self.substitutions[i] = (
                                self.substitutions[i][0], other.substitutions[j][0])
                    self.substitutions.append(other.substitutions[j])
            return self
        elif isinstance(other, list):
            # replace every occurrence of second by first
            new = []
            for element in other:
                if isinstance(element, variable):
                    rplc = False
                    for s in self.substitutions:
                        if s[1] == element:
                            new.append(s[0])
                            rplc = True
                    if not rplc:
                        new.append(element)
                elif isinstance(element, list):
                    new.append(self.__call__(element))
                else:
                    new.append(element)
            return new
        else:
            pass

    def __repr__(self):
        if not self.substitutions:
            return '{}'
        s = '{'
        for i in self.substitutions:
            s += '(' + repr(i[0]) + '/'
            s += repr(i[1]) + '), '
        return s[:-2] + '}'


class error(object):
    def __init__(self, msg):
        self.message = msg

    def __repr__(self):
        return "error: %s" % self.message


def head(ls):
    if not ls:
        return None
    return ls[0]


def tail(ls):
    return ls[1:]


def unify(k1, k2):
    """Return the most general unifier of two expressions k1 and k2."""

    if not k1 or not k2:
        return substitution()
    if isinstance(k1, (constant, variable, function, predicate)) or isinstance(k2, (constant, variable, function, predicate)):
        if k1 == k2:
            return substitution()
        if isinstance(k1, variable):
            if k1 in k2:
                return error(repr(k1) + " in " + repr(k2))
            else:
                return substitution(k2, k1)
        if isinstance(k2, variable):
            if k2 in k1:
                return error(repr(k2) + " in " + repr(k1))
            else:
                return substitution(k1, k2)
        if not isinstance(k1, variable) and not isinstance(k2, variable):
            return error(repr(k1) + " and " + repr(k2) + " cannot be unified!")

    alpha = unify(head(k1), head(k2))
    if isinstance(alpha, error):
        return alpha
    k3 = alpha(tail(k1))
    k4 = alpha(tail(k2))
    beta = unify(k3, k4)
    if isinstance(beta, error):
        return beta
    return alpha(beta)


P = predicate("P")
g = function("g")
f = function("f")
x = variable("x")
y = variable("y")
w = variable("w")
a = constant("a")

expr1 = [P, [f, a], [g, y], [f, w]]
expr2 = [P, x, [g, [f, x]], y]
uni = unify(expr1, expr2)     # find the most general unifier
new1 = uni(expr1)
new2 = uni(expr2)
print(uni)
print(new1)
print(new2)

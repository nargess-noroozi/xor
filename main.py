def unitStep(v):
    if v >= 0:
        return 1
    else:
        return 0

def perceptronModel(x, w, b):
    v = w[0] * x[0] + w[1] * x[1] + b
    y = unitStep(v)
    return y

w = [1, 1]
b = -1.5

test1 = [0, 1]
test2 = [1, 1]
test3 = [0, 0]
test4 = [1, 0]

print("AND({}, {}) = {}".format(0, 1, perceptronModel(test1, w, b)))
print("AND({}, {}) = {}".format(1, 1, perceptronModel(test2, w, b)))
print("AND({}, {}) = {}".format(0, 0, perceptronModel(test3, w, b)))
print("AND({}, {}) = {}".format(1, 0, perceptronModel(test4, w, b)))
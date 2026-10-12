# --------------------------------------------------------   תרגיל 1

d = {
    "bread":(12, 4.5),
    "milk":(9, 6.4),
    "cheese":(8, 8.2),
    "roll":(46, 1.5)
}

def inventory_summary(dic):
    sum_v = 0
    for k,v in dic.items():
        sum_v += v[0]
    return sum_v

print(inventory_summary(d))

# --------------------------------------------------------   תרגיל 2

def print_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

print_args_kwargs(1,3,5,"python",lesson="python", subject="args & kwargs", day="Tuesday")

from math import sqrt
from pprint import pprint
from itertools import permutations


def parse_input(filename):
    data = open(filename).read().splitlines()
    capacity, depot = list(map(eval, data[0].split()))
    customers = [{'loc': eval(loc), 'quantity': eval(quantity), 'delivered': False}
                 for quantity, loc in [line.split()
                                       for line in data[2:]]]
    return capacity, depot, customers

capacity, depot, customers = parse_input('input/doohickies.txt')


def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def load_truck():
    # Get unsatisfied customers
    undelivered = [c for c in customers if not c['delivered']]
    undelivered.sort(key=lambda c:c['quantity'], reverse=True)
    on_truck = [undelivered[0]]
    remaining = undelivered[1:]
    def sort_by_average_distance(item):
        distances = []
        for cust in on_truck:
            distances.append(distance(cust['loc'], item['loc']))
        return sum(distances) / len(distances)

    load = lambda: sum([cust['quantity'] for cust in on_truck])
    while load() + remaining[-1]['quantity'] <= capacity:
        # Sort remaining based on collective distance to customers on the truck
        by_location = sorted(remaining, key=sort_by_average_distance)
        next_cust = [cust for cust in by_location if load()+cust['quantity'] <= capacity][0]
        on_truck.append(next_cust)
        remaining.remove(next_cust)
        if not remaining:
            break
    return on_truck

def best_order(customers):
    perms = permutations(customers)
    best = None
    best_dist = None
    for p in perms:
        points = [cust['loc'] for cust in p]
        points.insert(0, depot)
        points.append(depot)
        dist = 0
        for i in range(len(points)-1):
            dist += distance(points[i], points[i+1])
        if best is None or best_dist > dist:
            best = p
            best_dist = dist
    return best
        

distance = euclidean_distance

truck = depot
runs = []
while not all([cust['delivered'] for cust in customers]):
    load = load_truck()
    run = best_order(load)
    for stop in run:
        stop['delivered'] = True
    runs.append(run)
# Do the runs!
total_distance = 0
for run in runs:
    print(('Load {} units onto truck'.format(sum([c['quantity'] for c in run]))))
    for customer in run:
        dist = distance(truck, customer['loc'])
        total_distance += dist
        truck = customer['loc']
        print(('Deliver {} units to {} ({}, total distance {})'.format(customer['quantity'], customer['loc'], dist, total_distance)))
    dist = distance(truck, depot)
    total_distance += dist
    truck = depot
    print(('Return to depot ({}, total distance {})'.format(dist, total_distance)))
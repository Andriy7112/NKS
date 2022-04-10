t = 5695

intensity = 1670

gamma = 0.95

work_hours = [41, 295, 842, 1365, 66, 1093, 102, 5340,
343, 1539, 333, 933, 854, 1630, 1434, 279,
1029, 574, 787, 2701, 1644, 853, 456, 846,
490, 328, 2360, 384, 1202, 1061, 342, 246,
445, 715, 736, 295, 345, 772, 41, 1510, 315,
889, 409, 809, 66, 64, 752, 746, 45, 1774,
469, 1508, 212, 581, 1136, 266, 186, 720,
295, 4668, 139, 586, 254, 2023, 1502, 292,
946, 1779, 152, 291, 7, 979, 646, 58, 2115,
957, 897, 5961, 392, 832, 2091, 2, 265, 187,
823, 1464, 449, 258, 533, 36, 525, 1571,
707, 1160, 1576, 25, 609, 486, 48, 230]

work_hours.sort()

sumed_work_hours = 0
for i in work_hours:
    sumed_work_hours += i
avarage = sumed_work_hours / len(work_hours)

print("Sorted hours: ", work_hours)
print("Avarage: ", avarage)

max_hours = work_hours[-1]
h = work_hours[-1] / 10

print("Max hours: ", max_hours)
print("Length: ", h)

intervals = []
i = 0
for _ in range(11):
    intervals.append(i)
    i += h

print("Intervals: ", intervals)
frequensy_possibilities = []
for i in range(len(intervals) - 1):
    times = []
    for time in work_hours:
        if intervals[i] < time <= intervals[i + 1]:
            times.append(time)
    frequensy_possibilities.append(len(times) / (len(work_hours) * h))
print("Failure probability: ", frequensy_possibilities)

probabilities = []

for time in intervals:
    frequensies = 0
    for i in range(0, int(time // h)):
        frequensies += frequensy_possibilities[i]

    current_frequensy_possibilities = frequensy_possibilities[int(time // h)] if not int(time // h) >= len(
        frequensy_possibilities) else 0
    integral = frequensies * h + current_frequensy_possibilities * (time % h)
    probabilities.append(1 - integral)

print("Probabilities: ", probabilities)

t_y_index = 0
for i in range(len(probabilities)):
    if probabilities[i] <= gamma:
        t_y_index = i
        break

print("T_y index: ", t_y_index)

t_i = t_y_index * h
t_i_decreased = (t_y_index - 1) * h

frequensies_t_i = 0
for i in range(0, int(t_i // h)):
    frequensies_t_i += frequensy_possibilities[i]

integral_t_i = frequensies_t_i * h + frequensy_possibilities[int(t_i // h)] * (t_i % h)

frequensies_t_i_decreased = 0
for i in range(0, int(t_i_decreased // h)):
    frequensies_t_i_decreased += frequensy_possibilities[i]

integral_t_i_decreased = frequensies_t_i_decreased * h + frequensy_possibilities[
    int(frequensies_t_i_decreased // h)] * (t_i_decreased % h)

t_y = t_i - h * (1 - integral_t_i - gamma) / ((1 - integral_t_i) - (1 - integral_t_i_decreased))

print("T_y : ", t_y)

frequensies_t = 0
for i in range(0, int(t // h)):
    frequensies_t += frequensy_possibilities[i]

probability_of_failure_free_operation = 1 - (frequensies_t * h + frequensy_possibilities[int(t // h)] * (t % h))

print("Probability of failure free operation : ", probability_of_failure_free_operation)

intensities = 0
for i in range(0, int(intensity // h)):
    intensities += frequensy_possibilities[i]

failure_intensity = frequensy_possibilities[int(intensity // h)] / (
            1 - (intensities * h + frequensy_possibilities[int(intensity // h)] * (intensity % h)))

print("Failure intensity : ", failure_intensity)
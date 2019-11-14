import time


def count_sort(in_list):
    k = max(in_list) + 1
    count_list = [0 for i in range(k)]
    for i in range(len(in_list)):
        count_list[in_list[i]] = count_list[in_list[i]] + 1
    for i in range(1, k):
        count_list[i] = count_list[i-1] + count_list[i]
    result = [0 for i in range(len(in_list) + 1)]
    for j in range(len(in_list)):
        result[count_list[in_list[j]]] = in_list[j]
        count_list[in_list[j]] = count_list[in_list[j]] - 1
    return result


def main():
    start_time = time.time()
    initial_list = [1,1,1]
    print(count_sort(initial_list)[1:])
    first_time = time.time()
    print("Time taken: %f ms" % (first_time - start_time))


if __name__ == '__main__':
    main()

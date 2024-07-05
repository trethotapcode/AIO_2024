# sliding window and list slicing.

def sliding_window(int_array, k):
    '''
    this function reveives two inputs: a list and an integer number.
    this function aims to return a maximum list of subarray contains k elements (k<len(arr))
    '''

    # nếu k lớn hơn len hoặc k < 0, trả về chuỗi rỗng
    if k > len(int_array) or k <= 0:
        return []

    # khai báo mảng kết quả, phần tử đầu cuối
    result = []
    low = 0
    high = k

    # bắt đầu duyệt sub_array
    while (high <= len(int_array)):

        # cắt chuỗi con
        sub_str = int_array[low:high]

        # lấy phần tử lớn nhất
        max_value = max(sub_str)

        # đưa vào cuối chuỗi kết quả
        result.append(max_value)

        # sliding mảng con.
        low = low + 1
        high = high + 1

    return result


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    print(sliding_window(num_list, 1))

# đưa text file về dictionary chứa các chữ giống nhau.


def letter_in_file(file_name):

    # dictionary word_count
    my_dict = {}

    # đọc file
    with open(file_name, 'r') as file:

        # đọc data từng dòng với readlines
        data = file.readlines()
        file.close()

        # tiền xử lý dữ liệu
        for line in data:

            # xử lý in thường, xóa enter và chia câu thành từ.
            line = line.lower()
            line = line.replace('\n', '')
            line = line.split(' ')

            # counting algorithm
            for word in line:
                my_dict[word] = my_dict.get(word, 0) + 1

    # trả về từ điển word: count
    return my_dict


if __name__ == "__main__":
    print(letter_in_file("P1_data.txt"))

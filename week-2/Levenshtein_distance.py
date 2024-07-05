# thường được sử dụng trong kiểm tra lỗi chính tả của text data.
# hàm trả về số lần thực hiện thay đổi (insert/delete/substitution) để
# đưa ra từ đúng ngữ pháp.

def levenshtein_distance(source, target):
    '''
    source is the input which users can enter from keyboard.
    target is the word we wanted to become.
    this function return nums of chance from source to target
    '''

    # khai báo row là độ dài của target + 1, col là độ dài của source + 1.
    # chú ý, "+1" là phần tử rỗng thêm vào ở đầu mỗi word.
    row = len(source) + 1
    col = len(target) + 1

    # tạo ma trận theo row-col
    matrix = [[0]*col for element in range(row)]

    # một hàng có col phần tử, một cột có row phần tử .
    for row_index in range(col):

        # gán phần tử hàng
        matrix[0][row_index] = row_index

    for col_index in range(row):

        # gán phần tử cột
        matrix[col_index][0] = col_index

    # khai báo các chi phí thay đổi chữ.
    # insert_cost = 0
    # delete_cost = 0
    # sub_cost = 0

    # duyệt qua từng phần tử ma trận, sử dụng công thức quy hoạch động dựa trên
    # bottom-up để xử lí.

    for i in range(1, row):
        for j in range(1, col):

            # nếu phần tử ở dòng và cột giống nhau, ta không mất chi phí hoán đổi.
            # vì vậy, lấy nguyên giá trị ô chéo trước đó là chi phí cần tìm.
            if source[i - 1] == target[j - 1]:
                matrix[i][j] = matrix[i-1][j-1]

            else:

                # insert: hola --> hell --> hello. hola sang hell đã biểu diễn ở ô trước,
                # cộng với '1' chi phí thêm 'o' ở bước cuối cùng.
                insert_cost = matrix[i][j-1] + 1

            # delete: hola --> hol --> hello. tốn '1' chi phí xóa 'a', cộng với chi phí
            # xử lý từ hol sang hello ở ô trên.
                delete_cost = matrix[i-1][j] + 1

            # substitution: 'hol'a--> 'hell'a --> hello. tốn chi phí chuyển từ hol sang hell
            # ở ô chéo trước, cộng với '1' chi phí từ 'a' sang 'o'.
                sub_cost = matrix[i-1][j-1] + 1

            # min của 3 trường hợp trên sẽ được điền vào ô [i][j]
                matrix[i][j] = min(insert_cost, delete_cost, sub_cost)

    # sau khi hoàn thành bảng, trả về phần tử cuối cùng của bảng, đây là số lần tối thiểu cần
    # biến đổi từ một từ sang từ chính xác.
    return matrix[row - 1][col - 1]


print(levenshtein_distance('hola', 'hello'))

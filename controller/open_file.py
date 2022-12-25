# membuka file aturan CNF / CNF rules
def open_file(filepath):
    # mempersiapkan list kosong
    data = []
    # membuka file dengan mode read
    with open(filepath, 'r') as file:
        # membaca aturan baris per baris
        raw = file.readlines()
        # menambahkan aturan kedalam list dan menghilangkan baris baru
        for rule in raw:
            data.append(rule.strip('\n'))
    # mengembalikan aturan yang terdapat dalam list
    return data
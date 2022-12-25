# import library atau framework yang diperlukan
import streamlit as st
from pandas import DataFrame

# simbol empty set
empty = '\u2205'


# mempersipaka tabel untuk algoritma CYK
def create_table(list_of_string):
    # mempersiapkan list kosong
    table = []
    # untuk setiap kata dalam kalimat
    for i in range(len(list_of_string)):
        # menambahkan list kosong sebagai baris
        table.append([])
        # untuk setiap kata dalam kalimat
        for j in range(len(list_of_string)):
            # jika i < j tambahkan baris saat ini dengan ' ' sebagai kolom
            if i < j:
                table[i].append(' ')
                # jika tidak, tambahkan baris saat ini dengan set kosong sebagai kolom
            else:
                table[i].append(set())
    # mengembalikan tabel kosong
    return table

# mengisi iterasi pertama
def filling_bottom(table, cnf, list_of_string):
    # untuk semua kata dalam list
    for i, word in enumerate(list_of_string):
        # siapkan set kosong untuk sel tabel
        cell = set()
        # untuk setiap aturan di cnf
        for row in cnf:
            # untuk setiap elemen di aturan body
            for element in row[1]:
                # jika kata saat ini sama dengan elemen saat ini
                if word in element:
                    # tambahkan ke kumpulan sel
                    cell.add(row[0])
                    break
        # isi tabel diagonal ([i][i]) dengan kumpulan sel
        table[i][i] = cell

# isi semua tabel pengisian, mulai dari baris 1
def filling_all(cnf, table, string, row = 1):
    # jika kolom pertama di baris terakhir bukan himpunan kosong [set()]
    if table[len(table) - 1][0] != set():
        # jika simbol awal ada di sana
        if 'K' in table[len(table) - 1][0]:
            # menunjukkan tanda bahwa kalimat baku
            st.write('Kalimat Baku')
        else:
            # menunjukkan tanda bahwa kalimat tidak baku
            st.write('Kalimat Tidak Baku')
        # hentikan rekursif
        return

    # temukan baris berikutnya untuk diisi dengan fungsi iterasi
    next_row = iteration(cnf, table, string, row)

    # panggil fungsi filling_all dengan next_row yang diperbarui
    filling_all(cnf, table, string, next_row)


# iterasi untuk mengisi sel tabel
def iteration(cnf, table, input_string, row):
    # iterasi menurun untuk kolom di baris saat ini
    for column in range(len(table) - 1, -1, -1):
        # jika sel saat ini kosong
        if table[row][column] == set():
            # siapkan daftar kosong untuk menyimpan persimpangan
            list_of_intersect = []
            # ulangi baris dalam sel saat ini dari baris 0
            for i in range(0, row):
                # jika sel di [i][kolom] adalah simbol himpunan kosong
                if table[i][column] == empty:
                    # tambahkan set kosong ke list_of_intersect
                    list_of_intersect.append(set())
                # jika sel di [i][kolom] bukan ' ' dan bukan set kosong
                elif table[i][column] != ' ' and table[i][column] != set():
                    # menambahkan konten sel ke dalam list_of_intersect
                    list_of_intersect.append(table[i][column])
            # iterasi kolom di sel saat ini dari kolom saat ini + 1
            for i in range(column + 1, len(table)):
                # jika sel di [baris][i] adalah simbol himpunan kosong
                if table[row][i] == empty:
                    # tambahkan set kosong ke list_of_intersect
                    list_of_intersect.append(set())
                # lain jika sel di [baris][i] bukan ' ' dan bukan set kosong
                elif table[row][i] != ' ' and table[row][i] != set():
                    # menambahkan konten sel ke dalam list_of_intersect
                    list_of_intersect.append(table[row][i])

            # membuat kombinasi dari list_of_intersect dan menyimpan kombinasi tersebut
            result_list = make_combination(list_of_intersect)

            # gabungkan semua kombinasi di result_list menjadi satu set
            combine_result = combine(result_list)

            # temukan aturan cnf yang tepat untuk sel tabel saat ini
            table[row][column] = find_cnf(combine_result, cnf)

            # tampilkan tabel pengisian yang diperbarui
            st.table(DataFrame(table, columns=input_string))

            # tingkatkan baris jika jumlah baris berikutnya < dari total semua baris, jika tidak, kembali ke baris nomor 1
            row = (row + 1) if row + 1 < len(table) else 1
            return row

    # tingkatkan baris jika jumlah baris berikutnya < dari total semua baris, jika tidak, kembali ke baris nomor 1
    row = (row + 1) if row + 1 < len(table) else 1
    # mengembalikan nilai baris
    return row


# buat kombinasi body pada baris dan kolom saat ini
def make_combination(list_input):
    # hitung semua elemen di list_input, lalu bagi dengan 2
    count = len(list_input) // 2
    # daftar kosong untuk semua kombinasi
    combination = []

    # iterasi sebanyak hitungan
    for i in range(count):
        # list1 adalah index i dari list_input
        list1 = list_input[i]
        # list2 adalah indeks i + count dari list_input
        list2 = list_input[i + count]

        # tambahkan daftar kosong ke dalam kombinasi
        combination.append([])

        # ulangi semua elemen di list1
        for element1 in list1:
            # ulangi semua elemen di list2
            for element2 in list2:
                # kombinasinya adalah tupel elemen1 saat ini dan elemen2 saat ini, lalu tambahkan
                combination[i].append(tuple((element1, element2)))

    # mengembalikan kombinasi
    return combination

# gabungkan semua kombinasi menjadi satu set
def combine(raw_combination):
    # siapkan set kosong
    result_set = set()
    # untuk setiap kombinasi dalam raw_combination
    for x in raw_combination:
        # untuk setiap tupel dalam kombinasi
        for y in x:
            result_set.add(y)

    # kembalikan result_set
    return result_set

# temukan kepala cnf yang tepat untuk mengisi sel saat ini
def find_cnf(combine, cnf):
    # siapkan set kosong
    cnf_return = set()

    # ulangi semua kombinasi
    for com in combine:
        # ulangi setiap aturan di cnf
        for row in cnf:
            # jika kombinasi di badan aturan saat ini
            if com in row[1]:
                # tambahkan kepala aturan saat ini ke set cnf_return
                cnf_return.add(row[0])

    # jika cnf_return kosong
    if cnf_return == set():
        # kembalikan simbol set kosong
        return empty
    else:
        # lain mengembalikan nilai cnf_return
        return cnf_return
# mengkonversi aturan agar dapat dibaca oleh python
def raw_to_cfg(raw):
    # menyiapkan list kosong
    cfg = []
    # untuk setiap baris dalam aturan, pisahkan dengan ' -> ', lalu tambahkan ke daftar cfg
    for line in raw:
        cfg.append(line.split(' -> '))
    # untuk setiap body dalam aturan, pisahkan badan dengan ' | ' lalu ubah menjadi set
    for rule in cfg:
        rule[1] = set(rule[1].split(' | '))
    # untuk setiap baris dalam aturan
    for rule in cfg:
        # menyiapkan set kosong
        new_body = set()
        # untuk semua elemen dalam body
        for element in rule[1]:
            # konversi setiap body (variabel dan terminal) menjadi tuple dengan memisahkannya
            element_to_tuple = tuple(element.split(' '))
            # masukan body baru kedalam set new_body
            new_body.add(element_to_tuple)
        # merubah format body lama menjadi format baru
        rule[1] = new_body
    # mengembalikan aturan yang dapat dibaca
    return cfg
def load_locations(file_path):
    locations = {}
    current_province = None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith("##"):  # Menandakan provinsi
                current_province = line[3:]  # Mengambil nama provinsi
                locations[current_province] = []
            elif line.startswith("**Kota:**"):  # Menandakan awal kota
                continue  # Lewati baris ini
            elif line.startswith("**Kabupaten:**"):  # Menandakan awal kabupaten
                continue  # Lewati baris ini
            elif line.startswith("-"):  # Menandakan kota atau kabupaten
                if current_province:  # Pastikan provinsi sudah ditentukan
                    locations[current_province].append(line[2:])  # Mengambil nama kota/kabupaten

    return locations 
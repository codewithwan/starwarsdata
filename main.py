from starwarsdata.starwars import StarWarsGalaxyAPI

# Buat objek dari kelas StarWarsGalaxyAPI
sw_api = StarWarsGalaxyAPI()

# Meminta pengguna untuk memasukkan nama karakter
name = input("Masukkan nama karakter Star Wars: ")

# Menggunakan metode search_person_by_name untuk mencari karakter berdasarkan nama
search_result = sw_api.search_person_by_name(name)

if "error" in search_result:
    print(f"Error: {search_result['error']}")
else:
    if search_result['results']:
        for result in search_result['results']:
            print("===========================")
            print(f"Name: {result['name']}")
            print(f"Height: {result['height']} cm")
            print(f"Mass: {result['mass']} kg")
            print("===========================")
    else:
        print("Karakter tidak ditemukan.")

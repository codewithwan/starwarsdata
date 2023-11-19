# Star Wars Galaxy API

Proyek ini berinteraksi dengan Star Wars Galaxy API untuk mengambil informasi tentang karakter dan menyimpannya ke dalam file teks.
## Penggunaan Class `StarWarsGalaxyAPI`

Untuk menggunakan class `StarWarsGalaxyAPI`, Anda dapat melakukan langkah-langkah berikut:

1. Import kelas tersebut ke dalam kode Python Anda:

    ```python
    from starwarsdata.starwars import StarWarsGalaxyAPI
    ```

2. Buat objek dari kelas `StarWarsGalaxyAPI`:

    ```python
    sw_api = StarWarsGalaxyAPI()
    ```

3. Gunakan metode yang disediakan oleh kelas `StarWarsGalaxyAPI`:

    - `get_person(person_id)`: Mendapatkan informasi tentang karakter berdasarkan ID karakter.
    - `get_film(film_id)`: Mendapatkan informasi tentang film berdasarkan ID film.
    - `search_person_by_name(name)`: Mencari karakter berdasarkan nama.

Pastikan untuk mengganti ID karakter atau nama yang digunakan dalam contoh penggunaan dengan nilai yang sesuai dari API.

## API 
Python Basic API wrapper
```http
  https://swapi.dev/
```

## Installation

Install my-project with npm

```bash
  pip install starwarsdata
```
    

## Notes

- Class `StarWarsGalaxyAPI` berinteraksi dengan Star Wars Galaxy API untuk mengambil informasi karakter.
- Data yang diambil disimpan dalam `starwars_data.txt`.

## Usage

Basic Usage :

```python
from starwars import StarWarsGalaxyAPI

# Create an instance of StarWarsGalaxyAPI
sw_api = StarWarsGalaxyAPI()

# Get information about a character
luke_skywalker = sw_api.get_person(1)
print(luke_skywalker)

# Get information about a film
a_new_hope = sw_api.get_film(1)
print(a_new_hope)

```

## Authors

- [@codewithwan](https://github.com/codewithwan)
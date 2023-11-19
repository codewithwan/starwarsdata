from starwarsdata.starwars import StarWarsGalaxyAPI

def print_person_info(person, file, number):
    with open(file, 'a') as f: 
        if "error" in person:
            f.write(f"Data {number}: Error - {person['error']}\n")
        else:
            f.write(f"Data {number} - Name: {person['name']}\n")
            f.write(f"Data {number} - Height: {person['height']} cm\n")
            f.write(f"Data {number} - Mass: {person['mass']} kg\n")
        f.write("===========================\n")

def main():
    file_name = "starwars_data.txt"
    sw_api = StarWarsGalaxyAPI()
    i = 1
    with open(file_name, 'w') as f:
        for i in range(100):
            person = sw_api.get_person(i)
            
            if i == 17 or "error" in person:
                print_person_info(person, file_name, i)
                i += 1
            
            print_person_info(person, file_name, i)
            i += 1

if __name__ == "__main__":
    main()

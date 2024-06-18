"""
TODO:
1. Buatlah class bernama Animal dengan ketentuan:
    - Memiliki properti:
      - name: string
      - age: int
      - species: string
    - Memiliki constructor untuk menginisialisasi properti:
      - name
      - age
      - species
2. Buatlah class bernama Cat dengan ketentuan:
    - Merupakan turunan dari class Animal
    - Memiliki method:
      - bernama "deskripsi" yang mengembalikan nilai string berikut ini.
        "{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
      - bernama "suara" yang akan mengembalikan nilai string "meow!"
 3. Buatlah instance dari kelas Cat bernama "myCat" dengan ketentuan:
    - Atribut name bernilai: "Neko"
    - Atribut age bernilai: 3
    - Atribut species bernilai: "Persian".
"""

#TODO: Silakan buat kode Anda di bawah ini.
class Animal:
    """
    Kelas dasar untuk mewakili hewan.

    Attributes:
        name (str): Nama hewan.
        age (int): Umur hewan.
        species (str): Spesies hewan.
    """

    def __init__(self, name, age, species):
        """
        Inisialisasi objek Animal.

        Args:
            name (str): Nama hewan.
            age (int): Umur hewan.
            species (str): Spesies hewan.
        """
        self.name = name
        self.age = age
        self.species = species


class Cat(Animal):
    """
    Kelas turunan dari Animal untuk mewakili kucing.
    """

    def deskripsi(self):
        """
        Mengembalikan deskripsi kucing.

        Returns:
            str: Deskripsi kucing.
        """
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"

    def suara(self):
        """
        Mengembalikan suara kucing.

        Returns:
            str: Suara kucing ("meow!").
        """
        return "meow!"


# Membuat instance dari kelas Cat
myCat = Cat("Neko", 3, "Persian")

# Mencetak deskripsi dan suara kucing
print(myCat.deskripsi())  # Output: Neko adalah kucing berjenis Persian yang sudah berumur 3 tahun
print(myCat.suara())     # Output: meow!
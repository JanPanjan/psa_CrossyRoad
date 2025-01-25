
class Parser:
    def read_data(file_name: str) -> list[float]:
        """
        Reads and returns numeric contents as floats from a file. For example,
        if the file contains lines as:
            1 2 3
            4 5 6
        the function will return a list [[1, 2, 3], [4, 5 ,6]].

        Args:
            file_name (str): name of file to be opened and read from. assumes 
            the format as shown in instructions.

        Returns:
            list (float): file contents
        """
        contents = []

        with open(file_name, "r") as file:
            contents = [[float(e) for e in line.split()] for line in file.readlines()]

        return contents

    def parse_data(data: list[float]) -> dict:
        """
        Parses and classifies given numeric data as instructions specify.
        
        Args:
            data (list): contents read with read_data function
        
        Returns:
            dict: parsed data, split for road and cars
        """
        a, b = data[0]
        lanes = [line[1:] for line in data[1:]]

        return {"a": a, "b": b, "lanes": lanes}
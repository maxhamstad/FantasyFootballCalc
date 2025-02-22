class Ingredient:
    """Initializes name, grams, calories  of ingredient"""  
    def __init__(self, name: str, grams: float, calories: float):
        self._name = name
        self._grams = grams
        self._calories = calories
        
    """Returns the name of the ingredient."""
    def get_name(self):
        return self._name
    
    """Sets the name of the ingredient if the name and makes sure its not empty."""
    def set_name(self, name:str) -> None:
        if not name is None and name != "":
            self._name = name
            
    """Returns the calorie count of the ingredient."""        
    def get_calories(self):
        return self._calories
    
    """Sets the calorie count for the ingredient if the value is positive."""
    def set_calories(self, calories:float) -> None:
        if calories > 0: 
            self._calories = calories
        else:
            raise ValueError("Calories cannot be negative")
    
    """Returns the weight of the ingredient in grams."""        
    def get_grams(self) -> float:
        return self._grams
    
    """Sets the weight of the ingredient in grams, making sure it is non-negative."""
    def set_grams(self, grams:float) -> None:
        if grams >= 0:  # Corrected the validation
            self._grams = grams
        else:
            raise ValueError("Grams cannot be negative")
        
    """Returns a string"""   
    def __str__(self)-> str:
        return (f"{self._grams} grams of {self._name}")
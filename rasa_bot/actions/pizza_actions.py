from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

AVAILABLE_PIZZA_TYPES = [
    "pepperoni", "vegetarian", "margherita", "Hawaiian",
    "BBQ Chicken", "Four Cheese", "Meat Lovers'", "Paneer Tikka", "Mushroom", "Veggie Supreme"
]

class ActionCheckPizzaAvailability(Action):
    def name(self) -> Text:
        return "action_check_pizza_availability"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        pizza_type = tracker.get_slot("pizza_type")

        if pizza_type is not None:
            if pizza_type.lower() in [pizza.lower() for pizza in AVAILABLE_PIZZA_TYPES]:  # Case-insensitive comparison
                dispatcher.utter_message(text=f"Great! We have {pizza_type}. What size would you like?")
                return []
            else:
                dispatcher.utter_message(text=f"Sorry, we don't have {pizza_type} available. Our available pizzas are: {', '.join(AVAILABLE_PIZZA_TYPES)}")
                return [SlotSet("pizza_type", None)]  # Reset the slot
        else:
            dispatcher.utter_message(text="What kind of pizza would you like?")
            return []

class ActionUtterPizzaList(Action): # New Action example
    def name(self) -> Text:
        return "action_utter_pizza_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        dispatcher.utter_message(text=f"Our available pizzas are: {', '.join(AVAILABLE_PIZZA_TYPES)}")
        return []
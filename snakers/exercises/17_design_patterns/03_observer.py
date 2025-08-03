"""
Exercise 17.3: The Observer Pattern

Learn about the Observer design pattern and its implementation in Python.

Tasks:
1. Complete the observer implementations below
2. Understand different ways to implement the observer pattern
3. Apply observers for event handling and notifications

Topics covered:
- Observer pattern
- Publisher-Subscriber model
- Event handling
- Callbacks and notifications
"""

from abc import ABC, abstractmethod
from typing import List, Callable, Dict, Any, Set

# Method 1: Classic Observer Pattern
class Subject(ABC):
    """Abstract base class for subjects (observable objects)."""
    
    def __init__(self):
        # TODO: Initialize list of observers
        self._observers = []
    
    def attach(self, observer: 'Observer') -> None:
        """
        Attach an observer to the subject.
        
        Args:
            observer: Observer to attach
        """
        # TODO: Add observer to list
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: 'Observer') -> None:
        """
        Detach an observer from the subject.
        
        Args:
            observer: Observer to detach
        """
        # TODO: Remove observer from list
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self) -> None:
        """Notify all observers of state change."""
        # TODO: Call update() on each observer
        for observer in self._observers:
            observer.update(self)

class Observer(ABC):
    """Abstract base class for observers."""
    
    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Update the observer based on subject changes.
        
        Args:
            subject: The subject that changed
        """
        pass

class WeatherStation(Subject):
    """A weather station that reports temperature changes."""
    
    def __init__(self):
        super().__init__()
        self._temperature = 0
    
    @property
    def temperature(self) -> float:
        """Get the current temperature."""
        return self._temperature
    
    @temperature.setter
    def temperature(self, value: float) -> None:
        """
        Set the temperature and notify observers.
        
        Args:
            value: New temperature
        """
        # TODO: Update temperature
        # TODO: Notify observers
        pass

class TemperatureDisplay(Observer):
    """Displays the current temperature."""
    
    def update(self, subject: Subject) -> None:
        """
        Update the display with the new temperature.
        
        Args:
            subject: The weather station
        """
        # TODO: Check if subject is a WeatherStation
        # TODO: Print the current temperature
        pass

class TemperatureAlert(Observer):
    """Alerts when temperature exceeds a threshold."""
    
    def __init__(self, threshold: float):
        self.threshold = threshold
    
    def update(self, subject: Subject) -> None:
        """
        Check if temperature exceeds threshold.
        
        Args:
            subject: The weather station
        """
        # TODO: Check if subject is a WeatherStation
        # TODO: Alert if temperature exceeds threshold
        pass

# Method 2: Event Dispatcher with Callbacks
class EventDispatcher:
    """A simple event dispatcher using callbacks."""
    
    def __init__(self):
        # TODO: Initialize a dictionary mapping event types to callbacks
        pass
    
    def add_listener(self, event_type: str, callback: Callable) -> None:
        """
        Add a listener for an event type.
        
        Args:
            event_type: Type of event to listen for
            callback: Function to call when event occurs
        """
        # TODO: Add callback to the list for the event type
        pass
    
    def remove_listener(self, event_type: str, callback: Callable) -> None:
        """
        Remove a listener for an event type.
        
        Args:
            event_type: Type of event
            callback: Callback to remove
        """
        # TODO: Remove callback from the list for the event type
        pass
    
    def dispatch(self, event_type: str, *args, **kwargs) -> None:
        """
        Dispatch an event to all registered listeners.
        
        Args:
            event_type: Type of event to dispatch
            *args: Positional arguments to pass to callbacks
            **kwargs: Keyword arguments to pass to callbacks
        """
        # TODO: Call all callbacks registered for the event type
        pass

# Method 3: Publisher-Subscriber with Topics
class Publisher:
    """A publisher that sends messages on topics."""
    
    def __init__(self):
        # TODO: Initialize a dictionary mapping topics to subscribers
        pass
    
    def subscribe(self, topic: str, subscriber: 'Subscriber') -> None:
        """
        Add a subscriber to a topic.
        
        Args:
            topic: Topic to subscribe to
            subscriber: Subscriber to add
        """
        # TODO: Add subscriber to the set for the topic
        pass
    
    def unsubscribe(self, topic: str, subscriber: 'Subscriber') -> None:
        """
        Remove a subscriber from a topic.
        
        Args:
            topic: Topic to unsubscribe from
            subscriber: Subscriber to remove
        """
        # TODO: Remove subscriber from the set for the topic
        pass
    
    def publish(self, topic: str, message: Any) -> None:
        """
        Publish a message to all subscribers of a topic.
        
        Args:
            topic: Topic to publish to
            message: Message to publish
        """
        # TODO: Send the message to all subscribers of the topic
        pass

class Subscriber:
    """A subscriber that receives messages."""
    
    def __init__(self, name: str):
        self.name = name
    
    def receive(self, topic: str, message: Any) -> None:
        """
        Receive a message on a topic.
        
        Args:
            topic: Topic the message was published on
            message: The message
        """
        # TODO: Print the received message and topic
        pass

# Test functions
def test_classic_observer():
    """Test the classic observer pattern."""
    print("Testing Classic Observer Pattern:")
    
    # Create subject and observers
    weather_station = WeatherStation()
    display = TemperatureDisplay()
    alert = TemperatureAlert(threshold=30)
    
    # Attach observers
    weather_station.attach(display)
    weather_station.attach(alert)
    
    # Change temperature a few times
    for temp in [25, 28, 32, 26]:
        print(f"\n  Setting temperature to {temp}°C:")
        weather_station.temperature = temp
    
    # Detach an observer
    weather_station.detach(alert)
    print("\n  Alert detached. Setting temperature to 35°C:")
    weather_station.temperature = 35

def test_event_dispatcher():
    """Test the event dispatcher."""
    print("\nTesting Event Dispatcher:")
    
    dispatcher = EventDispatcher()
    
    # Define some event handlers
    def temperature_changed(temp):
        print(f"  Temperature changed to {temp}°C")
    
    def high_temperature_alert(temp):
        if temp > 30:
            print(f"  ALERT: Temperature {temp}°C exceeds threshold!")
    
    # Register handlers
    dispatcher.add_listener("temperature_changed", temperature_changed)
    dispatcher.add_listener("temperature_changed", high_temperature_alert)
    
    # Dispatch events
    for temp in [25, 28, 32, 26]:
        print(f"\n  Dispatching temperature {temp}°C:")
        dispatcher.dispatch("temperature_changed", temp)
    
    # Remove a listener
    dispatcher.remove_listener("temperature_changed", high_temperature_alert)
    print("\n  Alert listener removed. Dispatching temperature 35°C:")
    dispatcher.dispatch("temperature_changed", 35)

def test_pub_sub():
    """Test the publisher-subscriber pattern."""
    print("\nTesting Publisher-Subscriber Pattern:")
    
    # Create publisher and subscribers
    publisher = Publisher()
    weather_sub = Subscriber("Weather Watcher")
    alert_sub = Subscriber("Alert System")
    
    # Subscribe to topics
    publisher.subscribe("temperature", weather_sub)
    publisher.subscribe("temperature", alert_sub)
    publisher.subscribe("humidity", weather_sub)
    
    # Publish messages
    print("\n  Publishing temperature updates:")
    for temp in [25, 28, 32]:
        publisher.publish("temperature", f"{temp}°C")
    
    print("\n  Publishing humidity update:")
    publisher.publish("humidity", "65%")
    
    # Unsubscribe
    publisher.unsubscribe("temperature", alert_sub)
    print("\n  Alert system unsubscribed from temperature. Publishing 35°C:")
    publisher.publish("temperature", "35°C")

if __name__ == "__main__":
    # Test each observer implementation
    test_classic_observer()
    test_event_dispatcher()
    test_pub_sub()
    
    # Compare approaches
    print("\nObserver Implementation Comparison:")
    print("  1. Classic Observer: Traditional OOP approach with clear subject-observer relationship")
    print("  2. Event Dispatcher: Flexible callback-based system good for decoupled components")
    print("  3. Publisher-Subscriber: Topic-based communication allowing targeted notifications")
    
    print("\nDiscussion:")
    print("  Which observer pattern variation is best suited for different scenarios?")
    print("  How do these patterns help in creating loosely coupled systems?")
    print("  What are the trade-offs in terms of complexity and flexibility?")

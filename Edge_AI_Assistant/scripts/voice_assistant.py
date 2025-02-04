class VoiceAssistant:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print(f"Hello, I am {self.name}. How can I help you today?")

# Example usage
assistant = VoiceAssistant("Alexa")
print(assistant.greet())
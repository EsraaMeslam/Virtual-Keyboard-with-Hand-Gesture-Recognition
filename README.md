# Virtual-Keyboard-with-Hand-Gesture-Recognition

<li>The Virtual Keyboard project is a gesture-based application that allows users to type text using hand movements. By detecting hand gestures through a webcam, the application simulates key presses on a virtual keyboard, making it an interactive and innovative way to input text.

## Project Idea

The idea behind this project is to create an intuitive and hands-free typing solution using computer vision and hand tracking technologies. By leveraging the webcam to detect hand gestures and movements, users can interact with a virtual keyboard displayed on the screen. This project demonstrates the potential of combining computer vision with human-computer interaction to create a novel user experience.

## Features


## Features

- **Real-time Hand Detection:**
  - Utilizes OpenCV for capturing video from the webcam and the `cvzone` library, which is built on top of MediaPipe, to detect and track hand movements in real-time.
  - The hand detection algorithm identifies the position of the hand and its key landmarks, such as the tips of the fingers, allowing precise gesture recognition.
  - Supports multiple hand detection and can handle occlusions to some extent, ensuring robust performance even with varying hand positions.

- **Virtual Keyboard Interface:**
  - A fully functional virtual keyboard is rendered on the screen, with a layout similar to a physical keyboard, including letters, numbers, and common punctuation marks.
  - The keyboard is dynamically drawn based on the `chars` list, allowing for easy customization of the keyboard layout to suit different languages or use cases.
  - Each key is represented by a `Btn` object, which includes properties for position, size, and text, enabling a flexible and scalable keyboard design.

- **Gesture-Based Input:**
  - The application uses hand gestures to simulate key presses. When the index finger is detected over a key and the thumb and index finger are brought close together, the key press is registered.
  - Distance-based interaction: A predefined distance threshold determines when a key is considered pressed. This threshold is adjustable to accommodate different users' hand sizes and gestures.
  - Provides real-time visual feedback by changing the color of the key being pressed, enhancing user experience and ensuring accurate input.

- **Text Display:**
  - The application features a text display area where the typed text appears in real-time. This area is updated dynamically as the user interacts with the virtual keyboard.
  - Includes an input box positioned at the top of the window, which is visually distinct and easy to read, making it clear to users what text they have entered.
  - Supports continuous text input with automatic line wrapping, allowing users to type long strings of text without needing to scroll.

- **Customizable Keyboard Layout:**
  - The keyboard layout can be easily customized by modifying the `chars` list, which defines the characters and their arrangement on the virtual keyboard.
  - The keyboard can be adapted for different languages, special characters, or specific use cases by updating the layout configuration.

- **Interactive Feedback:**
  - Provides visual feedback for key presses with color changes to indicate when a key is being pressed.
  - Includes additional visual elements such as corner rectangles around keys to improve readability and usability.

- **User-friendly Interface:**
  - The application features a user-friendly interface with clear visual indicators and an intuitive layout.
  - The virtual keyboard is designed to be easily accessible and usable, ensuring that users can interact with it without needing extensive setup or configuration.

These features combine to create a seamless and interactive virtual typing experience, demonstrating the power of combining computer vision with user interface design to create innovative input methods.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Required Python packages listed in `requirements.txt`.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>

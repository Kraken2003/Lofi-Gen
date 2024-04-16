## Lofi Music Generation with LSTMs

This repository contains code for generating lofi music using a Long Short-Term Memory (LSTM) network. 

# Key Libraries:

* Keras ([https://keras.io/](https://keras.io/))
* TensorFlow ([https://www.tensorflow.org/](https://www.tensorflow.org/))
* music21 ([http://web.mit.edu/music21/](http://web.mit.edu/music21/))
* pickle ([https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html))

# Functionality Overview:

1. **Data Loading and Preprocessing:**
    - Loads pickled music note data.
    - Creates sequences of fixed length from the note data.
    - Converts notes to numerical representations for network consumption.

2. **LSTM Network Creation:**
    - Builds a multi-layered LSTM network architecture.
    - Trains the network to predict the next note in a sequence.

3. **Music Generation:**
    - Provides a function to generate new musical sequences based on a seed sequence.
    - Utilizes the trained network to predict note by note, building a novel melody.

4. **MIDI File Creation:**
    - Converts the generated note sequence into a MIDI file for playback.

**Note:** This code is for demonstration purposes and may require adjustments for specific use cases.

# Getting Started :

* Install required libraries.
* Download or prepare your lofi music dataset in a pickle format.
* Execute the Python scripts to train the network and generate music.

# Further Exploration:

* Experiment with different network architectures and hyperparameters.
* Try incorporating music theory concepts into the generation process.
* Explore conditional music generation based on user input or genre.

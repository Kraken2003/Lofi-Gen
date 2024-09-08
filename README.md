# Lofi Music Generation with LSTMs

This repository contains code for generating lofi music using a Long Short-Term Memory (LSTM) network. 

## Table of Contents

- [Project Title](#lofi-music-generation-with-lstms)
- [Table of Contents](#table-of-contents)
- [Comprehensive Codebase Summary](#comprehensive-codebase-summary)
- [Key Libraries](#key-libraries)
- [Functionality Overview](#functionality-overview)
- [Getting Started](#getting-started)
- [Further Exploration](#further-exploration)
- [License](#license)

## Comprehensive Codebase Summary

This codebase is designed to generate Lofi music using a Long Short-Term Memory (LSTM) neural network. It comprises two main Python files: `LofiGen.ipynb` (a Jupyter notebook) and `preprocessing.py`. These files work together to process MIDI data, train a model, and generate new Lofi music sequences.

**1) Overall Structure and Interaction:**

The codebase operates in a two-step process:

* **Data Preparation (`preprocessing.py`):**  MIDI files are processed in batches to extract note information, converting them into strings representing individual notes or chords. 
* **Model Training and Generation (`LofiGen.ipynb`):** The extracted notes are used to train an LSTM network, which then generates new sequences of notes. These notes are converted back into a MIDI file for playback.

**2) Key Components and Data Structures/Algorithms:**

**Key Components:**

* **LSTM Network:**  The core of the system is an LSTM network, implemented using the Keras framework. This network learns patterns and relationships within the provided musical data.
* **MIDI Processing:** `music21` library is used to parse and manipulate MIDI data, extracting notes and chords, and converting generated note sequences back to a MIDI representation.

**Data Structures:**

* **`notes` (list):** Stores strings representing notes and chords extracted from MIDI files.
* **`pitchMapping` (dict):** Maps notes to numerical representations for input to the LSTM network.
* **`networkInput` (NumPy array):** Contains the input sequences for the LSTM network.
* **`networkOutput` (NumPy array):** Contains the target notes for the LSTM network.

**Algorithms:**

* **Long Short-Term Memory (LSTM):**  This recurrent neural network architecture is particularly effective for learning temporal dependencies in sequential data like music.
* **One-Hot Encoding:**  A technique used to represent individual notes numerically for input to the network.
* **Softmax Activation:** Used in the output layer of the LSTM network to predict the probability distribution over possible notes.
* **Temperature Sampling:**  A method used during note generation to control the diversity of generated notes.

**3) Logic Flow Across Files:**

* **`preprocessing.py`:**
    * Reads MIDI files in batches.
    * Extracts notes and chords using `music21`.
    * Converts note information to strings and stores them in a list (`notes`).
* **`LofiGen.ipynb`:**
    * Loads the preprocessed notes from a pickled file.
    * Creates the LSTM network architecture.
    * Trains the model using the note sequences.
    * Generates new sequences of notes using the trained model.
    * Converts the generated notes to a MIDI representation and saves it to a file.

**4) Inputs/Outputs Across the Codebase:**

**Inputs:**

* MIDI files (`.mid`): Provide the source material for Lofi music generation.
* A preprocessed file (likely in `.pkl` format) containing the extracted notes from the MIDI files.
* A seed sequence of notes to initiate the generation process.

**Outputs:**

* A MIDI file containing the generated Lofi music sequence.

**5) Dependencies:**

**Shared Dependencies:**

* `music21`: For processing MIDI data and creating MIDI files.
* `numpy`: For numerical computations and handling array data.
* `pickle`: For storing and retrieving the preprocessed note data.

**Unique Dependencies:**

* **`LofiGen.ipynb`:** 
    * `keras`: For building and training the LSTM network.
    * `tensorflow`: The backend for Keras, required for the LSTM implementation.
    * `pandas`: For potentially handling data manipulation tasks.
    * `glob`: For potentially searching for MIDI files within the directory. 

**Overall, the codebase effectively combines MIDI processing, LSTM network training, and music generation to create new Lofi music.  The clear separation of data preparation and model training enhances the code's modularity and makes it more reusable for different musical datasets and training settings.**

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

# Getting Started:

* Install required libraries.
* Download or prepare your lofi music dataset in a pickle format.
* Execute the Python scripts to train the network and generate music.

# Further Exploration:

* Experiment with different network architectures and hyperparameters.
* Try incorporating music theory concepts into the generation process.
* Explore conditional music generation based on user input or genre.

## License

This project is licensed under the MIT License. 

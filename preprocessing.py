def process_batch(batch, songs):
    notes = []

    for i, file in enumerate(batch):
        try:
            midi = converter.parse(file)
            notes_to_parse = None
            parts = instrument.partitionByInstrument(midi)

            if parts:  # instrument parts
                notes_to_parse = parts.parts[0].recurse()
            else:  # flat structure
                notes_to_parse = midi.flat.notes

            for element in notes_to_parse:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))

            # Print completion status for every 10 files
            if (i + 1) % 10 == 0:
                print(f'Processed {i + 1} files in the current batch')
        except Exception as e:
            print(f'FAILED: {i+1}: {file} - {e}')

    return notes

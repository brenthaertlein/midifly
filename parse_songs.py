import argparse
import glob
import pickle

from music21 import converter, instrument, note, chord
from music21.exceptions21 import StreamException


def parse_midis(name, midis_dir):
    """ Parse a directory of MIDI files into a stringified list of notes/chords, stored in binary"""
    print(f'Parsing MIDI files in {midis_dir}')
    notes = []

    for file in glob.glob(f'{midis_dir}/*.mid'):
        print('Parsing %s' % file)

        midi = None

        notes_to_parse = []

        try:
            midi = converter.parse(file)
            s2 = instrument.partitionByInstrument(midi)
            notes_to_parse = s2.parts[0].recurse()
        except StreamException as ex:
            print(f'Unexpected {ex} parsing {file}')
            if midi is not None:
                notes_to_parse = midi.flat.notes

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))

    filename = f'data/notes/{name}.notes.pkl'
    with open(filename, 'wb') as filepath:
        pickle.dump(notes, filepath)
    print(f'Saved notes for {name} to {filename}')

    return notes


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Name this dataset')
    parser.add_argument('midis_dir', help='Path to directory of MIDI files to analyze')

    args = parser.parse_args()
    parse_midis(args.name, args.midis_dir)

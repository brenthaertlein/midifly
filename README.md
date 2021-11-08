# Midify

_Ain't nobody got time to create MIDIs no more_

## Fork

This project was forked from https://github.com/Skuldur/Classical-Piano-Composer

## Requirements

* [Python](https://www.python.org/) (3.9.7 or higher)

## Getting started

* Install dependencies
* Add your MIDIs to `data/midi`
* Create a dataset using `parse_songs.py`
* Train your model with the dataset using `train.py`
* Generate music using `generate_midi.py`

## How to use

Provided below are some steps to help get started

### Generating data

To generate a set of data to use for training and prediction, run `parse_songs.py`

e.g.

`python parse_songs.py dataset_name path/to/midis`

### Training

To train the network run `train.py`

e.g.

`python train.py model_name path/to/notes`

If you already have a set of weights generated (from the same dataset a.k.a. notes), pass the optional flag `--weights`

**NOTE**: You can stop the process at any point in time and the weights from the latest completed epoch will be
available for text generation purposes.

### Prediction

To generate a song using your trained model run **generate_midi.py**

e.g.

`python generate_midi.py song_name path/to/notes path/to/weights`

You can run the prediction file right away using **sample_notes.pkl** and **sample_weights.hdf5** file

`python generate_midi.py sample sample_notes.pkl sample_weights.hdf5`

## Troubleshooting

> How do I install dependencies?

`pip install -r requirements.txt`

> I'm getting some weird error from... tensorflow? Something with the weights...

Try running the training without loading an existing model. Starting from scratch will take longer, but the model needs
to fit your dataset

> I tried generating a MIDI and it just plays one note over and over

It takes a number of generations before the model fits well enought to make accurate predictions. Using `loss` as a
metric, songs probably won't begin to have any coherence until reaching a values where `loss < 2.0` and
ideally `loss < 1.0`

> My `loss` value isn't going down or goes down very slowly

It may be that the initial dataset provided does not provide enough information for the model to efficiently train
itself. Try training on a larger dataset

## References

* https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5
* https://github.com/Skuldur/Classical-Piano-Composer
* https://ai.plainenglish.io/building-a-lo-fi-hip-hop-generator-e24a005d0144
* https://github.com/zacharykatsnelson/Lofi-Hip-Hop-Generator

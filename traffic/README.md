# Traffic — CS50 AI Project 5: Neural Networks

## What was implemented

In `traffic.py`, `load_data` walks the 43 category directories (numbered
0–42) inside the data directory, reads every image with OpenCV, resizes it
to 30x30 pixels with `cv2.resize`, and returns the list of images together
with the matching list of integer category labels. `get_model` returns a
compiled convolutional neural network built with TensorFlow/Keras.

## Model architecture

The network takes a 30x30 RGB image as input and produces a 43-way softmax
output, one unit per traffic-sign category:

- `Input(shape=(30, 30, 3))`
- `Rescaling(1.0 / 255)` — normalises pixel values from 0–255 to 0–1 inside
  the model, so the raw images returned by `load_data` can be used directly.
- `Conv2D(32, (3, 3), activation="relu", padding="same")` + `MaxPooling2D(2, 2)`
- `Conv2D(64, (3, 3), activation="relu", padding="same")` + `MaxPooling2D(2, 2)`
- `Conv2D(64, (3, 3), activation="relu", padding="same")` + `MaxPooling2D(2, 2)`
- `Flatten()`
- `Dense(128, activation="relu")`
- `Dropout(0.5)`
- `Dense(43, activation="softmax")`

The model is compiled with the Adam optimiser, `categorical_crossentropy`
loss and accuracy as the metric. Training uses the settings already in the
skeleton: 10 epochs and a 40% test split (`TEST_SIZE = 0.4`).

## Experimentation process

I started with a small CNN (two convolutional blocks, 32 and 64 filters,
followed by a 128-unit dense layer) because the images are only 30x30, so a
deep network is unnecessary and would be slow to train on a CPU-only
Codespace. I added a `Rescaling` layer as the first layer so the network
normalises its own inputs; this made training much more stable than feeding
raw 0–255 pixel values into the convolutions. A third convolutional block
(64 filters) was added to give the network more capacity to distinguish the
many similar-looking signs (for example, the different speed-limit signs).
Dropout (0.5) after the dense layer was included to reduce overfitting —
the GTSRB training set is only about 26,700 images across 43 categories,
and without dropout the training accuracy climbed while the test accuracy
lagged behind. With dropout, the model generalises well: training accuracy
finishes slightly below test accuracy because dropout is only active while
training.

The `main` function, constants and the overall program flow were left
unchanged from the distribution code; only `load_data` and `get_model`
were implemented.

## Results

Full training run on the GTSRB data set supplied with the project
(26,684 images; 16,010 training / 10,674 test after the 40% split),
10 epochs, run with `python traffic.py gtsrb model.h5`:

- Epoch 1: accuracy 0.2396, loss 2.7397
- Epoch 2: accuracy 0.5464, loss 1.4020
- Epoch 3: accuracy 0.7394, loss 0.7920
- Epoch 4: accuracy 0.8403, loss 0.4926
- Epoch 5: accuracy 0.8846, loss 0.3515
- Epoch 6: accuracy 0.9174, loss 0.2540
- Epoch 7: accuracy 0.9365, loss 0.2000
- Epoch 8: accuracy 0.9450, loss 0.1678
- Epoch 9: accuracy 0.9526, loss 0.1383
- Epoch 10: accuracy 0.9616, loss 0.1202
- Test evaluation: accuracy 0.9832, loss 0.0673

The final test accuracy of 0.9832 (98.32%) is well above the roughly 90%
that the specification suggests is attainable, and the trained model was
saved to `model.h5`.

## Environment note

This Codespace ships Python 3.14, while the specification recommends
Python 3.12 at most. TensorFlow 2.22.0-rc0 (installed from
`requirements.txt` with `pip3 install -r requirements.txt`) provides a
Python 3.14 wheel, and OpenCV 5.0.0 and scikit-learn 1.9.1 were installed
the same way; the project runs and trains correctly in this environment.

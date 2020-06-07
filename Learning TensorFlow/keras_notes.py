import tensorflow as tf
""""
import requests
requests.packages.urllib3.disable_warnings()
import ssl
# https://intellij-support.jetbrains.com/hc/en-us/community/posts/360000117730-SSL-error-in-accessing-MNIST-dataset
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
"""

model = tf.keras.Sequential()
minst = tf.keras.datasets.mnist
(train_x, train_y), (test_x, test_y) = minst.load_data()
test_x, test_y = test_x / 255, test_y / 255

model = tf.keras.models.Sequential([
  # this is hte shape of the origianl images 28x28
  # this just flattens that img
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

predictions = model(train_x[:1]).numpy()

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(train_y[:1], predictions).numpy()
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
model.fit(train_x, train_y, epochs=5)
# The Model.evaluate method checks the models performance, usually on a "Validation-set" or "Test-set".